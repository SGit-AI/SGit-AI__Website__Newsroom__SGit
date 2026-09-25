# The traps

Six ways to get `sg.llm.*` wrong, each with its reason. This page is written by this site rather than generated: [the reference](index.md) is the contract, and this is what the contract's authors learned enforcing it.

## 1. Base64 is chunked at 8190, not 8192

Use `sg.llm.imagePart()` rather than encoding an image yourself. It runs in your frame, so there is no host round trip and the bytes are already yours, and it chunks base64 at **8190**.

`8192 % 3 === 2`, so a 8192-sized chunk emits `=` padding mid-string, and `atob()` rejects the result.

Base64 encodes three bytes into four characters, so a chunk boundary is only safe on a multiple of three. 8190 is `3 × 2730`. 8192 is not a multiple of three, so splitting there terminates a group early, the encoder pads it, and the padding lands in the middle of the string where the decoder will not accept it. The symptom is an image that fails to decode above roughly 8 KB and works fine below it, which reads as a size limit and is not one.

> This codebase has shipped that exact bug three times.

Three times, in a codebase whose own authors wrote the explanation. That is the argument for using the helper rather than hand-rolling the encoder, and it is also the reason this page exists: a trap that catches its own authors repeatedly is documentation, not embarrassment.

## 2. `available()` is not optional politeness

Every other namespace in the vault runtime is a static capability question: the grant is in `app.json` and either you have it or you do not. `llm` is not, and that is the trap.

| What can be false at runtime | What you get |
|---|---|
| The vault has no key configured | `ENOKEY` |
| The app was not granted `llm.chat` | `EPERM` |
| The key is owner-sealed and this session is read-only | `EREADONLY` |
| The session's spend cap is already reached | `EBUDGET` |

An app that renders a chat box and finds out on submit has already made a promise it cannot keep. Ask first, then decide what to draw. The failure mode is not an error, it is a user typing a question into a box that was never going to work.

## 3. An image must clear after one send

An attached *file* persists across turns, deliberately: you are having a conversation about it. An attached *image* does not, and the reason is the bill:

> Unlike a file, an image left attached would silently re-send and re-bill on every turn.

The host panel clears it. If you are building your own pane, clear it too. This is the one trap on this page where the cost of getting it wrong is invisible to the user and visible on the invoice.

## 4. An estimate is never a bill

`cost` arrives labelled: `{value, source, estimated}`. `estimated: true` means it was computed from token counts times list price, not billed.

```
costPill.textContent = res.cost.estimated
 ? `~$${res.cost.value.toFixed(4)}` // computed - NOT billed
 : `$${res.cost.value.toFixed(4)}` // reconciled against /generation
```

The host reconciles from two sources: the stream's own `usage.cost` first, then the authoritative `/generation` lookup. Until the second arrives, the figure is an estimate and rendering it without the `~` makes a guess look like a fact about somebody's money. This site follows the rule it teaches: [its own cost figures carry the tilde](../openrouter/index.md).

## 5. `listen` is never implied by `chat`

An app that can talk to a model does not thereby get a microphone.

> Recording a room is a categorically different act from sending text.

It is a separate grant, and it asks for consent every time by default. The three control calls, `listenStop()`, `listenCancel()` and `listening()`, sit behind the same grant and raise **no** consent prompt: ending a take you already started is strictly less authority than starting one, and nobody should have to approve stopping. A second `listen()` while one is running is refused with `EBUSY` rather than opening a second microphone.

One more, easy to miss: **leave `model` alone unless you know the model hears.** Transcription does not use the vault's chat model. Most chat models have no audio endpoint at all, and OpenRouter answers `404 No endpoints found that support input audio`. `listen()` defaults to `google/gemini-3.5-flash`, and passing a model that does not accept audio is refused up front with `EMODEL` and a message naming one that does.

## 6. Branch on `err.code`, never on message text

All nine codes arrive as `err.code`. Message text is for humans and it changes; the code is the contract.

| Code | Meaning | What an app should usually do |
|---|---|---|
| `EPERM` | no grant | Do not render the UI at all: this was knowable at `available()` |
| `ECONSENT` | user declined | Nothing. A decline is not an error worth showing |
| `ENOKEY` | no key configured for this vault | Point at Settings → AI models, which is where the fix is |
| `EREADONLY` | owner-sealed key, read-only session | Say so plainly: this is cryptographic, not a setting to change |
| `EBUDGET` | cap reached | Show the meter. The user is not broken, the session is spent |
| `EMODEL` | model not allow-listed, none selected, or it cannot read what you sent | Read the message: it **names the model** |
| `EABORT` | cancelled | Keep the partial text. It is already rendered and it is already paid for |
| `EIMGSIZE` | image payload over the host ceiling | Downscale. The ceiling is not yours to raise: it is spending the vault's key |
| `EPROTO` | upstream failure | Offer a retry. This one really is somebody else's fault |

`listen()` adds three more: `ENOMIC` (no microphone, sandboxed, or refused by the browser), `EINSECURE` (not HTTPS) and `EBUSY` (a take is already running).

**`EMODEL` naming the model is a deliberate error-design choice** and worth copying. A model that cannot see gets you an error that says which model, instead of a provider error that names nothing. The host knows, because it reads capability from the live catalogue rather than a hard-coded list, so [a new vision model works the day it ships](../openrouter/index.md#catalogue).

## What the host does that you do not have to

The reference carries this as a table and it is the API's real argument, so it is worth restating as a count: **eight concerns an app does not implement**. Holding the key. Filtering the model list. Enforcing spend caps before the call. Clamping `maxTokens` rather than rejecting it. Raising the consent prompt. Checking whether the model can read an image. Capping the image payload. Reconciling cost from two sources.

The bridge is not a convenience wrapper. It is a list of things that would each be got wrong independently by every app that had to do them itself.

 [← The reference](index.md) [The security model →](../security/index.md)


==============================================================================
/security/index.md
==============================================================================

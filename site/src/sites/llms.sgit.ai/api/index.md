# The sg.llm.* reference

*Source: <https://llms.sgit.ai/api/index.html> · site v0.2.0 · the markdown twin of this page, generated from it.*

---

[llms.sgit.ai](../index.md) / api

# The `sg.llm.*` reference

Ten calls, four grants and nine error codes. Every app that talks to a model through a vault uses this surface, and until now the complete version of it existed only inside an agent authoring contract that no human reader would open.

 Generated, not written

Everything below the rule is **generated verbatim** from the section *Calling an LLM (`sg.llm.*`)* of `library/guides/vault-html/AUTHORING.md` in [the-cyber-boardroom/SGraph-AI__App__Send](https://github.com/the-cyber-boardroom/SGraph-AI__App__Send/blob/main/library/guides/vault-html/AUTHORING.md), at product version **v0.33.62** (commit `b561fa6b1`). Nobody edits it here.

That is deliberate. The corpus refused to create a second copy of this contract, on the grounds that *"adding a competing document would create a second source of truth that drifts"*, and it was right. It also left a gap: a contract nobody can find is not published. So the canonical file stays canonical, its hash is recorded in `sources/MANIFEST.json`, and the pre-release gate fails the build if this page stops matching it. The reference is readable here and it still has exactly one author.

Source hash `c8691cf98901721b` · [the vendored section, verbatim](../sources/AUTHORING__calling-an-llm.md) · [the traps page](traps.md) is written by this site and is not generated.

**The contract is young and it has moved.** The bridge shipped on 2 August 2026; `listen` and `imagePart` landed on 3 August, one day later. Read the dates in the headings as part of the contract, and check a claim against the shipped code before you build on it. [One place where this page and the shipped code already disagree](../shipped/index.md#drift) is recorded on the shipped page.

---

Your app can call a language model **without ever holding an API key**. The key lives in `.vault/llm/config.json` (inside the permission floor — your app cannot read it), and the host makes the call on your behalf. You send messages and receive text.

## 1. Declare the grants

Default-deny, like every other capability. In `app.json`:

```
{
 "entry": "index.html",
 "permissions": {
 "llm": { "chat": true, "models": true, "usage": true }
 }
}
```

`chat` is the one that spends money; `models` and `usage` are read-only. Grant only what you use.

## 2. Check availability BEFORE you render a chat UI

`sg.llm.available()` is not optional politeness. Unlike other namespaces, LLM access depends on *runtime* state: whether the vault has a key configured, whether this is a read-only session, whether the budget is spent. Ask first, then decide what to draw.

```
const a = await sg.llm.available();
if (!a.ok) {
 // 'ENOKEY' — no key configured for this vault (tell the user: Settings → AI models)
 // 'EPERM' — this app wasn't granted permissions.llm.chat
 // 'EREADONLY' — owner-sealed key, and this is a read-only session
 showFallbackUI(a.reason);
 return;
}
console.log('ready:', a.model, 'remaining:', a.remaining); // {calls, cost} — null = uncapped
```

## 3. Chat, with streaming

```
const res = await sg.llm.chat(
 { messages: [{ role: 'user', content: 'Summarise this vault in one line.' }] },
 (delta, acc) => { out.textContent = acc; } // optional — called as text arrives
);
console.log(res.content, res.usage, res.cost, res.id);
```

Three properties worth relying on:

- **The terminal reply is authoritative.** An app that ignores `onToken` entirely still gets the complete `content`. Deltas are a UX affordance, never the source of truth.
- **Deltas carry only the increment** (`delta`), plus the running `acc` for convenience. The host coalesces them on a ~50 ms timer, so you get readable chunks rather than a postMessage per token.
- **`cost` is labelled**: `{value, source, estimated}`. `estimated: true` means it was computed from token counts × list price, not billed. Render estimates with a `~`. Never show one as a bill.

Optional request fields: `model`, `maxTokens`, `temperature`, `topP`, `stream: false`.

## 4. Cancel a call in flight

The promise carries the request id:

```
const p = sg.llm.chat({ messages }, onToken);
stopBtn.onclick = () => sg.llm.cancel(p.requestId);
try { await p; } catch (e) { if (e.code === 'EABORT') { /* partial text is already rendered */ } }
```

## 5. Show what it costs

```
const u = await sg.llm.usage();
meter.textContent = `${u.calls} calls · $${u.cost.toFixed(4)} · ${u.remaining.cost ?? '∞'} left`;
```

`usage()` reports the **whole session**, including calls made by the vault UI's own chat panel — one bill per session, not one per surface.

## 6. Send an image (a screenshot, a chart, a scan) — NEW 2026-08-03

A message's `content` can be an array of parts instead of a string:

```
const part = await sg.llm.imagePart(blobOrBytes); // or a data: URL you already have
const res = await sg.llm.chat({
 messages: [{ role: 'user', content: [
 { type: 'text', text: 'What is wrong in this screenshot?' },
 part
 ] }]
});
```

**Use `sg.llm.imagePart()` rather than encoding it yourself.** It runs in your frame (no host round trip — the bytes are already yours) and chunks base64 at **8190, not 8192**. `8192 % 3 === 2`, so a 8192-sized chunk emits `=` padding mid-string and `atob()` rejects it; this codebase has shipped that exact bug three times. It accepts a `Blob`/`File`, a `Uint8Array`, an `ArrayBuffer`, or passes a `data:` URL straight through.

Accepted types: **png, jpeg, webp, gif**. Not svg — it is a scriptable document, not a bitmap, and no provider takes it.

**The model must be able to read images**, and the host checks before spending the call:

- capability is read from the **live model catalogue** (`architecture.modality` / `input_modalities`), not a hard-coded list, so a new vision model works the day it ships;
- a model that cannot see gets you `EMODEL` **naming the model**, instead of a provider error that names nothing;
- note that `text->image` is an image *generator*, not a reader — it is correctly refused.

The host also caps the total image payload (`EIMGSIZE`). That ceiling is not yours to raise: it is spending the vault's key.

Images appear in the request ledger as their own count, never folded into the character total — `sg.llm.usage()` and the AI Requests pane both stay honest about what the expensive calls were.

**Not a new grant.** An image is an ordinary `chat()` call under `permissions.llm.chat`.

## What the host does that you don't have to

| Concern | Who handles it |
|---|---|
| Holding the API key | Host. It is never in your frame, your bundle, or any message you receive. |
| Which models you may use | Host — `models()` is already filtered by the vault's allow-list, so a picker you build from it is automatically correct. |
| Spend caps | Host. `maxCostPerSession` / `maxCallsPerSession` are enforced before the call; you get `EBUDGET`. |
| `maxTokens` | Host **clamps** it to the vault policy. Asking for more is not an error, it is just capped. |
| Consent | Host. The first `chat()` raises a HUD prompt the user must accept; declining gives you `ECONSENT`. |
| Whether the model can read an image | Host, from the live catalogue. You get `EMODEL` naming the model, not a provider error naming nothing. |
| Image size ceiling | Host (`EIMGSIZE`). It is spending the vault's key, so the limit is not the app's to set. |
| Cost reconciliation | Host, two-source (stream `usage.cost`, then the authoritative `/generation` lookup). |

## Error codes

`EPERM` (no grant) · `ECONSENT` (user declined) · `ENOKEY` (no key configured) · `EREADONLY` (owner-sealed key, read-only session) · `EBUDGET` (cap reached) · `EMODEL` (model not in the allow-list, none selected, or it cannot read the image/audio you sent) · `EABORT` (cancelled) · `EIMGSIZE` (image payload over the host ceiling) · `EPROTO` (upstream failure). They arrive as `err.code`, so branch on that rather than on message text.

## Voice input (`sg.llm.listen`) — NEW 2026-08-03

Speak instead of type. One call: the **host** opens the microphone, shows a red recording bar with a Stop button, transcribes with the vault's key, and hands you back text.

```
{ "permissions": { "llm": { "chat": true, "listen": true } } }
```

```
micBtn.onclick = async () => {
 try {
 const { text } = await sg.llm.listen(); // opts: {maxMs, model, prompt}
 input.value = text; // then send it as a normal chat message
 } catch (e) {
 if (e.code === 'ECONSENT') return; // user declined — not an error worth showing
 if (e.code === 'ENOMIC') showTypeInstead();
 }
};
```

**`listen` is a separate grant and is never implied by `chat`.** Recording a room is a categorically different act from sending text, so an app that can talk to a model does not thereby get a microphone. It also **asks for consent every time** by default (tune with `permissions.consent["llm.listen"]` if you are building a kiosk).

**Your frame never touches audio.** A sandboxed app frame has no `navigator.mediaDevices` at all, so capture happens in the host — which is also why the recording indicator is on host chrome where the user can always see it. You receive `{text, durationMs, bytes, format, cost}` and nothing else; the recording itself never crosses into your frame.

The transcription is an ordinary paid call: it counts against the vault's spend caps, appears in the request ledger, and its cost is labelled `estimated` like any other.

## Driving the take from your own UI

`listen()` stays pending until the take ends. By default the **host's** bar ends it (Stop & send / Cancel) or `maxMs` expires — but an app that renders its own record button needs its own stop, so:

```
const p = sg.llm.listen({ maxMs: 120000 }); // do NOT await yet — you need the stop path
myStopBtn.onclick = () => sg.llm.listenStop(); // → p resolves with the transcript
myCancelBtn.onclick = () => sg.llm.listenCancel(); // → p rejects with EABORT, mic released
const { text } = await p;
```

- The transcript comes back through the **original `listen()` promise** — stopping does not open a second channel to read.
- Both resolve `{stopped:false}` when nothing is recording, so calling stop defensively (on unmount, on a route change) is safe and needs no error handling.
- `sg.llm.listening()` → `{recording}` if you need to render button state.
- All three sit behind the **same `llm.listen` grant** and raise **no consent prompt** — ending a take you already started is strictly less authority than starting one, and nobody should have to approve stopping.
- **The host's own Stop/Cancel stay on the bar.** An app gaining a stop button must not cost the user theirs.
- A second `listen()` while one is running is refused with `EBUSY` rather than opening a second microphone.

**Leave `model` alone unless you know the model hears.** Transcription does **not** use the vault's chat model — most chat models have no audio endpoint and OpenRouter answers `404 No endpoints found that support input audio`. `listen()` defaults to `google/gemini-3.5-flash`; passing a model that does not accept audio is refused up front with `EMODEL` and a message naming one that does. Currently accepted: `google/gemini-3.5-flash`, `google/gemini-3.1-flash-lite`, `google/gemini-3-flash-preview`, `google/gemini-3.1-flash-lite-preview`, `openai/gpt-audio`, `openai/gpt-audio-mini`, `mistralai/voxtral-small-24b-2507`. The vault's `models.allow` list still applies on top.

Extra error codes: `ENOMIC` (no microphone / sandboxed / permission refused by the browser), `EINSECURE` (not HTTPS), `EABORT` (user pressed Cancel).

**iPad note.** This works on iPad Safari — the host records `audio/mp4`, which OpenRouter accepts as `m4a` with no conversion. Desktop Chrome records `webm`, which is *not* accepted, so the host transcodes to WAV automatically. You do not need to care which happened.

## What this is not

There is no tool-calling loop. `sg.llm.chat` is a **reader**: it takes messages and returns text. If you want the model to act on the vault, *your app* decides what to do with the reply and calls `sg.vfs.*` / `sg.fs.*` itself — under the grants you already declared. That separation is deliberate: the LLM never gets ambient authority over the vault.

**Honest limitation.** The key still lives in the vault, so sharing a vault key still shares the credential with anyone who can open it. Short-lived minted credentials are planned (Phase 4) and would remove that; until then, treat a vault with an AI key configured as a vault that carries a secret.

 [← The samples](../chat-pane/samples.md) [The traps →](traps.md)

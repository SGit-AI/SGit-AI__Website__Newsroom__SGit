# 02 — The `sg.llm.*` API

The complete reference currently exists **only inside `library/guides/vault-html/AUTHORING.md`**, a 9,487-word agent authoring contract. Extracting it into a readable public reference is the single highest-value publishing act on this site.

Shipped **2 August 2026**; `listen` and `imagePart` added **3 August 2026**.

---

## 1. The surface

| Call | Grant | Returns |
|---|---|---|
| `sg.llm.available()` | — | `{ok, reason, model, remaining:{calls,cost}}` |
| `sg.llm.chat(req, onToken?)` | `chat` | `{content, usage, cost, id}` · promise carries `.requestId` |
| `sg.llm.cancel(requestId)` | — | aborts an in-flight call |
| `sg.llm.models()` | `models` | the vault's **already-filtered** allow-list |
| `sg.llm.usage()` | `usage` | `{calls, cost, remaining}` for the **whole session** |
| `sg.llm.imagePart(blobOrBytes)` | — | a content part for a multimodal message |
| `sg.llm.listen(opts?)` | `listen` | `{text, durationMs, bytes, format, cost}` |
| `sg.llm.listenStop()` / `listenCancel()` / `listening()` | `listen` | recording control and state |

**Request fields:** `messages` (required), plus optional `model`, `maxTokens`, `temperature`, `topP`, `stream: false`.

---

## 2. The three streaming properties to rely on

These are contract guarantees, not implementation details, and they are what let you write a chat UI without defensive code:

1. **The terminal reply is authoritative.** *"An app that ignores `onToken` entirely still gets the complete `content`. **Deltas are a UX affordance, never the source of truth.**"*
2. **Deltas carry only the increment** (`delta`), plus a running `acc` for convenience. *"The host coalesces them on a ~50 ms timer, so you get readable chunks rather than a postMessage per token."*
3. **`cost` is labelled** — `{value, source, estimated}`. *"`estimated: true` means it was computed from token counts × list price, not billed. **Render estimates with a `~`. Never show one as a bill.**"*

That third one is a house rule with teeth, and it should appear on the site as a rule rather than a note.

---

## 3. Error codes — branch on `err.code`

| Code | Meaning |
|---|---|
| `EPERM` | no grant |
| `ECONSENT` | user declined |
| `ENOKEY` | no key configured for this vault |
| `EREADONLY` | owner-sealed key, read-only session |
| `EBUDGET` | cap reached |
| `EMODEL` | model not allow-listed, none selected, or **it cannot read the image/audio you sent** |
| `EABORT` | cancelled |
| `EIMGSIZE` | image payload over the host ceiling |
| `EPROTO` | upstream failure |

> *"They arrive as `err.code`, so **branch on that rather than on message text.**"*

**`EMODEL` names the model.** *"A model that cannot see gets you `EMODEL` naming the model, instead of a provider error that names nothing."* That is a deliberate error-design choice and worth publishing as one.

---

## 4. Images

```js
const part = await sg.llm.imagePart(blobOrBytes);          // or a data: URL you already have
const res  = await sg.llm.chat({
    messages: [{ role: 'user', content: [
        { type: 'text', text: 'What is wrong in this screenshot?' },
        part
    ] }]
});
```

**Three things the site must carry, because each is a real trap:**

**(a) The 8190 bug — publish this verbatim.**

> *"Use `sg.llm.imagePart()` rather than encoding it yourself. It runs in your frame (no host round trip — the bytes are already yours) and **chunks base64 at 8190, not 8192**. `8192 % 3 === 2`, so a 8192-sized chunk emits `=` padding mid-string and `atob()` rejects it; **this codebase has shipped that exact bug three times.**"*

A three-times-shipped bug with the arithmetic explained is the best kind of documentation.

**(b) Vision capability is read from the live catalogue, not a hard-coded list** — *"so a new vision model works the day it ships."* And: *"note that `text->image` is an image **generator**, not a reader — it is correctly refused."*

**(c) Not a new grant.** *"An image is an ordinary `chat()` call under `permissions.llm.chat`."* And the size ceiling is the host's: *"That ceiling is not yours to raise: **it is spending the vault's key.**"*

Accepted types: **png, jpeg, webp, gif**. *"Not svg — it is a scriptable document, not a bitmap, and no provider takes it."*

Images appear in the ledger **as their own count, never folded into the character total** — *"`sg.llm.usage()` and the AI Requests pane both stay honest about what the expensive calls were."*

---

## 5. Voice

```json
{ "permissions": { "llm": { "chat": true, "listen": true } } }
```

```js
micBtn.onclick = async () => {
    try {
        const { text } = await sg.llm.listen();     // opts: {maxMs, model, prompt}
        input.value = text;
    } catch (e) {
        if (e.code === 'ECONSENT') return;           // user declined — not an error worth showing
        if (e.code === 'ENOMIC')   showTypeInstead();
    }
};
```

**Two design decisions to publish:**

> *"**`listen` is a separate grant and is never implied by `chat`.** Recording a room is a categorically different act from sending text, so an app that can talk to a model does not thereby get a microphone."* It also **asks for consent every time** by default.

> *"**Your frame never touches audio.** A sandboxed app frame has no `navigator.mediaDevices` at all, so capture happens in the host — which is also **why the recording indicator is on host chrome where the user can always see it.** You receive `{text, durationMs, bytes, format, cost}` and nothing else; the recording itself never crosses into your frame."*

The second is the better argument: the indicator is trustworthy *because* it is not the app's to draw.

---

## 6. What the host does that you do not have to

Verbatim, and this table is the API's real value proposition:

| Concern | Who handles it |
|---|---|
| **Holding the API key** | Host. *"It is never in your frame, your bundle, or any message you receive."* |
| Which models you may use | Host — `models()` is **already filtered**, so a picker built from it is automatically correct |
| Spend caps | Host. `maxCostPerSession` / `maxCallsPerSession` enforced **before** the call; you get `EBUDGET` |
| `maxTokens` | Host **clamps** it. *"Asking for more is not an error, it is just capped."* |
| Consent | Host. The first `chat()` raises a HUD prompt; declining gives `ECONSENT` |
| Whether the model can read an image | Host, from the live catalogue |
| Image size ceiling | Host (`EIMGSIZE`) |
| Cost reconciliation | Host, **two-source**: the stream's `usage.cost`, then the authoritative `/generation` lookup |

**Seven concerns an app does not implement.** That is the page's argument: the bridge is not a convenience wrapper, it is a list of things that would each be got wrong independently by every app that had to do them itself.

---

## 7. `usage()` reports the session, not the surface

> *"`usage()` reports the **whole session**, including calls made by the vault UI's own chat panel — **one bill per session, not one per surface.**"*

Which means a meter you draw in your app is the *true* total, including the host panel's spending. That is the right default and it is not the obvious one.

---

## 8. How to publish this

1. **Extract it into a real reference page**, per call, with the signature, the grant, the errors and one runnable sample.
2. **Keep `AUTHORING.md` canonical and generate from it**, or you create the second source of truth the corpus explicitly refused to create — see `08__` Q1.
3. **Lead every call with its grant.** Default-deny is the model; the grant is the first thing a reader needs.
4. **Publish the traps as their own page** — the 8190 chunking, `available()` before rendering, images clearing after one turn, estimates never shown as bills, `listen` never implied by `chat`. **That page will be the most-visited on the site.**

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
/briefs/03__the-security-model.md
==============================================================================

# 01 — The chat pane: three surfaces

The commission asked for *"the work and code samples of how to add an LLM chat pane to websites and vaults."* This document is the decision layer — **which of three surfaces you want**. `code__chat-pane-samples.md` is the code.

---

## 1. The decision table

| | **1. Vault chat panel** | **2. Beside a running app** | **3. Inside your app** |
|---|---|---|---|
| **Where** | `/vault` → ✨ AI Chat | `/en-gb/app/` → ✨ AI | your app's own UI |
| **Code required** | **none** | **none** | yes — `02__` |
| **Permission required** | **none** | **none** | `permissions.llm.chat` |
| **Who holds the key** | host, at the real origin | host, at the real origin | host — **never your frame** |
| **Who holds the microphone** | host | host | host, via `sg.llm.listen()` |
| **Can the app read the conversation?** | n/a | **no** | it *is* the app |
| **Works on existing apps unchanged** | n/a | **yes** | no |
| **Use when** | you want to chat about vault files | you want AI beside an app you did not write | AI is part of what your app *does* |

**Start at the top and stop as soon as one fits.** Surfaces 1 and 2 cost nothing to adopt and carry no attack surface of your own. Surface 3 is for when the model is part of the product, not a companion to it.

---

## 2. Surface 1 — the vault chat panel

Open it from **✨ AI Chat** in the vault header, or **➕ Add to chat** on any file. Nothing to build.

What it does, and each of these is a design decision worth publishing:

- **Attach several files.** Each shows as a chip with a `×`. **Re-adding a file replaces its contents**, so it refreshes after an edit rather than duplicating.
- **Files share one 24,000-character budget** — *"not one each, so attaching a second file cannot silently double your prompt or your bill."* Trimmed files say `TRUNCATED` **in the text the model sees**, *"so it cannot pretend to have read the whole thing."*
- **⚙ request params** — temperature, top-p, max tokens. Blank means the provider's default. **Max tokens is clamped to the vault policy, and says so when it clamps.**
- **🧾 AI Requests** — every call with its **OpenRouter generation id**, tokens, cost, latency and the files it referenced; running totals; CSV/JSON export. **Billed and estimated costs are shown separately** — *"an estimate is never rendered as a bill."*
- **🖼 paste a screenshot** — attaches as a thumbnail and goes with your **next message only, then clears**: *"unlike a file, an image left attached would silently re-send and re-bill on every turn."* Downscaled to 1568px. **If the picked model cannot read images the panel says so on attach, names it, and suggests ones that can.**
- **🎤 voice** — tap the mic, speak, tap ■. Recording is stated **in words** — *"● Recording — your microphone is on"* — *"not left to an icon."* **Cancel releases the device, not just the bar.** Transcription uses an audio-capable model (`google/gemini-3.5-flash` by default), *"not your chat model, which almost certainly cannot hear."*
- **Panels are ordinary `sg-layout` panes** — drag, resize, close. Closing **parks** them: transcript, attached files and cost pills survive reopening.

**Every one of those bullets is a small honesty mechanism**, and collectively they are the strongest argument the site can make. `TRUNCATED` in the model's own text, one shared budget rather than one per file, estimates never shown as bills, images that clear after one turn, recording announced in words. **Publish them as a list of decisions with their reasons** — that page is more persuasive than any feature tour.

---

## 3. Surface 2 — the same panel, beside a running app

Open a vault app at `/en-gb/app/#<key>` and there is a **✨ AI** button in the HUD, next to *Open Vault*. Identical chat and requests panels, beside the app.

> ***"The app is not involved.** The panel runs on host chrome at the real origin, so it holds the vault key and the microphone directly; the sandboxed app frame sees neither, cannot read the conversation, and needs no `permissions.llm.*`. **Every existing vault app gets this without being changed.**"*

App authors get a **preference, not authority**:

```json
{ "hud": { "show": { "llm": false } } }
```

`false` hides the button if a chat control would clash with their own UI; `true` forces it on in `minimal` mode, where it is off by default. *"That is a preference about chrome, not authority: it does not affect what the app itself may do."*

**This surface is the best-value thing on the whole site** — every existing app gets an AI panel for one config line or none — and it is currently documented in exactly one debrief.

---

## 4. Surface 3 — AI inside your app

This is the one that needs code and grants. Three steps, and step 2 is the one people skip.

**1. Declare the grants** in `app.json` — default-deny, like every other capability:

```json
{
  "entry": "index.html",
  "permissions": {
    "llm": { "chat": true, "models": true, "usage": true }
  }
}
```

*"`chat` is the one that spends money; `models` and `usage` are read-only. Grant only what you use."*

**2. Check availability BEFORE you render a chat UI.**

> *"`sg.llm.available()` is **not optional politeness**. Unlike other namespaces, LLM access depends on *runtime* state: whether the vault has a key configured, whether this is a read-only session, whether the budget is spent. **Ask first, then decide what to draw.**"*

```js
const a = await sg.llm.available();
if (!a.ok) { showFallbackUI(a.reason); return; }   // ENOKEY | EPERM | EREADONLY
console.log('ready:', a.model, 'remaining:', a.remaining);
```

**3. Chat.** Full samples in `code__chat-pane-samples.md`; the API in `02__`.

---

## 5. Turning it on for a vault (once)

Before any surface works, the vault needs a key:

1. Open the vault with its **full key** — *"an owner-sealed key cannot be unsealed in a read-only session — **that is cryptographic, not a policy check**."*
2. **Settings → AI models (OpenRouter)** → paste an OpenRouter key → **Test** → **Save**.
3. Optional: default model, an allowed-models list as **globs** (`anthropic/*`), and spend caps (`maxCostPerSession`, `maxCallsPerSession`, `maxTokensPerCall`).

**Two key tiers, and the choice matters:**

| Tier | Behaviour |
|---|---|
| **`owner`** (default) | Sealed with the vault's **write** key. A read-only opener gets `EREADONLY` and cannot use it |
| **`shared`** | Readable by anyone who can open the vault |

> *"Prefer `owner` unless you deliberately want every opener to be able to spend."*

And the warning that belongs on every configuration page:

> *"**Know what you are storing.** With a key configured, the vault contains a credential. Sharing the vault key shares the ability to spend it. Short-lived minted credentials are planned (Phase 4) and would remove this; **until then, treat such a vault as carrying a secret.**"*

---

## 6. Model defaults — a bug worth publishing

From the status section, and it is a good story:

> *"With no `models.default` configured the panel auto-picks, and it now tries named models first (`anthropic/claude-sonnet-5`, then opus-5, sonnet-4, gemini-3.5-flash, gpt-5). **It used to match only on the vendor prefix against an alphabetically sorted list, which picked `anthropic/claude-3-haiku` — the oldest model on the key, and not a vision model.**"*

Alphabetical order picked the worst available model, silently, and the symptom would have looked like *"the AI is bad"* rather than *"the default is wrong."* An explicit `models.default` and the `models.allow` list still win.

**Publish it under a "defaults are a design decision" heading.** It is exactly the kind of thing the site should teach.

---

## 7. What to build first

1. **The decision table** (§1) as the landing page. Most readers will discover they need no code at all, which is the right outcome.
2. **Surface 2's one-line HUD config**, because *"every existing vault app gets this without being changed"* is the single highest-value sentence in the corpus and it is buried in a debrief.
3. **The honesty-mechanism list** (§2), as decisions-with-reasons rather than features.
4. **Then the code** — `02__` and the samples.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
/briefs/02__the-sg-llm-api.md
==============================================================================

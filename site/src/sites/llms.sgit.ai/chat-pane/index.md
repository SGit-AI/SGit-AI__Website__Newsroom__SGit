# Adding an LLM chat pane

*Source: <https://llms.sgit.ai/chat-pane/index.html> · site v0.2.0 · the markdown twin of this page, generated from it.*

---

[llms.sgit.ai](../index.md) / chat-pane

# Adding an LLM chat pane

This page is the decision layer: **which of three surfaces you want**. Two of them need no code at all, and a reader who leaves having written nothing has had the best outcome this page can produce. [The samples](samples.md) are for the third.

## The decision table

| | 1. Vault chat panel | 2. Beside a running app | 3. Inside your app |
|---|---|---|---|
| **Where** | `/vault` → ✨ AI Chat | `/en-gb/app/` → ✨ AI | your app's own UI |
| **Code required** | **none** | **none** | yes |
| **Permission required** | **none** | **none** | `permissions.llm.chat` |
| **Who holds the key** | host, at the real origin | host, at the real origin | host, **never your frame** |
| **Who holds the microphone** | host | host | host, via `sg.llm.listen()` |
| **Can the app read the conversation?** | n/a | **no** | it *is* the app |
| **Works on existing apps unchanged** | n/a | **yes** | no |
| **Use when** | you want to chat about vault files | you want AI beside an app you did not write | AI is part of what your app *does* |

Start at the top and stop as soon as one fits.

Surfaces 1 and 2 cost nothing to adopt and carry no attack surface of your own. Surface 3 is for when the model is part of the product rather than a companion to it, and it is the only one where you are responsible for getting the honesty mechanisms right.

## Surface 1 — the vault chat panel

**Grants needed:** none **Code:** none

Open it from **✨ AI Chat** in the vault header, or **➕ Add to chat** on any file. There is nothing to build. What it does is worth reading closely, because **every behaviour below is a design decision rather than a feature**, and the decisions are the argument.

### The honesty mechanisms, as decisions with their reasons

These are the best work in the LLM bridge and, until this page, they were published nowhere. Each one is a small refusal to mislead, and collectively they are more persuasive than any feature tour. They are also the part that [transfers unchanged](../websites/index.md#transfers) to a chat pane with no vault behind it at all.

#### Attached files share one 24,000-character budget, not one each

Attach a second file and the budget is divided, not doubled. "Not one each, so attaching a second file cannot silently double your prompt or your bill."

#### A trimmed file says `TRUNCATED` in the text the model sees

The marker is not in the UI for the user. It is in the prompt, in the model's own input. "So it cannot pretend to have read the whole thing."

#### Re-adding a file replaces its contents rather than appending them

Attaching the same file twice refreshes it after an edit instead of sending it twice. A duplicate is a silent doubling of the same bill, for the same text.

#### Billed and estimated costs are shown separately

The ledger renders an estimate with a `~` and a reconciled figure without one. "An estimate is never rendered as a bill."

#### A pasted image goes with your next message only, then clears

Unlike an attached file, an image does not persist across turns. "An image left attached would silently re-send and re-bill on every turn."

#### Recording is stated in words, not left to an icon

The bar reads **● Recording — your microphone is on**, and cancelling releases the device rather than just hiding the bar. An icon is a symbol a user has to have learned. A sentence is not.

#### A model that cannot see says so on attach, and names alternatives

The panel checks the live model catalogue when you attach the image, not when you send it. Failing before the call costs nothing; failing after it costs a call.

#### `maxTokens` is clamped to the vault policy, and says so when it clamps

Asking for more than the vault allows is capped rather than refused. A silent clamp and a hard error are both worse than a clamp that tells you.

The rest of the panel is ordinary and pleasant: **⚙ request params** for temperature, top-p and max tokens, where blank means the provider's default; **🧾 AI Requests** listing every call with its OpenRouter generation id, tokens, cost, latency and the files it referenced, with running totals and CSV or JSON export; and panels that are ordinary `sg-layout` panes, so closing one **parks** it and the transcript, attachments and cost pills survive reopening.

## Surface 2 — the same panel, beside a running app

**Grants needed:** none **Code:** none

Open a vault app at `/en-gb/app/#<key>` and there is a **✨ AI** button in the HUD, next to *Open Vault*. It opens the identical chat and requests panels, beside the app.

> The app is not involved. The panel runs on host chrome at the real origin, so it holds the vault key and the microphone directly; the sandboxed app frame sees neither, cannot read the conversation, and needs no `permissions.llm.*`. Every existing vault app gets this without being changed.

An app author gets a **preference, not authority**. In `app.json`:

```
{ "hud": { "show": { "llm": false } } }
```

`false` hides the button if a chat control would clash with the app's own UI; `true` forces it on in `minimal` mode, where it is off by default. The flag is on by default in `full` mode and off in `minimal`, `hidden` and `none`. It is a preference about chrome and not authority: it does not change what the app itself may do, and it cannot suppress the sovereignty rail.

**Verified against the shipped code**, not only against the brief: `hud.show.llm` is still the config key and still carries those per-mode defaults, at product version v0.33.62. [The other claims this site re-checked](../shipped/index.md#verified), including one where the contract and the code now disagree.

## Surface 3 — AI inside your own app

**Grants needed:** llm.chat llm.models llm.usage **Code:** yes

Three steps, and step 2 is the one people skip.

**1. Declare the grants** in `app.json`. Default-deny, like every other capability:

```
{
 "entry": "index.html",
 "permissions": {
 "llm": { "chat": true, "models": true, "usage": true }
 }
}
```

`chat` is the one that spends money; `models` and `usage` are read-only. Grant only what you use, and note that [`listen` is never implied by `chat`](../security/index.md#ladder).

**2. Check availability before you render a chat UI.** This is the step that gets skipped and the one the contract is most insistent about:

> `sg.llm.available()` is not optional politeness. Unlike other namespaces, LLM access depends on *runtime* state: whether the vault has a key configured, whether this is a read-only session, whether the budget is spent. Ask first, then decide what to draw.

```
const a = await sg.llm.available();
if (!a.ok) { showFallbackUI(a.reason); return; } // ENOKEY | EPERM | EREADONLY
console.log('ready:', a.model, 'remaining:', a.remaining);
```

**3. Chat.** [Eight runnable samples](samples.md), and [the full reference](../api/index.md).

## Turning it on for a vault, once

Before any surface works, the vault needs a key:

1. Open the vault with its **full key**. An owner-sealed key cannot be unsealed in a read-only session, and **that is cryptographic rather than a policy check**.
1. **Settings → AI models (OpenRouter)**, paste an OpenRouter key, **Test**, **Save**.
1. Optionally: a default model, an allowed-models list as globs (`anthropic/*`), and spend caps (`maxCostPerSession`, `maxCallsPerSession`, `maxTokensPerCall`).

Use an obviously fake placeholder anywhere you write this down. This site never prints a realistic-looking key, and [its pre-release gate refuses to publish anything shaped like one](../admin/index.md#checks).

### Two key tiers, and the choice matters

| Tier | Behaviour |
|---|---|
| `owner` (default) | Sealed with the vault's **write** key. A read-only opener gets `EREADONLY` and cannot use it |
| `shared` | Readable by anyone who can open the vault |

Prefer `owner` unless you deliberately want every opener to be able to spend.

**Know what you are storing.** With a key configured, the vault contains a credential. **Sharing the vault key shares the ability to spend it.** Short-lived minted credentials are planned (Phase 4) and would remove this; until then, treat such a vault as carrying a secret. This changes the sharing calculus for a vault: [publishing a read key for a vault with AI configured is not the same act as publishing one for a plain vault](../security/index.md#storing).

## What to reach for first

1. **The decision table above.** Most readers need no code, which is the right outcome.
1. **Surface 2's one config line**, if you already have apps. Every one of them gets a chat panel.
1. **The honesty mechanisms**, if you are building surface 3. They are the difference between a demo and something a person can trust with a bill.
1. **Then the code**: [the samples](samples.md), [the reference](../api/index.md), [the traps](../api/traps.md).

 [← Front page](../index.md) [The code samples →](samples.md)

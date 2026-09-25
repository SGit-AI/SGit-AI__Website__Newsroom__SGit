# 03 — The security model, and the gap in it

The thesis is *"your app calls a model without ever holding an API key."* This document is how that works, and — in §5 — the one place it currently stops short of a guarantee.

---

## 1. Where the key lives

`.vault/llm/config.json`, **inside the permission floor**. The app cannot read it. The host makes every call.

> *"Holding the API key | **Host.** It is never in your frame, your bundle, or any message you receive."*

**Two tiers, and the difference is cryptographic rather than a policy check:**

| Tier | Behaviour |
|---|---|
| **`owner`** (default) | Sealed with the vault's **write** key. A read-only opener gets `EREADONLY` — *"an owner-sealed key cannot be unsealed in a read-only session — that is cryptographic, not a policy check"* |
| **`shared`** | Readable by anyone who can open the vault |

> *"Prefer `owner` unless you deliberately want every opener to be able to spend."*

---

## 2. The four-layer ladder

Every call passes four independent checks, and each one fails with its own code:

| Layer | Mechanism | Failure |
|---|---|---|
| **1. Grant** | `permissions.llm.*` in `app.json`, **default-deny** | `EPERM` |
| **2. Consent** | the first `chat()` raises a HUD prompt the user must accept | `ECONSENT` |
| **3. Budget** | `maxCostPerSession` / `maxCallsPerSession`, enforced **before** the call | `EBUDGET` |
| **4. Policy** | model allow-list (globs); `maxTokens` **clamped**, not rejected | `EMODEL` |

**Grant, consent, budget, policy.** A developer decision, a user decision, a spend decision and an owner decision — four different people can each say no, and the failure tells you which one did.

**The grants are deliberately narrow:** `chat` spends money; `models` and `usage` are read-only; **`listen` is never implied by `chat`.**

> *"Recording a room is a categorically different act from sending text, so an app that can talk to a model does not thereby get a microphone."*

---

## 3. What the frame cannot reach

The sandboxed app frame has **no `navigator.mediaDevices` at all**. Audio capture happens in the host — which is also why the recording indicator lives on host chrome:

> *"**the recording indicator is on host chrome where the user can always see it.** You receive `{text, durationMs, bytes, format, cost}` and nothing else; the recording itself never crosses into your frame."*

**An indicator the app cannot draw is an indicator the app cannot fake.** That is the strongest security argument in the whole design and it should be stated in exactly those terms.

Same principle on surfaces 1 and 2 (`01__`): the chat panel runs on host chrome at the real origin, so the app frame *"sees neither, cannot read the conversation, and needs no `permissions.llm.*`."*

---

## 4. Cost integrity

Three mechanisms, and they are honesty features rather than security ones — but they belong here because they are all about not being able to mislead:

- **Two-source reconciliation.** *"Host, two-source (stream `usage.cost`, then the authoritative `/generation` lookup)."*
- **Estimates are labelled and must be rendered as estimates.** `{value, source, estimated}` — *"Render estimates with a `~`. **Never show one as a bill.**"*
- **Images are counted separately**, never folded into the character total, *"so `sg.llm.usage()` and the AI Requests pane both stay honest about what the expensive calls were."*

And `usage()` reports the **whole session** including the host panel's own calls — *"one bill per session, not one per surface."*

---

## 5. ⚠️ The gap — publish this sentence

From the 2 August capability brief's *Not built* section:

> **CSP egress lockdown.** *"App frames are not yet served with a `connect-src` that blocks direct network access, so a malicious app could still call an LLM provider itself with its own key. **The bridge protects *your* key; it is not yet a boundary that prevents all egress. This is the gap that turns the current design from a convenience into a guarantee.**"*

**Read precisely what that does and does not say.**

- ✅ The vault's key is genuinely protected. It never enters the frame.
- ✅ Spend against the vault's key is genuinely capped, consented and logged.
- ❌ A malicious app can still reach the network with **its own** credential, so the bridge is **not** an egress boundary.

**The honest framing for the site:** the model here is *"we protect the credential you trusted us with"*, not *"nothing leaves this frame."* Those are different claims and only the first is currently true.

**Do not soften it, and do not bury it.** A site whose front page says *"your app never holds the key"* must carry the qualification within one click, because the corpus states it plainly and any reader who finds the brief first will trust the site less for having omitted it.

The named fix is **Phase 4 minted credentials** — *"short-lived, budget-capped tokens from SG-API so the vault holds a **reference**, not a key."* Described as *"what would make vault-sharing safe with AI configured, and… the commercially load-bearing piece."*

---

## 6. The standing warning about configured vaults

> *"**Know what you are storing.** With a key configured, the vault contains a credential. **Sharing the vault key shares the ability to spend it.** Short-lived minted credentials are planned (Phase 4) and would remove this; until then, **treat such a vault as carrying a secret.**"*

This connects directly to the estate's read-key/write-key doctrine (`standards.sgit.ai` `03__`, `open-source.sgit.ai` `02__` §6): **a vault with an LLM key configured is a vault whose sharing calculus has changed.** Publishing a read key for such a vault is not the same act as publishing one for a plain vault, and the site should say so beside the key-tier table in `01__` §5.

---

## 7. Two other gaps worth naming

**ViV kernel parity.** *"`sg.llm.*` is served by the `/en-gb/app/` host. Nested vault-in-vault kernels (`kernel-app-handlers.js`) do not relay it yet."* So an app running inside a nested vault silently has no LLM bridge.

**No per-vault audio model setting.** The transcription model is a constant (`google/gemini-3.5-flash`). Fine as a default; not configurable when it should be, since the chat model and the audio model are necessarily different and only one of them is a setting.

---

## 8. What the security page should say

1. **Lead with the ladder** (§2) — grant, consent, budget, policy — because it explains all nine error codes in one table.
2. **Make §3's argument explicitly**: the microphone indicator is trustworthy *because the app cannot draw it*.
3. **State the CSP gap in the same breath as the thesis**, not in a footnote.
4. **Put the "know what you are storing" warning next to the setup instructions**, where the decision is actually made.
5. **Name Phase 4** as the fix, and be clear it is not shipped.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
/briefs/04__websites-vs-vaults.md
==============================================================================

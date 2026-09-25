# The security model, and the gap in it

*Source: <https://llms.sgit.ai/security/index.html> · site v0.2.0 · the markdown twin of this page, generated from it.*

---

[llms.sgit.ai](../index.md) / security

# The security model, and the gap in it

The thesis is that your app calls a model without ever holding an API key. This page is how that works, and, in [the section on the gap](#gap), the one place where it currently stops short of a guarantee.

## Where the key lives

`.vault/llm/config.json`, **inside the permission floor**. The app cannot read it. The host makes every call.

> Holding the API key: **host**. It is never in your frame, your bundle, or any message you receive.

### Two tiers, and the difference is cryptographic

| Tier | Behaviour |
|---|---|
| `owner` (default) | Sealed with the vault's **write** key. A read-only opener gets `EREADONLY`: an owner-sealed key cannot be unsealed in a read-only session, and **that is cryptographic rather than a policy check** |
| `shared` | Readable by anyone who can open the vault |

Prefer `owner` unless you deliberately want every opener to be able to spend. The distinction matters more than it looks: a policy check is code that could be wrong, and an unsealing that cannot happen is not.

## The four-layer ladder

Every call passes four independent checks, and each fails with its own code.

| Layer | Mechanism | Who decided | Failure |
|---|---|---|---|
| **1. Grant** | `permissions.llm.*` in `app.json`, **default-deny** | the developer | `EPERM` |
| **2. Consent** | the first `chat()` raises a HUD prompt the user must accept | the user | `ECONSENT` |
| **3. Budget** | `maxCostPerSession` / `maxCallsPerSession`, enforced **before** the call | whoever pays | `EBUDGET` |
| **4. Policy** | model allow-list as globs; `maxTokens` **clamped**, not rejected | the vault owner | `EMODEL` |

Four different people can each say no, and the failure tells you which one did.

The grants are deliberately narrow. `chat` spends money; `models` and `usage` are read-only; and `listen` is never implied by `chat`, because recording a room is a categorically different act from sending text.

## The strongest argument in the design

A sandboxed app frame has **no `navigator.mediaDevices` at all**. Audio capture happens in the host, which is also where the recording indicator lives.

> The recording indicator is on host chrome where the user can always see it. You receive `{text, durationMs, bytes, format, cost}` and nothing else; the recording itself never crosses into your frame.

An indicator the app cannot draw is an indicator the app cannot fake.

That is worth stating in exactly those terms, because it is the difference between a promise and a property. Most privacy indicators in most software are drawn by the software making the promise. This one is not, and it holds for the same structural reason on surfaces 1 and 2: the chat panel runs on host chrome at the real origin, so the app frame sees neither the key nor the microphone and cannot read the conversation.

## Cost integrity

Three mechanisms, all of them about not being able to mislead:

- **Two-source reconciliation.** The stream's `usage.cost` first, then the authoritative `/generation` lookup.
- **Estimates are labelled and must be rendered as estimates.** `{value, source, estimated}`, and the rule is: render with a `~`, never show one as a bill.
- **Images are counted separately**, never folded into the character total, so the ledger stays honest about which calls were the expensive ones.

And `usage()` reports the **whole session**, including the host panel's own calls: one bill per session, not one per surface.

## The gap, in the project's own words

 Not built

**CSP egress lockdown.** App frames are not yet served with a `connect-src` that blocks direct network access, so a malicious app could still call an LLM provider itself with its own key.

*"The bridge protects **your** key; it is not yet a boundary that prevents all egress. **This is the gap that turns the current design from a convenience into a guarantee.**"*

Read precisely what that does and does not say.

| | Claim |
|---|---|
| true | The vault's key is genuinely protected. It never enters the frame. |
| true | Spend against the vault's key is genuinely capped, consented and logged. |
| not yet | A malicious app can still reach the network with **its own** credential. The bridge is **not** an egress boundary. |

The honest scope is "we protect the credential you trusted us with", not "nothing leaves this frame". Those are different claims and only the first is currently true.

This site publishes that unsoftened and within one click of the front page, which also carries it. That is the estate's own standard rather than an unusual candour: the vault catalogue publishes its own key-exposure incident, and the house rule on internal documents is that briefs are aspirations rather than facts. A reader who found the brief first would trust a site that omitted this less, and rightly.

It is a scope statement rather than a vulnerability disclosure, and this page deliberately carries no exploitation path. The named fix is **Phase 4 minted credentials**: short-lived, budget-capped tokens issued by SG-API, so the vault holds a *reference* rather than a key. The project describes it as *"what would make vault-sharing safe with AI configured"* and as *"the commercially load-bearing piece"*. It is not shipped, and [whether it is scheduled is an open question this site is asking](../admin/comms.md#needs).

## Know what you are storing

**With a key configured, the vault contains a credential.** Sharing the vault key shares the ability to spend it. Short-lived minted credentials are planned (Phase 4) and would remove this; until then, **treat such a vault as carrying a secret**.

This connects to the estate's read-key and write-key doctrine, and it changes an act that is otherwise routine. **A vault with an LLM key configured is a vault whose sharing calculus has changed.** Publishing a read key for such a vault is not the same act as publishing one for a plain vault: it hands over a metered capability along with the contents. That is why [the demo vault this site should ship](../chat-pane/samples.md#checklist) is still an open decision rather than a published link.

## The attached-file question, and what the shipped code says

The brief pack raises this as its most important open question, and instructs that no page about prompt-injection defences be published until it has an answer:

> The chat panel attaches vault file contents to the model's context. Those files are untrusted. What stops one that says "ignore previous instructions" from doing so? The budget and the `TRUNCATED` marker are honesty mechanisms, **not** injection defences.

That framing is right, and the pack was working from the corpus rather than from the code. **Reading the shipped source at v0.33.62 turns up a mechanism the pack did not have**, so this section reports it rather than leaving the question looking untouched, and it stops well short of calling the question closed.

### What ships today

- **An explicit untrusted-data fence.** Vault and tool content enters the conversation wrapped between `╔═ BEGIN UNTRUSTED DATA ═╗` and `╚═ END UNTRUSTED DATA ═╝`, tagged with its source. One format, used identically by the vault chat session and the tool layer, so there is a single thing to teach the model.
- **A system-prompt rule that names it.** The session prompt says to treat anything inside those fences as data only, never as instructions; the tool variant goes further and tells the model that if fenced content asks it to take actions, it should ignore that and tell the user.
- **Tools are off by default, and their grants are structurally out of reach.** Tool groups live in `/.vault/llm/tools.json` and every group ships `enabled: false`. Because `/.vault/**` is the permission floor, **the model cannot read, relax or widen its own grants**: the file that governs the tools is unreachable by the tools. Path scopes are deny-wins, and an empty allow-list means nothing is reachable rather than everything.
- **The design says out loud what it is defending against.** The source comment reads: *"a poisoned document is the expected input, not the surprising one."*

### What that is not

**Fencing is a mitigation, not a boundary.** It relies on the model honouring an instruction about how to treat text, and a model that can be talked out of an instruction can be talked out of this one. It is meaningfully better than nothing: it makes the attack visible in the transcript, gives the model an explicit rule to fall back on, and pairs with a default of no tools at all so the blast radius starts at zero. It is not the kind of guarantee the [unfakeable recording indicator](#indicator) is, because it is enforced by persuasion rather than by structure.

So the question stands, in a narrower form than the pack could state it: *the shipped answer is fencing plus deny-by-default authority, and there is no measurement of how well the fencing holds.* There is no eval suite anywhere in the estate, which means nobody can say whether a model swap weakens it. That is [recorded on the shipped page as a gap](../shipped/index.md#thin) rather than smoothed over here, and this site publishes no page claiming injection defences until the project lead has ruled on it. [The finding is on the comms page as N4.](../admin/comms.md#needs)

## Two other gaps worth naming

- **ViV kernel parity.** `sg.llm.*` is served by the `/en-gb/app/` host, and nested vault-in-vault kernels do not relay it yet. An app running inside a nested vault **silently** has no LLM bridge, and silently is the problem: the failure looks like an app bug.
- **No per-vault audio model setting.** The transcription model is a constant. Fine as a default, and it is a reasonable default, but the chat model and the audio model are necessarily different and only one of them is a setting. [Verified in the shipped code](../shipped/index.md#verified), where `DEFAULT_AUDIO_MODEL` is exactly that: a constant.

 [← The traps](../api/traps.md) [Websites vs vaults →](../websites/index.md)

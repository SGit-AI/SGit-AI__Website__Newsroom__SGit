# llms.sgit.ai — your app calls a language model without ever holding an API key

> The key lives in `.vault/llm/config.json`, inside the permission floor: the app cannot
> read it, and the host makes the call. You send messages and receive text. Everything
> else here follows from one decision, that the credential and the code that spends it
> should not sit in the same trust boundary.

*Source: <https://llms.sgit.ai/index.html> · site v0.2.0 · markdown twin of the front page.*

---

## The claim, and its limit

That sentence is true, and it is not the whole sentence. The bridge protects *the vault's*
key: it never enters your frame, your bundle, or any message you receive. It is **not yet
an egress boundary**. App frames are not served with a `connect-src` that blocks direct
network access, so a malicious app could still reach a provider itself, with its own
credential.

The project's own capability brief puts it in one line, and this site quotes it rather
than paraphrasing:

> "The bridge protects your key; it is not yet a boundary that prevents all egress. This
> is the gap that turns the current design from a convenience into a guarantee."

So the honest scope is **"we protect the credential you trusted us with"**, not "nothing
leaves this frame". Those are different claims and only the first is currently true.
[The gap, in full, and the fix that would close it](security/index.md).

## There are three chat-pane surfaces, not one

They differ in who holds the key and who needs permission, and most people assume there is
only one. Start at the top and stop as soon as one fits.

| Surface | Where | Code | Permission | Use when |
|---|---|---|---|---|
| **1. The vault chat panel** | `/vault` → ✨ AI Chat | **none** | **none** | You want to chat about vault files |
| **2. The same panel, beside a running app** | `/en-gb/app/` → ✨ AI | **none** | **none** | You want AI beside an app you did not write |
| **3. AI inside your own app** | your app's UI | yes | `permissions.llm.chat` | The model is part of what your app *does* |

Surfaces 1 and 2 run on **host chrome at the real origin**, so they hold the vault key and
the microphone directly; the sandboxed app frame sees neither and cannot read the
conversation. [The full decision table](chat-pane/index.md).

> Every existing vault app gets this without being changed.

Surface 2 is the highest-value thing on this site and until now it was documented in
exactly one debrief. An app written before the AI panel existed, by someone who has never
heard of it, gets a working chat panel beside it and needs no `permissions.llm.*` at all,
because the app is not involved.

## Four doors

- [**Add a chat pane**](chat-pane/index.md) — the decision table, all three surfaces, the
  honesty mechanisms published as decisions with their reasons, and turning a vault on
- [**The code samples**](chat-pane/samples.md) — eight samples for the surface that needs
  code, plus the pre-ship checklist
- [**The `sg.llm.*` reference**](api/index.md) — ten calls, four grants, nine error codes,
  generated from the canonical contract rather than hand-copied
- [**The security model**](security/index.md) — grant, consent, budget, policy: four
  independent checks and an error that tells you which one said no

## This estate's LLM position is not about models

The earliest dated artefact in the whole estate is a talk: *Deterministic GenAI Outputs
with Provenance*, OWASP AppSec Lisbon, 28 June 2024. Two years later the position has not
moved: **a model output is only usable when you can say where it came from**. Not "models
are unreliable, use a better one".

- [Provenance](provenance/index.md) — the oldest thread, and the spine of the rest
- [The provider layer](openrouter/index.md) — one key for many models, and what that costs
- [Local and offline](local/index.md) — Ollama, a flight, and the sovereignty argument
- [Pages that models read](agents/index.md) — being readable to a model that arrives from outside
- [Websites vs vaults](websites/index.md) — the thin half, labelled as such

[What is actually shipped, and what is not](shipped/index.md) keeps the list of absences:
no evals, no structured-output guidance, no model routing, and a fully instrumented cost
ledger nobody has analysed.

## Participant disclosure

Published by the sgit project, which builds the vault layer and the LLM bridge this site
documents. This is a participant documenting its own product, and the places where the
approach loses are listed rather than implied.
[The disclosure](about/participant.md).

## For machines

- [llms.txt](llms.txt) — the map, written as a document rather than a link list
- [llms-full.txt](llms-full.txt) — the whole site plus its brief pack in one fetch
- Every page has a `.md` twin at its own path, and links inside a twin point at twins

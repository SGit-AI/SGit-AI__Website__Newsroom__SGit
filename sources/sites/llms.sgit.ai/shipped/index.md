# What is shipped, and what is not

*Source: <https://llms.sgit.ai/shipped/index.html> · site v0.2.0 · the markdown twin of this page, generated from it.*

---

[llms.sgit.ai](../index.md) / shipped

# What is shipped, and what is not

A site about LLM engineering that lists what it has not built is more credible than one that does not. This page is the shipped list unsoftened, the absences with their sizes, and the claims this site checked for itself rather than repeating.

## Shipped

Quoted from the capability brief of 2 August 2026, and it is an unusually complete list for something that had no public documentation until this site:

 Shipped

The shared engine (`SGLlm`), vault key and policy resolution (`SGLlmVault`), the admin settings panel, the host-native chat panel (multi-file, params, ledger, **voice**, **pasted screenshots**) on **both** `/vault` and `/en-gb/app/`, and the `sg.llm.*` bridge with permission, consent, budget, streaming, cancel, `listen` and `imagePart`.

Since then, and not in that brief: an **opt-in tool layer** for the vault's own chat, with tool groups that ship disabled, path scopes where deny wins, and grants stored in a file the tools structurally cannot reach. [It is described on the security page](../security/index.md#injection), because the reason it exists is the injection question.

## Not built, and one item is load-bearing

| Item | What it means today |
|---|---|
| **CSP egress lockdown** | App frames are not served with a `connect-src` that blocks direct network access, so a malicious app could still call a provider itself with its own key. *"The bridge protects your key; it is not yet a boundary that prevents all egress. This is the gap that turns the current design from a convenience into a guarantee."* [In full](../security/index.md#gap) |
| **Phase 4 minted credentials** | Short-lived, budget-capped tokens so the vault holds a *reference* rather than a key. Described as what would make vault-sharing safe with AI configured, and as *"the commercially load-bearing piece"*. Whether it is scheduled is [an open question this site is asking](../admin/comms.md#needs) |
| **ViV kernel parity** | Nested vault-in-vault kernels do not relay `sg.llm.*`. An app inside a nested vault **silently** has no bridge |
| **A per-vault audio model setting** | The transcription model is a constant. Reasonable as a default; not configurable when it should be |
| **The `sg-llm-chat` web component** | Half the commission. No component, no documented pattern, no code for a chat pane on a plain website. [The options, compared honestly](../websites/index.md) |
| **The demo vault that is the documentation** | One app exercising every call, published as both the demo and the test, so [the samples](../chat-pane/samples.md) would be verified by existing rather than by review. Blocked on a real decision: [a vault with a key configured carries a credential](../security/index.md#storing) |

## The thin threads, with their sizes

Measured across the corpus. The counts are from the brief pack, dated 24 August 2026, and are quoted as a dated measurement rather than presented as a standing fact.

| Topic | Files | What that means |
|---|---|---|
| **Evals** | **0** | No eval suite, no benchmark, no regression test for prompt behaviour. Nothing would catch a model swap changing an output. **The most conspicuous absence here**, and it sits directly against [a thesis about provenance](../provenance/index.md) |
| **Model routing** | **1** | One mention. No fallback chain, no cost or quality tiering, no routing logic |
| **Cost per token** | **2** | Despite a full two-source reconciled ledger with CSV export. [The data exists and nobody has looked at it](../openrouter/index.md#ledger) |
| **Structured output** | 41 | `Type_Safe` validates the *result*; nothing documents how the *request* is shaped to get a valid one |
| **Hallucination** | 45 | Mostly framed as a grounding problem rather than a model problem, which is a position rather than a gap |
| **Embeddings** | 100 | Mentioned. No vector store, no retrieval implementation |
| **Prompt injection** | 92 | Real, and concentrated in the agent-to-agent and sentinel clusters. [What ships against the case this product creates](../security/index.md#injection) |

Three of these are load-bearing: evals, structured output and model routing are the difference between a working integration and an engineered one.

## What this site checked for itself

The brief pack's own closing instruction was to verify its claims against the shipped code rather than only against the contract, since the API is young and moved twice in two days. This site did, at product version **v0.33.62**.

| Claim | Result |
|---|---|
| Base64 chunked at 8190, not 8192 | confirmed in the shipped encoder, with the arithmetic in a comment |
| One 24,000-character budget shared across attached files | confirmed: `MAX_CONTEXT_CHARS = 24000`, commented as the total across *all* files |
| The default-model list, after the alphabetical-picker bug | confirmed, and [quoted exactly](../openrouter/index.md#defaults) rather than from the brief |
| `hud.show.llm` is still the config key, off by default in `minimal` | confirmed, with per-mode defaults intact |
| The transcription model is a constant | confirmed: a `DEFAULT_AUDIO_MODEL` constant, with a fixed list of accepted audio models |
| The attached-file injection question is unaddressed | superseded: a fenced untrusted-data mechanism ships. [What it does and does not promise](../security/index.md#injection) |
| "There is no tool-calling loop" | no longer true: see below |

## One place where the contract and the code disagree

 Contract drift

The canonical authoring contract states, in the section [this site generates its reference from](../api/index.md): *"There is no tool-calling loop. `sg.llm.chat` is a **reader**: it takes messages and returns text."*

That is still true of `sg.llm.chat`, the bridge an app calls. It is **no longer true of the product**: the vault's own chat panel ships an opt-in tool layer with a bounded tool loop, read-tier groups for the session ledger and for reading files, and per-group path scopes.

Both statements can be true at once, and a reader of the contract alone would not know the second one exists. That is not a bug in either place; it is what happens when a contract for app authors and a product feature move at different speeds. It is recorded here because [this site generates its reference from that contract](../api/index.md), so anything the contract does not say, this site does not say either, unless it says so here.

Reported to the project lead as [N5](../admin/comms.md#needs).

## The open questions, published unresolved

The brief pack carries eight, and the estate's habit is to publish them open rather than settle them quietly. Their current state on this site:

| | Question | Where it stands |
|---|---|---|
| Q1 | How does a public reference avoid becoming a second source of truth? | answered by mechanism: [the reference is generated from the canonical contract](../api/index.md) and the gate fails if it drifts |
| Q2 | Who owns the `/vault` chat-panel page, this site or `sgit.ai`? | proposed: this site owns the capability, `sgit.ai` owns the product tour. [On the network page](../network/index.md), awaiting confirmation |
| Q3 | What stops an attached vault file from injecting the prompt? | narrowed: fencing plus deny-by-default authority ships, and nothing measures how well it holds. [In full](../security/index.md#injection). No injection-defences page until the project lead rules |
| Q4 | Can the demo vault publish a read key at all? | open, and it blocks the demo. Hard caps chosen for publication, or BYOK |
| Q5 | When does the CSP gap close, and what does the site claim until then? | answered for the site: it claims the narrower thing, on [the front page](../index.md#thesis) and [the security page](../security/index.md#gap). The schedule is not this site's to set |
| Q6 | Is bring-your-own-key in the browser acceptable for a public page? | open. Honest, and it converts badly. [The trade](../websites/index.md#options) |
| Q7 | Should transcription model choice be per-vault? | open. Confirmed a constant in the shipped code |
| Q8 | What happens to `sg.llm.*` in nested vaults? | open. Not relayed, and the silence is the problem |

## The build order, and where this site is on it

| # | Section | State |
|---|---|---|
| 1 | [/chat-pane/](../chat-pane/index.md) and [its samples](../chat-pane/samples.md): the commission | published |
| 2 | [/api/](../api/index.md) and [/api/traps/](../api/traps.md) | published, generated |
| 3 | [/security/](../security/index.md), with the gap stated plainly | published |
| 4 | [/websites/](../websites/index.md): the thin half | published as a gap |
| 5 | [/provenance/](../provenance/index.md) | published |
| 6 | [/local/](../local/index.md), and [/openrouter/](../openrouter/index.md) | published |
| 7 | /shipped/ | this page |
| — | /injection/ | held, deliberately, until Q3 is ruled on |
| — | The demo vault app | blocked on Q4 |
| — | The `sg-llm-chat` component | not started |

 [← Pages that models read](../agents/index.md) [The documents →](../documents/index.md)

# Comms: tasks, requests & status

The working channel between the project lead and the site agent, kept in public on the site itself. Updated on every release. Current release: **v0.2.0**, 25 August 2026. Full history: [versions](versions.md).

## Needed from the project lead

| # | Request | Why it blocks | Status |
|---|---|---|---|
| N4 | **Rule on Q3, now that it has moved.** The pack calls the attached-file injection question the most important open question on the site and instructs that no injection page ship until it is answered. Reading the shipped source at v0.33.62 turns up a mechanism the pack did not have: an explicit `BEGIN/END UNTRUSTED DATA` fence around vault and tool content, a system-prompt rule telling the model to treat fenced text as data and to report anything inside it that asks for action, tool groups that ship `enabled: false`, and grants stored in `/.vault/llm/tools.json` where the tools structurally cannot reach them. [Published as a narrowing rather than an answer](../security/index.md#injection), because fencing is enforced by persuasion and nothing measures how well it holds. **Two calls are yours:** whether that is enough to lift the HOLD on the injection material in the source manifest, and whether the fencing claim may be stated more strongly than this site currently states it | The `/injection/` page and two tier-2 manifest rows stay held until you rule | waiting on human |
| N5 | **The contract and the code disagree about tool calling.** `AUTHORING.md` says *"There is no tool-calling loop. `sg.llm.chat` is a reader."* That is still true of the bridge and **no longer true of the product**: the vault's own chat ships an opt-in tool layer with a bounded loop, read-tier groups and per-group path scopes. Both statements are individually correct, and a reader of the contract alone would not know the second exists. Since [this site generates its reference from that contract](../api/index.md), the drift propagates here by design. **Recommendation:** a paragraph in the contract's own "What this is not" section, pointing at the tool layer as a separate, non-app-facing capability | Not blocking. It is [recorded on the shipped page](../shipped/index.md#drift) and will keep being recorded until the contract moves | reported |
| N6 | **The demo vault, and whether it can publish a read key at all** (pack Q4). The pack's own recommended artefact is a vault app that exercises every call, published as both the documentation and its test, which would also make [the samples](../chat-pane/samples.md) verified by existing rather than by review. It cannot be published casually: a vault with an LLM key configured carries a credential. Two workable answers, and the choice is yours: a `shared`-tier key with hard `maxCostPerSession` and `maxCallsPerSession` caps chosen deliberately for publication, or bring-your-own-key following the Article 9 Lab precedent | Blocks the demo vault, and with it the strongest thing this site could add next | waiting on human |
| N7 | **Confirm the network boundary with `sgit.ai`** (pack Q2). Proposed and published unconfirmed: this site owns the **capability**, `sgit.ai` owns the **product tour**. [On the network page](../network/index.md). Also worth a decision: which sibling network pages should now link here, since none of them list this site yet | Not blocking until two sites claim the same page, which is the failure the boundary exists to prevent | proposed |
| N8 | **Is Phase 4 scheduled?** Minted credentials are described as *"the commercially load-bearing piece"* and as what would make vault-sharing safe with AI configured. [This site's strongest claim is narrower than it wants to be](../index.md#thesis) until they exist, and a date would change what the front page can say | Not blocking. It changes the claim, not the build | open |
| N1 | **The brief pack.** Received 25 August 2026, twelve documents and a 24-row source manifest. [Published verbatim](../documents/index.md) with a reader page each, and the site built from it | No longer blocking | done |
| N2 | **GitHub Pages and the custom domain.** Done: [llms.sgit.ai](https://llms.sgit.ai) resolves and serves, the `github.io` address redirects to it, and the pipeline is verified end to end | No longer blocking | done |
| N3 | **The site's boundary with its siblings.** Superseded by N7, which asks the narrower question the brief pack actually raises | — | superseded |

## Task board

| # | Task | Owner | Status |
|---|---|---|---|
| T1 | CI pipeline: validate, auto-tag, deploy to Pages, ported from pki.sgit.ai with two improvements from graphs.sgit.ai | site agent | done v0.1.0, verified live v0.1.1 |
| T6 | **The site itself**, in the brief's build order: [the chat pane](../chat-pane/index.md) and [samples](../chat-pane/samples.md), [the API](../api/index.md) and [traps](../api/traps.md), [security](../security/index.md), [websites](../websites/index.md), [provenance](../provenance/index.md), [the provider layer](../openrouter/index.md), [local](../local/index.md), [agents](../agents/index.md), [shipped](../shipped/index.md) | site agent | done v0.2.0 |
| T7 | The brief pack captured verbatim under `briefs/` with [reader pages](../documents/index.md) generated alongside. The raw markdown stays the source of truth | site agent | done v0.2.0 |
| T10 | **Q1 answered by mechanism.** The API reference is generated from the canonical `AUTHORING.md` section, vendored under `sources/` with its hash recorded, and the gate fails if the page stops matching. No second source of truth, and no unreadable contract either | site agent | done v0.2.0 |
| T11 | **The agent surface**, treated as an acceptance criterion rather than a topic: a markdown twin at every path with links rewritten to point at twins, a self-sufficient `llms.txt`, [llms-full.txt](../llms-full.txt) (which pki.sgit.ai lacks), and a generated sitemap listing both. All four enforced by the gate | site agent | done v0.2.0 |
| T12 | **The brief's conditions turned into gates.** Key shapes (`sk-or-`, OpenRouter formats, the write prefix) banned before the first sample page shipped; the CSP qualification required on the front page; twins required; the generated reference required to match its source; house spelling enforced. A condition in a brief is one somebody forgets on the fourth page | site agent | done v0.2.0 |
| T13 | **Seven claims re-verified against the shipped source** at v0.33.62 rather than against the brief, per the pack's own closing instruction. [Five confirmed, one superseded, one no longer true](../shipped/index.md#verified) | site agent | done v0.2.0 |
| T14 | The `sg-llm-chat` web component with a pluggable transport, so one component serves the backend-proxy, BYOK and embedded-vault options. [The recommendation](../websites/index.md#recommendation), and half the commission | site agent | queued, and named as not built |
| T15 | The demo vault app that is the documentation | project lead + agent | blocked on N6 |
| T16 | The `/injection/` page | site agent | held on N4, deliberately |
| T17 | Ask the sibling sites to link here, and add this site to their network pages | site agent | queued, after N7 |
| T9 | Reported upstream: `standards.sgit.ai`'s repository ignores `admin/build/` through the inherited Python `.gitignore`, so its gate script is not committed and its CI runs against a file that is not in the checkout. This repository carries the one-line negation that fixes it | site agent | reported v0.1.0 |

## How to use this channel

- **Human to agent:** reply in the working session, or edit this page or open an issue in [the repo](https://github.com/SGit-AI/SGit-AI__Website__LLMs). Anything added under "Needed from the project lead" with an answer gets actioned next session.
- **Agent to human:** every release updates this page and [versions](versions.md); requests appear in the N-table above, most-blocking first.
- **Decisions log:** the pipeline shipped before the content, so every release goes through a gate that already works. The API reference is generated rather than written, so this site cannot become the second source of truth the corpus refused to create. The website half is labelled thin rather than levelled with the vault half. The injection page is held rather than written to a question that has no ruling. And the brief's conditions were made into build gates rather than left as intentions.

 [← How this site is built](index.md) [Release history →](versions.md)


==============================================================================
/admin/versions.md
==============================================================================

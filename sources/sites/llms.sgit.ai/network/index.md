# The network, and what this site does not own

*Source: <https://llms.sgit.ai/network/index.html> · site v0.2.0 · the markdown twin of this page, generated from it.*

---

[llms.sgit.ai](../index.md) / network

# The network, and what this site does not own

Several sites in this network already touch language models at their edges, and "LLMs" is a broad enough name to swallow all of them. So this page states the boundaries, and it does so on the first content release rather than after two sites have both claimed the same argument.

| Site | Owns | Boundary with this site |
|---|---|---|
| **llms.sgit.ai** | this site | The chat pane, the `sg.llm.*` contract, the LLM security model, provenance, providers, local models |
| [sgit.ai](https://sgit.ai) | The vault product, the catalogue, the demos | **The closest neighbour.** The authoring contract and the vault UI belong there; the LLM capability *inside* them belongs here. Open: who owns the `/vault` chat-panel page. Proposed, and not yet agreed: this site owns the **capability**, `sgit.ai` owns the **product tour** |
| [coding.sgit.ai](https://coding.sgit.ai) | How code is written | **The samples follow its component conventions.** If [the `sg-llm-chat` component](../websites/index.md#recommendation) gets built, that site owns the component pattern and this one owns the LLM contract |
| [risks.sgit.ai](https://risks.sgit.ai) · [standards.sgit.ai](https://standards.sgit.ai) | Risk and instruments | **They own the grounding ladder.** [Three lines and a link out](../provenance/index.md#grounding) is the right amount of it here: it is the reason the LLM work looks the way it does, not this site's subject |
| [open-source.sgit.ai](https://open-source.sgit.ai) | The open-source position | Sovereignty applies sharply to model providers, since *one SLA away from losing access* is not hypothetical for a hosted model. [Two links, not a rebuild](../local/index.md#sovereignty) |
| [graphs.sgit.ai](https://graphs.sgit.ai) | Graph theory, meaning through connectivity | Retrieval over graphs sits on the boundary. Light link. If a page here starts explaining what a graph is, it belongs there |
| [sg-compute.sgit.ai](https://sg-compute.sgit.ai) | The compute platform | **Owns the `ollama` and `local_claude` workload specs.** [This site links to them for the local-model story](../local/index.md#specs); that site owns the specs |
| [pki.sgit.ai](https://pki.sgit.ai) · [nhi.sgit.ai](https://nhi.sgit.ai) | Agent identity and mandate; non-human identity | They own *who an agent is and what it may do*. This site owns *what happens when code calls a model*. Adjacent and not overlapping: a question about model output is not an identity question. `pki` also supplies [the house pattern and the build pipeline this site runs](../admin/index.md) |
| [newsroom.sgit.ai](https://newsroom.sgit.ai) | The future of news | Shares the training-data licensing thread and the fact-graph-as-training-material argument |

## The rule these boundaries follow

Cross-link page to page, not domain to domain.

A link that says "see graphs.sgit.ai" is an instruction to go and search. A link that says *this specific argument, on that specific page* is a join. The network's own access review found three sites each holding a third of one answer and unjoined at the page level, so every cross-reference on this site points at a page.

## What this site borrowed, and from where

- **The pipeline and the house pattern** from [pki.sgit.ai](https://pki.sgit.ai): validate, tag, deploy, with a validation failure stopping the release entirely. [How it runs here](../admin/index.md).
- **Two pipeline improvements** from [graphs.sgit.ai](https://graphs.sgit.ai): anchoring the tag on the newest release commit reachable from `HEAD`, and checking the remote before pushing backfill tags.
- **A link-checker fix** from [standards.sgit.ai](https://standards.sgit.ai): strip query strings as well as fragments.
- **The honest-limitations posture** from all of them. The vault catalogue publishes its own key-exposure incident; this site publishes [the gap in its own security design](../security/index.md#gap).

And one thing it adds that none of them has: **[llms-full.txt](../llms-full.txt) and a markdown twin at every path, enforced by the build**. [Why that is an acceptance criterion here rather than a nicety.](../agents/index.md)

 [← What is shipped](../shipped/index.md) [Where we lose →](../about/participant.md)

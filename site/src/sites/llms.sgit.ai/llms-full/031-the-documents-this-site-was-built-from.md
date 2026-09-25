# The documents this site was built from

Every sibling site in this network publishes the brief pack that produced it, in full, so a reader can check the site against its own instructions. This is that pack: 12 documents and a source manifest, verbatim, with a reader page each and the raw markdown beside it.

**The raw file is the source of truth.** Each reader page renders its document from `briefs/` at read time rather than carrying a copy, so the page cannot drift from the document. If rendering fails, the page falls back to a link to the raw file: a document on this site is never unreachable.

| Document | Kind | What it carries | Raw |
|---|---|---|---|
| [The Brief](brief.md) | Leading brief | The commission and its shape: three chat-pane surfaces rather than one, the thesis that an app calls a model without ever holding an API key, what is actually shipped, the CSP gap that keeps the design a convenience rather than a guarantee, the wider LLM threads measured across the corpus, and the build order this site follows. | [raw](../briefs/00__BRIEF.md) |
| [The Chat Pane: Three Surfaces](chat-pane.md) | The commission | The decision layer: which of the three surfaces you want, and the finding that two of them need no code at all | [raw](../briefs/01__the-chat-pane.md) |
| [The sg.llm.* API](api.md) | Reference brief | The API as the brief describes it: the ten calls, the streaming contract's three guarantees, the nine error codes, the image traps including the 8190 chunking bug, voice, and the table of seven concerns the host handles that an app does not have to | [raw](../briefs/02__the-sg-llm-api.md) |
| [The Security Model, And The Gap In It](security.md) | Security brief | Where the key lives, the two key tiers and why the difference is cryptographic rather than a policy check, the four-layer ladder of grant, consent, budget and policy, the argument that the recording indicator is trustworthy because the app cannot draw it, and the CSP egress gap stated plainly with the instruction not to soften it. | [raw](../briefs/03__the-security-model.md) |
| [Websites Vs Vaults](websites.md) | Gap analysis | What changes when there is no host: every guarantee in the vault model depends on the app and the credential sitting in different trust boundaries, and on a plain website they do not | [raw](../briefs/04__websites-vs-vaults.md) |
| [The Wider LLM Work](wider-work.md) | Corpus survey | The estate's LLM material measured rather than described: provenance and determinism as the oldest thread, running back to an OWASP AppSec Lisbon talk in June 2024; grounding rather than prompting as the answer to fabrication; OpenRouter as the actual provider layer; local and offline models; prompt injection; and a table of what is thin, which includes no evals, no structured-output guidance and one file mentioning model routing. | [raw](../briefs/05__the-wider-llm-work.md) |
| [Site Architecture](architecture.md) | Build brief | Page by page, what must be generated rather than written, and the artefact the site should ship: a vault app that is the documentation, exercising every call so the samples are tested by existing | [raw](../briefs/06__site-architecture.md) |
| [Boundaries And Licensing](boundaries.md) | Boundary brief | The licensing split between the site's CC BY 4.0 content and the Apache-2.0 code it quotes, the refusal to create a second source of truth for the API contract, the do-not-publish list, the key rules that make this the most likely site in the estate to leak a credential, and the boundary with each sibling site. | [raw](../briefs/07__boundaries-and-licensing.md) |
| [Gaps, Open Questions And Honest Tensions](gaps.md) | Open questions | Eight things that must be built fresh, eight open questions and seven honest tensions, published unresolved | [raw](../briefs/08__gaps-and-open-questions.md) |
| [Code Samples: Adding An LLM Chat Pane](samples.md) | Runnable samples | Eight samples and a pre-ship checklist: the minimum viable pane, cancel, a cost meter that does not lie, a model picker that cannot be wrong, image attachment, voice input, and a file-grounded pane that copies the host panel's three honesty mechanisms | [raw](../briefs/code__chat-pane-samples.md) |
| [The Pack Readme](pack-readme.md) | Pack front matter | How the pack is meant to be read, in order, with the four things to know before writing: that the best documentation is the hardest to find, that the honesty mechanisms are the best work and are published nowhere, that the website half is a gap rather than an asset, and that one question has no answer and it matters. | [raw](../briefs/00__pack-readme.md) |
| [The Pack Licence](licence.md) | Licence | CC BY 4.0 for the pack and for this site, Apache-2.0 for the code quoted from SGraph-AI__App__Send, the key-handling rule specific to this site, the instruction to publish the security gap unsoftened, and the do-not-publish list. | [raw](../briefs/LICENCE.md) |

## The source manifest

[09__source-manifest.csv](../briefs/09__source-manifest.csv) lists every source behind the pack, tiered 0 to 3, with each path verified on disk. Tier 3 is marked do-not-publish and is not reproduced here or anywhere on this site. Two tier-2 rows are marked `HOLD`, both of them prompt-injection material, held until the pack's own Q3 has an answer: [what this site can say about that question today](../security/index.md#injection) is on the security page.

## Licence

The pack is released under **CC BY 4.0**, Dinis Cruz, with AI co-authorship. The full statement is in [the pack licence](licence.md). Code quoted inside the documents from `SGraph-AI__App__Send` is **Apache-2.0** and keeps its own notice: in the samples, the `sg.llm.*` calls are the shipped contract and the surrounding UI was written for the pack.

 [← Front page](../index.md) [What is shipped →](../shipped/index.md)


==============================================================================
/admin/index.md
==============================================================================

# Participant disclosure, and where we lose

*Source: <https://llms.sgit.ai/about/participant.html> · site v0.2.0 · the markdown twin of this page, generated from it.*

---

[llms.sgit.ai](../index.md) / about / participant

# Who is writing this, and where we lose

Published upfront rather than discovered later. A reader who finds out about an affiliation afterwards discounts everything they have already read; a reader told at the start can judge the work as it goes.

## Who is writing this

This site is published by the **sgit project**: encrypted vaults with git workflows, for humans and AI agents. The chat pane described here is the project's own feature, the `sg.llm.*` bridge is the project's own API, and the security model is the project's own design. **This is a participant documenting its own product.**

What makes that worth reading anyway is narrower than "trust us", and it is worth being precise about which parts do not depend on trusting us:

- **The contract is checkable.** [The reference](../api/index.md) is generated from a canonical file in a public repository, with the source hash on the page, so you can diff this site against the thing it describes.
- **The traps are our own mistakes.** [A bug that shipped three times](../api/traps.md#chunking) and [a default that silently picked the worst model on the key](../openrouter/index.md#defaults) are published because they are the useful part, not despite being embarrassing.
- **The limit is stated in the project's own words.** [The CSP gap](../security/index.md#gap) is quoted from an internal capability brief rather than paraphrased into something softer.

## Where our own approach loses

A site that only names other people's limits is not research. So, plainly, on this subject:

- **The bridge is not an egress boundary.** [The whole of it.](../security/index.md#gap) If your threat model includes a hostile app in the frame, this design protects your credential and does not contain the app.
- **A configured vault carries a credential, and that changes what sharing means.** [Publishing a read key for such a vault hands over the ability to spend.](../security/index.md#storing) The fix is planned and not shipped.
- **Fencing untrusted files is a mitigation, not a guarantee.** [It relies on the model honouring an instruction](../security/index.md#injection), and there is no measurement of how well it holds.
- **There are no evals.** None. A body of work whose thesis is that you must know where an output came from has no mechanism for knowing whether it was any good. [The absence, sized.](../shipped/index.md#thin)
- **Half the commission is thin.** [Chat panes on plain websites](../websites/index.md) is three options and one adjacent precedent. The vault half is shipped and complete; the website half is a gap, and this site says which is which rather than levelling them.
- **The samples are read, not run.** [They are verified by review rather than by existing](../chat-pane/samples.md), which is exactly the weaker of the two, and the artefact that would fix it is blocked on a decision nobody has taken.
- **We are not neutral about agents.** The parent project's answer to most questions involves vaults, versioning and agents in the loop. That is a real position and not the only one.
- **The corpus counts are a dated snapshot.** 442 files mentioning OpenRouter, 92 mentioning injection, 2 mentioning cost per token: measured on 24 August 2026, quoted rather than re-measured, and they will drift.

## Licensing

| What | Licence |
|---|---|
| The content of this site, and [the brief pack](../briefs/00__BRIEF.md) it was built from | **CC BY 4.0**, Dinis Cruz, with AI co-authorship |
| Code quoted from `SGraph-AI__App__Send`, including [the generated API reference](../api/index.md) and the vault-html guides | **Apache-2.0**, and it keeps its own notice |
| [The samples](../chat-pane/samples.md) | **Mixed, and the page says which is which:** the `sg.llm.*` calls are the shipped contract; the surrounding UI was written for this site and is CC BY 4.0 |

That distinction is not pedantry. A reader copying a sample needs to know which half is a contract they can rely on and which half is one example among many.

## The people and agents behind the site

The project lead is Dinis Cruz. This site is built and maintained with AI agents in the loop, which is a reasonable thing for a site about language models to do and also a reason to check its citations rather than trust them. [The comms page](../admin/comms.md) is the working channel between the project lead and the site agent, kept in public, including the questions this site is currently asking and cannot answer for itself.

 [← The network](../network/index.md) [Comms: tasks & requests →](../admin/comms.md)

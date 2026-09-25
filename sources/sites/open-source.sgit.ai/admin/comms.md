<!-- generated from admin/comms.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.2.2 · canonical: https://open-source.sgit.ai/admin/comms.html*

> The open board: the items only the author can supply, and the tasks the site is carrying. Numbered, dated, and published rather than held privately.

---

# Comms: tasks & requests

The open board. **Needs (N)** are items only the author can supply — first-person accounts and decisions. **Tasks (T)** are work the site can do. Both are published rather than held privately, because [publishing the build order with its open questions visible](../roadmap/index.md) is the house rule.

## Needs — only the author can answer these

| # | What is needed | What it unblocks | State |
|---|---|---|---|
| **N1** | **Was CC0 on `docs.diniscruz.ai` deliberate?** Answered 6 September 2026: **no — CC BY.** The documents layer is CC BY 4.0 throughout; replacing that repository's `LICENSE` file is the follow-through. | [The practice section](../practice/index.md#reading) now records the decision, and [thesis (d)](../agents/index.md#cc0) is reframed as what CC BY means for machine reuse. | answered |
| **N2** | **The OWASP interview** — [thirteen questions, published in full](../owasp/index.md#interview). Board tenure and what the role involved, projects led, whether `owasp-sbot` hosting was deliberate, why 2017 left the OWASP umbrella, and whether the Open Security Summit still runs. | [The whole OWASP section](../owasp/index.md), which currently ships the summit history in the third person and marks the rest pending. | open |
| **N3** | **Why was each project open-sourced?** O2 Platform, MGraph-DB, OSBot, memory_fs, sgit-ai, Issues-FS. **Six published projects, not one retrospective** — the O2 article being the exception, and written about him rather than by him. | A retrospectives section, and it would make [the practice page](../practice/index.md#published) something other than a list of packages. | open |
| **N4** | **Q1: is the customer subset open core or packaging?**[The test is proposed](../views/open-core.md#test) — does the customer build contain anything the public repo does not? — and the answer is a fact about the product that only the project knows. | [The open-core page](../views/open-core.md) can then state a verdict rather than a test. | open |
| **N5** | **Q4: will the estate change to pass its own stress test?**[Leg by leg, with what each fix requires.](../survivability/self-audit.md#change)*"No, and here is why that is an accepted risk"* is a publishable answer. | [The self-audit](../survivability/self-audit.md), which records the result and can then record the plan. | open |
| **N6** | **Confirmation of the summit facts** restated here from the author's own summit history — attendance figures, the 2008 travel funding, the 173 sessions at Woburn. | Removes the last third-hand layer from [the summit section](../owasp/index.md#summits). | open |

## Tasks — work this site can do

| # | Task | State |
|---|---|---|
| **T1** | **CI pipeline and auto-tagging** — validate → tag → deploy, matching the sibling sites. [Documented →](index.md#pipeline) | done |
| **T2** | **The agent-discovery ladder** — markdown twin at every URL, self-sufficient `llms.txt`, `llms-full.txt`, all generated and **enforced by the build**. [Read →](../practice/publish-the-source.md#ladder) | done |
| **T3** | **The stress test as a working tool** rather than an essay — four legs, client-side, exportable. [Run it →](../survivability/stress-test.md) | done |
| **T4** | **The self-audit, published in full.**[Read →](../survivability/self-audit.md) | done |
| **T5** | **Why Apache-2.0 rather than MIT** — the most conspicuous unwritten page in the brief. [Read →](../practice/apache-vs-mit.md) | done |
| **T6** | **An SBOM of the estate, plus a licence audit in CI.** Roughly a day's work, and it converts [the labelling argument](../funding/index.md#labelling) from proposal to demonstration. [First on the build order.](../roadmap/index.md#supply-chain) | next |
| **T7** | **The four agent-era theses** — [named on the agents page, none written](../agents/index.md#unwritten). The most original writing still available. | open |
| **T8** | **A licence taxonomy** — copyleft vs permissive as a position, compatibility, AGPL, source-available. [The history research supplies the ground.](../roadmap/index.md#taxonomy) | open |
| **T9** | **A published trademark policy** — [the clearest unforced gap in the self-audit](../survivability/self-audit.md#change), and it costs almost nothing. | open |
| **T10** | **Separately license the schemas** (CC0 or CC BY), which is the cheapest self-audit fix and has no argument against it. | open |
| **T11** | **Visual assets** — a timeline, a licence-family diagram, a map of the estate. [On the build order.](../roadmap/index.md#visual) | open |
| **T12** | **Verify the marked-unverified facts** in the research document — several founding dates and licences are flagged. [Nothing flagged has been published as established.](../history/numbers.md#unverified) | open |
| **T14** | **Link the sources this site names.**[The HBS paper](../history/numbers.md#88tn) and [the Mozilla interview](../agents/index.md#training) are now linked; **OSSRA, the Stack Overflow survey, the kernel release notes and the Let's Encrypt telemetry are still named without a URL**. A site whose credibility position is that it checks other people's citations should make its own followable — by a reader and by [the agents it says are its primary audience](../agents/index.md#audience). | open |
| **T13** | **Get indexed** — [the top rung of the ladder, and the real fix](../practice/publish-the-source.md#ladder). The other three rungs are shipped. | open |

## Corrections

None yet — the site is new. Corrections will be recorded here with the date and what changed, rather than being applied silently. [A site that corrects other people's numbers](../history/numbers.md) has to show its own working when it gets something wrong.

[← Admin & engineering](index.md)[Release history →](versions.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*

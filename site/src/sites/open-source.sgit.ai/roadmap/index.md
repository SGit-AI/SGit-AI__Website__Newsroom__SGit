<!-- generated from roadmap/index.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.2.2 · canonical: https://open-source.sgit.ai/roadmap/index.html*

> What is built, what is next in order, and the open questions — seven still open, one decided — including whether the customer subset is open core, which funding model to back, and what the estate will change after its own stress test.

---

# What's next

The build order is published **with its open questions visible**, because a position that hides what it has not yet settled is advertising. This page is what is built, what is next in order, and the open questions — seven still open and one decided — several of which are decisions for the project rather than research tasks for the site.

## What is built

| Section | State | Note |
|---|---|---|
| [**/views/**](../views/index.md) — the argument | shipped | The position, sovereignty, open core, the villagers. Each with its counter-case attached. |
| [**/survivability/**](../survivability/index.md) | shipped | The argument, [the stress test as a working tool](../survivability/stress-test.md), and [the self-audit, run on the estate itself](../survivability/self-audit.md). |
| [**/history/**](../history/index.md) | shipped | Six corrections leading, timeline behind them, six success stories, and [the numbers with the unpublishable ones named](../history/numbers.md). |
| [**/practice/**](../practice/index.md) | partial | The three licences and [Apache-vs-MIT](../practice/apache-vs-mit.md) are written. Q5, the licence alignment, is decided: CC BY. |
| [**/agents/**](../agents/index.md) | partial | The argument ships. **Four theses are named and next to be written** — the most original writing still available. |
| [**/funding/**](../funding/index.md) | shipped | Three proposals compared for the first time, a position taken, and [cURL](../funding/curl.md). |
| [**/owasp/**](../owasp/index.md) | partial | Summit history ships from the public record. **The first-person account is the author's to write**, and is planned. |
| [**/founders/**](../founders/index.md) | shipped | [Owning the code, or opening it](../founders/index.md) — the guidance from a strategy session with another founder, released CC BY. |
| [**/about/**](../about/index.md) | shipped | The author, the companies the strategy runs on, and interests declared. |
| **Agent surface** | shipped | [Markdown twin at every URL, self-sufficient llms.txt, llms-full.txt](../practice/publish-the-source.md) — all three enforced in CI. |

## What is next, in order

1. **An SBOM of the estate, and a licence audit in CI.** The single highest-value item on the list: it is roughly a day's work and it converts [the labelling argument](../funding/index.md#labelling) from a proposal into a demonstration. The site asks companies to declare their supply chain; this is the estate's own declaration. One manual licence review exists (February 2026 — 17 transitive dependencies, an SPDX table, a clean verdict); the automated, continuous version is the item.
2. **The four agent-era theses** — [licence compliance at machine speed](../agents/index.md#compliance), [provenance of AI-generated code](../agents/index.md#provenance), [training-data licensing](../agents/index.md#training), and [what CC BY means for machine reuse](../agents/index.md#cc0). Each follows obviously from material that exists; none is written.
3. **A licence taxonomy.** Copyleft versus permissive as a position, compatibility, where AGPL fits, and how to treat source-available. [The history research supplies the ground](../history/index.md); the position is next.
4. **The first-person OWASP account, and six project retrospectives** — [thirteen questions, already published](../owasp/index.md#interview), that only the author can answer. O2 Platform, MGraph-DB, OSBot, memory_fs, sgit-ai, Issues-FS: why each was open-sourced, and what happened next.
5. **A trademark policy.**[The clearest quick win from the self-audit](../survivability/self-audit.md#change): publishing one costs almost nothing and removes the worst of the ambiguity even while the holder stays the same.
6. **Separately licensing the schemas.** The cheapest of the self-audit fixes, and there is no good argument against it.
7. **Visual assets.** A timeline, a licence-family diagram, a map of the estate. [The timeline](../history/timeline.md) and [the four-leg test](../survivability/stress-test.md) both want a picture.

## The open questions — seven open, one decided

| # | Question | Where it stands |
|---|---|---|
| **Q1** | **Is the customer subset open core or packaging?** | [The test is proposed](../views/open-core.md#test): does the customer build contain anything the public repo does not? The June and July positions are both published, and the July document names the tension itself. **Needs a decision, not more analysis.** |
| **Q2** | **Which funding model?** | [A position is now taken](../funding/index.md#position) — they address three different failures and were never competitors. Still: none costed, none piloted, and the value-contribution calculation unsolved. |
| **Q3** | **Does the junior pipeline restructure, or break?** | [March and July say opposite things, four months apart.](../agents/index.md#pipeline) What would settle it is a cohort measurement nobody appears to be making. [The villagers argument depends on the July answer.](../views/villagers.md) |
| **Q4** | **Would the estate change to pass its own stress test?** | [Leg by leg, with what each fix requires.](../survivability/self-audit.md#change) The honest answer on leg one may be *"no, and here is why that is an accepted risk"* — still publishable, and better than silence. |
| **Q5** | **Was CC0 on the articles deliberate?** | **Decided, 6 September 2026: no — CC BY.** The CC0 in the published-articles repository was drift, not a third layer; the documents layer is CC BY 4.0 throughout and the repository's licence file follows. [Recorded on the practice page.](../practice/index.md#reading) |
| **Q6** | **Do agents help or harm open-source sustainability?** | Current evidence says harm — [cURL's bounty closed 31 Jan 2026](../funding/curl.md), vulnerabilities reported up 107%. **Is that a transition cost or the steady state?** Nobody knows, and [this site declines to claim the optimistic answer](../agents/index.md#audience). |
| **Q7** | **Is "open source AI" coherent without training data?** | The OSI's definition exists and drew heavy criticism; almost no model marketed as open source meets it. [The author's 2025 position, and a browser vendor now betting on the open-weight side of the line.](../agents/index.md#training) |
| **Q8** | **What does this site owe a community it does not have?** | [The position that open source is right even with zero contributions](../views/index.md#zero-contributions) is coherent — and it means governance, review and codes of conduct are not yet written about here, despite [the survivability argument turning on DCO-versus-CLA in practice](../survivability/index.md#cla). The next contributor relationship is where that page gets written. |

## Where this site stops

Several arguments here sit on a boundary with a sibling site, and the rule is **one canonical copy, cross-linked** rather than a duplicate on each.

| Site | Owns | The shared edge |
|---|---|---|
| [wardley-maps.sgit.ai](https://wardley-maps.sgit.ai) | Mapping technique; Explorer/Villager/Town Planner as a pattern | ["Somebody has to be the villagers"](../views/villagers.md) — they own the pattern, this site owns the NFR market argument. |
| [standards.sgit.ai](https://standards.sgit.ai) | Instruments, provisions, crosswalks, the SPDX machinery | [Licence compliance at machine speed](../agents/index.md#compliance) — they own the machinery, this site owns the argument. |
| [graphs.sgit.ai](https://graphs.sgit.ai) | Graph theory, meaning through connectivity | Semantic OWASP and the PBOM. This site owns the *why*; graphs owns the *how*. |
| [pki.sgit.ai](https://pki.sgit.ai) | Keys, signatures, the registry design | [Provenance of AI-generated code](../agents/index.md#provenance) — they hold the signing machinery, the licensing argument belongs here. |
| [sgit.ai](https://sgit.ai) | The parent project and the vault layer | Should link *here* for the licence and sovereignty argument. |

[← OWASP](../owasp/index.md)[The documents →](../documents/index.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*

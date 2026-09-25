<!-- generated from documents/index.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.2.2 · canonical: https://open-source.sgit.ai/documents/index.html*

> The commissioning brief pack this site was built from, published whole and unedited: nine briefs, an 18,000-word history research document, and a 55-row source manifest. The raw markdown is the source of truth.

---

# The documents

A site that argues you should [publish the source next to the render](../practice/publish-the-source.md) owes a reader its own. These are the briefs this site was built from, published **whole and unedited**. Where a page here summarises, disagrees with, or declines to follow one of them, **the raw markdown is the source of truth** and you can check.

> **How to read these.** The brief pack was written *to* the agent commissioning this site, so it reads as instructions rather than as content — including instructions this site did not follow, and open questions it could not close. That is the useful part. [Where the site diverges from the brief is listed at the bottom of this page.](#divergences)

## The commissioning brief pack

| Document | What it holds | Where it landed |
|---|---|---|
| [**00 — The brief**](../briefs/00__brief.md) | The commission, the honest split across the three asks, the thesis, the five pages only this author can write, the two dated changes of position, and the build order. | [Front page](../index.md), [build order](../roadmap/index.md) |
| [**01 — Concepts index**](../briefs/01__concepts-index.md) | All 56 concepts with verbatim quotes, paths and dates, classified as widely-held, personal position, or original argument. **24 originals.** | [The position](../views/index.md) |
| [**02 — The practice**](../briefs/02__practice.md) | The three-licence estate, the CC0 discovery, publish-the-source-next-to-the-render, the read-key discipline, and the compliance gap. | [Practice](../practice/index.md), [publish the source](../practice/publish-the-source.md) |
| [**03 — The history, and how to use it**](../briefs/03__history-and-success-stories.md) | The editorial guidance: lead with corrections not a timeline, pick six success stories not fourteen, and the numbers to handle carefully. | [History](../history/index.md) |
| [**04 — The arguments**](../briefs/04__the-arguments.md) | Survivability, the stress test, open core, funding, sovereignty, the villagers — with the counter-case for each. | [Survivability](../survivability/index.md), [funding](../funding/index.md), [views](../views/index.md) |
| [**05 — Agents and open source**](../briefs/05__agents-and-open-source.md) | Code-reading as the scarce asset, the March/July change of position, and **four theses that are named nowhere and written nowhere.** | [Agents](../agents/index.md) |
| [**06 — OWASP and the summits**](../briefs/06__owasp-and-the-summits.md) | The OWASP thread, four summits, and the interview that has to happen — thirteen questions ready. | [OWASP](../owasp/index.md) |
| [**07 — Architecture and boundaries**](../briefs/07__site-architecture-and-boundaries.md) | The house pattern, the quoting table, do-not-publish, and the network boundaries between sibling sites. | [Boundaries](../roadmap/index.md#boundaries), and this site's structure |
| [**08 — Gaps and open questions**](../briefs/08__gaps-and-open-questions.md) | Ten build-fresh items, eight open questions, eight honest tensions. | [What's next](../roadmap/index.md), [open questions](../roadmap/index.md#open) |
| [**09 — Source manifest**](../briefs/09__source-manifest.csv) | 55 rows: every source tiered 0–3 with its proposed page and publishability. Every path verified on disk. | Provenance for the whole pack |

## The history research

|  |  |
|---|---|
| [**research — the history, from scratch**](../briefs/research__history-and-success-stories.md) ~18,000 words · compiled 24 August 2026 | The single largest document behind this site, and the reason [the history section exists at all](../history/index.md): the author's writing contained **no history of open source**, so one was researched. A sourced timeline 1955→2026, fourteen success stories, two instructive failures, an evidence table, seven both-sides arguments, seventeen corrected myths, and a source list that separates what was fetched from what was only search-derived. **It reports its fetch failures inline rather than working around them**, and marks several facts as not verified. [Those are listed on this site as unpublished](../history/numbers.md#unverified) rather than quietly promoted to established. |

## The pack's own front matter

- [**README**](../briefs/README__brief-pack.md) — the reading order, and the four things the pack said would shape the build.
- [**LICENSE**](../briefs/LICENSE__brief-pack.md) — CC BY 4.0, the three-licence problem, and the quoting table that governs how this site handles other people's material.

## Where this site diverges from the brief

Publishing the instructions makes the divergences checkable, so they are stated rather than left to be found.

| The brief said | What was done, and why |
|---|---|
| **"Resolve the licensing inconsistency *before* writing a word"** — it is described as blocking the practice section. | **Resolved by the author on 6 September 2026: CC BY.** Until then [both readings were published and neither picked](../practice/index.md#reading), because declaring an intention on his behalf would have been the tidying this site argues against. The decision is recorded on the practice page and [Q5 is closed](../roadmap/index.md#open). |
| **"Copy `pki.sgit.ai`. Add the `/llms-full.txt` it lacks."** | **Done, and extended.** Same CI pipeline (validate → tag → deploy), same chrome tooling. `llms-full.txt` ships, and so does [a markdown twin at every URL](../practice/publish-the-source.md#ladder) — generated, and **enforced by the build** rather than maintained by hand. |
| **"Ship the stress test as a form or checklist, not an essay."** | **Done** — [it runs in the browser](../survivability/stress-test.md), keeps your answers locally, and exports a markdown summary. Nothing is sent anywhere. |
| **"Ship `/practice/` with an SBOM, or state the gap with a date."** | **Stated as a gap, without a date** — which the brief itself calls the weaker of the two options. It is [first on the build order](../roadmap/index.md#supply-chain). |
| **Publish market figures from the villagers brief.** | **Declined.** The brief flags them as loosely attributed and notes that much of what circulates is vendor commentary recycling a smaller set of studies. [They are omitted, and the omission is stated on the page.](../views/villagers.md#numbers) |
| **Do not publish a marked-unverified fact as established.** | **Followed.**[The unverifiable claims have their own section](../history/numbers.md#unverified), naming what was not established and why, rather than being silently dropped. |

> **On quoting other people's material.** This site quotes the open-source world at length, under the rules in the pack's licence file: Wikipedia material is CC BY-SA and is **quoted with attribution rather than adapted**; project documentation is quoted briefly and never mirrored; **vendor and analyst reports are cited by number, source, date and caveat, and their charts are never reproduced**. Naming projects, foundations, licences and the public authors of public work is fine and necessary. [Running the stress test on a named commercial competitor and publishing a scorecard is not](../survivability/stress-test.md#notascorecard) — we ship the test and let readers run it.

[← The build order](../roadmap/index.md)[About the author →](../about/index.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*

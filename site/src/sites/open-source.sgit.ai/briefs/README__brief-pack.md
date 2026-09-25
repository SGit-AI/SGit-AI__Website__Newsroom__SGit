# open-source.sgit.ai — brief pack

**For:** the agent commissioned to build `open-source.sgit.ai`
**From:** Dinis Cruz, via the SG/Send Librarian
**Version:** v0.33.62 · 24 August 2026
**Licence:** CC BY 4.0 — **read `LICENSE.md` first.** The estate runs three licences and one of them is undocumented.

---

## What this is

A site for your views on open source, how you actually use it, and its history. Three asks, and they are in very different states:

| Ask | State |
|---|---|
| **Your views** | **Very rich.** 56 concepts catalogued — **24 original arguments**, not restatements |
| **How you use it** | **Rich, and partly undocumented even to you** — three licences, a real publish-the-source practice, six published projects with no retrospectives |
| **The history** | **Absent. Not thin — absent.** Researched from scratch: 18,000 words shipped in this pack |

On that last row: **zero occurrences of "free software", "copyleft", "Stallman", "GNU" as a movement, "Netscape", "SourceForge" or "FSF"** anywhere in the corpus. Nothing before 2001. The GPL appears twice, both as litigation precedent. There is no licence taxonomy at all — **yet the whole estate runs on Apache-2.0, CC BY and CC0, and the reasons are written down nowhere.**

Clean division of labour: **you supply the argument, the research supplies the ground under it.**

---

## Read in this order

| File | Words | What it does |
|---|---:|---|
| **`00__BRIEF.md`** | 2.0k | **Start here.** The honest split, the thesis, the five original pages, the two dated self-contradictions, the build order |
| **`04__the-arguments.md`** | 2.1k | **The best pages the site can have** — survivability, the stress test, open core, funding, sovereignty, the villagers |
| **`03__history-and-success-stories.md`** | 1.7k | How to use the research: six corrections to lead with, six success stories not fourteen, and the numbers to handle carefully |
| **`05__agents-and-open-source.md`** | 1.6k | **The most original writing still available** — and four theses that are named nowhere and written nowhere |
| `01__concepts-index.md` | 3.7k | All 56 concepts with verbatim quotes, paths, dates, classified [C]/[P]/[O], plus a five-altitude reading order |
| `02__his-practice.md` | 1.6k | The three-licence estate, the CC0 discovery, publish-the-source-next-to-the-render, the compliance gap |
| `06__owasp-and-the-summits.md` | 1.4k | The OWASP thread, four summits, and **the interview that has to happen** — 13 questions ready |
| `07__site-architecture-and-boundaries.md` | 1.4k | Page by page, the quoting table, do-not-publish, network boundaries |
| `08__gaps-and-open-questions.md` | 1.1k | 10 build-fresh items, 8 open questions, 8 honest tensions |
| `09__source-manifest.csv` | 55 rows | Every source, tiered 0–3, with proposed page and publishability. **Every path verified on disk** |
| **`research__history-and-success-stories.md`** | **18k** | The fresh history — timeline 1955→2026, 14 success stories, 2 failures, evidence table, 7 both-sides arguments, **17 corrected myths**. Fetch failures reported inline |
| `LICENSE.md` | — | CC BY 4.0, the three-licence problem, and the quoting table |

---

## The four things that will shape the build

**1. The licensing inconsistency blocks `/practice/`.** `docs.diniscruz.ai` is **CC0 1.0**; every brief footer says **CC BY 4.0**. Nobody has noticed and no document reconciles them. Deliberate layered choice, or drift? Decide before writing. And the missing page underneath it: **why Apache-2.0 rather than MIT** — the entire estate rests on that choice and the reasoning exists nowhere.

**2. The history research supports your thesis better than the romantic version does.** Unix circulated because the 1956 AT&T consent decree made it *illegal to sell*. BSD lost to litigation risk, not licensing — the settlement removed **3 files out of 18,000**. Netscape's release was a six-year near-failure; **Firefox 1.0 did not ship until November 2004**. Christine Peterson coined "open source", not Eric Raymond. And "given enough eyeballs" is not a security property — **xz was engineered by the maintainer to survive review**, and caught by one engineer benchmarking SSH latency. Every one of those says the model wins on **economics and structure**, not virtue.

**3. Your best idea would fail on you.** *"Survivable is not a property of the licence file. It is a property of the copyright and trademark structure."* The Change-of-Control Stress Test is four legs, all answerable from public artefacts, and it should ship as a tool. **SGraph's copyright is held by one company** — the exact single-holder pattern the argument identifies as the failure mode. Publishing that self-audit would be the most credible page on the site.

**4. cURL is your page.** ~30 billion installations, seven volunteers on the security team, and the bug bounty **shut down on 31 January 2026** because ~20% of 2025 submissions were AI slop against ~5% genuine. That is your own AI-slop finding with a named casualty and a date — and the strongest evidence anywhere for *"charity will not fix this."*

---

## Two contradictions to publish rather than resolve

**Open core.** 18 June: *"There should be **nothing proprietary**."* 17 July: *"customers only have a subset of the code that exists in the main repo."* The July brief names it itself — *"this is open-core, and worth saying so plainly."* `04__` §3 proposes the test that settles it.

**The junior pipeline.** 21 March: *"the density of learning per hour increases."* 28 July: *"apparent gains shifted work from juniors to seniors."* 31 July: the pipeline *"is being disrupted at exactly the moment the maintenance need is growing."* Four months, opposite directions.

A site that shows its own position moving as evidence arrived is more persuasive than one that only publishes the settled view.

---

## One thing the pack cannot supply

**`/owasp/` is blocked on an interview.** Former OWASP board member, named organiser of the 2011 Lisbon summit and primary organiser of 2017 Woburn (173 sessions), email of record `dinis.cruz@owasp.org`, the whole current estate under `owasp-sbot`. **All of it is written in the third person, from public sources, about you.** There is no memoir, no board-tenure dates, no project list, no Open Security Summit founding story — and no retrospective on any of your six published open-source projects except O2 Platform, which was also written about you rather than by you.

`06__` §4 has thirteen questions ready. Ship the summit history and mark the first-person account pending rather than writing around it.

---

## House pattern

Copy `pki.sgit.ai`. Add the `/llms-full.txt` it lacks. And treat the **agent-discovery ladder as a build requirement, not a topic** — your own agent-access report found that *"it can read the map and cannot walk it"*, and a site about open source that agents cannot traverse fails in exactly the way you already diagnosed.

Publish the build order unresolved, with `08__`'s open questions and tensions visible.

---

This file is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).

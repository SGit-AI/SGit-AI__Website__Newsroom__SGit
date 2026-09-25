# Licence

## This pack

Everything in this brief pack — the nine numbered documents, `09__source-manifest.csv`, `research__history-and-success-stories.md`, this file and `README.md` — is released under the **Creative Commons Attribution 4.0 International licence (CC BY 4.0)**.

    Copyright (c) 2026 Dinis Cruz
    Licensed under CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/

Attribution: **Dinis Cruz**, with AI co-authorship (Claude, Anthropic).

**The sources cited inside `research__history-and-success-stories.md` retain their own licences.** That file is our writing about other people's work; quoting it is not the same as quoting them. See §3.

## The site this pack commissions

**The entire content of `open-source.sgit.ai`** is to be published under **CC BY 4.0**, consistent with the network. Stamp every raw markdown document:

    This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).

Gate it in CI with `licence-audit.py --check` from the `graphs.sgit.ai` pack, and **publish the coverage number** — on this site more than any other, the licence discipline is part of the argument.

---

## ⚠️ Resolve this first: the estate runs three licences and one is undocumented

| Layer | Licence |
|---|---|
| **Code** — `SGraph-AI__App__Send`, all seven Issues-FS repos | **Apache-2.0** |
| **Briefs / corpus documents** | **CC BY 4.0** — footer on ~1,100+ files |
| **Published articles** — `docs.diniscruz.ai` | **CC0 1.0 Universal** |

**The briefs assume CC BY is the site-wide answer. The published-articles repo is public domain, and no document in the corpus mentions it.**

A site *about open source licensing* that carries an unexplained licence mismatch will be caught. Decide before writing `/practice/`: deliberate layered choice, or drift to be fixed. Either way it is a page — and in an era of model training, choosing CC0 over CC BY is a decision about **machine** reuse, not human reuse (`08__` Q5).

**And the missing page:** why **Apache-2.0 rather than MIT**. The patent grant? The NOTICE file? Defensive termination? The whole estate rests on that choice and the reasoning exists nowhere in the corpus.

---

## Quoting other people's material

| Source | Regime | What the site may do |
|---|---|---|
| **`docs.diniscruz.ai` articles** (13 in the manifest) | **CC0 1.0** | Republish freely. Attribute anyway and keep `rel="canonical"` with the first-published date |
| **Wikipedia** — used heavily in the research | **CC BY-SA 4.0** | Quote with attribution and a link back. **Do not adapt** — ShareAlike would bind the page |
| **Project documentation** — curl, sqlite.org, letsencrypt.org, ASF | Varies; several permissive, some ARR | Quote briefly with attribution. **Do not mirror.** The ASF FY2025 report is a PDF — link it, do not rehost |
| **Vendor and analyst reports** — Black Duck OSSRA, CNCF, Stack Overflow, Octoverse, StatCounter, W3Techs | **All rights reserved** | Cite number, source, date and caveat. **Never reproduce their charts.** The research file's evidence table is already in the safe form |
| **HBS WP 24-038** | Academic | Cite and link. **Never publish the $8.8tn figure without its definition and the critique** — the corpus currently does |
| **Personal blogs** — Stenberg, antirez, Peterson's account | ARR unless stated | Quote briefly, attribute by name, link out |

## Naming people and organisations

**Fine, and necessary:** projects, foundations, licences, and the public authors of public work — Torvalds, Stallman, Peterson, Raymond, Stenberg, Hipp, Roosendaal, Freund. Reporting that curl closed its bounty on 31 January 2026, in Stenberg's own published words, is factual reporting the community needs.

**Fine:** the relicensing history — MongoDB, Elastic, HashiCorp, Redis, IBM, Oracle. Documented corporate acts with dates and public statements.

**Not fine:** running the Change-of-Control Stress Test on a named commercial competitor and publishing the verdict as a scorecard. **Ship the test; let readers run it.** The one exception is running it on yourself, which `04__` §2 recommends doing publicly.

**Never:** quoting forum, Discord or mailing-list participants without consent, or naming a private individual from the internal corpus.

## Accuracy

`research__history-and-success-stories.md` marks several facts **not verified this session** and reports every fetch failure inline rather than working around them. **Do not publish a marked-unverified fact as established.** The site's whole credibility position is that it corrects other people's unsourced numbers.

Specifically do not publish: *"Linux runs 90% of the cloud"* (no primary source exists), *"all 500 TOP500 systems run Linux"* (unverified — the table could not be fetched), Wikipedia's traffic figures (the circulating numbers are from February 2014), or *"70–90% of a codebase is open source"* (the real finding is 98% of audited codebases *contain* open source).

## Manifest tiers

- **Tier 3 (6 rows)** — do not publish, quote or paraphrase.
- **Tier 2 (2 rows)** — `FACT ONLY` and `RE-SOURCE`. Note the OWASP board claim is sourced from an investor document: **the fact is public and quotable; the document is not.** Cite the public record instead.
- **`CARE` / `VERIFY NUMBERS` / `STALE`** flags in Tier 0–1 mark documents that are publishable with specific fixes. Read `why_it_matters` before touching them.

---

This file is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).

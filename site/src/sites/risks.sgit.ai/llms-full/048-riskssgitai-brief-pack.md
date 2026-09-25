# risks.sgit.ai — brief pack

**For:** the agent commissioned to build `risks.sgit.ai`
**From:** Dinis Cruz, via the SG/Send Librarian
**Version:** v0.33.62 · 22 August 2026
**Licence:** CC BY 4.0 (see `LICENSE.md`)

---

## What this is

A **research site** for risk. Not a product site — that is `riskmandate.ai`, which stays commercial and starts referencing here instead of carrying the concepts itself.

The commission has two halves:

1. **Consolidate** ~496,000 words of risk thinking, written 18 June – 22 August 2026 (plus a February pre-history and 8 articles from 2025), into a surface an agent can hold. **42 distinct concepts**, most well-developed, almost none reachable today.
2. **Refactor** the concept material *out* of `riskmandate.ai`, leaving stubs that point here.

The audience named in the commission is **agents**: *"to handle the cases where I need agents to have a good understanding of some of those key concepts and ideas."* That is why `/agents/` and a machine-readable definitions endpoint are treated as first-class deliverables, not an afterthought.

---

## Read in this order

| File | Words | What it does |
|---|---:|---|
| **`00__BRIEF.md`** | 2.0k | **Start here.** The commission, the honesty constraint, the thesis, the ten concepts an agent must hold, the refactor table, the four vaults, the numbers, the build order |
| **`02__risk-acceptance.md`** | 1.6k | The commissioned centrepiece — the acceptance thread traced chronologically from June to August. Build `/acceptance/` from this |
| **`04__riskmandate-refactor.md`** | 1.0k | The other half of the commission — page-by-page split of `riskmandate.ai`, with the leave-behind stub template |
| `01__concepts-index.md` | 6.0k | All 42 concepts: canonical path, maturity, newcomer-readiness, best quote. Plus a six-altitude teaching order. This is the raw material for `/concepts/` |
| `03__worked-examples-and-vaults.md` | 1.8k | The four live risk vaults on `sgit.ai/demos/vaults/`, three worked graphs, prior-art table |
| `05__site-architecture.md` | 1.5k | Page-by-page IA, including `/agents/` and the definitions endpoint |
| `06__boundaries-and-house-style.md` | 2.3k | Seven-site boundary map, redaction watch-list, provenance rules |
| `07__gaps-and-open-questions.md` | 1.1k | 6 write-fresh items, 8 open questions, 7 honest tensions |
| `08__source-manifest.csv` | 37 rows | Every source, tiered 0–3, with proposed page and publishability. **Every path verified to exist at v0.33.62** |
| `sources__docs-diniscruz-ai-risk.json` | 8 articles | Prior art with `first_published`, `source_url`, `source_pdf`, `source_linkedin` — for canonical links |
| `LICENSE.md` | — | CC BY 4.0, plus the three regimes it does *not* cover |

---

## The three things that will bite you

**1. There is no risk code.** Not one line. The corpus is a specification, not an implementation. `/shipped/` must say so plainly — the sibling sites (`pki`, `nhi`, `sg-sentinel`, `issues-fs`) all ship a page that separates what exists from what is designed, and this site inherits that convention with an unusually empty column. Over-claiming here would poison the network's credibility.

**2. Four manifest rows are Tier-3.** Commercial terms, a competitor map naming two large vendors [REDACTED · Tier-3 · see PUBLIC.md], investment scenarios, a contract draft. They are in the manifest so you know to skip them. Do not publish, quote or paraphrase.

**3. The prior art is CC0, not CC BY.** The 8 `docs.diniscruz.ai` articles were published CC0. Republishing under CC BY is legally fine, but keep `rel="canonical"` on the original URL and the recorded `first_published` date. The historical link matters more than the licence does.

---

## House pattern

Same as the siblings: `/llms.txt` is the whole agent surface; `/llms-full.txt` is one-file concatenation; `/documents/` carries raw markdown as source of truth; `/admin/comms.html` numbers asks (N1…) and tasks (T1…); `/admin/versions.html` tracks versions; `/about/participant.html` names the participants. Publish the build order unresolved, with the open questions and the honest tensions visible. `07__gaps-and-open-questions.md` supplies both.

---

This file is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).



==============================================================================
== briefs/00__BRIEF.md — source document, verbatim
==============================================================================


# Brief pack — `threat-modeling.sgit.ai`

**Version** v0.33.63 · 7 September 2026 · CC BY 4.0

The commission pack for `threat-modeling.sgit.ai`. Its thesis: **a threat model is a claim about a system, and the site's job is to show claims being checked.** The estate can do this because on 16 March 2026 it wrote a threat model, and on 17 March it validated every finding against the actual code — publishing the ones that turned out to be proposals with nothing built behind them alongside the ones that were confirmed real.

## Contents

| File | Words | What it is |
|---|---|---|
| `00__BRIEF.md` | 932 | Commission, thesis, what exists, constraints, build order |
| `01__the-research.md` | 1,048 | The seven white papers as one four-move argument |
| `02__the-practice.md` | 1,307 | Seven real threat models; the validation pair; the method |
| `03__site-architecture.md` | 582 | URLs, claim→check spine, sibling deconfliction table |
| `04__disclosure-boundaries.md` | 685 | What may be published about a live product, by category |
| `05__the-vault-argument.md` | 775 | Threat models as vault-native data; real-vs-argued table |
| `06__gaps-and-open-questions.md` | 495 | 6 gaps, 7 questions (Q1 is a launch blocker) |
| `threat-models__catalogue.json` | — | Measured counts, 7 papers, 7 models, vault figures, sgit.ai context |
| `09__source-manifest.csv` | — | 4 tiers; all tier-0/1 paths verified on disk; counts via `wc -w` |

## Measured, not estimated

269 corpus files mention threat models · 58 AppSec role documents · 7 named threat-model documents · 27 files mention STRIDE · 19 mention attack trees. The ThreatModCon vault's figures (11 layers, 51 nodes, 179 threats, 3 critical findings) are **quoted from the published vault page, not computed** — gap G2 says recompute from the vault's own JSON before publishing them as generated.

## The one blocker

**Q1 — the closure pass.** Every finding in the practice section dates from February–March 2026. Nothing may be published as open or closed until re-checked against current code. Publishing a fixed vulnerability as open defames the product; publishing an open one as fixed is precisely what the mandatory-disclosure paper condemns.

## Licence

Pack text, tables, schemas and analysis: CC BY 4.0 (attribute Dinis Cruz; several source papers also credit ChatGPT Deep Research). STRIDE, MITRE ATT&CK, CAPEC, CWE/CVE, OWASP Top 10 and ASVS are referenced and linked, never reproduced.


---

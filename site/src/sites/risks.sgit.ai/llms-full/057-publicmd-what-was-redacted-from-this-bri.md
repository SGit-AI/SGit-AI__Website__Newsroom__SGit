# PUBLIC.md — what was redacted from this brief pack before publication

**Applies to:** the eleven source documents published under `/briefs/` on risks.sgit.ai
**Redacted:** 23 August 2026, at site v0.1.0
**Convention:** the same one the Regulation Graph vault adopted after an audit — *publish the
artefact, and publish what was taken out of it*. A clean document with an unexplained gap is
worse than a redacted one with a receipt.

---

## Why anything was redacted at all

The brief pack was written as a working document for the agent commissioned to build this site.
It names four sources as **Tier-3 — do not publish, quote or paraphrase** — and, being a working
document, it names them *by name* so the builder knows what to skip. That is correct for a
working document and wrong for a published one: republishing the pack verbatim would publish
exactly the four things the pack says not to publish.

So the pack is published in full, with the identifying detail of those four rows removed and each
removal recorded here. **Nothing else was changed** — no argument was softened, no number
adjusted, no finding dropped. Every redaction is marked in place with
`[REDACTED · Tier-3 · see PUBLIC.md]` or `[redacted]` inside a file path.

The rule is also enforced rather than remembered: `admin/build/validate.js` pattern-matches the
distinctive strings of all four Tier-3 rows across **every file in the tree**, with no exemption
for `briefs/`, and fails the build if one reappears. A future edit cannot quietly undo this.

---

## The four Tier-3 rows, and what was taken out

| Row | What it is | What was redacted |
|---|---|---|
| **Vendor assessment** (`tier 3`, manifest row 35) | A comparative maturity assessment scoring two named real companies at Level 1, concluding one presents more exposure on the axis it markets hardest. Rigorous, sourced, scrupulous about its own limits — and a legal and relationship exposure | **Both company names**, and the source file path that carries them. The row itself, its word count, its tier and its `HOLD - LEGAL READ` disposition are published unchanged |
| **Competitor map** (`tier 3`, manifest row 36) | Competitor maps naming two large risk-management vendors, with dismissive characterisations of their products | **Both company names**, the two disparaging quotes, and the file path that carries one of the names |
| **Investment strategy** (`tier 3`, manifest row 37) | Illustrative revenue, valuation and exit figures, explicitly framed at source as scenarios rather than projections | **The figures.** The existence of the document, its word count and its internal-only disposition are published unchanged |
| **Partnership contract draft** (`tier 3`, manifest row 38) | An actual contract draft with commercial terms | **The commercial terms**, in the prose and in the file path that spells them out |

## Where each redaction appears

| File | Redactions | What |
|---|---:|---|
| `08__source-manifest.csv` | 4 | The four Tier-3 rows: company names, source paths and commercial figures |
| `06__boundaries-and-house-style.md` | 6 | The redaction watch-list itself — company names, two quotes, four entries in the mention-count list, the investor figures, and the contract terms |
| `07__gaps-and-open-questions.md` | 1 | Company names in honest tension #5 |
| `04__riskmandate-refactor.md` | 1 | Company names and the disparaging quote in "what must not happen" |
| `README.md` | 1 | Company names in the Tier-3 warning |
| `LICENSE.md` | 1 | Company names in the licence scope note |

**Total: 14 redactions across 6 of the 11 documents.** Five documents — `00__BRIEF.md`,
`01__concepts-index.md`, `02__risk-acceptance.md`, `03__worked-examples-and-vaults.md` and
`05__site-architecture.md` — are published byte-identical to the pack as received.

---

## What is *not* redacted, and why

- **The fact that Tier-3 material exists**, its word counts, its tiers and its dispositions. A
  manifest naming a do-not-publish row is the mechanism working, and hiding the row would hide the
  mechanism.
- **Every other named organisation in the pack.** AWS, MITRE, the EU institutions, and the
  organisations named in the redaction watch-list's *other* categories are not Tier-3 and are not
  redacted — the pack's own reasoning for treating them differently is published intact.
- **The redaction watch-list's reasoning.** Section 2 of `06__boundaries-and-house-style.md`
  survives in full apart from the names: the analysis of *why* certain material needs a legal read,
  framing or a right of reply is the most useful part of that document and is published as written.

## Standing offer

If any organisation named in the un-redacted corpus believes a characterisation on this site is
unfair, that is [ask N3 on the comms board](https://risks.sgit.ai/admin/comms.html#n3) — a legal
read and a right-of-reply process is a precondition of publishing any of that material, and the
offer stands whether or not it is ever published.

---

This file is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).



==============================================================================
== briefs/LICENSE.md — source document, verbatim
==============================================================================


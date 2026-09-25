# 05 — Site architecture, and the split designed in from day one

## The decision this implements

Everything on `subscriptions.sgit.ai` now; the commercial service refactors out later to its own property **if a business partner emerges** — the `riskmandate.ai` / `risks.sgit.ai` pattern, run in the other direction (they split content out of a commercial site; this starts unified and splits the commercial part off). **Design for the split now and it is a DNS change; ignore it and it is a migration.**

Three mechanisms make the split cheap:

1. **The register data lives in a vault** — the site renders it. Re-pointing the render target moves the register to a neutral domain or non-profit without touching an entry. This also answers the founder-led-register criticism structurally: the data was never coupled to the founder's domain.
2. **The service pages live under one path** — `/service/` — and nowhere else links into their internals. The split is an export of one directory plus a stub.
3. **The licence boundary is drawn now** — everything outside `/service/` is CC BY forever; `/service/` content is CC BY too while it lives here, but its *branding and pricing* are the parts a partner would own, so keep them thin.

## Page by page

**`/`** — the principle as the epigraph, the do-you-hold-it question, the current register table (even at ten rows), and the last-row honesty: *"you did not use it" yields nothing on its own.*

**`/standard/`** — `01__`. The five clauses, the adopters list, the conformance route (policy page = answer), and **`/standard/proposal/`** — the law-shaped draft, explicitly labelled a proposal, with the 2027-regime delta table. This is the legislative artefact.

**`/register/`** — `02__`. The table, the schema, the templates by version, the governance page (selection rule, interval, review process) published **before entry one**.

**`/exit/`** — the exit-path measurements: method first, then fifty companies, dated, re-runnable. **The first thing built.**

**`/workflows/`** — `03__`. The agentic pipeline with the plaintext step stated, the vault architecture, the parser workspaces, BYOM-first. This page doubles as the sgit showcase and should be linked from `sgit.ai` and the `services.sgit.ai` gallery when that exists.

**`/law/`** — `04__`. The levers table, the status table, as-at dates, named owner. **The pages with an expiry date.**

**`/service/`** — the future-commercial directory: intake, the merit test, the decline rate, fees. Thin at launch; the founder's ten cases run through it.

**`/shipped/`** — what exists vs designed, per house pattern: at launch, the standard and the method exist; the register has N rows; the parsers have M providers; the service has one client, who built it.

**`/network/`, `/admin/`** — house pattern; `/llms.txt` self-sufficient; `/llms-full.txt`; markdown twins.

## Boundaries within the network

| Site | Relationship |
|---|---|
| `standards.sgit.ai` | Owns instruments-as-graphs; **this site's law pages link its method** (dated provisions, "derived not canonical") rather than rebuilding it |
| `risks.sgit.ai` | The acceptance/evidence vocabulary; the claim file is a small evidence graph |
| `nfrs.sgit.ai` | The dated-page/staleness discipline — this site is its sharpest test case |
| `open-source.sgit.ai` | The standard-as-adoptable-artefact argument; CC BY rationale |
| `llms.sgit.ai` / `coding.sgit.ai` | The agentic workflow conventions the parsers follow |
| `sgit.ai` | **Should feature `/workflows/` as the business-model worked example** |

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
== briefs/v0.33.62__subscriptions-brief-pack__06__publishing-rules-and-boundaries.md
==============================================================================

# Licence

## This pack

Everything in this brief pack — all eight numbered markdown files, `08__source-manifest.csv`, `sources__docs-diniscruz-ai-risk.json`, this file and `README.md` — is released under the **Creative Commons Attribution 4.0 International licence (CC BY 4.0)**.

    Copyright (c) 2026 Dinis Cruz
    Licensed under CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/

Attribution: **Dinis Cruz**, with AI co-authorship (Claude, Anthropic). Where a source document names model co-authors, carry those names forward.

CC BY is irrevocable. That is deliberate: the point is that these documents remain readable, quotable and re-mixable by the author, by other people, and by agents, permanently and without asking.

## The site this pack commissions

**The entire content of `risks.sgit.ai`** — every page, every file under `/documents/`, `/llms.txt`, `/llms-full.txt`, and the admin surfaces — is to be published under **CC BY 4.0**, consistent with the rest of the `*.sgit.ai` network. Put the licence in `/llms.txt`, in the page footer, and as a line at the foot of every raw markdown document:

    This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).

Use `licence-audit.py` (shipped in the `graphs.sgit.ai` pack, file `licence-audit.py`) in `--check` mode as a CI gate so the stamp cannot silently drift.

## What this licence does *not* cover

Three categories carry different regimes. Do not assume CC BY where it does not apply.

| Material | Regime | What the site must do |
|---|---|---|
| **The 8 prior-art articles on `docs.diniscruz.ai`** (Feb–Jul 2025, 59,131 words) | **CC0 1.0** as published on that site | CC0 is *more* permissive than CC BY, so republishing under CC BY is legally fine — but attribute anyway, and keep `rel="canonical"` pointing at the original URL plus the recorded `first_published` date. See `sources__docs-diniscruz-ai-risk.json`. |
| **Source PDFs and LinkedIn posts** referenced in that JSON | As originally published | Link, do not mirror silently. Record `source_pdf` and `source_linkedin` in front-matter. |
| **Vault contents** at `sgit.ai/demos/vaults/` | Per-vault; read keys are publishable, **write keys never** | Before linking a vault from `risks.sgit.ai`, confirm the write key is escrowed. Publishing a read key for a vault whose write key is lost freezes it permanently. Each vault should carry a `PUBLIC.md`. |
| **Tier-3 rows in the manifest** (4 rows) | Internal — commercial terms, competitor naming, investment scenarios | **Do not publish, do not quote, do not paraphrase.** They are listed so you know they exist and know to skip them. |

## Third-party names

The corpus names real organisations (two large risk-management vendors [REDACTED · Tier-3 · see PUBLIC.md], AWS, MITRE), real frameworks (EU AI Act Article 26(5), MITRE ATT&CK T1110.004) and real people. Naming a framework or citing a technique is fine. Reproducing a competitor map, or attributing a position to a named company, is not — that material is Tier-3 for exactly this reason. See `06__boundaries-and-house-style.md` § redaction watch-list.

---

This file is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).

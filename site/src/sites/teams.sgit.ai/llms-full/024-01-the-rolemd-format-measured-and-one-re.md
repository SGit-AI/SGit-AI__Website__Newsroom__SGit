# 01 — The `ROLE.md` Format: measured, and one recommendation

**Version** v0.33.64 · 7 September 2026
**Method** All 39 `ROLE.md` files on disk parsed for section headers and Identity fields, 7 September 2026. Every count below is generated, not estimated.

---

## 1. The schema

Five fields make up a role's identity, and they appear (in one markup or the other) across 31 of the 39 files:

| Field | What it does | Why it matters |
|---|---|---|
| **Name** | The role's handle | It is how other roles address it in comms |
| **Location** | `team/roles/<name>/` | The role's home for reviews and outputs |
| **Core Mission** | One sentence of purpose | The routing key — the Conductor reads this to assign work |
| **Central Claim** | The role's testable assertion | See §3. This is the field that does the real work |
| **Not Responsible For** | The explicit exclusion list | See §2. This is the field nobody else writes |

## 2. `Not Responsible For` — the field that makes it a team

**31 of 39 role files carry it.** It is the most distinctive thing in the corpus and the reason a multi-role setup works at all.

Conductor: *"writing code, running tests, deploying infrastructure, making architecture decisions, or performing security reviews."* Librarian: *"writing application code, making architecture decisions, running tests, deploying infrastructure, creating original specifications, or making product decisions."*

Why it matters more than the responsibility list: an LLM given a task will attempt it. Capability is not the constraint — **willingness is**, and the exclusion list is the only thing that converts a capable generalist into a specialist that hands off. Without it, every role silently becomes the same role, and a "team" of nine agents is one agent invoked nine times.

The site should state this as a rule: **a role without an exclusion list is not a role.**

## 3. `Central Claim` — write it as a failure condition

This is the pack's most useful finding, and it is a regression the estate has not noticed.

**The older bullet-list format states claims as falsifiable failures**:

- Librarian — *"If a piece of knowledge exists in this repo but cannot be found in under 30 seconds, the Librarian has failed."*
- Cartographer — *"If a dependency, data flow, or security boundary exists but is not visible on a map, the Cartographer has failed."*
- AppSec — *"If any code path exists where plaintext, decryption keys, or original file names could reach the server, AppSec has failed."*
- Historian — *"If a decision was made but its rationale is not recorded, the Historian has failed. The team will re-litigate it…"*
- Journalist — *"If a potential user visits the site and cannot understand the zero-knowledge guarantee within 60 seconds, the Journalist has failed."*

**The newer table format states them descriptively**:

- Architect — *"The Architect owns the boundaries. Every interface contract… passes through architectural review."*
- Conductor — *"The Conductor sees the full picture. No task starts without routing."*
- QA — *"QA owns the test matrix… No release ships without QA sign-off."*

The descriptive claims are true and useful. But you cannot *check* them. The failure-condition claims name a condition, a threshold and sometimes a time bound — *thirty seconds*, *sixty seconds* — which means an auditor (human or agent) can look for a counter-example and find one. That is the same falsifiability discipline that runs through `risks.sgit.ai`, `wardley-maps.sgit.ai` ("maps are claims") and `threat-modeling.sgit.ai` (the validated threat model), applied to organisational design.

**Recommendation for the site**: publish the failure-condition form as the canonical one, show the drift honestly, and offer a rewrite of the seven descriptive claims into testable form as an open build item.

## 4. Format drift, quantified

Across the 17 Explorer role directories:

| State | Count | Roles |
|---|---|---|
| Identity as **table** (`\| **Field** \|`) | 7 | architect, conductor, designer, dev, devops, dpo, qa |
| Identity as **bullet list** (`- **Field:**`) | 6 | appsec, cartographer, grc, historian, journalist, librarian |
| **No `ROLE.md` at all** | 4 | advocate, alchemist, ambassador, sherpa |

Two markup dialects of one schema, plus four directories that exist without a definition. The schema is stable; the presentation is not. A parser reading these files must handle both — which is itself an argument for the site publishing a **canonical machine-readable form** (`teams__roster.json` in this pack is the first cut) rather than only prose.

## 5. Section anatomy, by frequency

Measured across all 39 files:

| Section | Files | Note |
|---|---|---|
| `## Identity` | 37 | The schema above |
| `## Tools and Access` | 37 | Where skills are named — link out to `skills.sgit.ai` |
| `## For AI Agents` | 37 | **The role speaking to its own occupant** — see below |
| `## Quality Gates` | 32 | What must be true before the role signs off |
| `## Core Workflows` | 25 | The role's repeatable procedures |
| `## Primary Responsibilities` | 19 | |
| `## Integration with Other Roles` | 19 | The routing table, per role |
| `## Measuring Effectiveness` | 18 | |
| `## Escalation` | 18 | When to hand up rather than out |
| `## What You DO (Villager Mode)` | 17 | Topology-specific mandate |
| `## What You Do NOT Do` | 15 | The prose form of the exclusion list |
| `## Incident Response` | 12 | |

**`## For AI Agents` in 37 of 39 files is the quiet innovation.** These documents are written for a non-human occupant and say so in a dedicated section. That is the difference between an org chart and an agent brief, and it is the section a reader building their own team should copy first.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
source: /briefs/02__the-roster.md

==============================================================================


# 06 — Site Architecture: `teams.sgit.ai`

**Version** v0.33.64 · 7 September 2026
**Base** House pattern (copy `pki.sgit.ai`): `llms.txt` + `/llms-full.txt`, `/documents/` raw markdown, markdown twin at every URL, `/admin/comms.html`, `/shipped/`, versions, participant page.

---

## 1. URL scheme

```
/                      Roles are boundaries. The Conductor never does the work.
/role-format/          the ROLE.md schema, measured; the failure-condition claim
/role-format/drift/    the two dialects and the four empty directories, honestly
/roster/               the nineteen roles; the portable six; add-a-role triggers
/roster/<slug>/        one role: claim, exclusions, comms addresses, tools
/topologies/           Explorer / Villager / Town Planner; the handback rules
/topologies/designer/  the same role, three ways — the fastest way to get it
/comms/                inbox/outbox addressing; the session-start ritual
/evolution/            dated learnings as diffs; what broke, what rule was added
/setup/                stand up a multi-role team from these files
/documents/            raw markdown of everything
```

## 2. The site is a reference, so ship the machine-readable form

The primary consumer is an agent being configured. `teams__roster.json` (this pack) is the seed: every role with tier, teams present in, claim, claim-form (falsifiable / descriptive / absent), exclusions, comms addresses. The site serves it at a stable URL alongside the prose, and every `/roster/<slug>/` page is a projection of one record.

**Ship the raw `ROLE.md` files too**, under `/documents/`, so a reader can copy one and start. A reference site about reusable role definitions that makes you retype them has failed its own Librarian test.

## 3. Generated, not claimed

Role counts, per-team coverage, format-dialect tallies, commit counts per role, and the timeline dates are all derivable from the repo. Publish the scan script's identity and date beside every number, and regenerate on each build. `01__` and `02__` carry the 7 September 2026 figures; they will drift.

## 4. Deconfliction

| Topic | Owner | This site's part |
|---|---|---|
| `SKILL.md`, skill lifecycle, description-as-trigger | **skills.sgit.ai** | Only *which* skills a role holds, linked out |
| Pioneers–Settlers–Town Planners, evolution axes | **wardley-maps.sgit.ai** | Only the staffing of PST as three agent teams |
| Issues-as-files, the `.issues/` tree | **issues-fs.sgit.ai** | Only how roles address it |
| Coding conventions the Dev role follows | **coding.sgit.ai** | Only that the role points there |
| CI, testing, documentation as properties | **nfrs.sgit.ai** | Only the roles that own them |
| Vault keys, `sgit` mechanics | **pki.sgit.ai** / sgit.ai | Only the prohibition as it appears in a role file |
| Threat modelling as a method | **threat-modeling.sgit.ai** | Only that AppSec is the role that does it |

The rule: **this site owns composition.** Anything about the work itself belongs to the site that owns that work.

## 5. `/setup/` is the page people will actually use

Everything else is reference; this is the deliverable. It should answer, in order: which six roles to start with (the portable core, evidenced by sg-playwright), what each one's exclusion list must say, where to put the comms tree, what the session-start sequence is, and when to split into Explorer/Villager. Written as a procedure, with the corpus's own files as the worked example.

## 6. What this site does NOT do

No agent-framework comparison (LangGraph, CrewAI, AutoGen) — the corpus has no evidence about them and inventing it would break the network's sourced-claims rule. No claim that these roles are optimal; they are *ours, measured, with the gaps shown*. And no synthetic role definitions: the four empty directories stay empty on the site until someone writes them, labelled as missing.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
source: /briefs/07__boundaries-and-licensing.md

==============================================================================


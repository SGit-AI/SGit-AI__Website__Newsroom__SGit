# 00 — The Brief: `teams.sgit.ai`

**Version** v0.33.64 · 7 September 2026
**From** Dinis Cruz, via the SG/Send Librarian
**To** the agent commissioned to build `teams.sgit.ai`
**Licence** CC BY 4.0

---

## 1. The commission

The key reference for setting up **agentic teams with more than one role**: the effective workflows and how they evolved, the `ROLE.md` and `SKILL.md` reference material, and the learnings that got written back into the role definitions after something went wrong.

**The name, decided:** `teams.sgit.ai`. The unit is the *team*, not the agent. Every site in the network is named for its unit, and this one is named for the thing the industry keeps skipping.

**The tagline:** *Roles are boundaries. The Conductor never does the work.*

---

## 2. The thesis

> **The leverage in agentic work is division of labour, not model capability.**

The evidence is in the corpus and it is unusual. Most people building multi-agent systems write down what each agent *can* do. This estate writes down what each agent **must not** do — and it does so in a named schema field. The Conductor's own definition lists, under *Not Responsible For*: *"writing code, running tests, deploying infrastructure, making architecture decisions, or performing security reviews."* Its governing principle is stated outright:

> *"Roles are boundaries. The Conductor routes work to the right role; the Conductor never does the work."*

And the second thesis, which the corpus proves and almost nothing else in the field does:

> **A role definition is a falsifiable claim, and it should be written as a failure condition.**

Six roles state their Central Claim as an *if-then failure*: *"If a piece of knowledge exists in this repo but cannot be found in under 30 seconds, the Librarian has failed."* *"If a dependency, data flow, or security boundary exists but is not visible on a map, the Cartographer has failed."* *"If any code path exists where plaintext, decryption keys, or original file names could reach the server, AppSec has failed."* A role written this way can be audited. A role written as a job description cannot.

---

## 3. What exists — measured 7 September 2026

**39 `ROLE.md` files. 19 unique role names. Four team instantiations.**

| Team | Role directories | With `ROLE.md` | Character |
|---|---|---|---|
| **Explorer** (`team/roles/`) | 17 | 13 | Builds new things |
| **Villager** (`team/villager/roles/`) | 17 | 17 | Hardens what Explorer built |
| **Town Planner** (`team/town-planner/roles/`) | 4 | 3 | Financial models, investor narrative, commodity classification |
| **sg-playwright** (`team/roles/`) | 6 | 6 | A second product, same method |

The nineteen: accountant · advocate · alchemist · ambassador · appsec · architect · cartographer · conductor · designer · dev · devops · dpo · grc · historian · journalist · librarian · qa · sherpa · translator.

**The finding that should be the site's second page.** Explorer / Villager / Town Planner is **Wardley's Pioneers–Settlers–Town Planners, staffed as three agent teams** — the same role names carrying different mandates at different evolutionary stages. The Villager Designer's brief is explicit: *"The UX as delivered by Explorer is what ships. No additions, no changes… Do NOT design new UX features — send to Explorer."* The Villager AppSec: *"Security architecture is frozen from Explorer. Harden what exists. If a redesign is needed, send it back."* The handback path is named in the role definition itself.

Nobody else has published this. It is the most original thing in the corpus on this subject.

**130 files in `team/comms/`** — the inter-role protocol: `briefs/`, `changelog/`, `plans/`, `qa/briefs/`, `qa/questions/`, and a `QA_START_HERE.md` landing page.

**40 `SKILL.md` files**, 7 first-party in `library/skills/` — but these belong to the sibling; see §5.

---

## 4. The honest constraints

- **The format drifted, and it regressed.** Of 17 Explorer role directories: 7 carry the Identity schema as a *table*, 6 as a *bullet list*, and 4 have no `ROLE.md` at all (advocate, alchemist, ambassador, sherpa). Worse, the newer table format's Central Claims are *descriptive* (*"The Architect owns the boundaries"*) while the older bullet format's are *falsifiable* (*"…the Librarian has failed"*). **The migration lost the best property of the format.** The site should say so and recommend restoring it. This is the pack's most useful single finding.
- **The Town Planner team is thin** — 4 directories, 3 definitions, and its Librarian is missing. Publish it as a sketch, not a template.
- **Role evolution is in git, not in the files.** The learnings the founder asked for exist only as diffs. `05__` does that archaeology; the site must keep doing it.

---

## 5. Deconfliction: `skills.sgit.ai` already exists

The network page lists nineteen sites — eighteen live, and `skills.sgit.ai` with subdomain and repo established but nothing published. The seam, decided:

> **A skill is a capability. A role is a boundary. A team is a routing table.**

`skills.sgit.ai` owns `SKILL.md` — anatomy, description-as-trigger, lifecycle, the seven first-party skills. `teams.sgit.ai` owns `ROLE.md`, the roster, the topologies, the comms protocol and the workflows. Each links to the other; neither duplicates. Where this site shows a role's tool access, it names the skills and links out.

---

## 6. Build order

1. **`/role-format/`** — the `ROLE.md` schema, measured, with the failure-condition claim as the recommended form and the drift documented (`01__`).
2. **`/roster/`** — nineteen roles, each with its claim, its boundary and its comms addresses (`02__`).
3. **`/topologies/`** — Explorer / Villager / Town Planner, and the handback rule. Links to `wardley-maps.sgit.ai` for PST itself (`03__`).
4. **`/comms/`** — the inbox/outbox protocol and the session-start ritual (`04__`).
5. **`/evolution/`** — the dated learnings, as diffs (`05__`). This is the memory layer and the reason the site is not a template gallery.
6. **`/setup/`** — the assembly guide: how to stand up a multi-role team from these files.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
source: /briefs/01__the-role-format.md

==============================================================================


# 02 — The Roster: nineteen roles

**Version** v0.33.64 · 7 September 2026
**Source** `SGraph-AI__App__Send/team/` (Explorer, Villager, Town Planner) and `sg-playwright/team/roles/`

---

## The nineteen

Grouped by what they are *for*, not alphabetically — because the grouping is itself the lesson about how to compose a team.

### Build (5)
**architect** · **dev** · **devops** · **qa** · **designer**

The conventional core. Two things are not conventional. First, the Architect's claim is about *boundaries*, not design: *"The Architect owns the boundaries. Every interface contract, dependency direction, and abstraction layer passes through architectural review."* Second, the Designer's remit is unusually wide — *"A well-designed API is as much a design artifact as a well-designed interface. The structure of a configuration file, the shape of a CLI command, the naming of a function, the rhythm of a test suite — these are all design."* That role is where the estate's Design-with-a-capital-D influence lands operationally (the Jonathan Ive test as a mandatory UI validator).

Designer is also the newest of the founding group — added **16 March 2026**, five weeks after the rest.

### Assure (4)
**appsec** · **grc** · **dpo** · **advocate**

Security, risk, data protection, and the user's corner. Three carry falsifiable claims; the DPO's is the sharpest on consequence: *"If a privacy claim is made that is not legally accurate, the DPO has failed."*

### Remember (4)
**librarian** · **historian** · **cartographer** · **journalist**

**This quartet is the estate's real signature and the hardest thing for others to copy.** Each owns a different failure of institutional memory:

- **Librarian** — findability. *"If a piece of knowledge exists in this repo but cannot be found in under 30 seconds, the Librarian has failed."*
- **Historian** — rationale. *"If a decision was made but its rationale is not recorded, the Historian has failed. The team will re-litigate it…"*
- **Cartographer** — visibility. *"If a dependency, data flow, or security boundary exists but is not visible on a map, the Cartographer has failed."*
- **Journalist** — comprehensibility to outsiders, with a time bound: sixty seconds to understand the zero-knowledge guarantee.

Four roles whose entire job is that the team can still think next month. This is the same thesis as the sites-as-memory network, staffed.

### Route (1)
**conductor**

The orchestrator that does no work. Principles worth publishing verbatim: *"Flow over heroics"*, *"Priority is singular"* (every role knows its single most important task), *"Visibility is accountability"* (*"if it is not tracked in `.issues/` or a review document, it does not exist"*), *"Roles are boundaries"*, *"Blockers decay fast"* (*"an unresolved blocker older than one session is an escalation"*).

### Represent (3)
**ambassador** · **sherpa** · **translator**

Outward and onboarding-facing. `translator` exists only in the Villager team — worth asking why (Q4).

### Capitalise (2)
**accountant** · **alchemist**

Town Planner roles. The Accountant *"provides the financial models and projections that the Alchemist wraps in investor narrative."* An agent role for turning numbers into a story, named *alchemist* — the honesty of that naming is a small masterpiece and should be quoted on the site.

---

## Where each role exists

| Role | Explorer | Villager | Town Planner | sg-playwright |
|---|---|---|---|---|
| architect · dev · devops · qa · historian · librarian | ● | ● | ○ | ● |
| designer | ● | ● | ● | ○ |
| appsec · grc · dpo · cartographer · journalist · conductor · advocate · ambassador · sherpa | ● | ● | ○ | ○ |
| alchemist | ● | ○ | ● | ○ |
| accountant | ○ | ○ | ● | ○ |
| translator | ○ | ● | ○ | ○ |

● present · ○ absent. Explorer has 17 directories but only 13 definitions (advocate, alchemist, ambassador, sherpa are empty); Town Planner has 4 directories and 3 definitions (librarian missing). The site must publish the gaps as gaps — a roster page that hides four empty roles is exactly the false memory `nfrs.sgit.ai` warns about.

## The portability finding

**Six roles are defined in all three *operational* teams** — architect, dev, devops, qa, historian, librarian — across Explorer, Villager and the second product, sg-playwright. (Town Planner is excluded from this test: it is a commercial team — accountant, alchemist, designer, librarian — not an operational one, and only its Librarian overlaps.)

That is the reusable core, and it answers the reader's real question ("what roles do I actually need?") with evidence rather than opinion: the estate independently reached for these six when standing up a second product, which is the closest thing to a controlled experiment the corpus contains.

The `/roster/` page should lead with those six as the recommended starting team, and present the other thirteen as additions with a stated trigger — *add a DPO when you process personal data; add a Cartographer when the dependency graph outgrows one head; add a Journalist when outsiders must understand you.*

## Growth timeline (from git)

| Date | Event |
|---|---|
| **11 Feb 2026** | *"Add ROLE.md identity documents for all 10 agent roles"* — eleven files land: appsec, architect, cartographer, conductor, dev, devops, historian, journalist, librarian, qa (+1) |
| **12 Feb 2026** | advocate, grc, sherpa |
| **13 Feb 2026** | ambassador, dpo — and *"Execute full team activation for incident handling series (5 phases)"*, the first real exercise |
| **16 Mar 2026** | designer |

Ten to nineteen in five weeks, then stable. Note the commit message says *ten* roles while eleven files landed — publish the discrepancy rather than smoothing it; a memory site that quietly corrects its own sources teaches agents to do the same.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
source: /briefs/03__the-three-topologies.md

==============================================================================


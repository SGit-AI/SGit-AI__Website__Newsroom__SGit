# teams.sgit.ai — roles are boundaries

> **Roles are boundaries. The Conductor never does the work.** The reference for
> setting up agentic teams with more than one role — not what each role can do, but
> how nineteen of them are composed into a team that hands work off instead of one
> generalist doing everything nine times.

*Measured from [Dinis Cruz's](about/index.html) own product team, SG/Send: 39
`ROLE.md` files, 19 unique role names, four team instantiations, 130 comms files and
4,335 commits searched — 7 September 2026.*

*Source: <https://teams.sgit.ai/index.html> · site v0.1.0 · markdown twin of the front page.*

---

## What exists, measured

Every number here is computed from [`data/roster.json`](data/roster.json) on every
build, not typed. 19 unique role names across four team instantiations. 6 carry a
**falsifiable** central claim — the recommended, older form. 7 carry a **descriptive**
claim — true, but not checkable. 6 have **no Core Mission or Central Claim recorded**
and are published as gaps. 6 form the **portable core** — reached for twice,
independently, when the estate stood up a second product.

## The finding

Explorer, Villager and Town Planner are the same role names, staffed with different
mandates — Wardley's Pioneers–Settlers–Town Planners, implemented as agent
configurations rather than drawn as a diagram. As far as the commissioning pack can
determine, nobody else has published this.

- **Explorer** — build the new thing. 17 role directories, 13 defined. The governing
  rule is *discover*. [The topologies →](topologies/index.html)
- **Villager** — harden what exists. 17 directories, 17 defined — the only complete
  team. *"Harden, do not build."* If a redesign is needed, send it back to Explorer.
- **Town Planner** — industrialise and capitalise. 4 directories, 3 defined — a
  sketch, not a template. Financial models wrapped in investor narrative.

## What makes it a team, not one agent nine times

An LLM given a task will attempt it. Capability is not the constraint — willingness
is — and two fields in the format are what convert a capable generalist into a
specialist that hands off.

- **`Not Responsible For`** — 31 of 39 files. The explicit exclusion list. A role
  without one is not a role. [The format, in full →](role-format/index.html#exclusions)
- **The Central Claim, as a failure condition** — 6 of 39 files. *"If a piece of
  knowledge exists in this repo but cannot be found in under 30 seconds, the Librarian
  has failed."* Checkable. The newer table format lost this.
  [The drift, quantified →](role-format/index.html#claim)
- **Addresses, not messages** — 130 comms files. A role's definition names the
  directories it reads and writes, so a new occupant knows its inbox and outbox
  without being told. [The comms protocol →](comms/index.html)

## What this site does not smooth over

A memory site that edits its own past teaches agents to do the same — so the honest
parts are published as content, not footnotes.

- **A regression.** Six older roles state their claim as a falsifiable failure. Seven
  newer ones state it descriptively — true, but not checkable. The migration improved
  the markup and lost the property that made the field valuable.
- **Six roles carry no recorded Core Mission or Central Claim.** advocate, alchemist,
  ambassador and sherpa have an empty directory in Explorer; accountant and translator
  are marked defined elsewhere with no identity fields extracted from that file. Town
  Planner's librarian directory is a fifth, separate empty case. Published as gaps,
  never filled in for this website. [See where they exist →](roster/index.html)
- **Learnings recovered from diffs, not files.** A `ROLE.md` shows what a role is
  today. The history shows what went wrong badly enough that someone wrote a rule into
  it. [Three learnings →](evolution/index.html)

## Build one

Everything above is reference. [The assembly guide](setup/index.html) is the
deliverable: which six roles to start with, what each exclusion list must say, where
the comms tree goes, and when to split into Explorer and Villager. Or
[read the source pack first](documents/index.html).

---

CC BY 4.0 — Dinis Cruz, with AI co-authorship (Claude, Anthropic).
Pioneers–Settlers–Town Planners is Simon Wardley's model, credited and linked, never
reproduced.

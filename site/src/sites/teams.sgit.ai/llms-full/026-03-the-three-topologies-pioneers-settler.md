# 03 — The Three Topologies: Pioneers, Settlers, Town Planners, staffed

**Version** v0.33.64 · 7 September 2026
**Source** `team/roles/` (Explorer), `team/villager/roles/`, `team/town-planner/roles/`

---

## 1. The finding

The repo contains **three staffed teams using the same role names with different mandates**, and the naming is Wardley's: Explorer (pioneer), Villager (settler), Town Planner. This is Pioneers–Settlers–Town Planners implemented as agent configurations rather than drawn as a diagram.

As far as this pack can determine, **nobody else has published this**. It should be the site's second page and the thing it is known for.

## 2. What each team is for

| | **Explorer** | **Villager** | **Town Planner** |
|---|---|---|---|
| Mandate | Build the new thing | Harden what exists | Industrialise and capitalise |
| Roles | 17 dirs / 13 defined | 17 / 17 | 4 / 3 |
| Governing rule | Discover | *"Harden, do not build"* | Classify and fund |
| On encountering a needed redesign | Do it | **Send it back to Explorer** | — |

The Villager mandate is stated in the role files, not inferred:

> *"The code works. Your job is to make it work reliably under production conditions."*
> *"Preserve behaviour exactly — every change must produce identical outputs for identical inputs. If behaviour changes, send it back to Explorer."*
> *"User experience is frozen — the UX as delivered by Explorer is what ships. No additions, no changes."*
> *"Harden, do not redesign — security architecture is frozen from Explorer. Harden what exists. If a redesign is needed, send it back."*

And the corresponding exclusions: *"Do NOT design new UX features — send to Explorer."* *"Do NOT redesign security architecture — that's Explorer territory."*

The Town Planner team is small and commercial: the Accountant *"provides the financial models and projections that the Alchemist wraps in investor narrative"*, with the Cartographer supplying *"maturity classification (Genesis/Custom/Product/Commodity) and Wardley map financial flows"* — the evolution axis reappearing as the thing that decides which team owns a component.

## 3. Why this solves a real problem

The failure mode in multi-agent systems is not incapacity; it is **an agent improving something it was asked to preserve**. A capable model handed hardening work will notice a better design and implement it, and the result is a system that never stabilises because every pass rewrites the previous one.

The Villager mandate is a *refusal* engineered into the role: preserve behaviour exactly, and when you see something better, **hand it back rather than build it**. That is a genuinely hard instruction to give a capable generalist, and writing it into the role definition — with the destination named — is what makes it stick.

**The handback path is the mechanism.** A topology without a defined return route is just a label; here, every freeze rule names where the work goes instead.

## 4. How to publish it

`/topologies/` should carry:

1. **The three mandates side by side**, quoted from the role files.
2. **The same role, three ways** — Designer is the best example, existing in all three teams: creating UX in Explorer, guarding frozen UX in Villager, and shaping investor-facing material in Town Planner. One page showing one role's three definitions makes the whole idea land faster than any explanation.
3. **The handback rules** as a table: what is frozen, and where it goes when it must change.
4. **The link to `wardley-maps.sgit.ai`** for PST itself — that sibling owns the model; this site owns only its staffing. Do not re-teach evolution axes here.

## 5. The honest caveats

- **Town Planner is a sketch**, not a template: four directories, three definitions, its Librarian missing, and its content is investor-facing rather than operational. Publish it as an early experiment.
- **The transition is undocumented.** Nothing in the corpus states *when* a component moves from Explorer to Villager, or who decides. The Cartographer's Genesis/Custom/Product/Commodity classification is the obvious candidate, but that connection is inferred by this pack, not stated in the files. It is the single most valuable thing the founder could write next (Q3), and until he does, the site says the trigger is undefined.
- **Explorer/Villager may have been driven by context limits as much as by Wardley theory** — running one enormous team is impractical, and splitting it is convenient. If that is the real origin, say so; a discovered-then-rationalised pattern is still a good pattern, and the honesty is worth more than the theory.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
source: /briefs/04__the-comms-protocol.md

==============================================================================


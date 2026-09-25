# 07 — Boundaries and Licensing

**Version** v0.33.64 · 7 September 2026

---

## 1. What is being published

Role definitions, a comms protocol, and the git history of both — all the founder's own work, in his own repos. **This is the least legally exposed site in the network**: no third-party text to reproduce, no findings about a live system, no personal data. The whole corpus can go out under CC BY 4.0.

That makes the *reuse* question the interesting one, not the permission question.

## 2. Publish for copying — and make the licence say so

The point of this site is that someone stands up their own team from it. CC BY 4.0 permits that, including commercially, with attribution. State it in plain words on `/setup/`: *take these role files, change the names, ship your team; keep the attribution line.* A reference site whose licence terms are ambiguous will simply not be used.

The role files should carry the attribution line **inside** them, as a comment or footer, so it survives being copied out of the site and into someone's repo — which is exactly how they will travel.

## 3. What must be scrubbed before publication

The `ROLE.md` files are operational documents from a live product team. Before any file is published verbatim:

| Category | Action |
|---|---|
| Vault keys, share tokens, access tokens, API keys | **Never publish.** The 8 April commit exists *because* this is a live risk; grep every file before it ships |
| Internal hostnames, bucket names, account IDs, ARNs | Replace with placeholders |
| Paths into private repos | Keep — they are structural and carry no secret — but check for anything under a private path that reveals unreleased work |
| Named individuals other than the founder | Remove or get consent; roles are named by function, so this should be rare |
| `.issues/` references pointing at unresolved security defects | Generalise; cross-check against `threat-modeling.sgit.ai`'s disclosure rule |

**The grep is a build step, not a review step.** Run it in CI over everything the site publishes, the same way `licence-audit.py --check` runs elsewhere in the network.

## 4. Third-party frameworks

**Wardley's Pioneers–Settlers–Town Planners** is Simon Wardley's model, published by him under CC BY-SA. Name it, credit him, link to `wardley-maps.sgit.ai` and to his own material. The site's contribution is the *staffing* of it, which is original. Do not present PST as the estate's idea, and do not reproduce his diagrams — redraw, as `influences.sgit.ai` requires.

**Team Topologies** and **Cynefin** appear in the corpus as influences; if the site references them, same rule — name, credit, link, never reproduce.

## 5. The honesty rule that outranks the licence

This site's value is that its claims are checkable against a real repo. Two consequences:

1. **Never publish a role definition that does not exist on disk.** Four Explorer directories and one Town Planner directory have no `ROLE.md`; they are published as gaps, never as drafts written for the website. An invented role definition would make every real one unverifiable.
2. **Never smooth the history.** The commit that says ten roles while eleven files landed, the format regression, the undocumented Explorer→Villager trigger — these go on the site as they are. A memory site that edits its own past teaches agents to do the same.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
source: /briefs/08__gaps-and-open-questions.md

==============================================================================


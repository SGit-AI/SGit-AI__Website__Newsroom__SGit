# 08 — Gaps and Open Questions

**Version** v0.33.64 · 7 September 2026
**House rule** Published unresolved. Questions go to `/admin/comms.html`.

---

## Gaps

**G1 — Four Explorer roles have no definition**: advocate, alchemist, ambassador, sherpa. Directories exist, `ROLE.md` does not. Town Planner's librarian is likewise missing. Publish as gaps; do not write them for the website (`07__` §5).

**G2 — The Explorer→Villager transition trigger is undocumented.** Nothing states when a component moves from build to harden, or who decides. The Cartographer's Genesis/Custom/Product/Commodity classification is the obvious mechanism, but that link is this pack's inference, not the corpus's statement. It is the highest-value thing the founder could write next.

**G3 — No `SKILL.md`-to-role mapping exists.** 40 skill files and 39 role files, with no index of which roles hold which skills. Both sites need it; it is the natural shared artefact and the cleanest way to prove the capability/composition seam works.

**G4 — The workflows are implicit.** The founder asked for *"highly effective agentic workflows"*. What the corpus holds is 25 `## Core Workflows` sections inside role files, plus 130 comms files showing workflows in action — but no standalone workflow documents. Whether the site should extract them into first-class pages, or keep them role-scoped, is an editorial decision (Q6).

**G5 — Effectiveness is asserted, not measured.** 18 role files have a `## Measuring Effectiveness` section, but no measurements appear anywhere in the corpus. The site cannot claim these roles work; it can only show they are defined, used, and revised. Say so plainly.

**G6 — Only three learnings were recovered.** The archaeology in `05__` found three high-signal changes across seven months. There are 4,335 commits; a deeper pass over `team/comms/` and `.issues/` would likely surface more, and the changelog tree (`changelog/03/` through `changelog/08/`) is unexamined.

**G7 — The sg-playwright team was counted, not read.** Six role files in a second product, used here as evidence for the portable core. Their content has not been compared against the main team's — which is the actual test of whether the roster is reusable.

## Open questions for the founder

**Q1** — Is Explorer/Villager/Town Planner deliberately Wardley PST, or did it emerge from practical context limits and get named afterwards? Both are good answers; the site should tell the true one (`03__` §5).

**Q2** — The failure-condition Central Claim (*"…the Librarian has failed"*) versus the newer descriptive form: agreed that the older one is better and should be restored? If so, the site can publish rewrites of the seven descriptive claims as a build item.

**Q3** — What moves a component from Explorer to Villager, and who decides? (G2 — the biggest gap.)

**Q4** — `translator` exists only in the Villager team, and `accountant` only in Town Planner. Deliberate, or accident of when they were written?

**Q5** — Should the comms protocol get an acknowledgement mechanism — a way to tell a read brief from an unread one? (`04__` §5.)

**Q6** — Workflows: extract as first-class pages, or keep them inside the role definitions where they currently live? (G4.)

**Q7** — Are there roles you *tried and removed*? A `status: retired` entry with the reason would be the most useful page on the site for anyone composing their own team — and nothing in the git history shows a deletion, so if it happened it happened before 11 February 2026.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
source: /briefs/09__source-manifest.csv

==============================================================================


tier,path,words,role,notes
0,00__BRIEF.md,952,pack,commission; thesis; measured inventory; build order
0,01__the-role-format.md,982,pack,"ROLE.md schema measured; the failure-condition claim; drift quantified"
0,02__the-roster.md,893,pack,"nineteen roles; the operational core of six; growth timeline"
0,03__the-three-topologies.md,747,pack,"Explorer/Villager/Town Planner as staffed PST; handback rules"
0,04__the-comms-protocol.md,560,pack,"inbox/outbox addressing; the 8-step session-start ritual"
0,05__evolution-and-learnings.md,1001,pack,"git archaeology; three learnings as diffs — the memory layer"
0,06__site-architecture.md,594,pack,URLs; machine-readable roster; deconfliction table
0,07__boundaries-and-licensing.md,565,pack,"publish-for-copying; the pre-publication scrub; PST attribution"
0,08__gaps-and-open-questions.md,553,pack,7 gaps / 7 comms questions
0,teams__roster.json,,pack,"19 roles generated from disk + git; claim forms; topologies; learnings"
1,SGraph-AI__App__Send/team/roles/,,evidence,"Explorer team: 17 role directories, 13 with ROLE.md"
1,SGraph-AI__App__Send/team/roles/conductor/ROLE.md,1803,evidence,"'Roles are boundaries. The Conductor never does the work.'; Not Responsible For list"
1,SGraph-AI__App__Send/team/roles/librarian/ROLE.md,1961,evidence,"bullet-format Identity; the 30-second falsifiable claim"
1,SGraph-AI__App__Send/team/roles/qa/ROLE.md,2128,evidence,"most-revised role (6 commits); the 8-step session-start sequence"
1,SGraph-AI__App__Send/team/roles/dev/ROLE.md,1929,evidence,"comms write addresses; sgit tool row with its prohibition"
1,SGraph-AI__App__Send/team/roles/appsec/ROLE.md,2311,evidence,"falsifiable claim on plaintext/keys reaching the server"
1,SGraph-AI__App__Send/team/roles/designer/ROLE.md,3076,evidence,"widest remit; exists in all three topologies"
1,SGraph-AI__App__Send/team/villager/roles/,,evidence,"Villager team: 17 directories, 17 defined — the only complete team"
1,SGraph-AI__App__Send/team/villager/roles/dev/ROLE.md,1150,evidence,"'Harden, do not build'; 'Preserve behaviour exactly'; send-back rule"
1,SGraph-AI__App__Send/team/town-planner/roles/,,evidence,"Town Planner: 4 directories, 3 defined; librarian missing"
1,SGraph-AI__App__Send/team/town-planner/roles/accountant/ROLE.md,385,evidence,"financial models the Alchemist wraps in investor narrative"
1,SGraph-AI__App__Send/team/comms/,,evidence,"130 files: briefs, changelog, plans, qa/briefs, qa/questions, QA_START_HERE.md"
1,sg-playwright/team/roles/,,evidence,"second product, 6 roles — the portable-core evidence"
2,SGraph-AI__App__Send git history (4335 commits),,method,"role evolution recovered via git log over team/roles/*/ROLE.md; full clone, not shallow"
2,https://sgit.ai/network/index.html,,live-source,"fetched 2026-09-07: 19 sites, 18 live, skills.sgit.ai reserved and unpublished"
2,skills.sgit.ai (reserved sibling),,deconflict,"owns SKILL.md, lifecycle, triggering; this site links out and never duplicates"
2,wardley-maps.sgit.ai (sibling pack),,deconflict,"PST model itself lives there; this site owns only its staffing"
2,issues-fs.sgit.ai (sibling),,deconflict,"issues-as-files argument lives there; here only how roles address it"
3,vault keys / share tokens / access tokens in any ROLE.md,,DO-NOT-PUBLISH,"07__ §3: grep as a CI build step before any file ships"
3,internal hostnames / bucket names / account IDs / ARNs,,SCRUB,replace with placeholders before publication
3,the four undefined Explorer roles and town-planner librarian,,PENDING,"publish as gaps; never author replacements for the website (07__ §5)"


==============================================================================
source: /briefs/LICENSE.md

==============================================================================


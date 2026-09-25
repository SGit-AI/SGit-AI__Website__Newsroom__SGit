# 05 — Gaps and Open Questions

**Version** v0.33.62 · 25 August 2026
**House rule** Published unresolved. Questions for the founder go to `/admin/comms.html`.

---

## Gaps (known, owned)

**G1 — The full Victor register text.** The pack's `sources/` file is a faithful summary of the register's structure and closing argument; the **full verbatim text lives with the founder** (it was supplied in conversation; this environment could not retain it across a context boundary). Entry one cannot ship without it. *First ask in comms.*

**G2 — Seven STATED entries have no corpus evidence.** By design (the founder's briefing documents are pending), but the site launches with 7 of 24 entries as stubs. The mitigation is §3 of `03__`: stubs are honest roadmap, with research plans published.

**G3 — The founder's past publications are under-mined.** The corpus scanned here is the current estate + docs.diniscruz.ai. Two decades of earlier material — the O2 Platform era blog, OWASP talks, conference decks on SlideShare, the books (e.g. his OWASP testing-era writing) — were not reachable from this environment and are exactly where the STATED influences' traces will be found. The founder's own plan ("including doing a research on my past publications or presentations on them") covers this; the research plans in the seed JSON say where to look per entry.

**G4 — No influence has a complete trace table yet except Victor's.** T2–T12 have evidence *files*, not pattern→implementation→version rows. Building each table is the site's core editorial work; the register format (01__) is the spec.

**G5 — Screenshot/artwork production.** Original portraits and redrawn idea-figures (04__) need an artist pass or a generation workflow the founder approves. External-site screenshots hit the same egress constraint as the wardley pack — the `capture.js` pattern from that pack is reusable here.

## Open questions for the founder (comms threads)

**Q1** — Please supply the full immediate-connection register text for `/register/bret-victor/` (G1).
**Q2** — DISCOVERED confirmations: Luhmann, Christopher Alexander, Team Topologies/Cynefin, Vannevar Bush — do they belong? Any to demote to "corpus citation, not influence"? (The falsifiability of the site starts with you falsifying its discoveries. **Design & Steve Jobs: confirmed by the founder 2026-08-25** — the first discovered→confirmed transition, before the site even exists.)
**Q2b** — The Design entry's anchor: which artefact is canonical for you — the "Design is how it works" quote, the MP3-to-CD whiteboard story, an Apple keynote, Ive's process, a specific product? And the personal history: when did Design-with-a-capital-D become explicit in your thinking?
**Q3** — Briefing order for the STATED seven: which first? (Suggested: Neil Peart or music-and-band — the entries no one can research but you.)
**Q4** — Anchors to confirm: Kevin Kelly (*What Technology Wants* vs *The Inevitable*?), Sinek (*Start With Why* book vs the TED talk?), David Rice (which year's keynote recording is canonical?).
**Q5** — Are there influences you *rejected* — things everyone assumes shaped you but did not, or that you outgrew? A `/register/<slug>/` with `status: counter-influence` would be unique on the web and very much in the site's falsifiable spirit.
**Q6** — Personal-history detail for T4 (graphs): where did graphs actually enter — O2's code-flow work, or earlier?
**Q7** — The `/map/` graph: should it live here or in the graphs sibling once it becomes a G³ demonstration? (Proposal: authored here, mirrored there.)

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
source: /briefs/09__source-manifest.csv

==============================================================================


tier,path,words,role,notes
0,00__BRIEF.md,840,pack,the commission
0,01__the-register-format.md,907,pack,entry template canonised from the Victor register
0,02__the-influence-map.md,1581,pack,all 24 entries with evidence
0,03__site-architecture.md,534,pack,URLs / data model / tier movement
0,04__boundaries-and-licensing.md,542,pack,no-verbatim rule as licence armour
0,05__gaps-and-open-questions.md,483,pack,5 gaps / 7 comms questions
0,influences__seed.json,,pack,24 entries; authoritative tier state
0,sources/register__bret-victor__inventing-on-principle.md,124,pack,structural summary; full register text with the founder (comms Q1)
1,SGraph-AI__App__Send/team/humans/dinis_cruz/briefs/03/28/v0.19.7__article__education-gaps-git-opensource.md,943,evidence,"contains the section 'The Brett Victor Problem'"
1,docs.diniscruz.ai/docs/2025/07/04/the-joy-of-programming-in-the-age-of-ai-assisted-development.md,5614,evidence,"Victor immediate-feedback thesis; Csikszentmihalyi named; flow criteria applied"
1,docs.diniscruz.ai/docs/2025/06/18/bridging-niklas-luhmanns-ideas-with-semantic-knowledge-graphs-and-g3.md,4673,evidence,"Luhmann/Zettelkasten mapped to G3; Vannevar Bush memex entry point"
1,SGraph-AI__App__Send/library/concepts/v0_4_0__thinking-in-graphs.md,5013,evidence,"section 'The Semantic Web's Insight (and Mistake)' — node-first vs edge-first"
1,SGraph-AI__App__Send/team/humans/dinis_cruz/briefs/02/24/v0.6.17__architecture__solid-protocol-integration-complementary-architectures.md,3278,evidence,"TBL's Solid vs sgit vaults; Schneier at Inrupt"
1,SGraph-AI__App__Send/team/roles/designer/ROLE.md,3076,evidence,"Christopher Alexander; Rams; Vignelli; Norman; the design canon"
1,SGraph-AI__App__Send/library/guides/development/ifd/v1.2.1__ifd__intro-and-how-to-use.md,1956,evidence,"IFD centers on preserving developer flow state"
2,wardley-maps.sgit.ai (sibling pack),,deconflict,Wardley material lives there; influence entry links out
2,open-source.sgit.ai (sibling pack),,deconflict,open-source history lives there; Cathedral & Bazaar / Torvalds nest under the influence entry
2,graphs + owasp sibling sites,,deconflict,link-out entries own resonance only
3,founder's full immediate-connection register (in conversation),,DO-NOT-PUBLISH-YET,supplied verbatim by founder; not retained in this environment; request via comms Q1 then publish as entry one
3,founder's briefing documents for the STATED seven,,PENDING,do not fabricate; stubs carry status awaiting-briefing until these arrive
1,SGraph-AI__App__Send/team/humans/dinis_cruz/briefs/02/27/part-2/v0.7.4__brief__advocate-designer-in-the-loop-notebooklm-case-study.md,2879,evidence,"'The Jonathan Ive Principle'; the Jobs MP3-to-CD whiteboard story; good design is invisible"
1,SGraph-AI__App__Send/team/humans/dinis_cruz/claude-code-web/02/28/v0.7.4__explorer-response__security-and-process-briefs.md,2479,evidence,"the 'Jonathan Ive test' as mandatory validator for every UI change"


==============================================================================
source: /briefs/LICENSE.md

==============================================================================


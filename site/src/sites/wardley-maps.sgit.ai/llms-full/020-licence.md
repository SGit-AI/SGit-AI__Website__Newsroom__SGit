# Licence

## This pack

Everything in this brief pack — the nine numbered documents, `09__source-manifest.csv`, both `sources__*.json` files, the four maps in `maps/` (both `.mmd` source and rendered `.svg`), `screenshots/capture.js`, `screenshots/targets.json`, this file and `README.md` — is released under the **Creative Commons Attribution 4.0 International licence (CC BY 4.0)**.

    Copyright (c) 2026 Dinis Cruz
    Licensed under CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/

Attribution: **Dinis Cruz**, with AI co-authorship (Claude, Anthropic). Where a source document names model co-authors, carry those names forward.

The four maps are **original works**, drawn from this pack's own research. They carry no ShareAlike obligation. The *technique* they use is Simon Wardley's and is credited as such — crediting a technique is good practice, not a licence condition.

## The site this pack commissions

**The entire content of `wardley-maps.sgit.ai`** — every page, `/documents/`, `/llms.txt`, `/llms-full.txt` and the admin surfaces — is to be published under **CC BY 4.0**, consistent with the rest of the `*.sgit.ai` network. Put the licence in `/llms.txt`, in the page footer, and at the foot of every raw markdown document:

    This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).

Use `licence-audit.py` (shipped in the `graphs.sgit.ai` pack) in `--check` mode as a CI gate so the stamp cannot drift.

---

## ⚠️ The one that matters: CC BY vs CC BY-SA

**This site sits inside a CC BY-SA ecosystem.** That is the single biggest licensing trap in the build, and it does not apply to any other site in the network.

ShareAlike is viral. **Quoting** CC BY-SA material with attribution is fine. **Adapting** it — rewriting, restructuring, translating, building a derivative table from it — obliges you to license the resulting page CC BY-SA 4.0, not CC BY 4.0.

> **The rule: CC BY-SA material appears as clearly-marked quotation and link-out, never as adaptation.** Then every page stays CC BY 4.0 and the network's licence stays uniform. Where you genuinely want to adapt, do it on a page carrying its own CC BY-SA 4.0 notice and say why at the top.

Standard attribution string, used across the ecosystem:

> *Wardley Mapping is provided courtesy of Simon Wardley, CC BY-SA 4.0.*

**Watch the version split.** The book and most of the ecosystem are **CC BY-SA 4.0**. Simon Wardley's blog `blog.gardeviance.org` is **CC BY-SA 3.0**. Different licences, different notices — do not merge them into one footer.

---

## What this licence does not cover

| Material | Regime | What the site must do |
|---|---|---|
| **Simon Wardley's book, Learn Wardley Mapping's free reference, the Mapping Canvas, wardleymaps.com, Wikipedia** | **CC BY-SA 4.0** | Quote and screenshot with the attribution string. Do not adapt. |
| **`blog.gardeviance.org`** | **CC BY-SA 3.0** ⚠️ | Same, with a *separate* 3.0 notice. |
| **awesome-wardley-maps** | **CC0 1.0** | Anything, no attribution required. The best base for your own list — and it lists five dead things as live, so correct it while crediting it. |
| **OWM, Mermaid, wardleyToGo, cli-owm, ArcKit** | **MIT** | Retain the notice. Technique credit to Wardley is separate. |
| **Obsidian plugin, Tranquil's Map** | **AGPL-3.0** ⚠️ | Network clause — matters if you ever embed one in a service. |
| **The 8 prior-art articles on `docs.diniscruz.ai`** | **CC0 1.0** | More permissive than CC BY, so republishing is fine — but attribute anyway and keep `rel="canonical"` on the original URL with the recorded `first_published` date. |
| **InfoQ, YouTube, GCATI, Xebia, LWM's paid course, Hudson's and Bell/Thorpe's books** | **All rights reserved** | Brief quotation and a page screenshot for identification. **No re-hosting, no clipping, no reproducing their diagrams.** |
| **Vault contents** at `sgit.ai/demos/vaults/` | Per-vault; read keys publishable, **write keys never** | Confirm the write key is escrowed before linking. Publishing a read key for a vault whose write key is lost freezes it permanently. |
| **Tier-3 rows in the manifest** (6 rows) | Internal | **Do not publish, quote or paraphrase.** Listed so you know to skip them. |
| **Tier-2 rows** (7 rows) | Partial | Marked `EXTRACT ONLY` / `IDEA ONLY` / `CARE` / `ARCHIVE FIRST`. Read the `why_it_matters` column before touching them. |

## 🚩 Six flagged — link only until resolved

- **`swardley/WARDLEY-MAP-REPOSITORY`** — README says CC BY-SA, GitHub licence field says **GPL-3.0**. **Do not mirror.** 147 maps are worth one email to resolve.
- **WardleyPedia** — no licence stated. Do not assume the MediaWiki default.
- **Matt Edgar's critique** — no statement, assume ARR. Highest-value critique, least clear rights.
- **Open Security Summit session pages** — no licence stated, including Dinis's own sessions.
- **Miro / Figma / draw.io templates** — mostly unstated, varying. Check per template.
- **Discord and forum content** — personal messages. Never quote a member without consent.

## Third-party names

Naming a technique, framework, standard, tool or public author is fine — Simon Wardley, Ben Mosior, Chris Daniel, Matt Edgar, Danny Buerkli, Tristan Slominski and the others in `04__` are credited for public work. Recording that MapKeep shut down on 30 May 2026 and crediting Slominski for building it is a factual obituary the community needs.

Attaching maturity or capability judgements to **named commercial competitors** is not fine — that is why Map 8 of the eight-maps brief is marked REDACT and why the whole `library/alchemist/materials/` tree is Tier-3.

---

This file is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
=== /maps/M1__tooling-ecosystem.mmd — wardley-beta source
==============================================================================
wardley-beta
  title M1 - The Wardley mapping tool ecosystem, August 2026
  anchor "Mapper" [0.95, 0.55]
  component "Draw a map" [0.86, 0.62]
  component "Share a map" [0.80, 0.48]
  component "Version a map" [0.74, 0.55]
  component "Assess doctrine" [0.70, 0.22]
  component "Agent authoring" [0.66, 0.20]
  component "OnlineWardleyMaps" [0.58, 0.70]
  component "OWM text syntax" [0.50, 0.78]
  component "Mermaid wardley-beta" [0.46, 0.66]
  component "Git" [0.38, 0.95]
  component "SVG rendering" [0.30, 0.82]
  component "Real-time collaboration" [0.62, 0.30]
  component "Doctrine tool" [0.56, 0.10]
  component "ArcKit" [0.60, 0.34]
  "Mapper" --> "Draw a map"
  "Mapper" --> "Share a map"
  "Mapper" --> "Version a map"
  "Mapper" --> "Assess doctrine"
  "Mapper" --> "Agent authoring"
  "Draw a map" --> "OnlineWardleyMaps"
  "OnlineWardleyMaps" --> "OWM text syntax"
  "Version a map" --> "Mermaid wardley-beta"
  "Mermaid wardley-beta" --> "OWM text syntax"
  "Mermaid wardley-beta" --> "Git"
  "Mermaid wardley-beta" --> "SVG rendering"
  "OnlineWardleyMaps" --> "SVG rendering"
  "Share a map" --> "Real-time collaboration"
  "Assess doctrine" --> "Doctrine tool"
  "Agent authoring" --> "ArcKit"
  "ArcKit" --> "OWM text syntax"


==============================================================================
=== /maps/M2__the-two-absences.mmd — wardley-beta source
==============================================================================
wardley-beta
  title M2 - The two absences - what the ecosystem lost in 2026
  anchor "Mapping practitioner" [0.95, 0.50]
  component "Situational awareness" [0.88, 0.40]
  component "Collaborative authoring" [0.72, 0.32]
  component "Doctrine self-assessment" [0.70, 0.20]
  component "Single-player authoring" [0.68, 0.72]
  component "Maps in version control" [0.60, 0.64]
  component "Mapkeep" [0.55, 0.30]
  component "doctrine.wardleymaps.com" [0.52, 0.12]
  component "MapScript" [0.50, 0.26]
  "Mapping practitioner" --> "Situational awareness"
  "Situational awareness" --> "Collaborative authoring"
  "Situational awareness" --> "Doctrine self-assessment"
  "Situational awareness" --> "Single-player authoring"
  "Situational awareness" --> "Maps in version control"
  "Collaborative authoring" --> "Mapkeep"
  "Doctrine self-assessment" --> "doctrine.wardleymaps.com"
  "Single-player authoring" --> "MapScript"


==============================================================================
=== /maps/M3__maps-for-agents.mmd — wardley-beta source
==============================================================================
wardley-beta
  title M3 - Maps for agents - where the new user need sits
  anchor "Agent" [0.95, 0.30]
  component "Reason about strategy" [0.88, 0.22]
  component "Read a map" [0.80, 0.55]
  component "Write a map" [0.76, 0.38]
  component "Contest a placement" [0.72, 0.08]
  component "Machine-readable corpus" [0.60, 0.45]
  component "OWM DSL" [0.55, 0.78]
  component "Mermaid wardley-beta" [0.52, 0.66]
  component "Coordinate contract" [0.46, 0.40]
  component "Evidence for placement" [0.40, 0.10]
  component "Deterministic renderer" [0.34, 0.60]
  "Agent" --> "Reason about strategy"
  "Reason about strategy" --> "Read a map"
  "Reason about strategy" --> "Write a map"
  "Reason about strategy" --> "Contest a placement"
  "Read a map" --> "Machine-readable corpus"
  "Machine-readable corpus" --> "OWM DSL"
  "Write a map" --> "Mermaid wardley-beta"
  "Write a map" --> "Coordinate contract"
  "Mermaid wardley-beta" --> "Deterministic renderer"
  "Contest a placement" --> "Evidence for placement"


==============================================================================
=== /maps/M4__the-site.mmd — wardley-beta source
==============================================================================
wardley-beta
  title M4 - wardley-maps.sgit.ai as a value chain
  anchor "Reader or agent" [0.95, 0.45]
  component "Understand mapping" [0.88, 0.50]
  component "Find the good resources" [0.84, 0.35]
  component "Read the doctrine work" [0.78, 0.25]
  component "See a worked example" [0.74, 0.42]
  component "Resource pages" [0.62, 0.30]
  component "Doctrine assessment" [0.58, 0.18]
  component "Rendered maps" [0.54, 0.55]
  component "Map sources in git" [0.46, 0.70]
  component "llms.txt surface" [0.40, 0.48]
  component "Static hosting" [0.24, 0.92]
  "Reader or agent" --> "Understand mapping"
  "Reader or agent" --> "Find the good resources"
  "Reader or agent" --> "Read the doctrine work"
  "Reader or agent" --> "See a worked example"
  "Find the good resources" --> "Resource pages"
  "Read the doctrine work" --> "Doctrine assessment"
  "See a worked example" --> "Rendered maps"
  "Rendered maps" --> "Map sources in git"
  "Understand mapping" --> "llms.txt surface"
  "Resource pages" --> "llms.txt surface"
  "llms.txt surface" --> "Static hosting"
  "Map sources in git" --> "Static hosting"


==============================================================================
=== /index.md
==============================================================================
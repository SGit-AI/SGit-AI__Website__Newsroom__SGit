# infographics.sgit.ai — the catalogue of every rendered brief

> Across the sgit.ai family, most writing starts as a markdown brief. Some of those
> briefs get turned into a single visual artefact — usually by pasting the brief into
> an image model by hand, not by any site's own build pipeline. Once that image
> exists it tends to live nowhere durable. **infographics.sgit.ai is where it lives
> instead** — stored, dated, and kept traceable back to the brief that argued for it.

*Source: <https://infographics.sgit.ai/index.html> &middot; site v0.1.0 &middot; markdown twin of the front page.*

---

## How an infographic gets here

1. **The brief exists somewhere** — a markdown file in a sibling site's `briefs/`
   folder, a vault document, a strategy note. It is already the source of truth
   before any image is made.
2. **Someone renders it** — today, almost always a person pasting the brief into an
   image model by hand. A documented pipeline exists for this at scale (see
   [the network page](https://infographics.sgit.ai/network/index.html#pipeline)), but
   most entries so far were not made with it.
3. **It gets catalogued here** — the image, plus a `metadata.json` naming the source
   brief, the source site, what rendered it, and its licence. Nothing is catalogued
   without that trail.

## What this is, honestly, right now

- **1** infographic catalogued
- **1** source site it was drawn from so far (graphs.sgit.ai)
- **0** infographics rendered by this site's own pipeline — none exists yet
- **CC BY 4.0** default licence, stated per entry

## What this site is not

It is not an infographic generator, and it does not decide what a brief means — the
brief and its rendered document stay the source of truth. This site is a library card
catalogue: it stores the picture, and points back at the argument.

**The honest sentence:** everything catalogued so far arrived by hand, one entry at a
time. There is no crawler pulling images in from sibling sites, and no guarantee every
infographic anyone on the team has ever made is here — only the ones someone chose to
catalogue. [Open requests, in public →](https://infographics.sgit.ai/admin/comms.html)

## For an agent

This site stores rendered visual artefacts and the metadata linking each one back to
its source brief and, where one exists, its rendered prose document on the source
site. It does not itself generate infographics — check each entry's `generator`
field before assuming otherwise.
[library/data/catalogue.json](https://infographics.sgit.ai/library/data/catalogue.json)
is the full machine-readable index.
[llms.txt](https://infographics.sgit.ai/llms.txt) is the whole agent surface.

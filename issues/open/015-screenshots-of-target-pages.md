---
title: Screenshots of the pages a piece is about
created: 2026-09-25T12:05:00Z
priority: medium
type: task
owner: build.desk
source: admin/inbox/2026-09-25__notes-from-the-flight.md
parent: 001-reading-experience
estimated_effort: medium
---

# Screenshots of the pages a piece is about

Walls of text: pieces that talk about a page should show it. A build-time step (Playwright, outside the
standard-library build; committed webp files under `assets/shots/`) captures the live page of each source a
piece cites, and the piece shows a thumbnail with the target site's branding, linking to the local copy.

Plan: `tools/screenshots.js` reads data/index.json for the pages cited by desk files, captures at 1280 wide,
writes `assets/shots/<site>/<path>.webp` plus a manifest with the capture time; the build shows them where the
`[shot: <url>]` marker appears, or automatically in the byline block for the first two sources.

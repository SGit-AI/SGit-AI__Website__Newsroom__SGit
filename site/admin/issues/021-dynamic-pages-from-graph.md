---
title: Render pages from a graph of pieces, merged with the reader's state
created: 2026-09-25T12:05:00Z
priority: medium
type: task
owner: build.desk
source: admin/inbox/2026-09-25__notes-from-the-flight.md
parent: 002-personalised-site
estimated_effort: large
---

# Render pages from a graph of pieces, merged with the reader's state

Build a graph at build time: pieces, the sources they cite, the concepts they touch, what follows what
(editions by day, stories by topic). Ship it inlined (like the search index) so the browser can compose the
reader's view: what is new for them, what to read next or back given what they have read, related pieces
beside the current one. The front page's dynamic parts render from it.

Done when: `data/graph.json` is built and documented; a "read next" block on each piece uses it; the front
page composes its sections from the editor's picks intersected with the reader's log.

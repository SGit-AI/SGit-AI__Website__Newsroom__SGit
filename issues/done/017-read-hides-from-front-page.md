---
title: Marking a piece read hides it from the front page and the sections
created: 2026-09-25T12:05:00Z
priority: high
type: task
owner: build.desk
source: admin/inbox/2026-09-25__notes-from-the-flight.md
parent: 002-personalised-site
estimated_effort: medium
---

# Marking a piece read hides it from the front page and the sections

The single biggest value: the site shows only what the reader has not yet read. Every card and list row
carries the piece's id; the reader's log (already in localStorage) hides read ones, leaves a one-line clue
("3 read pieces hidden · show") and a page listing everything read, in order, with undo.

Done when: front page, News, Perspective, Maps, Signals, Editions, History and the reading room all hide
read items in the reader's view; the count and the link are shown; nothing is hidden in the editor's view.

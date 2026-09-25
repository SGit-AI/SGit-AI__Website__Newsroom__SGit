---
title: A history of every action, with undo and redo
created: 2026-09-25T12:05:00Z
priority: high
type: task
owner: build.desk
source: admin/inbox/2026-09-25__notes-from-the-flight.md
parent: 002-personalised-site
estimated_effort: medium
---

# A history of every action, with undo and redo

The feedback log is append-only. Add a history page (all events, newest first, per piece), undo (appends
the inverse event, so the log stays complete) and redo. Show the last action in the device bar with an
"undo" link.

Done when: `feedback/history.html` exists, undo and redo work offline, and "Copy for Claude" carries undone events marked as such.

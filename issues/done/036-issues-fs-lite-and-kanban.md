---
title: issues-fs-lite in issues/, rendered as a kanban and pages in admin
created: 2026-09-25T12:05:00Z
priority: high
type: task
owner: build.desk
source: admin/inbox/2026-09-25__notes-from-the-flight.md
parent: 006-back-office
estimated_effort: small
---

# issues-fs-lite in issues/, rendered as a kanban and pages in admin

This file is the first proof. Three folders (open, blocked, done), one markdown file per issue with YAML
front matter (created, priority, type, parent, owner, source, estimated_effort, tags), moved between folders
by mv, committed with the work. The build renders admin/issues (a kanban by status, filter by epic, owner
and priority), one page per issue, and counts on the admin page.

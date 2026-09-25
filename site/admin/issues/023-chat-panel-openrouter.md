---
title: A chat panel with tools over the site, on the reader's OpenRouter key
created: 2026-09-25T12:05:00Z
priority: high
type: task
owner: build.desk
source: admin/inbox/2026-09-25__notes-from-the-flight.md
parent: 003-chat-and-relay
estimated_effort: large
---

# A chat panel with tools over the site, on the reader's OpenRouter key

Tier 0: a local matcher over the inlined search index, no key, works offline. Tier 1: paste an OpenRouter
key (kept in localStorage, never sent anywhere but openrouter.ai, said plainly) and chat with a model that
has tools: search(query), open(page) (the page's .md twin, when served over http), my_feedback(),
file_feedback(page, kind, text), read_next(). Streams; falls back to tier 0 when the call fails. Cost line
shows tokens and the model.

Done when: the panel is on every page; tier 0 works from file://; tier 1 works on localhost and the live
site; the validator allows fetch only in chat.js and only to openrouter.ai and the site's own .md files.

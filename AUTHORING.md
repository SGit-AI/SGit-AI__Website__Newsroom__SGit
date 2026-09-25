# Authoring contract: how desk files are written so the build can read them

Every desk writes plain files. `tools/build.py` turns them into `site/`. This file is the contract
between the two. The house rules in `brief/06-house-rules.md` are binding on top of it.

## Front matter (every `.md` under editions/, stories/, history/, signals/)

A small YAML subset: `key: value` lines, and lists as `  - item` lines under a key.

```
---
title: A brief written on one site, built on another the same day
date: 2026-09-24
desk: Journalist
sources:
  - https://sgit.ai/docs/briefs/riskmandate-interview-page-and-voice-prompt.html
  - https://riskmandate.ai/versions/1.34.2.md
reviewed_by:
reviewed_on:
---
```

`reviewed_by` and `reviewed_on` stay empty: only the editor of record fills them. Signals add
`from_site`, `to_site`, `status` (new, sent, acted on, dismissed) and `action` (one line).

## Links: how to cite

Write ordinary markdown links. The build decides where each one goes.

| You write | The build renders |
|---|---|
| `[text](https://sgit.ai/docs/briefs/x.html)` (any live URL of a snapshotted page, `.html` or `.md`) | a link to the **local copy** in the reading room, with a ↗ link to the live page beside it |
| `[text](https://example.org/)` (not in the snapshot) | an external link, marked ↗ |
| `[text](src:cli-briefs/09/24/brief__riskmandate__interview-page-and-voice-prompt.md)` | the local rendered copy of a file under `sources/` (use for cli-briefs, vaults, history, which have no live URL) |
| `[text](src:sites/riskmandate.ai/versions/1.34.2.md)` | the same, by snapshot path |
| `[text](nr:editions/2026-09-24)`, `nr:signals/2026-09-24__slug`, `nr:loose-ends`, `nr:history/lessons` | a page of this newsroom |

Prefer live URLs for anything on a site (they are what a reader outside the newsroom can follow);
use `src:` for files that only exist in the seed. A link the build cannot resolve fails validation.

## Data files (JSON, UTF-8, 2-space indent)

`data/changes/YYYY-MM-DD.json` (Librarian):

```json
{
  "date": "2026-09-24",
  "desk": "Librarian",
  "basis": "sgit.ai version log and new-pages list; riskmandate.ai version record (no earlier snapshot to diff)",
  "changes": [
    {
      "site": "sgit.ai",
      "kind": "release",
      "version": "v0.6.7",
      "url": "https://sgit.ai/docs/briefs/riskmandate-interview-page-and-voice-prompt.html",
      "title": "For RiskMandate.ai: an interview page, and a ChatGPT voice prompt to run it",
      "type": "brief",
      "summary": "One line, written after reading the page.",
      "concepts": ["append-lanes", "interview-pages"]
    }
  ]
}
```

`kind` is `release` (a version-log entry) or `new-page`. `type` is one of: article, brief, update,
business plan, partnership, vault, doc, policy, other. `concepts` are ids from `data/concepts.json`.

`data/concepts.json` (Librarian): a list of
`{"id", "name", "definition", "defined_at": "<url or src:>", "terms": ["regex", ...]}`.
The build finds every page that uses a concept by searching the snapshot for its `terms`
(case-insensitive), so pages per concept are computed, never typed.

`data/loose-ends.json` (all desks): a list of
`{"id", "what", "said_at": ["<url or src:>"], "said_on": "YYYY-MM-DD", "waiting_on": "<role or site>",
"status": "open | closed | unclear", "status_note", "closed_by": ["<url or src:>"], "desk"}`.

## Style

British English, plain words, short sentences, no em-dashes. Quotes are exact or they are not
quotes. Shipped and proposed keep the source's own words. Roles and sites, not people (the founder
may be named as editor of record). No model names or identifiers anywhere.

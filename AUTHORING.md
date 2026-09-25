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

## Pieces: standfirst and section

Stories, history pieces and maps carry two more front-matter fields, used by the front page and the section pages:

```
standfirst: One or two sentences that tell the reader what the piece is and why it matters.
section: news            # stories: news, feature, explainer or back-catalogue
```

Without a `standfirst`, the build uses the first paragraph, which is rarely as good.

## Maps (the Cartographer)

`maps/<slug>.md`: front matter like any desk file (with `standfirst`), a short text saying what the map shows and where
each position comes from, and one or more fenced `mermaid` blocks. Mermaid 12 is bundled with the site
(`tools/vendor/`), so every map renders offline. Supported and tested: `wardley-beta`, `flowchart`, `timeline`, `mindmap`.

```mermaid
wardley-beta
title The value chain
anchor Founder [0.95, 0.60]
component "sgit.ai site" [0.70, 0.55]
component Encrypted vaults [0.45, 0.50]
Founder -> "sgit.ai site"
"sgit.ai site" -> Encrypted vaults
evolve Encrypted vaults 0.70
```

Wardley coordinates are `[visibility, evolution]`, both 0 to 1 (evolution: genesis under 0.25, custom to 0.5, product
to 0.75, commodity above). **A name that contains a dot must be quoted** (`"sgit.ai site"`), or the map renders as a
syntax error. Build, open the page, and look: a broken diagram shows an error box, not a map. The network map at
`maps/network.html` is computed on every build from `data/network.json`; do not draw it by hand.

## The front page and the sections (the Editor)

`data/frontpage.json`:

```json
{
  "date": "2026-09-24",
  "lead": "stories/2026-09-24__brief-to-build-in-a-day",
  "top": ["history/week-2026-39", "maps/sgit-network-wardley", "editions/2026-09-24"],
  "sections": [
    {"title": "News", "from": "stories", "limit": 6, "more": "news/index.html"},
    {"title": "Perspective", "items": ["history/the-story-so-far"], "more": "history/index.html"}
  ],
  "briefs": [{"text": "Sixteen loose ends are open.", "link": "loose-ends"}]
}
```

Refs are `<folder>/<slug>` of a desk file (`stories`, `editions`, `history`, `maps`, `signals`) or `maps/network`. A
section either lists `items` or takes the newest `limit` from a folder (`from`), skipping what already leads. A brief's
`link` is a ref, an `nr:` path, a live URL or a `src:` path. `data/sections.json` is the navigation, in order.

## Findings go somewhere visible (principle 8)

A desk that finds a problem while writing (a page it could not find, two sites that disagree, an ask with no answer,
a count that does not add up) does not leave it in the middle of the prose. It records it as a loose end
(`data/loose-ends.json`, with `said_at`) or an open question (`history/open-questions.md`, `Q-nnn`), and the piece
links it in one line ("Finding: ... (le-024)"). The reader learns that something is wrong from the byline or the
first lines, never from page three.

## Words not to use (principle 12)

`rung`, `rungs`: say *level* or *step*. The validator fails a desk file that uses a banned word in its own prose;
a quotation of a source that uses it is allowed inside quotation marks. The list is in `brief/07-principles.md`.

## Briefing cards (principle 9)

A piece may carry `cards:` in its front matter: short facts in the same place on every piece, rendered as tiles under
the byline. Each card is `label: value` with an optional link:

```
cards:
  - What happened: A brief written on sgit.ai was built on riskmandate.ai the same day
  - Where: https://riskmandate.ai/versions/1.34.2.md
  - Waiting on: sgit.ai, to close the ask on its briefs index
  - Next: the lead's own run of the interview (le-009)
```

The value after the first colon is the text; a bare URL or `src:` path becomes a link; `(le-nnn)` or `(Q-nnn)` at the end
links the loose end or question.

## The semantic twin (an experiment, issue 029)

For new pieces only, the desk may write `<piece>.json` beside `<piece>.md`: the graph the prose was written from,
in the shape fractal semantic graphs use. The build renders it under the piece as a graph and a list by type, and
validates it. Two rounds, then the editor of record decides whether it stays.

```json
{
  "of": "stories/2026-09-25__slug.md",
  "depends_on": ["https://sgit.ai/...", "src:history/sgit.ai-version-log.json"],
  "nodes": [
    {"id": "f1", "type": "Fact", "text": "riskmandate.ai v1.34.2 built the interview page on 24 September", "source": "https://riskmandate.ai/versions/1.34.2.md"},
    {"id": "q1", "type": "Question", "text": "Will the lead run the interview themselves?"},
    {"id": "h1", "type": "Hypothesis", "text": "A brief built the same day means the two sites share a working loop"}
  ],
  "edges": [
    {"from": "f1", "to": "h1", "rel": "supports"},
    {"from": "q1", "to": "f1", "rel": "asks_about"}
  ]
}
```

Node types: Evidence, Fact, Statement, Observation, Idea, Hypothesis, Question, Comment. Edge relations: supports,
contradicts, cites, asks_about, answers, follows, leads_to. Every Evidence and Fact node names its `source` (a live
URL or a `src:` path). The validator checks types, relations, that edges name existing nodes, and that sources exist.

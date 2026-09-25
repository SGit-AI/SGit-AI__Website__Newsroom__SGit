<!-- DERIVED FILE: do not edit. Rendered from data/agents.json by tools/agents.py; tools/validate.py fails when this file and the register disagree. -->

# Editor of record: @EditorOfRecord

**Register id** `editor.human` · **kind** human · **cadence** before anything is called published

## Mission

> Read before anything is called reviewed, and own the register of agents. The founder, Dinis Cruz, for now.

## The central claim, written as a failure condition

A role that says what it does can only be admired; a role that says when it is failing can be contradicted.

> This role is failing when: A page shows as reviewed that nobody read.

## Gravity

> Reviewed means read.

## Reads

- every edition, story, history piece and signal
- the reading room's feedback, copied from the reader's device

## Writes (its mandate: the validator holds a run record to these)

- editions/
- stories/
- history/
- signals/
- maps/
- data/agents.json
- admin/
- briefings/

Plus what every run shares: `runs/`, `site/`, `version.txt`, `data/loose-ends.json`, `issues/`. Every run writes its run record, may add or close a loose end (brief/02: every desk adds to the list), files or moves issues (issues-fs-lite: the folder is the status), and rebuilds and releases the site.

## Produces

- reviewed_by and reviewed_on on each page
- the register of agents
- priorities in admin/notes.md

## How a run goes

1. Read the page and its sources.
2. Fill reviewed_by and reviewed_on, or send it back to its desk with a note.

## Works with

- @Editor (the desk), who composes the front page
- every desk

The mandate, what this role refuses and whose work it is not: [MANDATE.md](MANDATE.md).

<!-- DERIVED FILE: do not edit. Rendered from data/agents.json by tools/agents.py; tools/validate.py fails when this file and the register disagree. -->

# Editor of record: mandate

**Register id** `editor.human`. A run record for this role names `"agent": "editor.human"`.

## Not responsible for

Without this, every role quietly becomes the same role; each entry says whose the work is.

**Writing the editions**  
Belongs to: @Journalist

**Composing the front page**  
Belongs to: @Editor

## Refuses

- Marking a page reviewed without reading it

## Wrong when

- A page shows as reviewed that nobody read.

## May write

- editions/
- stories/
- history/
- signals/
- maps/
- data/agents.json
- admin/
- briefings/
- runs/
- site/
- version.txt
- data/loose-ends.json
- issues/

Anything else in a run record's `folders_changed` fails `tools/validate.py`.

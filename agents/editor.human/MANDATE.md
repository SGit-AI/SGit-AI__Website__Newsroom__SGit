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
- runs/
- site/
- version.txt
- data/loose-ends.json

Anything else in a run record's `folders_changed` fails `tools/validate.py`.

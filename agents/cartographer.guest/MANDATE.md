<!-- DERIVED FILE: do not edit. Rendered from data/agents.json by tools/agents.py; tools/validate.py fails when this file and the register disagree. -->

# Cartographer: mandate

**Register id** `cartographer.guest`. A run record for this role names `"agent": "cartographer.guest"`.

## Not responsible for

Without this, every role quietly becomes the same role; each entry says whose the work is.

**Editing another site's links**  
Belongs to: that site's own team

## Refuses

- A connection it did not see in a link

## Wrong when

- The map says two sites are connected when neither links the other, or misses a link that exists.

## May write

- signals/
- runs/
- site/
- version.txt
- data/loose-ends.json

Anything else in a run record's `folders_changed` fails `tools/validate.py`.

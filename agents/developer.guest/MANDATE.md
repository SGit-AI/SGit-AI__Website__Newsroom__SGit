<!-- DERIVED FILE: do not edit. Rendered from data/agents.json by tools/agents.py; tools/validate.py fails when this file and the register disagree. -->

# Developer: mandate

**Register id** `developer.guest`. A run record for this role names `"agent": "developer.guest"`.

## Not responsible for

Without this, every role quietly becomes the same role; each entry says whose the work is.

**Porting the code**  
Belongs to: the receiving project

## Refuses

- A reuse signal without a file to reuse

## Wrong when

- A reuse signal points at code nobody can find from the link, or at something the source calls a proposal.

## May write

- signals/
- briefings/
- runs/
- site/
- version.txt
- data/loose-ends.json
- issues/

Anything else in a run record's `folders_changed` fails `tools/validate.py`.

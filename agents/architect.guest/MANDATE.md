<!-- DERIVED FILE: do not edit. Rendered from data/agents.json by tools/agents.py; tools/validate.py fails when this file and the register disagree. -->

# Architect: mandate

**Register id** `architect.guest`. A run record for this role names `"agent": "architect.guest"`.

## Not responsible for

Without this, every role quietly becomes the same role; each entry says whose the work is.

**Sending the signal to the other project**  
Belongs to: @Editor, until signals are delivered as briefs

## Refuses

- A signal with one side cited
- A recommendation dressed as a finding

## Wrong when

- A signal cites only one side, or claims one project does not know about another without checking both.

## May write

- signals/
- runs/
- site/
- version.txt
- data/loose-ends.json
- issues/

Anything else in a run record's `folders_changed` fails `tools/validate.py`.

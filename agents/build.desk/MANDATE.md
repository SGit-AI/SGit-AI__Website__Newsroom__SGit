<!-- DERIVED FILE: do not edit. Rendered from data/agents.json by tools/agents.py; tools/validate.py fails when this file and the register disagree. -->

# Build desk: mandate

**Register id** `build.desk`. A run record for this role names `"agent": "build.desk"`.

## Not responsible for

Without this, every role quietly becomes the same role; each entry says whose the work is.

**Any edition, story, signal or history piece**  
Belongs to: the desk that owns it

**The register of agents**  
Belongs to: @Editor: a new agent is an editorial decision

## Refuses

- Weakening a gate to make a build pass
- Loading anything from the network in a page
- Hand-editing site/

## Wrong when

- The site does not open from file:// with the network off, or a gate passes something the house rules forbid.

## May write

- tools/
- .github/
- .claude/
- agents/
- run-local.sh
- README.md
- AUTHORING.md
- CLAUDE.md
- runs/
- site/
- version.txt
- data/loose-ends.json

Anything else in a run record's `folders_changed` fails `tools/validate.py`.

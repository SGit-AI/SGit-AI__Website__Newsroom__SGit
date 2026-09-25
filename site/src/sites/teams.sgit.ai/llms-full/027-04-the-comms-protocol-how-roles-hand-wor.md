# 04 — The Comms Protocol: how roles hand work to each other

**Version** v0.33.64 · 7 September 2026
**Source** `SGraph-AI__App__Send/team/comms/` — 130 files

---

## 1. The structure

```
team/comms/
├── QA_START_HERE.md      the landing page for one role
├── briefs/               inter-team briefs
├── changelog/MM/DD/      what changed, written by whoever changed it
├── plans/MM/DD/          forward work
└── qa/
    ├── briefs/MM/DD/     "here is what to test and why"
    └── questions/        QA asking the build team
```

Date-foldered `MM/DD/`, which is the estate's convention everywhere (and itself the product of a refactor — see `05__`).

## 2. The protocol is addresses, not messages

The insight worth extracting: roles do not message each other. **Each role's definition names the directories it reads and the directories it writes.** Communication is a set of addresses in the role file, so a new occupant of a role knows its inbox and outbox without being told.

From the Dev role: write *"a changelog entry in `team/comms/changelog/MM/DD/` documenting the fix and expected test impact"*, and *"if the fix affects UI behaviour, write a QA brief in `team/comms/qa/briefs/MM/DD/` with updated test cases."*

From the QA role, as a read/write table: read `QA_START_HERE.md` — ***"Read first every session"*** — read `changelog/` *"to classify test failures (good vs bad)"*, read `qa/briefs/` for test cases, write `qa/questions/` for the build team.

**That one QA line — reading the changelog to classify a failure as expected or genuine — is the whole value of the protocol in miniature.** Without it, a test failure is ambiguous and the agent must guess or ask. With it, the answer is a file lookup.

## 3. The session-start ritual

QA's role file carries an eight-step opening sequence, which the site should publish as the template for any long-running agent role:

1. Read `QA_START_HERE.md` — *"your landing page for what changed since your last session"*
2. Check `changelog/` (most recent date folder first)
3. Check `qa/briefs/` for briefs from the build team
4. Read your own previous reviews and coverage reports
5. Read the latest Conductor brief for sprint priorities
6. Run the test baseline to confirm it is green
7. Check `.issues/` for open defects
8. Review the test matrix for the highest-priority untested cell

Steps 1–3 rebuild context, 4–5 restore intent, 6–8 select the next action. **An agent that runs this sequence starts its session knowing what happened while it was gone** — which is the actual problem in long-running agentic work, and it is solved with files rather than memory.

## 4. Why files rather than a message bus

Every property that makes this work is a property of files in a versioned tree: durable across sessions, greppable, diffable, reviewable by a human, and — in this estate — publishable to a vault with a read-only key. A message bus gives none of that. The corpus's `issues-fs.sgit.ai` sibling makes the general argument (*"the issues are files, the files are a graph"*); this site makes the narrower one for **inter-agent comms specifically**, and links out rather than restating.

## 5. What is missing

No acknowledgement mechanism, no delivery guarantee, and no way to tell a read brief from an unread one. The Conductor's *"blockers decay fast"* principle implies chasing, but nothing in the tree records whether a brief was picked up. For a human team that is fine; for an agent team it is the obvious next mechanism (Q5).

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
source: /briefs/05__evolution-and-learnings.md

==============================================================================


---
name: desk
description: Work as one of the sgit newsroom's desks (Librarian, Journalist, Historian, a guest desk, the Build desk) on one task, under that desk's role and mandate, and leave a run record. Use when asked to "act as the Journalist", "have the Historian look at...", "run the Librarian", or "/desk <agent> <task>".
---

You are about to work as one desk of the sgit newsroom. The arguments name the desk and the task, for example
`journalist write the edition for 2026-09-25` or `historian add today's lessons`.

1. **Pick the agent.** Match the first word to a register id in `data/agents.json` (`librarian` → `librarian.desk`,
   `journalist` → `journalist.desk`, `historian` → `historian.desk`, `cartographer` → `cartographer.desk`,
   `editor` → `editor.desk`, `architect`/`developer` → `<name>.guest`, `build` → `build.desk`). If none fits, stop and say so: a new agent is the editor's decision.
2. **Become it.** Read `agents/<id>/ROLE.md` and `agents/<id>/MANDATE.md`, then `CLAUDE.md`, `AUTHORING.md` and
   `brief/06-house-rules.md`. Say in one line which desk you are and what you will write.
3. **Do the task inside the mandate.** Write only in the folders the ROLE lists under Writes, plus the shared ones
   (`runs/`, `site/`, `version.txt`, `data/loose-ends.json`). Work that belongs to another desk (MANDATE, "Not
   responsible for") is not done: note it for that desk in the run record's `note`, or run `/desk` again as that desk.
   Read every source before you write about it. Cite live URLs or `src:` paths as AUTHORING.md says.
4. **Record the run.** Write `runs/<YYYY-MM-DDTHHMMSSZ>__<agent id>.json` with the fields in `runs/README.md`.
   `folders_changed` must be honest: list every prefix you touched.
5. **Gate.** `python3 tools/build.py && python3 tools/validate.py`. The validator checks your run record against the
   mandate. Red because of your files: fix your files, never the gate. Red for another reason: stop and report it.
6. **Release** only if asked to publish: bump `version.txt` to the next patch above `origin/dev`, rebuild, commit as
   `site vX.Y.Z: <one sentence>`, push to `dev`. Never force-push. Otherwise commit on your branch and say so.
7. Report: which desk, what it read, what it wrote (with counts), what it left for other desks.

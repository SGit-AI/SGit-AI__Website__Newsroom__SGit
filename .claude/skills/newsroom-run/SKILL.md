---
name: newsroom-run
description: One pass of the sgit newsroom's daily run (brief/05-daily-run.md), desk by desk (Librarian, Journalist, Historian, guest desks), each under its own role and with its own run record. Use when asked to "run the newsroom", "do today's edition" or "/newsroom-run".
---

One pass of the daily run in `brief/05-daily-run.md`. Each step is done AS a desk: before it, read that desk's
`agents/<id>/ROLE.md` and `MANDATE.md`; after it, write that desk's run record in `runs/` (fields in
`runs/README.md`). Do the steps in order; if a step has nothing to do, say so in its run record.

1. **Preflight.** `git pull origin dev`. Read `CLAUDE.md`, the newest files in `runs/`, and `data/loose-ends.json`.
   `python3 tools/build.py && python3 tools/validate.py` on the tree as found; red → stop and report, do not fix
   work that is not this run's.
2. **Librarian** (`librarian.desk`). `python3 tools/fetch_sources.py`; commit the snapshot on its own
   (`snapshot YYYY-MM-DD: N files changed on M sites`). Diff the manifest against the previous commit. **Nothing
   changed anywhere: stop here and publish nothing** (write the Librarian's run record saying so). Otherwise read
   every changed file and write `data/changes/<today>.json`; `python3 tools/librarian.py`; update concepts.
3. **Journalist** (`journalist.desk`). `editions/<today>.md` from the changes file, `reviewed_by` empty; stories
   where one deserves the room.
4. **Historian** (`historian.desk`). Lessons and decisions from today's version logs; a piece if there was a moment.
5. **Guest desks** (`architect.guest`, `developer.guest`, `cartographer.guest`). Today's changes against the whole
   index; a signal only when both sides are cited. One run record per desk that wrote something.
6. **Loose ends** (whichever desk found them). Add new ones; close ones today's changes resolved, citing the change.
7. **Build, gate, release.** `python3 tools/build.py && python3 tools/validate.py`. Green: bump `version.txt` to the
   next patch above `origin/dev`, rebuild, commit `site vX.Y.Z: <today>, N changes, M stories`, push to `dev`.
   Never push red. Never force-push.
8. **Report** to the editor: what changed, what each desk wrote, what waits for review (every page with
   `reviewed_by` empty), what is blocked.

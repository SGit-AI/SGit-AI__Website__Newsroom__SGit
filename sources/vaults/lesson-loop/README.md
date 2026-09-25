# Lesson Loop

A business plan for padel coaches, and any teacher with students: capture what the coach knows at the moment they know it, in a record the student holds, and start every lesson from a briefing instead of from memory.

**Start with `index.html`** (it opens automatically): the problem, one invented player's record across four lessons with three coaches, the themes each coach saw, the phases, how it is built, and the business with a calculator. Or read `plan/` in order.

| Path | What it is |
|---|---|
| `index.html`, `app.json`, `content.json` | The app. All data inlined; opens anywhere, offline included. |
| `plan/00-START-HERE.md` to `plan/10-open-questions.md` | The plan as documents. |
| `plan/plan.json` | The problem, phases, components, prices and assumptions the app shows. |
| `player/record.json` | One invented player's record: lessons, matches, a clip, briefings. |
| `spec/` | The lesson note, and a player's data vault layout. |
| `prototypes/` | The coach-memo prompt and the briefing prompt: phase one, ready to use. |
| `diagrams/` | The loop and the two vaults. |
| `tools/build-content.py` | Rebuilds `content.json` and inlines it into the app. |
| `PUBLIC.md` | The rules this vault is published under. |

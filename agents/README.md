<!-- DERIVED FILE: do not edit. Rendered from data/agents.json by tools/agents.py; tools/validate.py fails when this file and the register disagree. -->

# The agents

The newsroom's work is done by desks, each with a role, a mandate and the folders it may write in. The register is [`data/agents.json`](../data/agents.json); every file in this folder is rendered from it by `tools/agents.py`. Edit the register, never these files.

| Agent | Alias | Kind | Cadence | Writes | Role |
|---|---|---|---|---|---|
| [**Editor**](editor.desk/ROLE.md) | `@Editor` | desk | last, every run | `data/frontpage.json`, `data/sections.json`, `admin/`, `AUTHORING.md`, `brief/`, `briefings/` | [ROLE](editor.desk/ROLE.md) · [MANDATE](editor.desk/MANDATE.md) |
| [**Librarian**](librarian.desk/ROLE.md) | `@Librarian` | desk | first, every day | `sources/`, `data/changes/`, `data/index.json`, `data/concepts.json`, `data/vaults.json`, `data/network.json` | [ROLE](librarian.desk/ROLE.md) · [MANDATE](librarian.desk/MANDATE.md) |
| [**Journalist**](journalist.desk/ROLE.md) | `@Journalist` | desk | every day that had changes | `editions/`, `stories/` | [ROLE](journalist.desk/ROLE.md) · [MANDATE](journalist.desk/MANDATE.md) |
| [**Historian**](historian.desk/ROLE.md) | `@Historian` | desk | every day for lessons and decisions; a piece when there is a moment | `history/` | [ROLE](historian.desk/ROLE.md) · [MANDATE](historian.desk/MANDATE.md) |
| [**Cartographer**](cartographer.desk/ROLE.md) | `@Cartographer` | desk | every run: the computed network map always, drawn maps when there is something to map | `maps/` | [ROLE](cartographer.desk/ROLE.md) · [MANDATE](cartographer.desk/MANDATE.md) |
| [**Architect**](architect.guest/ROLE.md) | `@Architect` | guest desk | when the day's changes give it something to say | `signals/`, `briefings/` | [ROLE](architect.guest/ROLE.md) · [MANDATE](architect.guest/MANDATE.md) |
| [**Developer**](developer.guest/ROLE.md) | `@Developer` | guest desk | when the day's changes give it something to say | `signals/`, `briefings/` | [ROLE](developer.guest/ROLE.md) · [MANDATE](developer.guest/MANDATE.md) |
| [**Build desk**](build.desk/ROLE.md) | `@Build` | construction | when the site, the tools or the pipeline change | `tools/`, `.github/`, `.claude/`, `agents/`, `run-local.sh`, `README.md`, `AUTHORING.md`, `CLAUDE.md`, `data/network.json`, `assets/`, `data/releases.json` | [ROLE](build.desk/ROLE.md) · [MANDATE](build.desk/MANDATE.md) |
| [**Editor of record**](editor.human/ROLE.md) | `@EditorOfRecord` | human | before anything is called published | `editions/`, `stories/`, `history/`, `signals/`, `maps/`, `data/agents.json`, `admin/`, `briefings/` | [ROLE](editor.human/ROLE.md) · [MANDATE](editor.human/MANDATE.md) |

## How to work as one

1. Read the desk's `ROLE.md` and `MANDATE.md`, then `CLAUDE.md` and `brief/06-house-rules.md`.
2. Do only that desk's work, in its folders (plus the shared ones: `runs/`, `site/`, `version.txt`, `data/loose-ends.json`, `issues/`).
3. Write `runs/<YYYY-MM-DDTHHMMSSZ>__<agent id>.json` (fields in `runs/README.md`).
4. `python3 tools/build.py && python3 tools/validate.py`; commit and push only when both pass.

The skills do this for you: `/desk <agent> <task>` runs one task as one desk; `/newsroom-run` runs the whole day, desk by desk, in the order of `brief/05-daily-run.md`.

**If no desk fits the work, that is a message to the editor, not a licence to invent one.** A new agent is an editorial decision: a new mandate and a new write scope in the register.

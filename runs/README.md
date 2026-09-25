# Run records

One JSON file per run, `runs/<YYYY-MM-DDTHHMMSSZ>__<agent id>.json`: the newsroom's memory of who did what, under
which mandate. `tools/validate.py` fails a record whose agent is not in `data/agents.json`, or whose
`folders_changed` go outside that agent's `writes` plus the shared ones.

| Field | What it holds |
|---|---|
| `when` | ISO 8601 UTC, with the Z |
| `agent` | a register id: `librarian.desk`, `journalist.desk`, `historian.desk`, `architect.guest`, `developer.guest`, `cartographer.guest`, `build.desk`, `editor.human` |
| `kind` | `desk` (a desk's daily work) or `construction` (tooling: no source fetched, no edition written) |
| `task` | what the run was asked to do, in one or two sentences |
| `folders_changed` | every path prefix the run changed, as the mandate names them (`editions/`, `data/changes/`) |
| `did` | what it did, one line each, with counts |
| `commit` | the commit that landed it (filled after the commit, or left out) |
| `gates` | true only if `python3 tools/build.py && python3 tools/validate.py` both passed |
| `note` | anything the next session should know |

One session doing several desks' work writes one record per desk. If no desk fits the work, write to the editor
instead of inventing an agent.

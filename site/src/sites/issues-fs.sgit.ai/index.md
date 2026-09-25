# issues-fs.sgit.ai — the issues are files and the files are a graph

> A node is a JSON file on disk. An edge is a typed verb stored on **both** endpoints. The
> folder hierarchy is the containment structure. **Nothing runs** — no server, no daemon, no
> database — so the tracker lives inside the repository it tracks, versions with it, branches
> with it, and can be read by `cat`, `grep` and `find`.

*Source: <https://issues-fs.sgit.ai/index.html> · site v0.1.2 · markdown twin of the front page.*

**5,401** lines of source across 98 files · **604** test functions across 45 files, 1.5 lines of
test per line of source · **14** CLI commands, every one taking `--for-agent` · **3**
agent-operable surfaces · **71** nodes and 141 link entries in the flagship live graph, depth 8 ·
**59** documents in the corpus.

---

## It installs and it works, today

```bash
pip install issues-fs-cli
issues-fs init
issues-fs types init
issues-fs create task "Write the DSL grammar page" --priority high --tags site,docs
issues-fs link Task-1 blocks Bug-1
issues-fs list --for-agent          # same data, JSON, for an agent
```

[The walkthrough](start/index.html) · [all 14 commands](cli/index.html).

## What is built

| | |
|---|---|
| **[A real type system](model/index.html)** | 12 node types and 10 link types — and an edge type is not a string, it carries a declared inverse and *domain and range constraints* on which node types it may join. Five regex-validated primitives underneath, in strict mode, so invalid input **raises rather than being coerced** |
| **[Four storage backends](model/index.html#backends)** | `memory`, `local_disk`, `sqlite`, `zip` — all real, all through one factory. The same graph can live in a directory, a SQLite file, a zip archive, or nothing at all |
| **[A complete CLI](cli/index.html)** | 14 commands, 1,080 lines, 94 tests, three output formats, git-style repository discovery — it walks *up* to find `.issues/`, so it works from anywhere in the tree |
| **[Four live graphs](examples/index.html)** | 147 nodes in real use. The flagship carries 71 nodes and 141 link entries across 84 files, nested eight path segments deep, with **all 13 schema fields on all 71 nodes** |
| **[The foundational corpus](concepts/index.html)** | 59 documents, and the five at the centre became the conceptual foundation of the whole `*.sgit.ai` estate |
| **[An eleven-role team](roles/index.html)** | Each role is its own repository with its own `ROLE.md` and its own `.issues/` graph |

## Three agent-operable surfaces

**No other project in the estate has three.** One needs no install at all.

| | | |
|---|---|---|
| **1 · [Issues-FS-lite](lite/index.html)** | Markdown + YAML front-matter, three folders, four `mv` operations. No install, no Python, no runtime | Usable today |
| **2 · [The `.issues` DSL](dsl/index.html)** | A line-oriented format parsed into nodes: 11 source files, ~55 tests, 3 live examples, a five-stage pipeline wired into the repository API | Built and tested |
| **3 · [`--for-agent` JSON](cli/index.html)** | Every one of the 14 commands forces JSON output. Not a mode — one flag, and an agent that knows only that rule can drive the whole surface | Shipping in 0.3.0 |

## What you can install right now

| Install | Version | What you get |
|---|---|---|
| `pip install issues-fs` | **0.7.0** | The Python API. 103-file wheel · 5,401 LOC · **604 tests**. Repository, node and link services, graph traversal, comments, status services, the `.issues` parser |
| `pip install issues-fs-cli` | **0.3.0** | The `issues-fs` command. 23-file wheel · **14 commands** · 94 tests · `--for-agent` on every one |

Four more repositories exist and are further along on `dev` than on `main`: the service UI (142
files, its own 49-node graph), the documentation package (all 59 documents), the development
umbrella (19 submodules), and dev utils (535 LOC, 19 tests). CI publishes to PyPI only from
`main`, so what is on PyPI is the last state of `main` rather than the state of the work.
[The release mechanism](shipped/why.html) · [package by package](shipped/index.html).

## Why a graph rather than a schema of fields

A node has no inherent meaning; **meaning is discovered through the edges you can trace from
it**. That is why the type system is a graph of typed relationships rather than a schema of
fields, and why an edge type carries domain and range constraints.

That thinking was written **here**. `thinking-in-graphs.md` is dated **5 February 2026**, was
written for Issues-FS, and reached SGraph Send four months later.

**The boundary:** [graphs.sgit.ai](https://graphs.sgit.ai) owns the philosophy and teaches it
at length. **This site owns the implementation — and the origin.**
[The full map](network/index.html).

## The backlog, for when this project has energy again

Issues-FS was built fast in February 2026 and the code has been ahead of its documentation ever
since — **the good direction for a project to drift in**. Everything here is a chore rather than
a defect, and most of them are one command.

- **Merge `dev` → `main` where it is overdue.** Seven of eight repositories are ahead on `dev`,
  and CI publishes only from `main`. The release helper is already in every repository.
  [The gap, per repository](shipped/why.html).
- **Fill or retire the two service placeholders.** Published early; the code behind them has not
  been written yet. Either outcome is fine — the page just says which is true today.
- **Refresh the READMEs.** They describe an earlier version: fewer tests than there are, a
  backend and an integration considered and not taken, a lexicon that is still a design.
  [All of them, with what was measured](shipped/corrections.html).
- **Write down what is already built** — the `.issues` DSL, the status services, the eleventh
  role. [`/dsl/`](dsl/index.html) is the first write-up of the DSL anywhere.
- **Name the copyright holder.** One line per repository, and it is what makes the licence
  usable by anybody else.
- **Decide the seven open questions.** [Q1–Q7](network/index.html#open) — none blocks using the
  tool.

## For an agent

Issues-FS is a git-native tracker with three operable surfaces. With a filesystem and no
tooling, use **lite**: `issues/open|blocked|done/NNN-slug.md` with YAML front-matter, and four
`mv` operations. If you can install, `pip install issues-fs-cli` and pass `--for-agent` to any
of the 14 commands to force JSON. Address nodes by label (`Task-1`, `Bug-27`), never by GUID;
`link` writes the inverse edge for you. Read another agent's `issues/`; never write into it.
Enumerate a graph by walking for `issue.json` rather than reading `_index.json`, which is a
cache. The upstream READMEs describe an earlier version — check a capability claim against
[/shipped/corrections.html](shipped/corrections.html) before repeating it.

---

Published by the sgit project, which builds and uses Issues-FS —
[participant disclosure](about/participant.html). Site content CC BY 4.0; the upstream
Issues-FS repositories are Apache 2.0.

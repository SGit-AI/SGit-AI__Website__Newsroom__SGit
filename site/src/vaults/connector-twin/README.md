# Connector Twin

A business plan for a service that gives every AI agent deployment a twin of its connectors: a journal of every request and response the agent makes to Gmail, Google Calendar, Drive, Slack or any other connected system, replayed into the views the agent saw, with a before and after for every change and a revert plan for each one.

The sales question is one line: **do you know what your agents did?**

**Start with `index.html`** (it opens automatically). It replays one invented agent session against Gmail and Google Calendar, rebuilt from 17 journal entries, and then sets out the business. Or read the plan as documents in `plan/`, in order.

## What is in this vault

| Path | What it is |
|---|---|
| `index.html`, `app.json`, `content.json` | The replay and the plan as a single-page app. All data is inlined, so it renders anywhere the vault opens, offline included. |
| `plan/00-START-HERE.md` | The one-page version and the reading order. |
| `plan/01` to `plan/10` | The idea, the facts with their sources, the architecture, the service, the business model, go-to-market, the first ninety days, why invest, the risks, and what is still open. |
| `plan/plan.json` | The packages, prices, capture modes and assumptions the app displays. |
| `spec/journal-entry.md` | The entry format: the contract between whatever captures and whatever replays. |
| `spec/revert-rules.md` | Every Gmail and Calendar action in scope, what the platform keeps, and the inverse the twin can offer. |
| `prototypes/` | The agent-reported capture instruction, the broker design, and the processor schedule. |
| `journal/` | The invented session: 17 hash-chained entries, and the captured instruction and summary. |
| `diagrams/` | The pipeline and the three capture modes, as SVG and WebP. |
| `tools/make-demo-journal.py` | Regenerates the journal. |
| `tools/verify-journal.py` | Checks the hash chain offline. Exit 0 if intact. |
| `tools/build-content.py` | Rebuilds `content.json` from `journal/` and `plan/plan.json` and inlines it into the app. |
| `PUBLIC.md` | The three rules this vault is published under. |

## How to edit

Change the journal or the plan, then from the vault root:

```
python3 tools/make-demo-journal.py   # only if you changed the generator
python3 tools/verify-journal.py
python3 tools/build-content.py
```

## What is real and what is not

The session is invented. The behaviour it relies on is not: Gmail's permanent delete, Undo Send being an interface feature, the 30-day trash, the administrator's 25-day bulk restore, Google Vault not being a backup tool, and the append lanes the capture writes to are all documented, and `plan/02-the-facts.md` links each one to its source.

# Agent as Webmaster

A business plan for a company that gives small businesses a website they can actually change, by putting an AI agent in the webmaster's chair. The plan is complete enough to run, and it is written for somebody else to run it.

**Start with `index.html`** (it opens automatically) or read the plan as documents in `plan/`, in order.

## What is in this vault

| Path | What it is |
|---|---|
| `index.html`, `app.json`, `content.json` | The plan as a single-page app. All content is inlined, so it renders anywhere the vault opens. |
| `plan/00-START-HERE.md` | The one-page version and the reading order. |
| `plan/01` to `plan/10` | The idea, the architecture, the workflow, what you sell, the business model, go-to-market, the first ninety days, why invest, the risks, and why it is open. |
| `mockups/` | Three invented customer websites and the sales site for the service, as standalone HTML pages. Open them from the app or from the file tree. |
| `diagrams/` | The architecture, the workflow and the money, as SVG. |
| `prototypes/` | The webmaster agent's operating instructions, the GitHub Pages setup, and worked change requests. Enough to run the first customer. |
| `tools/inline-content.py` | Copies `content.json` into the app after an edit. |
| `PUBLIC.md` | The three rules this vault is published under. |

## How to edit

Everything the app shows comes from `content.json`, with a copy inlined into `index.html` as a fallback. Edit the JSON, run `python3 tools/inline-content.py`, commit, push. The markdown in `plan/` is the same content in prose, kept in step by hand.

## Provenance

Written on 23 September 2026 from a voice memo by the founder of sgit.ai, as the first of a set of business plans published for others to build companies on. The numbers are starting hypotheses and are marked as such. The mock-ups are invented businesses.

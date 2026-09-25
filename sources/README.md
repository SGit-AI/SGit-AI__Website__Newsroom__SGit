# The sources

A text snapshot of the sgit network, taken on 24 September 2026 around 23:40 UTC, plus the history and material behind the last week's work. Everything here is public, and every file is plain text, readable offline in any editor.

## `sites/`: the network, as text

675 files from 29 sites, fetched by `tools/fetch_sources.py`. `sites/manifest.json` records each file's URL, size, sha256 and fetch time: that is what tomorrow's run diffs against. `llms-full.txt`, where a site has one, is the whole site in one file.

| Site | Files | Size |
|---|---|---|
| sgit.ai | 185 | 3,864 KB |
| abp.sgit.ai | 180 | 3,109 KB |
| riskmandate.ai | 213 | 1,141 KB |
| risks.sgit.ai | 2 | 523 KB |
| open-source.sgit.ai | 28 | 454 KB |
| graphs.sgit.ai | 2 | 299 KB |
| newsroom.sgit.ai | 2 | 282 KB |
| wardley-maps.sgit.ai | 13 | 247 KB |
| llms.sgit.ai | 2 | 227 KB |
| influences.sgit.ai | 2 | 199 KB |
| sg-compute.sgit.ai | 2 | 119 KB |
| coding.sgit.ai | 2 | 119 KB |
| teams.sgit.ai | 2 | 91 KB |
| store.sgit.ai | 2 | 90 KB |
| games.sgit.ai | 17 | 72 KB |
| subscriptions.sgit.ai | 2 | 67 KB |
| nfrs.sgit.ai | 2 | 63 KB |
| threat-modeling.sgit.ai | 2 | 52 KB |
| pki.sgit.ai | 1 | 50 KB |
| standards.sgit.ai | 2 | 48 KB |
| providers.sgit.ai | 2 | 37 KB |
| skills.sgit.ai | 2 | 29 KB |
| twins.sgit.ai | 2 | 28 KB |
| issues-fs.sgit.ai | 1 | 13 KB |
| pt.newsroom.sgit.ai | 1 | 12 KB |
| nhi.sgit.ai | 1 | 12 KB |
| sg-sentinel.sgit.ai | 1 | 7 KB |
| chrome-extensions.sgit.ai | 1 | 7 KB |
| infographics.sgit.ai | 1 | 2 KB |

## `history/`: what changed

| File | What it is |
|---|---|
| `sgit.ai-new-pages-since-2026-09-18.md` | 61 pages published on sgit.ai in the last week, newest first, each with its local copy. **Start reading here.** |
| `sgit.ai-version-log.json` | Every sgit.ai release since v0.1.1 (166 entries): version, date, commit and the release note. The notes record what went wrong and how it was caught. |
| `sgit.ai-git-log.txt`, `sgit.ai-content-changes.txt` | The site repo's commits since 18 September, and the content files each one touched. |
| `sgit-cli-branch-log.txt` | Commits on the CLI branch that carries the briefs. |

riskmandate.ai keeps its own version record: `sites/riskmandate.ai/versions.md`, with a release note per version in `sites/riskmandate.ai/versions/`.

## `cli-briefs/`: briefs written for other teams

Briefs committed to the sgit CLI repository under `team/humans/dinis_cruz/claude-code-web/09/`, by date.

## `vaults/`: the five business plans, as their files

The source folders of the five business-plan vaults published this week: Company X-Ray, Lesson Loop, Risk Acceptance Office, Connector Twin and Agent as Webmaster. Read `plan/00-START-HERE.md` in each. Each `index.html` is the plan's app, with its data inlined, and opens offline in a browser. `published-vaults.json` lists all 36 vaults sgit.ai publishes, with their ids. No vault keys are included; the read keys are on the vaults' pages on sgit.ai.

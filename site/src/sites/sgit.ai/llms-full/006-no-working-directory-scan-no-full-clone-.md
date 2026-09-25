# no working-directory scan, no full clone needed
$sgit write notes/finding.md --file result.md \
 --message "agent A: analysis" --push --json
 {
"status": "pushed",
"path": "notes/finding.md",
"blob_id": "obj-cas-imm-9c2e41ab77d0"
 }

The vault key is the address, the auth, and the encryption key, one high-entropy string. Keep it safe.

**Git-like version control**commit, branch, merge, diff, log, stash, revert your encrypted files

**Client-side encryption**AES-256-GCM before upload; keys derived from your vault key, never sent to the server

**Real three-way merge**conflict files plus a base/ours/theirs `resolve --show` view

**The two-branch model**a private clone branch per machine or agent; shared named branches for collaboration

**Apps live inside the data**a vault can carry its own sandboxed app, with the permissions it asks for declared in a file

**Browser interop**open the same vault in SG/Vault on the web, CLI and browser speak one wire format

## What the server sees

### Your machine

- filenames & folder structure
- file contents
- commit messages
- branch names
- the vault key & derived keys

*[diagram]*

### The server

- obj-cas-imm-3f9c41ab77d0
- ref-pid-muw-8e02cc194b3a
- ciphertext blobs (AES-256-GCM)
- object sizes · timestamps
- the vault id

That's the whole list, and we publish the threat model, including what the server *can* see (sizes, timing, vault ID). [Read the security model →](security/index.md)

## Built for agents

Agents need shared state. Shared state needs versioning, and privacy. sgit is the encrypted, versioned workspace for humans and AI agents.

Persistent memory

### A vault is just a folder

An agent clones it, reads and writes files normally, commits, pushes. The next session pulls and continues. State survives the context window.

Multi-agent, human-merged

### A branch per agent

Each agent gets its own private clone branch; work meets on named branches; a human reviews the merge, in the terminal or in the SG/Vault browser.

Agent-grade plumbing

### Machine-readable everything

`sgit write` for surgical single-call commits, `--json` on every read path, `cat --id` with zero network calls, sparse clones for fast cold starts. [What that costs, measured](demos/fractal-graphs/performance.md).

[Read the agent guide →](docs/agents.md) · [Performance & cost →](demos/fractal-graphs/performance.md) · [Install the skills →](skills/index.md) · [Use cases →](use-cases/index.md) · [llms.txt](llms.txt)

## In production, and honest about it

sgit is in beta, powering production workflows daily. No superlatives, just the evidence, and a page that tells you when *not* to use it.

**~4,000** tests**mutation testing** in CI**integration tests** against a real server**2** runtime dependencies**Apache-2.0** [**security model** published](security/index.md) [**when NOT** to use sgit](docs/limitations.md) [**why** does this exist?](why/index.md) [**sgit · SG/Vault · SG/Send**: the three doors](docs/what-is-sgit.md)

## Nineteen sites, one question each

Most of the thinking behind sgit no longer lives on this site. It moved out to **`*.sgit.ai`**: a family of focused sites, each taking one question further than a section here could, each with its own version history and repository. This site stayed about sgit.

[**Agents & AI**identity for agents · calling an LLM with no API key · how the code is written](network/index.md#agents-ai) [**Risk & governance**you cannot deny a risk · cite the provision · the requirements nobody writes down](network/index.md#risk-governance) [**Graphs & method**meaning lives in the edges · issues as files · maps are claims](network/index.md#graphs-method) [**Security & infrastructure**a key registry for agents · an edge guard · ephemeral environments](network/index.md#security-infrastructure) [**Business & publishing**open source is a strategy · subscriptions are not rent · provenance as the product](network/index.md#business-publishing)

[Find the one that answers your question →](network/index.md)

## Start with an argument, not a menu

The articles are the readable way in: one page, one argument, with the screenshots and the links to check it. If you only read one thing here, read one of these.

[2026-09-24**Before you give an agent a connector, give the connector a twin**When an AI agent is given a Gmail or Google Calendar connector, it can read, send, move, decline and permanently delete on somebody's behalf, and for several of those actions the platform itself documents that there is no way back. This article argues that a twin of the connector is the minimum requirement for deploying an agent with confidence. The twin is a journal of every request and response the agent makes, appended as it happens to a write-only lane, processed later, and replayed into the inbox and calendar as the agent saw them, with a before and after for every change and a revert plan for each one. It gives provenance, explanation and a named list of what can and cannot be undone, and it changes the agent's behaviour policy from a hope into a list. Every claim about Gmail and Calendar is taken from Google's own documentation and linked. A working replay of an invented session, and a business plan for the service, are published alongside it as a vault.Read it →](articles/connector-twin-before-you-deploy-an-agent.md) [2026-09-24**Every risk is already accepted. The only question is by whom, and for how long.**A foundation article on risk acceptance, for readers who have never met the idea. A risk exists the moment the exposure does, so an organisation is always carrying it; the only open questions are who has accepted it, and until when. There is no deny button, only three doors (accept for a stated interval, fund the work, or fix it), and silence escalates. The interval is the decision, from four hours, which is an incident, to six months, which is a named decision to wait. Accepted is not the same as acceptable, which matters because the EU AI Act requires providers of high-risk AI systems to have residual risk judged acceptable, and never defines the word. Every risk has a holder, every holder has a boss, and every path ends at the board. Every risk is established by facts and ended by facts, from the board down to the configuration file, which is what closes the gap between a register and reality. The article walks one invented risk through six weeks, argues that each material risk deserves a vault of its own as its evidence pack, explains why executives resist the model, and shows why it fits alongside every GRC platform rather than replacing one. A business plan for a company that runs this loop is published with it.Read it →](articles/every-risk-is-already-accepted.md) [2026-09-22**The future of news is the story vault, not the paywall**The news industry runs on two commercial models, advertising and subscriptions, and both are bad for the reader. One sells the reader to somebody else. The other charges rent on something most people have stopped using. Both are now being dismantled from outside, by a search layer that has stopped sending traffic and by consumer law that arrives in January 2027. This article is about what to build instead, in practical terms. The objective is a commercial model that rewards investigative journalism, so that the expensive, evidenced kind of reporting drives usage, usage drives revenue that depends on neither search nor renewals, and that revenue funds more of the same. The mechanism is to stop selling the article and start selling what the article was made from. The story is a graph, a fractal semantic graph in which meaning comes from connectivity and every claim walks down to hashed evidence, so that trust comes through provenance and provenance comes via evidence. The article is one projection of it. From that one graph a newsroom can sell five things, on demand and in pence, to readers, to firms and to agents, and every payment walks back to the people who made the facts. It is built, in parts, on things we have already published.Read it →](articles/future-of-news-story-vault-not-paywall.md)

[All articles →](articles/index.md)

Encrypted vaults. **Git workflows.** Zero knowledge.

[5-minute quickstart →](docs/quickstart.md) [Star on GitHub →](https://github.com/SGit-AI/SGit-AI__CLI)



==============================================================================
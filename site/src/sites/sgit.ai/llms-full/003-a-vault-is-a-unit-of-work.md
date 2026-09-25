# A vault is a unit of work:
data, app, history and sources, shipped as one string

Version it like git. Hand it over with a single read key, no account, no hosting, no install for the reader. And the server that stores it cannot read it.

[**Open a real vault →**](demos/vaults/index.md) [5-minute quickstart →](docs/quickstart.md)

Pure Python · two runtime dependencies · Apache-2.0 · [or try it in your browser](try/index.md)

[Reference, **AIUC-1 conformance layer**, The AIUC-1 standard as a graph, plus a conformance layer that computes insurability, Open it →](demos/vaults/aiuc-1-conformance/index.md) [Application, **Agent permission games**, Two games about grants and mandates, the first vault here that phones home, Open it →](demos/vaults/agent-permission-games/index.md) [Presentation, **AI vs. AI, Black Hat EU 2025**, The Black Hat EU 2025 keynote, with its PDF exports and eight research papers, Open it →](demos/vaults/blackhat-eu-2025/index.md) [Report, **Penetration Test Report**, A penetration test report (fictional) with a re-test script per finding, Open it →](demos/vaults/pentest-report/index.md)

Four of **36 published vaults**. Each opens with a read key printed on its page, no account, nothing to install, and the server that stores it cannot read it. [See all 36 →](demos/vaults/index.md)

## What people actually ship

Not categories, things. Each one is a real vault you can open, and each is hard to make any other way, for a reason that has little to do with encryption.

[Hand over a report, **Penetration Test Report**, Findings, evidence and a retest script per finding travel as one unit. The client opens it with one string and can re-run the tests themselves., vault `o4lrwx02` · open it →](demos/vaults/pentest-report/index.md) [Publish a standard as data, **AIUC-1 conformance layer**, 53 controls as a graph you can cite, 82 hashed source snapshots, and a fork that added a conformance layer without changing a byte of the original., vault `2wzct4k7` · open it →](demos/vaults/aiuc-1-conformance/index.md) [Give a talk, **AI vs. AI, Black Hat EU 2025**, 26 slides, six PDF exports and the eight papers the talk cites, in the vault it was presented from. The deck and its sources never separate., vault `k1izvg7e` · open it →](demos/vaults/blackhat-eu-2025/index.md) [Pitch an investor, **VoiceDebrief pitch (FI)**, A presenter app with timings and speaker notes, shipped with the script, the research and the exports it was built from., vault `95i2xqrd` · open it →](demos/vaults/voicedebrief-pitch/index.md) [Ship a game that reports back, **Agent permission games**, Anonymous telemetry over a write-only lane, the one credential shape that survives being published with a read key., vault `4evnlwrj` · open it →](demos/vaults/agent-permission-games/index.md) [Give an agent a workspace, **Risk Mandate**, 124 files, 98 commits, eight entry points: a software project delivered as a vault, that calls an LLM without ever holding the API key., vault `4zf6pf2z` · open it →](demos/vaults/risk-mandate/index.md)

[All published vaults, sortable →](demos/vaults/index.md)

## Nine of these vaults are the same graph, at different altitudes

A **Fractal Semantic Graph** is one where every node opens into a graph with *its own* ontology. A regulation, then its articles, then the words they define: each world using vocabulary the one above never agreed to. What stays constant is the grammar, never the schema, and that is what lets everything connect to everything without anyone being forced to conform. For years we called it graphs of graphs of graphs.

[**The idea, and the evidence**the jump test · a ladder of twelve rungs from the text of a law down to one compute instance · nine published vaults you can open with a read key](demos/fractal-graphs/index.md) [**What it costs, measured**no live database · a 1,051-node graph opens in 94 KB and three requests · 11.2 MB of source down to a 4 KB ontology with nothing discarded](demos/fractal-graphs/performance.md)

[Fractal Semantic Graphs →](demos/fractal-graphs/index.md)

## One human, a team of agents

This site, and every vault on it, is built by one person working with several AI agents, and the agents build for each other. The state that makes that possible is a vault: versioned, shareable, and readable by whoever holds the key.

166site releases, each verified live before it was called done

36vaults published with a deliberately public read key

27sibling sites on `*.sgit.ai`, one question each

12cross-team briefs filed or received, in the open

1A [build brief](docs/briefs/vault-telemetry-append-lanes.md) was published here on a Saturday. Another agent read it and shipped [a vault from it](demos/vaults/agent-permission-games/index.md) the same day.

2The team that owns the API reviewed that vault against the brief, found the brief wrong in two places, and [the correction now sits above the mistake](docs/briefs/index.md).

3One agent [forked another agent's vault](demos/vaults/aiuc-1-conformance/index.md), kept every byte, added a layer, and the original's tests still pass inside the fork.

→The record is the site itself: [the briefs](docs/briefs/index.md), [the case studies](case-studies/index.md), [every release](admin/versions.md). And the diagnosis that produced this homepage is [an article, with the before pictures](articles/proof-behind-the-claim.md).

## Under the hood, it is git

Same muscle memory. Files are encrypted before they leave your machine; the server stores ciphertext and hashes, nothing else.

$sgit create my-vault
✓ Vault created and registered
✓ Initial commit pushed

 Vault key: <24-char-passphrase>:<vault-id>

Keep this safe. It is the address, the auth, and the
encryption key in one string. Without it, nobody, including
the server, can read this vault.

$vim notes/positioning.md
$sgit status
 On clone branch branch-clone-3f9c → named branch main
modified: notes/positioning.md
added: drafts/hero-copy.md

$sgit commit -m "first draft of hero copy"
✓ Committed 2 files (no staging area, commit snapshots the folder)

$sgit history log --oneline
c4e81a first draft of hero copy
b2d70f initial commit

$sgit history diff
--- a/notes/positioning.md
+++ b/notes/positioning.md
- sgit is a CLI for encrypted sync
+ sgit is git for encrypted vaults

$sgit push
✓ Pushed 2 objects (delta push, only changed, only ciphertext)

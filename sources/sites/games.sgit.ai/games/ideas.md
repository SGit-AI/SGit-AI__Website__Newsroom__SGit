# Ideas & feedback — the reply channel

> What players argue with becomes ideas, grouped into themes and answered with a published position — as a graph, joined to the mesh the questions come from, naming nobody.

*Source: <https://games.sgit.ai/games/ideas.html> · site v0.5.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / [Games](../games/index.md) / Ideas & feedback

# The reply channel — and why it is a graph

A game that collects disagreement and never answers it is a survey. The thing that turns these games into a conversation is the third app in *What Can It Do?*'s vault: what players argue with, turned into ideas, grouped into themes, and answered with a position that is published rather than filed.

## The answer comes back to where the argument happened

The by-product that matters most is `answers.json` — capability id to the position taken on it. The game inlines it at build time, so **a question somebody argued with now carries the answer**, folded above its 👍/👎. You disagree with a row, and the next player to reach that row sees what we said about it.

That is a deliberately unaddressed reply. Answering the person who complained would require knowing who they were, and that is the option that costs privacy rather than the one that gains capability. Keying the answer to the question instead reaches everyone who cares about it and identifies nobody.

## Published as a graph, under the mesh's own rules

The graph is compiled from three files by a builder that **refuses an edge whose type is not in the ontology, or whose ends are of the wrong type** — the same rule the mesh at [pki.sgit.ai](https://pki.sgit.ai) is built under. Node types are `idea`, `theme`, `signal`, `capability`, `decision` and `release`.

| File | What | Written by |
|---|---|---|
| `ontology.json` | the taxonomy: node types, edge types, their direction and meaning | hand |
| `ideas.json` | the authored half — ideas, themes, and the positions taken | hand |
| `signals.json` | the received half — one entry per drained feedback record | a person reading the feedback |

**Capability ids are the mesh's own** (`capability:read.file.host`), so this graph joins onto that one with no mapping in between. That is the payoff of writing both under the same grammar: an argument about a question is attached to the same node the question was generated from.

## What is deliberately not in it

- **No player is named.** There are no person nodes and no identifiers of any kind.
- **Nobody's words are quoted** unless a quote was deliberately filled in on that signal. Paraphrase is the default, because quoting somebody back in a public file is a disclosure they did not choose to make.
- **The raw feedback stays in the private telemetry vault.** What is published is the reading of it.

Every row is arguable, which is the point of publishing a graph rather than a summary. [What is sent when you press 👍 or 👎](../telemetry/index.md).

---

*[Site index for agents](../llms.txt) · [HTML version](https://games.sgit.ai/games/ideas.html)*

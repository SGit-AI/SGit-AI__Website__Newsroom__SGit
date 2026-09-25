# The catalogue

> Every game this family has published, with a maturity rung that has a test behind it, and the vault each one ships in.

*Source: <https://games.sgit.ai/games/index.html> · site v0.5.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / The catalogue

# The catalogue

Three things in two vaults, at three different stages. Nothing here is finished, and the rung on each card says how far off it is.

| What | Rung | What it measures | Where |
|---|---|---|---|
| [What Can It Do?](../games/what-can-it-do.md) | `scored` | Whether you can predict what your agent can do — scored for calibration, in both directions | [play](https://what-can-it-do.games.sgit.ai) · [open](https://dev.vault.sgraph.ai/#cf04d8a9bac6185dcb71e9c6f19ae13238b6434780324b1873504f2d6f7b505f%3Apg87npy3) |
| [Which Agent Is It?](../games/which-agent-is-it.md) | `playable` | Whether a handful of cheap questions can identify an agent, and how wrong your picture of its reach was | [open](https://dev.vault.sgraph.ai/#f94c8b1d42352d95703ac3d39032735d9b4e388d16ab5b87c948928d8e111118%3A4evnlwrj) |
| [Ideas & feedback](../games/ideas.md) | `answered` | Not a game — the reply channel: what players argue with, and the position taken on it | [open](https://dev.vault.sgraph.ai/#cf04d8a9bac6185dcb71e9c6f19ae13238b6434780324b1873504f2d6f7b505f%3Apg87npy3) |
| [The map — view, browse, propose](https://what-can-it-do.games.sgit.ai/map/contribute/index.html) | `playable` | Not a game — the pack's two matrices drawn live, and a way to propose a change to any row without a GitHub account: one sealed record over a write-only lane, which a drain on the player site turns into a pull request | [open](https://dev.vault.sgraph.ai/#3e1009cc489f07e9b1ffa9ff08087a5ff23f60367451708860ecde9439128816%3Amxhepww5) |
| [The Mavs PoC](https://what-can-it-do.games.sgit.ai/packs/mavs/index.html) | `sketch` | The same scoreboard on a different pack — how Mavs AI works, in the map's own terms: four surfaces, with Mavs in the path and direct. A draft, every row derived from mavsai.ai and pending their input | [open](https://dev.vault.sgraph.ai/#d7f6ae52196e96c532210b7d8a9743a2ed544749fe0677d337c4ef704430e155%3A0833bu5a) |

## Two vaults, one lock

Until 9 September 2026 all three shipped in one vault, `4evnlwrj`, *Two games about what your agent can do*. That day v0.25.0 was locked there on branch `release-2026-09-09`, and *What Can It Do?* moved to a vault of its own, `pg87npy3` (v1.0.0), taking the reply channel and the telemetry lane with it. It no longer carries a copy of its data: it reads [the pack](https://what-can-it-do.games.sgit.ai/data/index.html) from the player site on every load, and its footer names the version and hash it read.

`4evnlwrj` keeps the home page and *Which Agent Is It?*, at v0.26.0 with every permission removed and nothing sent, and stays the vault for the next experiments. What the split cost: the floor plan used to hand its matched profile to the scoreboard through the host's state, and that does not cross a vault boundary — the scoreboard asks you to name the agent again. The 9 September version, handover and all, is on the locked branch.

> **Open them yourself.** Two vaults since 9 September 2026. *What Can It Do?*: read key `cf04d8a9bac6…7b505f:pg87npy3` — [open it read-only in a new tab](https://dev.vault.sgraph.ai/#cf04d8a9bac6185dcb71e9c6f19ae13238b6434780324b1873504f2d6f7b505f%3Apg87npy3). The games vault, with *Which Agent Is It?* and the 9 September version of both on branch `release-2026-09-09`: `f94c8b1d4235…111118:4evnlwrj` — [open it](https://dev.vault.sgraph.ai/#f94c8b1d42352d95703ac3d39032735d9b4e388d16ab5b87c948928d8e111118%3A4evnlwrj); the full string is on [its page at sgit.ai](https://sgit.ai/demos/vaults/agent-permission-games/). Both are read keys: they cannot write, which is what makes publishing them safe.

**Where the data lives now:** the profiles, primitives, reductions and ceiling the games run on moved out of the vault into the player site's repository as a data pack — [the map](https://what-can-it-do.games.sgit.ai/map/index.html) — so that a pull request can change them. The vault still vendors a snapshot; the pack is the canonical copy.

## What is in the vault besides the games

- `what-can-it-do/source/` and `which-agent-is-it/source/` — each game's readable source: the engine as an ES module, `selftest.json`, the vendored data snapshot, the build script, and a README carrying a rules table and a *does-not-prove* list.
- `telemetry.html`, `telemetry.js`, `telemetry.config.json` — what the games send and the two write-only lanes they send it on. [Our page on it](../telemetry/index.md).
- `ideas/` — the reply channel: `ontology.json`, `ideas.json`, `signals.json`, and the `graph.json` compiled from them.
- `version.json` and `version.html` — the badge on every page and the release history behind it.

## Adjacent, and deliberately not listed above

**Licence to Operate** ([open it](https://dev.vault.sgraph.ai/#d990a52efb9af32c8463e2962f3ca5ccf92b3b6e8ea788e55009073c29b4da29%3Aposrhzp3) · [write-up](https://sgit.ai/demos/vaults/licence-to-operate/index.html)) is a published vault holding one agent's grant of 12 capabilities, its mandate of 4, and the 8-capability delta no policy covers — with every reply priced against a live policy. It is the best demonstration in this family of what the games are pointing at, and it is **not a game**: it never makes you commit to a belief before showing you the answer. Listing it above would blur the one distinction this site is built on. It is embedded on the player site instead, beside the game whose output it prices: [what-can-it-do.games.sgit.ai/licence-to-operate](https://what-can-it-do.games.sgit.ai/licence-to-operate/index.html).

## Coming, and deliberately not built yet

The game authors' own *next* list is short and honest: fit the point values from play data, show a returning player their previous calibration, export the mandate draft into the probes' shape, and put a model at the game's three edges — free text for an unlisted setup, question generation, narration. **None built, on purpose.** A game that generates its own questions cannot be self-tested against a reference, and the self-test is what makes the score arguable.

---

*[Site index for agents](../llms.txt) · [HTML version](https://games.sgit.ai/games/index.html)*

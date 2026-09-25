# The maturity ladder

> Five rungs, each with a test that moves a game up, so a label on a catalogue card is a claim rather than a mood.

*Source: <https://games.sgit.ai/maturity/index.html> · site v0.5.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / Maturity

# Five rungs, each with a test

Games arrive half-built. A catalogue that hides that is useless, and a catalogue whose labels mean whatever the author felt on the day is worse. So every rung here has a **test**, and a game moves up when the test passes — not when it feels ready.

| Rung | Means | The test that moves it up |
|---|---|---|
| `sketch` | an idea and a rules table, nothing playable | — |
| `playable` | you can finish a run | a stranger finished it without being told how |
| `scored` | the scoring is a stated rule, self-tested | `selftest.json` passes and the rule is published where a player can read it |
| `measured` | play data exists and has changed something | a release whose notes cite play data |
| `answered` | players argue with it and get answers back | positions published in the [ideas graph](../games/ideas.md) |

## Where the games sit today

| Game | Rung | Why not the next one |
|---|---|---|
| [What Can It Do?](../games/what-can-it-do.md) | `scored` | It has telemetry and a reply channel, but **no release note yet cites play data**. v0.16.1 moved the feedback controls on a bias argument — that is reasoning, and good reasoning, but it is not data. |
| [Which Agent Is It?](../games/which-agent-is-it.md) | `playable` | Its engine is self-tested against a reference, but it has had far less play than the scoreboard and its reveal predates the results redesign. |
| [Ideas & feedback](../games/ideas.md) | `answered` | Not a game, so the ladder fits it awkwardly. It is listed at the rung it enables for the others — it was seeded with the first three real pieces of feedback. |

> These placements are **our reading of somebody else's work**, made by reading the vault rather than by asking. If a release did move because play data said so, name it and the rung moves — that is what the [reply channel](../games/ideas.md) is for.

## Why the rungs are ordered this way

The order is not effort, it is **how much the game can be argued with**. A `playable` game produces an experience. A `scored` one produces a number you can check the rule behind. A `measured` one has been changed by contact with players. An `answered` one has a public position on the objections. Each rung is a step further from *we made a thing* toward *we made a claim and defended it*.

One consequence worth stating: **`measured` is the hard one**, and everything before it is under the author's control. A game can be built to `scored` in a weekend and then sit there for a year, because moving up needs other people to play it. That is the honest reason the first game has its own domain at [what-can-it-do.games.sgit.ai](https://what-can-it-do.games.sgit.ai) — a link you can send to somebody is the mechanism by which a rung gets earned.

---

*[Site index for agents](../llms.txt) · [HTML version](https://games.sgit.ai/maturity/index.html)*

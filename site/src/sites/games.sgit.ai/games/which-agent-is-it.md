# Which Agent Is It? — the floor plan

> The floor-plan game: think of an agent, answer cheap questions, chalk which wings of the building you think it can enter — then the doors open.

*Source: <https://games.sgit.ai/games/which-agent-is-it.html> · site v0.5.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / [Games](../games/index.md) / Which Agent Is It?

# Which Agent Is It? — the floor plan

Think of an agent. A handful of cheap questions narrow the field while you chalk which wings of the building you believe it can enter. Then the doors open, and the prediction gap is shown capability by capability.

## The board is the interesting part

Capabilities are drawn as rooms grouped into wings — filesystem, identity, process, code, network, communication, schedule, money, browser — and the legend keeps four states apart: **chalk** (asserted, you drew it), **pencil hatching** (inferred, the plan says so), **dotted** (possible, still consistent with what you have answered) and plain (no visitor above 5% likelihood holds a key). A belief column ranks the nine public profiles by likelihood, live, as you answer.

The game is careful about what a drawing is, and says so on the board: *"a room is a rendering choice, not a place — rooms are not ordered, sized or adjacent by anything in the data."* That sentence is doing real work. A floor plan invites you to read adjacency as meaning, and there is no adjacency in the underlying graph.

## The question that measures nothing

Mid-game there is a question labelled `IDENTIFIES` which the board says *"identifies and measures nothing"*, and it never counts toward the prediction gap. It is there to narrow the belief column — to work out *which* agent you are thinking of — and keeping it out of the score is the honest thing to do: you should not lose points for a question asked to help the game, not to test you.

## It used to hand you to the scoreboard

Until 9 September 2026 the reveal screen linked into [What Can It Do?](../games/what-can-it-do.md) with the matched profile already handed over, through the vault host's state — the reason the two shipped in one vault. The scoreboard now lives in a vault of its own, and host state does not cross that boundary, so the reveal links to it and it asks you to name the agent again. The version with the handover is locked on branch `release-2026-09-09` of the games vault.

**Rung: `playable`.** It scores, and its engine is self-tested against a reference, but it has had far less play than the scoreboard and its reveal has not been reworked since the scoreboard's results page was. [What the rungs mean](../maturity/index.md).

> **Open them yourself.** Two vaults since 9 September 2026. *What Can It Do?*: read key `cf04d8a9bac6…7b505f:pg87npy3` — [open it read-only in a new tab](https://dev.vault.sgraph.ai/#cf04d8a9bac6185dcb71e9c6f19ae13238b6434780324b1873504f2d6f7b505f%3Apg87npy3). The games vault, with *Which Agent Is It?* and the 9 September version of both on branch `release-2026-09-09`: `f94c8b1d4235…111118:4evnlwrj` — [open it](https://dev.vault.sgraph.ai/#f94c8b1d42352d95703ac3d39032735d9b4e388d16ab5b87c948928d8e111118%3A4evnlwrj); the full string is on [its page at sgit.ai](https://sgit.ai/demos/vaults/agent-permission-games/). Both are read keys: they cannot write, which is what makes publishing them safe.

---

*[Site index for agents](../llms.txt) · [HTML version](https://games.sgit.ai/games/which-agent-is-it.html)*

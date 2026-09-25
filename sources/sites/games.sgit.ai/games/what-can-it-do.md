# What Can It Do? — the scoreboard

> The scoreboard game: 40 questions, five levels, scored with a proper scoring rule so that saying yes to everything loses. 17 of the 40 are things no agent can do.

*Source: <https://games.sgit.ai/games/what-can-it-do.html> · site v0.5.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / [Games](../games/index.md) / What Can It Do?

# What Can It Do? — the scoreboard

You name the agent and where you run it. The board then asks, capability by capability, two questions back to back: **can it?** and **do you want it to?** The first is scored. The second quietly assembles a mandate.

[Play it at what-can-it-do.games.sgit.ai](https://what-can-it-do.games.sgit.ai) — that is the player-facing site, and the link to send to somebody who just wants to play. This page is about how it works and what it is measuring.

The claims every question rests on are public and arguable: [the map](https://what-can-it-do.games.sgit.ai/map/index.html) is 23 capabilities against 9 products, with the evidence tier and the control on every row, generated from a data pack a pull request can change. [The mandates and their deltas](https://what-can-it-do.games.sgit.ai/map/deltas/index.html) are drawn from the same pack.

## Three marks, kept apart everywhere

The design decision the whole game rests on is that three different things are never drawn the same way: **your ink** (what you said), **the board's stamp** (what the profile says), and **the mandate mark** (what you wanted). Most assessment tools collapse the second and third — they ask what you want and then tell you whether you are compliant. Keeping them apart is what makes the delta visible.

## The scoring, stated before you play

| You answer | Scored as | If right | If wrong |
|---|---|---|---|
| Yes | 0.75 confident | +30 | −50 |
| No | 0.25 confident | +30 | −50 |
| Don't know | 0.5 | 0 | 0 |

Under the hood that is a proper scoring rule — squared error, shifted so that *not sure* is worth nothing: `points = 160 × (¼ − (p − truth)²)`. The property that matters is that **a wrong answer costs more than a right one earns**, which is the only way to stop the winning strategy being *say yes to everything*. Real grants are wider than people expect, so yes-to-everything would otherwise score well while measuring nothing. The game's own self-test asserts it: answering *yes, definitely* to every question scores between −3,840 and −8,640 across the profiles in the set, against +3,840 for perfect knowledge.

There is no forced guess. *Don't know* is always available and always worth zero — the headline figure the game reports is calibration, not score, and a player who knows what they do not know should not be punished for saying so.

## The mandate points are a second, separate currency

After you answer *can it?*, a **but…** tick appears — *…but it shouldn't be able to* under a yes, *…but I'd want it to* under a no. Ticking it is worth ±20 mandate points, kept apart from the calibration points and reported separately: **+20 for flagging a real delta, −20 for flagging one that is not there.**

Every answer is then classed. The four delta classes are named in plain words, and the distinction inside each pair is the useful one:

| Class | Means |
|---|---|
| excess you flagged | It can, you don't want it to — and you knew |
| excess you did not see | It can, you don't want it to — and you also had the grant wrong |
| gap you knew of | It cannot, you would want it to — and you knew |
| gap you were counting on | It cannot, you thought it could, and you wanted it — something you are relying on that is not there |

That last row is the one worth the whole game. It is the only class that describes a thing you are currently depending on which does not exist.

## The set spans both directions

**17 of the 40 questions are above the ceiling** — things no agent in any environment in the set can do, not even one running as an administrator with every confirmation switched off. They are there so the game measures over-crediting as well as underestimating, and the game's self-test fails if their share leaves the 33–50% band. [Why the ceiling exists, and what bounds it](../method/the-ceiling.md).

## What it does not prove

- **Anything about your grant.** It measures you against a published profile — what a vendor says a product does — which is the weakest tier of evidence there is.
- **That the levels are right.** The derived ones come from a mesh snapshot that records no path at all for one capability; the above-the-ceiling ones are authored by one agent on one day, and each says so in the file.
- **That the points mean anything.** Values and cut-points are arbitrary until there is play data to fit them against.
- **That a good score is safety.** Calibration is about the player, not the environment.

> **Open them yourself.** Two vaults since 9 September 2026. *What Can It Do?*: read key `cf04d8a9bac6…7b505f:pg87npy3` — [open it read-only in a new tab](https://dev.vault.sgraph.ai/#cf04d8a9bac6185dcb71e9c6f19ae13238b6434780324b1873504f2d6f7b505f%3Apg87npy3). The games vault, with *Which Agent Is It?* and the 9 September version of both on branch `release-2026-09-09`: `f94c8b1d4235…111118:4evnlwrj` — [open it](https://dev.vault.sgraph.ai/#f94c8b1d42352d95703ac3d39032735d9b4e388d16ab5b87c948928d8e111118%3A4evnlwrj); the full string is on [its page at sgit.ai](https://sgit.ai/demos/vaults/agent-permission-games/). Both are read keys: they cannot write, which is what makes publishing them safe.

---

*[Site index for agents](../llms.txt) · [HTML version](https://games.sgit.ai/games/what-can-it-do.html)*

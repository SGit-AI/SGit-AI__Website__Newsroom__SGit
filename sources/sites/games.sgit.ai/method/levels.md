# Levels are distance, not danger

> A level is the number of hops from a capability to a one-way consequence, computed from the mesh — and the game says on the rail that it is distance, never a danger rating.

*Source: <https://games.sgit.ai/method/levels.html> · site v0.5.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / [Method](../method/index.md) / Levels

# Derive the levels from the graph

Difficulty tiers in most assessments are assigned by whoever wrote them, which means the tiers encode the author's intuition and nothing else. These are computed, and the computation is published.

## The definition

A **consequence** is a one-way exposure — an edge in the mesh marked `reversible: no`. A capability's level is the fewest hops from it to any consequence, moving through `at` edges (exposure → reach) and `runs-in` edges (reach → environment), within a single profile's exposures, minimised across every profile in the set.

| Hops to a one-way consequence | Level |
|---|---|
| 0 | 1 |
| 2 | 2 |
| 4 | 3 |
| 6 or more | 4 |
| no path found | 5 |

With the current snapshot that gives **13 / 3 / 5 / 1 / 1** derived capabilities across the five levels, plus **8 / 4 / 4 / 1 / 0** authored above-the-ceiling ones. The distribution is lumpy, which is a property of the mesh rather than of the game, and a long level is played in rounds of eight with a carry-on-or-finish card in between rather than being padded out.

## The sentence on the rail

The level rail says what each level means **and that it is distance, not danger**. That caveat is not decoration. A capability zero hops from a one-way consequence is not necessarily more dangerous than one six hops away — it is closer, which is a different claim. Reading a distance as a risk rating is exactly the mistake a numbered tier invites, so the game refuses the reading in the place where the number appears.

## The honest limits

- **The mesh has a gap.** It records no path at all for one capability in the set, which lands that capability at level 5 by absence of evidence rather than by distance.
- **The data is a snapshot.** Taken 2026-09-06 from [pki.sgit.ai](https://pki.sgit.ai) and vendored into the vault, with the date shown in the header of every screen. A vendored snapshot is reproducible and gets stale; a live fetch is current and unreproducible. The game vendors and stamps the date, and takes `?live=1` for the other behaviour.
- **Levels unlock, but nothing is locked.** A level unlocks when the one before scored ≥ 0; a locked level is dimmed and still tappable. Gating play on performance would measure persistence rather than calibration.

---

*[Site index for agents](../llms.txt) · [HTML version](https://games.sgit.ai/method/levels.html)*

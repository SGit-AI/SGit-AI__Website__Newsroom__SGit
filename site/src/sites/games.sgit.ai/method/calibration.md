# Calibration, not knowledge

> Why the scoreboard scores how well you know what you know, with a proper scoring rule that makes saying yes to everything a losing strategy.

*Source: <https://games.sgit.ai/method/calibration.html> · site v0.5.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / [Method](../method/index.md) / Calibration

# Score calibration, not knowledge

A quiz about agent capabilities would measure whether you have read the release notes. That is not the interesting question. The interesting question is whether the confidence you already act on is warranted.

## The failure this avoids

Score bare accuracy and the game has a dominant strategy: **say yes to everything**. Real grants are wider than people expect, so a blanket yes scores well — and a player who wins that way has learned nothing and demonstrated nothing. Every capability quiz that scores one point per right answer has this hole.

## The rule

```
points = 160 x (1/4 - (p - truth)^2)

  yes         -> p = 0.75
  don't know  -> p = 0.5
  no          -> p = 0.25

  right       -> +30
  wrong       -> -50
  don't know  ->   0
```

This is the squared-error (Brier) rule, shifted so that the midpoint scores zero. Two properties follow, and both are load-bearing. It is **proper**: your best strategy is to report what you actually believe, because any other report lowers your expected score. And it is **asymmetric in the way that matters**: −50 against +30 means confident-and-wrong costs nearly twice what confident-and-right earns, so blanket confidence loses.

## How we know it holds

It is asserted, not hoped for. The game's `selftest.json` plays *yes, definitely* to every question against every profile in the set and requires the result to land between −3,840 and −8,640, where perfect knowledge scores +3,840. If a change to the question set ever made blanket-yes profitable, the build fails.

## The simplification that came from playing it

The brief asked for three confidence levels plus an always-present *not sure*. The built game has three answers and no confidence row at all, and the note in the source is worth quoting as a design finding: a confidence slider *"confused the loop more than it measured"*. Fewer, coarser answers that people actually use beat a finer scale they answer noisily — the rule stays proper either way, and the numbers a player sees (+30, −50, 0) are ones they can hold in their head.

## What would show this is wrong

Play data where calibration scores cluster near the ceiling — meaning people already know what they know, and the game is measuring nothing. Or a wide spread with no relationship to how the player actually configured their agent, meaning it is measuring a trivia score after all. Neither can be checked yet: **no release has cited play data.** That is exactly why the scoreboard sits at `scored` on [the ladder](../maturity/index.md) and not at `measured`.

---

*[Site index for agents](../llms.txt) · [HTML version](https://games.sgit.ai/method/calibration.html)*

# The ceiling

> 17 of the 40 questions are things no agent can do, because a control outside the environment bounds them. Without them the game could only measure underestimating.

*Source: <https://games.sgit.ai/method/the-ceiling.html> · site v0.5.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / [Method](../method/index.md) / The ceiling

# Put a ceiling in the question set

If every question in a capability quiz has a real answer, then the only mistake the quiz can detect is underestimating. Somebody who believes their agent is less capable than it is gets caught. Somebody who believes it is a god does not.

## The fix, and its size

**17 of the 40 questions are above the ceiling**: things no agent in any environment in the set can do — not even one running as an administrator on a desktop with every confirmation switched off. They are interleaved evenly through every level, and the self-test fails if their share leaves the 33–50% band. At 43% the set spans both directions, so the score measures over-crediting and underestimating alike.

## The ceiling is a control, not the agent's restraint

This is the distinction that makes the whole idea work. Each above-the-ceiling row names the control that bounds it, and the control is always **outside the whole environment**: the provider's tenant boundary, an append-only log, cryptography, a second factor, a lockout, billing ownership, the provider's own isolation.

So the answer is not *the agent is well behaved*. The answer is *there is a wall there, and it is not made of the agent's good intentions*. Thirteen of the seventeen are **attemptable**, and their verdicts say exactly that: what happens when the agent tries, that it fails, and that the attempt is visible.

## They have to sound powerful

An above-the-ceiling question that reads as obviously silly teaches nothing and is spotted instantly, which turns the whole mechanism into a tell. These are written to sound like things a capable agent might well do — the player has to actually reason about the boundary rather than pattern-match on absurdity.

## Where the levels for them come from

Nowhere derivable, and the game says so. The mesh records no exposure for a thing that cannot happen, so the levels of above-the-ceiling capabilities are **authored** — stated as a judgement in the file, by one agent on one day, with every verdict linking back to it. That is a weaker claim than the derived levels next to them, and it is labelled as one rather than blended in. [How the derived ones work](../method/levels.md).

## What would show this is wrong

Somebody demonstrating an agent stepping over one of the seventeen. The game's own source calls that *"a correction, not a quibble"* — the row names its control, so a counter-example is a specific, checkable claim about that control, and the [reply channel](../games/ideas.md) is where it would be answered in public.

---

*[Site index for agents](../llms.txt) · [HTML version](https://games.sgit.ai/method/the-ceiling.html)*

<!-- generated from views/villagers.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.2.2 · canonical: https://open-source.sgit.ai/views/villagers.html*

> Maintaining the non-functional requirements — version control, reliability, resilience, security, backups, consistency, explainability, documentation — as a market, and the ability to read and repair code somebody else wrote as an appreciating scarce asset. Published with both of its own counter-arguments.

---

# Somebody has to be the villagers

The name comes from Wardley's Pioneers–Settlers–Town Planners pattern, which [wardley-maps.sgit.ai owns as a technique](https://wardley-maps.sgit.ai). What this page owns is the market argument built on top of it: **maintaining the non-functional requirements is a business**, the skill it requires is becoming scarce, and the mechanism that used to produce that skill is being taken apart at the moment demand for it is rising.

## The market, stated plainly

> "the sweet spot is to find the economic value where it's cheaper for these companies to pay a third party to maintain what I call the **non-functional requirements**, which fundamentally is the whole version control, reliability, resilience, security, backups, consistency, explainability, and documentation."

And the reason that market exists at all:

> "**none of the people who are doing it know how, and they don't want to**, because they are focusing on the domain."

That second quote is the whole business case in one line. The people building the applications are not bad at NFRs through carelessness; they are correctly allocating their attention to the domain, which is the thing only they can do. The NFRs are real work that somebody has to do and nobody wants to do — which is the classic shape of a service market, and it is why it is *villagers* rather than pioneers: this is the settlement work, not the exploration.

The demand side is expanding fast, and for a specific reason:

> "this market is going to grow exponentially because **every single team, every single department, every single function, even professionals, are going to create tons and tons of apps**."

Explorers are now everybody. Every one of those applications will need version control it does not have, backups nobody configured, and a security posture no one reviewed — and each one was built by someone who solved a real problem and has no interest whatsoever in any of that.

## The appreciating asset

> "The scarce asset in this market is **the ability to read and repair code somebody else wrote**." — "**Demand for a specific skill is rising sharply while the mechanism that produces that skill is being dismantled**, and firms with established engineers hold an asset that is appreciating rather than depreciating."

The mechanism being dismantled is the junior pipeline, and that is [where this argument meets the other place the author's position moved](../agents/index.md#pipeline): in March the position was that the learning path was restructured rather than eliminated and the density of learning per hour *increases*; by July it was that apparent gains shifted work from juniors to seniors rather than removing it, and the pipeline is being disrupted at exactly the moment the maintenance need is growing.

Both are on the record. Both are published. The July version is what this page's market claim rests on — which means **if March turns out to be right, this argument weakens considerably**, and that is worth saying out loud.

## The two counter-arguments — which the author raised himself

These are not objections collected from critics. They are in the original brief's own honest-tensions table, and leaving them in is what makes the rest of the page trustworthy.

> **1. The scarce-asset argument versus how long it lasts.**
>
> > "Tooling for reading and repairing unfamiliar code is improving quickly, and **the advantage may be a window rather than a moat**."
>
> This is the objection that most threatens the business model, and it is a genuinely open empirical question. If code comprehension is one of the things agents get reliably good at, then "can read somebody else's code" stops being scarce quite fast, and the appreciating asset depreciates on a schedule nobody can currently forecast. The honest position is that the window is real and its width is unknown.

> **2. Maintaining what should not have been built.**
>
> > "Some of these applications should be retired rather than hardened, and **a firm paid to maintain has no incentive to say so**."
>
> This is the sharper objection and it is a structural conflict of interest, not a risk of bad behaviour. A maintenance business is paid per thing maintained. The advice "delete this" is the one recommendation that costs the adviser money every time it is right. Nothing in the business model corrects for it, and any honest version of this service has to say what it does about that — a question this page raises and does not answer.

## A note on the numbers

> **Deliberately absent.** The original brief carries a market-size statistic and several figures attributed as *"reported"* and *"is cited as finding"* — and it flags, itself, that *"much of what circulates is vendor commentary recycling a smaller set of underlying studies."* They are not reproduced here. The direction of the argument does not depend on them, and [this site's position is that you do not publish a number you cannot source](../history/numbers.md) — a standard it holds others to, so it does not get an exemption.

## Where this sits in the network

Wardley's Pioneers–Settlers–Town Planners pattern belongs to [wardley-maps.sgit.ai](https://wardley-maps.sgit.ai), which owns the mapping technique and the pattern itself. This page owns the NFR-market argument built on it. One canonical copy each, cross-linked — the split is deliberate, and it is the same discipline applied to [standards.sgit.ai](https://standards.sgit.ai) for SPDX (they own the machinery, this site owns [the argument about running it continuously](../agents/index.md#compliance)).

[← Open core, or packaging?](open-core.md)[Survivability →](../survivability/index.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*

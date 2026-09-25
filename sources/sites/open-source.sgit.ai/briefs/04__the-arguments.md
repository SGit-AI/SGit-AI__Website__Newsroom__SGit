# 04 — The arguments: where you are opinionated, and where you disagree with yourself

The corpus is unusually honest — most briefs carry a mandatory *Honest Tensions* table. **These are the best pages the site can have**, and several of them are better published unresolved than tidied.

`research__history-and-success-stories.md` Part 4 supplies the both-sides framing for seven of these from outside the corpus. Use it: a page that only states your side reads as advocacy, and the site's whole credibility position is that it corrects the romantic story before making its own argument.

---

## 1. Survivability is a copyright and trademark property, not a licence property

**The site's best original idea.** Stated plainly:

> ***"Survivable is not a property of the licence file. It is a property of the copyright and trademark structure."***

And the mechanism, which is what makes it a finding rather than an opinion:

> *"An OSI licence is irrevocable for code already published, but the copyright holder may ship the next version under different terms. **Every catalogued relicensing between 2018 and 2024 followed the same legal pattern: a single corporate copyright holder, having aggregated contributor copyright via a CLA, exercised the right to change terms going forward. Distributed-copyright projects could not be moved the same way, because no single party had standing.** And acquisition entrenches rather than reverses the closure: **HashiCorp went BUSL, IBM acquired it, and the licence stayed.**"*

**The history research corroborates this from two directions.** PostgreSQL is the control case — no company owns it, so no company can relicense it, and it is now the most-used database at 55.6%. OpenSolaris is the counter-case — open-sourced under a deliberately GPL-incompatible licence, with Sun retaining governance, then killed by Oracle after acquisition. **The licence was not the problem; the copyright holder was.**

One update the corpus does not have: **two of the four relicensings partially reversed.** Elastic added AGPLv3 in August 2024; Redis 8 shipped AGPLv3 around 1 May 2025. That does not weaken the argument — it sharpens it. The same single-holder standing that let them leave let them come back. **Structure determines what is possible in both directions.**

---

## 2. The Change-of-Control Stress Test — ship it as a tool

Four legs, each answerable from public artefacts:

| Leg | Passes | Fails |
|---|---|---|
| **Copyright** | DCO / inbound=outbound, distributed holders | Single-entity CLA aggregating contributor copyright |
| **Trademark** | Neutral foundation, charter-level transfer restrictions | Held by the operating company |
| **Schema licence** | CC0 or CC BY, licensed separately from the code | Undeclared, or bundled with the code licence |
| **Fork capacity** | **A named party with the headcount and mandate to run the fork** | *"The community would fork it"* with no named party |

> ***"The stress test is a query, not an interview. 'Show me the CLA' and 'show me who holds the trademark' are answerable from public artefacts, and a vendor that cannot answer them has answered them."***

**Build this as a form or checklist, not an essay.** It is the single most useful artefact the site can hand a working buyer, it requires no cooperation from the vendor, and nobody else publishes it.

**And run it on yourself, publicly.** SGraph's copyright is held by one company — the exact single-holder pattern the argument identifies as the failure mode. Publishing that self-audit, with what would have to change and whether you intend to change it, would be **the most credible page on the site**. A tool whose author will not apply it to themselves is a marketing asset; one who does is a standard.

---

## 3. Open core — the corpus contradicts itself, five weeks apart

**18 June:** *"There should be **nothing proprietary**. You never have the temptation of the bait model, where some of the best features are locked behind proprietary stuff, because the community always sees through it."*

**17 July:** *"more and more we want situations where the **customers only have a subset of the code that exists in the main repo**, because of security, because of maintainability, because of complexity."*

And the July document diagnoses itself in its own tensions table:

> *"Open source versus the customer subset | A fuller main repo than the customer receives sits uneasily with a pure open-source claim; **this is open-core, and worth saying so plainly.**"*

**There is a real reconciliation available, and it is a different argument.** The 4 June brief frames the subset as **subtraction, not withholding**: *"customisation is not only addition; it is subtraction… less attack surface… cheaper to run… maintainable."* A 10% subset that is *smaller* than the public repo is not open core. A subset that contains something the public repo does not is.

**The page should state the test explicitly:** does the customer build contain anything the public repo does not? If no, it is packaging. If yes, it is open core, and — per the 17 July brief's own instruction — say so plainly.

**Both sides, from the research:** the case for open core is that it is the only model that has repeatedly funded large-scale development without rent extraction on the core; the case against is that the boundary always moves toward the vendor under revenue pressure, which is exactly what 2018–2024 demonstrated. **VS Code is the strongest live example of open core done well** — and the research note is pointed: most of its 75.9% user base does not know it is running proprietary software.

---

## 4. Funding — three incompatible answers, none costed

The corpus proposes three, and never compares them:

**Market forces and labelling** (29 Mar): *"Charity will not fix this. 'It is the right thing to do' will not fix this. **The only thing that will fix this is market forces.**"* → declare your supply chain, calculate value contribution, pay proportionally, publish a rating. With the best image in the corpus: *"Just like a restaurant health rating on the door: you can still choose to eat at the restaurant with a bad rating. **But you know.**"*

**A maintainer platform** (11 May): the problem is not licences but missing infrastructure — *"A solo maintainer publishing a Python package today has no realistic path to capture value from production users. **The relationship is missing because the platform is missing.**"* With the boundary: *"the commercial line is where the package touches the target app… A consultancy can study the package. **The maintainer is the package.**"*

**State-funded exit bounties** (24 Jul): *"**Every one of those programmes funds the supply side**… None of them funds the **substitution side**… on present evidence nobody is funding it."*

And the standing admission: *"**the sustainable funding question is unsettled.**"*

**cURL settles part of the argument empirically.** Thirty billion installations, a bounty programme that paid $90,000 across 81 genuine reports since 2019, and it was **shut down on 31 January 2026** because ~20% of 2025 submissions were AI slop against ~5% genuine. Charity did not fix it. The platform did not fix it. **An externality nobody was paying for destroyed the mechanism.** That is the strongest evidence in the world for the organic-food argument, and it arrived after the argument was written.

**The page should pick one and say why**, or argue that all three are needed and name which failure each addresses. Three unreconciled proposals read as thinking; three unreconciled proposals *presented as a position* read as indecision.

---

## 5. Sovereignty bounties — fund the exit, not the supply

The strongest single idea in the corpus, and genuinely unclaimed elsewhere.

Fund the **substitution side**: pay companies to build and operate documented, working migration paths *off* proprietary platforms. Two second-order ideas make it more than a grant scheme:

**Bounty size as a published lock-in metric** — *"it's then market economics, like the more complicated is the bigger the bounty."* If the cost of exit is published, lock-in becomes a measurable, comparable property of a vendor rather than a vague complaint.

**Vendor-sponsored proof of no lock-in** — a vendor funding *"a documented, working exit path from its own product acquires a strong and checkable claim that it does not hold its customers by lock-in."* That is a genuinely novel commercial move and it should be written up as one.

**Its weakness, which should be stated:** nobody has piloted it, no bounty has been sized, and the moral hazard is unaddressed — a vendor sponsoring its own exit path controls how good that path is.

---

## 6. Sovereignty — the four-step argument

OS1–OS5, and it is tight:

1. *"it is only when the code is open source that there is a possibility and the ability to have independence and sovereignty. Because if you suddenly get cut off from the service, at least you have a chance."*
2. *"**the data schemas are as important as the code.** Sometimes you say the data is open, you have access to the data, but you do not have access to the code or the schemas. And by access I mean you need to be able to **control** it, to **own** it."*
3. *"without owning it you are dependent on service-level agreements, so **you are one SLA away from losing access**. And whichever government has jurisdiction and control over the company that controls the code controls the other countries. It is literally that simple."*
4. *"who owns a company is already very fuzzy… especially with acquisitions you lose control. **A European company gets acquired by a US company and the sovereignty moves, you lose it.**"*

Plus the counter to the standard objection: *"I do not buy that this will stifle innovation, because the work is there. It is a question of whether there is a **rent-extraction process** happening, which is what proprietary software provides."*

**Note that step 4 is step 1 of §1.** Sovereignty and survivability are the same argument at different scales — one about a country, one about a project. The site should say so; it makes both stronger.

---

## 7. Somebody has to be the villagers

> *"the sweet spot is to find the economic value where it's cheaper for these companies to pay a third party to maintain what I call the **non-functional requirements** — version control, reliability, resilience, security, backups, consistency, explainability, and documentation."*

> *"none of the people who are doing it know how, and they don't want to, because they are focusing on the domain."*

> *"**Demand for a specific skill is rising sharply while the mechanism that produces that skill is being dismantled**, and firms with established engineers hold an asset that is appreciating rather than depreciating."*

**Publish both of its own counter-arguments**, which the corpus already wrote:

- *"The scarce-asset argument versus how long it lasts | Tooling for reading and repairing unfamiliar code is improving quickly, and **the advantage may be a window rather than a moat**."*
- *"Maintaining what should not have been built | Some of these applications should be retired rather than hardened, and **a firm paid to maintain has no incentive to say so**."*

That second one is the sharper objection and it is the corpus's own. Leaving it in is what makes the page trustworthy.

---

## 8. The other tensions, in brief

**Hyperscalers: threat or tide?** Argued both ways in one document — *"you want the hyperscalers to adopt and embrace these technologies, because they open up the market"* versus *"Hyperscalers could commoditise it. Their embrace opens the market but could also absorb it."* No resolution offered. The research's version of this argument (Part 4, §4) has the numbers on whether they fund more than they take; use it.

**Lock-in degrades your own architecture** — *"you introduce attrition, and by introducing attrition you create much worse architectures, because there is a lot of simplicity when you do not have copyrights, licensing, and restrictions."* An unusual and good argument: the case against lock-in made on *engineering* grounds rather than ethical ones.

**Open source frees you to delete your own code** — *"it makes you more motivated, and with less false sense of ownership, to cannibalise your own code or remove code you had, because it is open source, the code does not particularly have value."* Short, original, and true.

**The moat is a rate, not a wall** — *"A competitor who forks our code today gets our position as of today. **They do not get our velocity.**"* / *"The code is open source. The execution is not forkable."*

**Necessary but not sufficient** — open source as a precondition for sovereignty rather than a guarantee of it. The corpus is careful about this and the site should stay careful.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).

<!-- generated from agents/index.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.2.2 · canonical: https://open-source.sgit.ai/agents/index.html*

> Code-reading as the appreciating scarce asset, two dated positions on the junior pipeline both published, and four theses that follow from the author's writing and are next to be written — including licence compliance at machine speed.

---

# Agents and open source

The claim this page makes: **the economics of maintaining open source have changed, the change is measurable, and it currently runs against maintainers before it runs for them.** The claim it deliberately does not make is that agents will fix the sustainability problem — every piece of 2025–26 evidence points the other way, including this project's own.

## Code-reading was already the problem. It was accelerated, not created

The argument opens by refusing its own easy version, which is why it is worth reading:

> "Before AI agents started writing code, you could argue that **90% of the code running in production was not being read by anyone**… So let us not pretend that 'nobody reads the code anymore' is a new problem. **It is an old problem, accelerated.**"

And the passage underneath it, which is the best-written thing the author has published on this subject:

> "I would argue that this narrative has caused more damage than people admit… **Applications with 2,000 dependencies. CI pipelines that download half the internet. Layers of abstraction where nobody on the team understands what is happening below their layer.** The answer was never 'stop abstracting.' The answer was '**someone still needs to understand what is underneath.**' Linus Torvalds reads C code."

The three-phase answer maps onto [the Wardley teams](../views/villagers.md): *"Explorers: agents read it (scans, checks, basic quality)… Villagers: mid-level developers read it… Town Planners: senior developers really read it."* Which is a coherent structure — and it depends entirely on the middle tier continuing to exist.

## Two dated positions on the junior pipeline, both published

This is the second place the author's position moved between two dated documents. Like [the open-core question](../views/open-core.md), it is more valuable published as two dates than tidied into one.

| When | The position |
|---|---|
| **21 March 2026** optimistic | *"The learning path is not eliminated. It is restructured… Instead of learning by writing simple code from scratch, **juniors learn by reading, evaluating, and improving code at scale. The density of learning per hour increases.**"* |
| **28 July 2026** evidence | *"apparent gains **shifted work from juniors to seniors** rather than removing it."* |
| **31 July 2026** the market claim | the junior pipeline *"is being disrupted at exactly the moment the maintenance need is growing."* |

Four months, opposite directions. The March position is a plausible theory about how learning could restructure; the July position is what the evidence looked like when someone went and checked. **Both are on the record here.**

> **What would settle it.** Not opinion — a cohort measurement: are people who entered the profession after 2023 acquiring the ability to read and repair unfamiliar code at the same rate, faster, or slower than the cohort before them? Nobody appears to be measuring it. Until someone does, this is [an open question](../roadmap/index.md#open), and [the villagers market argument rests on the July answer being the right one](../views/villagers.md) — which is worth saying plainly, because it means that argument is exposed if March turns out to be correct.

## Agents currently add maintenance load

The author wrote this down before the evidence arrived, which is the strongest form of a prediction:

> "**AI slop** for low-quality, auto-generated pull requests that flood maintainer queues without adding value, increasing the burden on already-stretched maintainers. So AI is, for now, **adding maintenance load** rather than only creating maintainable work. **This does not refute the thesis, it sharpens it.**"

And then it acquired a named casualty with a date. cURL — ~30 billion installations, seven volunteers on the security team — **closed its bug bounty on 31 January 2026**, because roughly 20% of 2025 submissions were AI-generated slop against roughly 5% genuine, each report consuming three or four people for up to three hours. [The full story is its own page →](../funding/curl.md)

Independent corroboration, with the caveat it needs: Black Duck's OSSRA 2026 reports **mean vulnerabilities per codebase up 107% year on year** and attributes it to AI-accelerated code creation. That attribution is **the report's interpretation, and correlation rather than demonstrated causation** — [this site's rule is to say so](../history/numbers.md).

## Where the economics genuinely do change

Four pieces exist across the author's writing and had not been assembled into one claim. Assembled:

1. **Agentic mass-customisation replaces professional services.***"you turn the tail around. You use agentic workflows to create mass-customised and supported versions of the product… whoever creates this will be a domain expert in all of them, but the company is unlikely to have a person who understands all those phases."*
2. **The value margin moves.***"The sweet spot is to operate at that margin where it is profitable for companies to pay you versus doing it themselves. As long as you operate there, you have a valid business model, and **now with agents that is possible in ways it was not before**."*
3. **Multi-level expertise becomes affordable.***"In the past, having people who could operate at multiple levels of abstraction was expensive and rare. **With AI agents handling the volume, it becomes economically viable.**… That is not a problem AI creates. It is a problem AI finally makes economical to solve."*
4. **And, for now, it runs the other way** — see above.

The assembled thesis is narrower than the optimistic version and more defensible: **agents make it economically possible to pay attention to things that were previously too expensive to attend to** — which is precisely [the NFR maintenance market](../views/villagers.md). Whether that materialises before the maintainer attrition it is currently causing is genuinely undecided.

## Four theses that follow, and are written nowhere

These are the most original writing still available on this subject, and each is an obvious consequence of material that already exists. None is written. They are listed here as an agenda rather than claimed as work done.

### (a) Licence compliance at machine speed

Three components exist separately. **One:** a single manual SPDX review of 17 transitive dependencies, from February 2026. **Two:** the PBOM idea — *"you leverage the ideas and concepts around SBOMs, but say, this is about permissions… a bill of actions or a bill of permissions"*, with the claim that *"this mapping is more important than the SBOM, because it should impact the SBOM"*. **Three:** the bridge — *"**SPDX identifiers are the evidence artefact**"*, with a falsifiable predicate attached.

Nobody has written **"agents doing licence compliance continuously"** as a thesis, and the external evidence makes it urgent: OSSRA 2026 reports **licence conflicts in 68% of audited codebases, up 12 points — the highest in its history**, and that **only 24% of organisations check AI-generated code across security, IP/licence, quality and all four categories.**[standards.sgit.ai owns the SPDX machinery](https://standards.sgit.ai); the argument belongs here.

### (b) Provenance and attribution of AI-generated code

The closest existing artefact is a **signed-licence proposal** from February 2026 which explicitly extends to code: *"**MIT-S** adds: 'This software includes a cryptographic signature from the original author. You must preserve this signature in all copies and substantial portions of the software.'… If the code is modified (fork): → Fork must be signed by the modifier → Original signature preserved alongside → **Chain: original author → modifier**"*.

It was written about **human** authorship and never applied to machine-generated code. **The bridge is the obvious next move**: a signature chain is exactly what an AI-authored contribution needs and exactly what it cannot currently produce. [pki.sgit.ai holds the signing machinery](https://pki.sgit.ai); nobody has written the licensing argument on top of it.

### (c) Training-data licensing

One substantive passage exists, from a 2025 article: *"European lawmakers and creative industries are discussing mechanisms so that **creators can be remunerated when AI uses their works**… **Open-source projects can lead the way here by openly cataloguing their training sets** and filtering out data that's proprietary or sensitive. Ultimately, an ecosystem where **both models and their training data are open and auditable** is one where users (and regulators) have far more control."*

The argument has moved a long way since then, and the author's published position has not yet followed it. The live question is the **OSI's Open Source AI Definition**, which drew heavy criticism, and the fact that **almost no model marketed as "open source AI" meets it** — "open weights" being the accurate term for most of them. That is a licensing argument, it is exactly this site's subject, and it is unwritten.

> **A browser vendor is now betting on that distinction, in public.** Mozilla's chief executive **Anthony Enzor-DeMeo**, interviewed by Sabrina Ortiz for [↗ The Deep View](https://www.thedeepview.com/articles/why-mozilla-is-on-a-mission-to-prevent-ai-lock-in) (August 2026), states that Mozilla will *not* build a frontier model and will instead ship **model choice** in Firefox — *"We want to give users access to different things they wouldn't normally have access to when they're kind of confined and locked in."* The stated failure mode being avoided is the search default: one provider becoming everyone's default and the default becoming the market. The bet is placed on **open-weight** models, which is precisely the term this thesis says is the accurate one.

The reason he gives is [this site's own argument](../views/index.md#zero-contributions), arrived at independently and applied to models rather than to code — *"if you're giving something away, it's obviously easier to gain adoption, and then more people will conform to those standards — and thus those people will be in more control. We saw that with the web"*, his own pull-quote from the same conversation. Giving it away is not generosity. It is how the standard gets set, and whoever sets the standard keeps the control. That is the strategy-not-charity claim in somebody else's words, made by somebody with a browser to fund.

> **Read it as positioning rather than as evidence.** It is a strategy statement from an interested party — Mozilla's commercial position depends on there being no single gatekeeper, so it would make this argument whether or not it were correct, and a stated intention to ship is not a shipped thing. What it does establish is a **dated instance**: an organisation with real distribution choosing open weights on lock-in grounds in 2026.
>
> **And it sharpens [Q7](../roadmap/index.md#open) rather than settling it.** "Open weight" is exactly the category the OSI's definition holds is *not* open source AI. So the most prominent organisation making the openness argument for models is backing the thing the definition excludes, and the interview does not address training data at all — which is the whole of what the definition is about. That gap, between the openness people are willing to fund and the openness the definition requires, is the argument this thesis still has to make.

### (d) What CC BY means for machine reuse

[The estate's writing is CC BY 4.0 throughout](../practice/index.md#reading) — the published essays included, since 6 September 2026, when the CC0 in that repository's licence file was settled as drift rather than a third layer. In a world where models train on public text and agents synthesise from it, **choosing CC BY over CC0 is a decision about machine reuse, not human reuse**: it keeps the one obligation that can survive into a synthesised output — attribution — where CC0 would have removed it.

What attribution *means* when the reuser is a model rather than a person is the page nobody has written: what a synthesised paragraph owes its sources, whether a licence footer is machine-readable enough to count, and whether the estate's provenance discipline — every document dated and footed — is exactly the artefact that makes the obligation enforceable. It may be the most interesting of the four.

## Agents are a primary audience of this site

Not a topic — an audience, which makes traversal a build requirement. *"**The audience is disproportionately agents**… If agents are a primary audience, the failure mode is a primary failure mode."*[How this site implements the mitigation ladder →](../practice/publish-the-source.md), and [the whole site in one file](../llms-full.txt) if you are one.

[← Publish the source](../practice/publish-the-source.md)[Funding →](../funding/index.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*

<!-- generated from index.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.2.2 · canonical: https://open-source.sgit.ai/index.html*

> Open source as a strategy rather than a charity — by Dinis Cruz, founder of the sgit.ai network, MyFeeds.ai and The Cyber Boardroom, and former OWASP Board member. Guidance for founders on owning the code or opening it; the position with its counter-cases; the licences actually in force; and a history checked against its sources, including six corrections to the story most sites tell.

---

Open source · sovereignty · survivability · the economics

# Open source is a strategy. It is not a charity.

Most sites arguing for open source argue that it is generous. This one does not. **The power of open source is not for the community, it is not because it is nice for others, and it is not to give back** — it is that technology stops being the moat, that you become free to delete your own code, and that sovereignty becomes possible at all. And the accurate history supports that far better than the romantic one does.

By [**Dinis Cruz**](about/index.md) — founder of [sgit.ai](https://sgit.ai) and [sgraph.ai](https://sgraph.ai), [MyFeeds.ai](https://investor.myfeeds.ai/), [RiskMandate.ai](https://riskmandate.ai), [VoiceDebrief.ai](https://voicedebrief.ai) and [The Cyber Boardroom](https://thecyberboardroom.com); former OWASP Board member. This is the strategy those companies run on. [↗ LinkedIn](https://www.linkedin.com/in/diniscruz)

[For founders: owning the code, or opening it →](founders/index.md)[Read the position →](views/index.md)[Run the stress test on a vendor →](survivability/stress-test.md)

## For founders: owning the code, or opening it

Every solo founder who ships something that works arrives at the same fear: a bigger, better-resourced company takes the code and there is nothing left. Notes from a strategy session with an early-stage SaaS founder — the walk-through that answers it, and what it changes about how you build.

### [What copying you would actually cost them](founders/index.md#cost)

*The answer*

An established company holding a full copy of your code still has to decide, fund, staff, deploy and own it forever. **Optimistic: three months to reach where you already are. Realistic: closer to a year.** Which turns the fear into the pitch: *"You can take it. It will cost you that. Or you can pay me, and have it next week."*

### [Instinct versus leverage](founders/index.md#issues)

*Four things that surface*

The shop-front reflex, the keys in the repo, prototype code asked to behave like a product, and the collaboration that is not a commitment — each an instinct that made sense once, with the counter-argument that reverses it now.

### [Eight steps, in order](founders/index.md#route)

*The practical route*

Four you do while the repo is still private, one point of no return, and three habits that run alongside from this week. Plus the three things to settle before you publish: the licence is a commercial decision, trade marks come first, and where the cost argument stops holding.

### [A week of this, counted](founders/index.md#week)

*The discipline*

Releases tagged, untrue claims removed, support channels live. The handover from prototype to product is invisible from the outside unless you count it — and publishing the count means you cannot quietly skip a week.

## Not free. Free*dom*.

Two sentences carry the whole site. The first is the unfashionable one; the second is the one that makes it land.

> "the power of open source is not for the community, it is not because it is nice for others, and it is not to give back."

> "open source is not free, somebody is always paying for it. What you get from open source is freedom, that is different… We play the game of empowering the user and being the reputable source of trust. **We are selling trust.**"

Everything else here is a consequence of those two. If open source is a gift, then its funding problem is a moral failure and the answer is to shame people into paying. If it is a strategy, the funding problem is an *externality* — and externalities are fixed by structure and by market forces, not by virtue. [cURL is the case that settles it →](funding/curl.md)

## The position, the practice, and the history

Three things a site about open source should be able to show: what it thinks, what it actually ships and under which licence, and whether the history it leans on is true. This one does all three, and says where each comes from.

| What | Where it comes from | What this site does |
|---|---|---|
| **The position** | **The author's own writing** — 56 catalogued concepts, 24 of them original arguments rather than restatements | [Argues them, and names the counter-case each time](views/index.md) |
| **The practice** | **The licence files** — three licences across three layers of a real, shipping estate | [Publishes the licences, and the reasoning behind each](practice/index.md) |
| **The history** | **Researched from primary sources** for this site — 1955 to 2026, every number carrying its source, date and caveat | [Leads with six corrections to the standard story](history/index.md) |

The division of labour is deliberate: **the argument comes from experience, the ground under it comes from research** — and the research turned out to support the argument better than the version everybody repeats. [The numbers, and the ones this site declines to publish →](history/numbers.md)

## Six things the standard history gets wrong

These lead, rather than a timeline, because everyone has a timeline and almost nobody publishes these. Each one is checkable, and each one points the same way: the model wins on **economics and structure**, not on virtue and not on eyeballs.

### [Unix circulated because it was illegal to sell it](history/index.md#unix)

*1955–1982*

The 1956 AT&T consent decree barred Bell Labs from any business but common-carrier communications. Unix shipped for media and postage as a **compliance artefact**. The decree lifted in 1982 and AT&T commercialised System V immediately.

### [BSD lost to litigation risk, not to its licence](history/index.md#bsd)

*1992–1994*

USL v. BSDi clouded free Unix during exactly the window Linux needed. The settlement removed **three files out of eighteen thousand**. The claim was nearly empty; the two years of uncertainty were decisive.

### [Netscape's source release was a six-year near-failure](history/index.md#netscape)

*1998–2004*

The code was so degraded the team threw it away and rewrote. **Firefox 1.0 did not ship until November 2004**, by which time IE had won. The founding case study of the movement is a cautionary tale.

### [Eric Raymond did not coin "open source"](history/index.md#peterson)

*Feb 1998*

**Christine Peterson** did — and deliberately had someone with more credibility as a Linux programmer introduce it, so that it would spread. Sources disagree on the exact day; they do not disagree on who.

### ["Given enough eyeballs" is not a security property](history/index.md#eyeballs)

*2014, 2024*

Heartbleed survived two years in the most security-critical library on the internet. **xz was engineered by the maintainer to survive review** — and was caught by one engineer benchmarking SSH latency, not by a security review.

### [Two of the four relicensings reversed](history/index.md#reversals)

*2018–2025*

Elastic added AGPLv3 in August 2024; Redis 8 shipped AGPLv3 in May 2025. That does not weaken the survivability argument — **it sharpens it**. The same single-holder standing that let them leave let them come back.

## Survivability is not a property of the licence file

Buyers read licence files. Licence files are the *weakest* of the structural protections, and 2018–2024 is the proof.

> "Survivable is not a property of the licence file. **It is a property of the copyright and trademark structure.**"

The mechanism, which is what makes it a finding rather than an opinion: *"Every catalogued relicensing between 2018 and 2024 followed the same legal pattern: a single corporate copyright holder, having aggregated contributor copyright via a CLA, exercised the right to change terms going forward. Distributed-copyright projects could not be moved the same way, because no single party had standing."* And the kicker — **HashiCorp went BUSL, IBM acquired it, and the licence stayed.** Acquisition entrenches the closure; it does not reverse it.

### [Why the licence is the weakest protection](survivability/index.md)

*The argument*

PostgreSQL is the control case — no company owns it, so no company can relicense it, and it is now the most-used database. OpenSolaris is the counter-case. The licence was not the problem; the copyright holder was.

### [The Change-of-Control Stress Test](survivability/stress-test.md)

*The tool*

Four legs — copyright, trademark, schema licence, named fork capacity — every one answerable from public artefacts, with no cooperation from the vendor. **Run it here, on any project, and keep the result.**

### [We run it on our own estate, in public](survivability/self-audit.md)

*The self-audit*

A test its author will not apply to themselves is marketing. The four legs run against the sgit estate, the verdict published, and what each leg would take to change — including the one that is not in any project's own gift.

## The positions, with their counter-cases attached

A page that only states one side reads as advocacy. Every argument here carries the strongest objection to it — and where the author's own position moved between one dated document and the next, both dates are published rather than tidied into one.

### [Sovereignty requires open source](views/sovereignty.md)

*Four steps*

You are one SLA away from losing access; the schemas matter as much as the code; and whichever government has jurisdiction over the company that controls the code controls everyone downstream. Necessary, but not sufficient — and the site stays careful about that.

### [Open core, or packaging?](views/open-core.md)

*Position moved*

18 June: *"There should be nothing proprietary."* 17 July: *"customers only have a subset of the code that exists in the main repo."* Five weeks apart, and the July document names the tension itself. Here is the one-question test that settles which one it is.

### [Somebody has to be the villagers](views/villagers.md)

*The market*

Maintaining the non-functional requirements as a market, and the ability to read and repair code somebody else wrote as an appreciating asset — published with both of its own counter-arguments, including the sharp one: a firm paid to maintain has no incentive to say the thing should be retired.

### [Agents, and the junior pipeline](agents/index.md)

*Two dates*

March: the density of learning per hour increases. July: the gains shifted work from juniors to seniors, at exactly the moment the maintenance need is growing. Both on the record, and what would settle it.

### [Three funding answers, and how they fit](funding/index.md)

*A position*

Labelling, a maintainer platform, sovereignty bounties. Three proposals for three different failures — information, transaction, substitution — compared for the first time, with a position on which is the precondition and which is the mechanism.

### [The position in full](views/index.md)

*All of it*

Technology is not the moat. Lock-in relocates to quality and certification. Lock-in degrades your own architecture. Open source frees you to cannibalise your own code. And the moat is a rate, not a wall: a competitor who forks today gets your position, not your velocity.

## Anyone can hold a position. Showing the licence file is different

This is the page that makes the rest credible: the licences actually in force across a shipping estate, and the reasoning behind each of them.

### [Apache-2.0 on the code, CC BY 4.0 on everything written](practice/index.md)

*Three licences*

Code is Apache-2.0, where the patent grant matters. Around 1,100 working documents and the published essays at `docs.diniscruz.ai` carry CC BY 4.0, where attribution carries provenance — settled on 6 September 2026, after the published-articles repository was found to say CC0. Two licences, three layers, and what each is for.

### [Why Apache-2.0 rather than MIT](practice/apache-vs-mit.md)

*The choice*

The entire estate rests on that choice. The patent grant, the defensive termination clause, the NOTICE file — and the cost, which is that Apache-2.0 is the heavier licence to comply with.

### [Publish the source next to the render](practice/publish-the-source.md)

*A mechanism*

Every page available as markdown at the same path with the extension swapped, and the links inside the markdown pointing at markdown — **which is how this site is built**. Plus the radical version: publish the evidence, the provenance, and every prompt.

## Agents are a primary audience of this site, so traversal is a build requirement

An agent-access report run against this estate found the failure precisely: *"many agents can only fetch URLs that a search engine has already returned to them… **A link listed inside a fetched document did not count as having been seen.** It can read the map and cannot walk it."* A site about open source that agents cannot traverse would fail in exactly the way its own author had already diagnosed — so the mitigation is built in.

| The rung | What this site ships | What it fixes |
|---|---|---|
| **The markdown twin** | **Every page**, same path, extension swapped — and links inside the markdown point at markdown | An agent never parses HTML, and never leaves the markdown surface once it arrives |
| **`llms.txt`** | **Self-sufficient** — it states the thesis rather than linking to it | A bare link list is the failure mode when links inside a document do not count as seen |
| **`llms-full.txt`** | **Every page in one file** | Removes link-following from the problem entirely |
| **Getting indexed** | **In progress** — the site is new | The rung that takes time rather than engineering. [On the build order →](roadmap/index.md) |

Read this page as [markdown](index.md), take the whole site as [llms-full.txt](llms-full.txt), or start from [llms.txt](llms.txt). The generator is [published with the rest of the build tooling](admin/index.md), because a site making this argument should show the mechanism.

## What's next

The build order is published with its open questions visible, because a position that hides what it has not yet settled is advertising. Three items lead.

### [An SBOM of the estate, and a licence audit in CI](roadmap/index.md#supply-chain)

*Next*

The site argues that companies should declare their supply chain. The estate's own declaration is the first item on the build order — roughly a day's work, and it converts the labelling argument from a proposal into a demonstration.

### [The agent-era licensing arguments](agents/index.md#unwritten)

*Four theses*

Licence compliance at machine speed, provenance of AI-generated code, training-data licensing, and what CC BY means for machine reuse. Each follows from material already published; each is named, and next to be written.

### [Seven questions still open, one decided](roadmap/index.md#open)

*Open questions*

Is the customer subset open core or packaging? Do agents help or harm sustainability? Is "open source AI" coherent without training data? Several are decisions for the project rather than research for the site — listed so the decisions can be seen being made.

### [What is built, and what is next, in order](roadmap/index.md)

*The build order*

Every section's state, seven items in sequence, and where this site stops and a sibling site in the network begins.

## Who is writing this

**Dinis Cruz** — founder of The Cyber Boardroom, MyFeeds.ai, RiskMandate.ai, VoiceDebrief.ai and the sgit.ai network (commercialised through sgraph.ai); former OWASP Board member and organiser of the OWASP Summits; creator of the O2 Platform and of the OSBot, MGraph-DB, Issues-FS and sgit families of open-source tools. This site is the strategy those companies run on, written from the experience of running it: everything they ship is open source, and so are their investor materials. The estate is run through [its own stress test](survivability/self-audit.md), result published.

[About the author, and interests declared →](about/index.md)[↗ LinkedIn](https://www.linkedin.com/in/diniscruz)[↗ Investor materials, published in the open](https://investor.myfeeds.ai/)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*

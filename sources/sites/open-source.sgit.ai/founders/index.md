<!-- generated from founders/index.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.2.2 · canonical: https://open-source.sgit.ai/founders/index.html*

> Field notes from a strategy session with a solo founder: what copying your code would actually cost an incumbent, four instincts and their counter-arguments, the explorer–villager–town-planner frame, eight steps in order, what to settle before you publish, and what a week of building in the open looks like when it is counted.

---

# Owning the code, or opening it

Every solo founder who ships something that works arrives at the same fear: **a bigger, better-resourced company takes the idea and there is nothing left.** These are the notes from a strategy session with an early-stage SaaS founder who had arrived at exactly that point — the walk-through that answers it, and what it changes about how you build.

> **The question on the table.***"A larger company in my market could take this code, drop it into their own system, hand it to their users, and I would have nothing left. A well-funded incumbent has already shipped something adjacent. What exactly stops them?"* That is where most solo founders start, and it is the right question. The answer is not a principle. It is a walk through what would actually happen.

## Part one · What copying you would actually cost them

The useful response is to walk the scenario through rather than argue the principle. An established company of a few hundred people, holding a full copy of the code, still has to do all of the following before a single user touches it. **Each step is a place the plan stalls.**

| # | What they have to do | What it costs them |
|---|---|---|
| **01** | **Decide to do it at all.** Somebody senior has to sponsor a project that is not currently on the roadmap. | stall risk |
| **02** | **Fund it.** Budget has to come off something else that is already committed. | + weeks |
| **03** | **Find someone to run it.** If they already had that person in-house, they would have built it themselves. The obvious hire is the person who already did. | + weeks |
| **04** | **Pull developers off other work.** Or recruit. Either way something else stops. | + months |
| **05** | **Deploy it into their estate.** Security review, integration with the intranet, internal marketing to get their own users onto it. | £5k–£20k+ |
| **06** | **Own it forever.** Once their users depend on it, they carry support, maintenance and every future feature, with nobody who understands the product. | permanent cost |

**Optimistic: three months to reach where you already are. Realistic: closer to a year.** Which turns the fear into the pitch:

> "You can take it. It will cost you that. Or you can pay me, and have it next week."

Price the licence below their internal build cost and the buy decision makes itself. And there is a second trap for them on top: **taking a competitor's code hands that competitor control of their roadmap.** Every fix and every new feature either comes from you, or gets maintained by them in perpetuity.

## Part two · Four things that surfaced

The cost argument answers the question that was asked. These are the four things underneath it that came up once the fear was priced — each an instinct that made sense once, and the counter-argument that reverses it now.

| The instinct | The counter-argument |
|---|---|
| **The shop-front reflex.** Owning the code feels like owning the shop. That instinct is normal for anyone who cannot build the thing themselves, and it made sense when competitors were slow. | The instinct now produces bad decisions. **Open-sourced work gets cloned far less often than founders fear**, because the hard part is execution and staying with it, not access to the source. |
| **"I can't open it, there are keys in there."** The stated reason for keeping the repo private is the wrong reason. The exposure already exists in a private repo. It is just unobserved, and it bites later. | Give yourself the problem so you are forced to solve it. **Public pressure produces the practice** of not putting secrets there in the first place, and catching them fast when they appear. |
| **Prototype code, product expectations.** What ships first is custom-build work carrying prehistoric experiments from the exploration phase. It gets asked to behave like a product it was never rebuilt to be. | Do a clean pass. **Extract what you want, rebuild it in a new repo — identical functionality and no new features.** This used to be prohibitively expensive. It is not now. |
| **A collaboration is not a commitment.** Early technical partnerships are easy to enter and easy to drift out of. A promising conversation is not a working relationship, and waiting to find out which one you have costs weeks you cannot get back. | Keep looking regardless. **Alignment matters more than raw skill**, because experienced developers can be set in their own way of working, and the right collaborator is usually already somewhere in your network. Talking to several people at once is prudence, not disloyalty. |

## Part three · Explorer, villager, town planner

Simon Wardley's evolution model is the spine of the technical argument. Each stage is a different job with different standards, and **the common mistake in AI-assisted building is treating all three as one.** The pattern itself belongs to [wardley-maps.sgit.ai](https://wardley-maps.sgit.ai); what matters here is the moment between the first two.

### Explorer

*Stage one*

Genesis and custom build. Try things, fail fast, keep what works. Engineering discipline is deliberately light — that is the point of the stage, not a failing of it.

### The handover

*The moment that matters*

Custom build passing to villagers. Clean rebuild, structure, tests, no secrets. **The bar goes up because other people are about to read it.**

### Villager → product

*Stage three*

Stable feature set, real SLAs, separate environments. Users start depending on it, so change slows deliberately.

This is the same frame that produces [the maintenance market this site argues for](../views/villagers.md): somebody has to be the villagers, and the founder's first job after the prototype works is to become one for their own code.

## Part four · The practical route, in order

Eight steps. The first four happen while the repo is still private and nothing is exposed; the fifth is the point of no return; the last three are habits that run alongside, starting this week.

### Do now, while the repo is private — nothing exposed yet

01

### Create a fresh GitHub repository from the web interface

Use a naming convention you can repeat, such as `project__component`. Set it private for the first version. **Select the licence at creation, not later.**

02

### Connect your coding agent to that repository

A terminal-based agent with repo access, not a chat window. Then point it at the existing project folder.

03

### Run the conversion pass

New session, one job: produce an open-source-ready version of the current code. **Same functionality, same behaviour, cleaned structure, no secrets, no dead experiments.**

04

### Hand the cleaned folder back to your build platform as a new project

This also opens the door to hosting elsewhere later. **No build platform should be a permanent dependency.**

### Only after licence and IP are settled — the point of no return

05

### Invite one trusted reviewer to the private repo

Reviewer first, then their team, then it goes public. **A good reviewer will refuse access to your live environment**: the point is to make you capable, not to make them a dependency.

### Running alongside, from this week — habits

06

### Start measuring profitability now

Small problems solved while they are small. **Unit economics before the user count grows.**

07

### Use a voice model to interview yourself

Two uses: a founder journal capturing what has actually been achieved, and a feedback method where beta users are interviewed by the model and send back the report.

08

### Publish the story as it happens

The decision, the fears, what gets learned. Marketing that carries the brand without being a sales pitch, because **at this stage the founder is the story.**

## Worth settling before you publish

> **The licence is a commercial decision, not a technical one.** A permissive licence is simple and frictionless, and it gives away any claim on what others build with your work. A copyleft licence with a contributor agreement and a separate commercial licence keeps the option of a revenue share, and obliges resellers to stay current. **Decide which you want before the repo exists, because the licence is chosen at creation.**[Why this estate chose Apache-2.0 →](../practice/apache-vs-mit.md)
>
> **Trade marks and IP advice come first.** Everything up to the clean rebuild is safe while the repo is private. Inviting the first outside reviewer is the point of no return — which is also why [the trademark is one of the two things that actually decides survivability](../survivability/index.md), and the licence file is not.
>
> **The cost argument has a limit.** It holds well against a large organisation with no product team, where every step is a place the plan stalls. It holds far less well against a funded competitor that already has the team, the budget and the market. **Slowness is the moat, so it only protects you from slow competitors.** Against a fast one, [the moat is your velocity](../views/index.md#rate-not-wall) — a competitor who forks today gets your position, not your rate.

## Part five · What your past self would have called success

Before the fear of being copied, there was a set of things that would have counted as winning. They are worth writing down, because they are all closer than the fear makes them feel.

1,000

site visits in the first months

1

first paying customer, converted

Shipped

live product with real users on it

100

paying users, target by year end

## Part six · What a week of this looks like, counted

The handover from prototype to product is invisible from the outside unless you count it. A week of this work produces almost no new features and a great deal of the following. **Publishing the count is itself the discipline**, because you cannot quietly skip a week when the row has to be filled in.

| Counted each week | What it is evidence of |
|---|---|
| **Releases tagged** | Versioned, dated, reversible. |
| **Untrue claims removed** | Site audited against the working product. |
| **Support channels live** | Where a user can reach a human. |

### Four habits that produce those numbers

### Audit the site against the product

*Habit*

Every claim that cannot be demonstrated comes down before the repo opens. *"Instantly"*, *"every time"* and *"your credits never expire"* are the usual casualties.

### Quote the cost as a ceiling

*Habit*

Show the price before the run, not after. A job can come in under the quote. It should never come in over it.

### Ask for keys at run time, store nothing

*Habit*

The data stays in the user's own environment. This is also the answer to every compliance question you will be asked later.

### Make the tests prove the claim

*Habit*

If the demo on your home page is not the real workflow, the build should fail rather than ship.

## The point of building in the open

> Be the new generation of artist — the one who controls the master, not the one who was successful and never saw the money.

Which is [the argument of this whole site](../views/index.md) at the scale of one founder: the code is not the moat, the execution is; opening it costs you far less than the fear says and buys you a pitch, a discipline and a story; and what you keep — the trademark, the velocity, the relationship with the people who pay — is what was ever worth keeping.

> **Provenance.** Prepared from a recording of the strategy call, transcribed and edited in Audio Genius, and first published as an infographic. Released under a Creative Commons CC BY licence. **Attribution: Dinis Cruz and Kate Curtis-Evans.** Details of the founder's product are theirs to tell; the reasoning is published here because it applies to every solo founder asking the question at the top of this page.

## Where to go next

### [Run the stress test on a vendor](../survivability/stress-test.md)

*The tool*

Before you depend on somebody else's open source: four questions, all answerable from public artefacts, about who could change the terms and what would stop them.

### [Why Apache-2.0 rather than MIT](../practice/apache-vs-mit.md)

*The licence*

The patent grant, the defensive termination clause, the NOTICE file — and the cost, which is that Apache-2.0 is the heavier licence to comply with.

### [Publish the source next to the render](../practice/publish-the-source.md)

*The mechanism*

Step eight, done properly: every page of this site is also its own markdown, so what is published is the source and not only the rendering of it.

[← Front page](../index.md)[The position →](../views/index.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*

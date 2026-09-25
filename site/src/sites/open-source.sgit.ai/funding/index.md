<!-- generated from funding/index.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.2.2 · canonical: https://open-source.sgit.ai/funding/index.html*

> Market forces and supply-chain labelling, a maintainer platform, and sovereignty bounties that fund the exit rather than the supply. None was costed, none piloted, and none compared against the others — until here.

---

# Three funding proposals, and a position

The author has proposed three answers to the sustainability question at different times, while being clear that *"the sustainable funding question is unsettled."* This page puts them side by side for the first time, says what each one actually fixes, and takes a position on how they fit together.

> **The framing that makes the whole page work** comes from [the site's central argument](../views/index.md): if open source is a gift, underfunding is a moral failure and the remedy is persuasion. If it is [a strategy whose costs someone always bears](../views/index.md#not-free), underfunding is an **externality** — and externalities have never once been corrected by asking nicely.

## 1. Market forces and supply-chain labelling

> "**Charity will not fix this. 'It is the right thing to do' will not fix this. The only thing that will fix this is market forces.**"

The mechanism: declare your supply chain, calculate your value contribution, pay the projects you depend on proportionally — *"Not as charity. As a cost of doing business. The same way you pay for cloud infrastructure, for office space, for salaries"* — and **publish a rating**.

With the best image in the argument:

> "Just like a restaurant health rating on the door: you can still choose to eat at the restaurant with a bad rating. **But you know.**"

And the counterintuitive claim that gives it commercial legs: *"paying for open source is cheaper than not paying… They spend more money internally maintaining open source software than they would have spent supporting the project directly."*

| What it fixes | What it does not |
|---|---|
| The **information problem**. Nobody currently knows which companies free-ride, so there is no reputational cost to doing it. A published rating creates one, and reputational costs are the only lever that works on organisations too large to shame individually. | It is **uncosted and unpiloted**, and "calculate your value contribution" is doing enormous unexamined work — that calculation is the entire hard problem, and no method is proposed. Ratings systems also get gamed, captured, or quietly ignored. |

## 2. A maintainer platform — the relationship is missing because the platform is

This one relocates the problem entirely. The claim is that the obstacle is not licensing and not goodwill but **missing infrastructure**:

> "A solo maintainer publishing a Python package today has no realistic path to capture value from production users. **The relationship is missing because the platform is missing.**"

With a boundary sharp enough to build on:

> "the commercial line is where the package touches the target app." / "A consultancy can study the package. **The maintainer *is* the package.**"

And a principle it refuses to trade away: *"It does not pull docs behind paywalls… That generosity is a core principle of open source and it stays."*

| What it fixes | What it does not |
|---|---|
| The **transaction problem**, and there is strong evidence this is the right diagnosis. [Let's Encrypt did not succeed because certificates got cheaper — it succeeded because the transaction disappeared.](../history/stories.md#letsencrypt) Build the mechanism and behaviour changes without anyone being persuaded of anything. | Platforms need **critical mass on both sides**, and several have tried. It also does nothing for the projects most at risk — the ones with no commercial users to transact with, which are frequently the most load-bearing. |

## 3. Sovereignty bounties — fund the exit, not the supply

The strongest single idea of the three, and genuinely unclaimed elsewhere.

> "**Every one of those programmes funds the supply side**… None of them funds the **substitution side**… on present evidence nobody is funding it."

Every public open-source funding programme pays people to *build and maintain* open-source software. None pays anyone to build **documented, working migration paths off proprietary platforms** — which is the thing an organisation actually needs in order to have the sovereignty that [the argument says open source makes possible](../views/sovereignty.md). Having the source is a precondition. **Having a walked path is the capability**, and nobody is buying it.

Two second-order ideas make it more than a grant scheme:

**Bounty size as a published lock-in metric.***"it's then market economics, like the more complicated is the bigger the bounty."* If the cost of exiting a platform is *published*, then lock-in stops being a vague complaint and becomes a **measurable, comparable property of a vendor** — a number in a procurement spreadsheet.

**Vendor-sponsored proof of no lock-in.** A vendor funding *"a documented, working exit path from its own product acquires a strong and checkable claim that it does not hold its customers by lock-in."* That is a genuinely novel commercial move: the only credible way to prove you are not holding someone captive is to pay for the door.

| What it fixes | What it does not |
|---|---|
| The **substitution problem**, which nothing else addresses and which is the binding constraint on every sovereignty argument ever made. It also converts a political goal into a procurement line item, which is where things actually get funded. | **Nobody has piloted it, no bounty has been sized, and the moral hazard is unaddressed** — a vendor sponsoring its own exit path controls how good that path is. An exit path that technically works and is miserable to walk is worse than none, because it can be pointed at. |

## The three, side by side

|  | Labelling | Platform | Sovereignty bounties |
|---|---|---|---|
| **Failure it addresses** | Information — nobody knows who free-rides | Transaction — there is no way to pay | Substitution — the exit is theoretical |
| **Who pays** | Consuming companies, under reputational pressure | Production users, per transaction | States, and vendors proving a point |
| **Who it reaches** | Projects with identifiable corporate dependants | Projects with commercial users | **Nobody currently** — it is not the maintainers, it is the migrators |
| **Helps cURL?** | **Yes** — 30bn installations is a very visible rating | **Partly** — no natural production-user transaction | **No** — different problem entirely |
| **Piloted?** | **No** | **No** | **No** |

## The position

**They are not competing answers, and presenting them as three options was the error.** They address three different failures, and the reason the sustainability problem has resisted a single solution is that it is not one problem.

- **Labelling is the precondition.** Nothing else can be priced while consumption is invisible. It is also the one whose hard part — the value-contribution calculation — is entirely unsolved, and that should be the next piece of work rather than a fourth proposal.
- **The platform is the mechanism**, and the Let's Encrypt precedent is the strongest evidence on this page that mechanisms beat exhortation.
- **Sovereignty bounties are the most original and the least connected to the other two.** They do not fund maintenance at all — they fund *migration*. Filing them under "open-source funding" is what caused three answers to look like competitors.

> **And cURL settles part of the argument empirically — after all three were written.** Thirty billion installations. A bounty programme that paid over $90,000 across 81 genuine reports since 2019. **Shut down on 31 January 2026** because the cost of processing AI-generated submissions exceeded the value of the programme. **Charity did not fix it. No platform existed to fix it. An externality nobody was paying for destroyed the mechanism.** That is the strongest evidence in the world for the market-forces argument, and it arrived after the argument was made. [The full story →](curl.md)

[← Agents](../agents/index.md)[cURL →](curl.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*

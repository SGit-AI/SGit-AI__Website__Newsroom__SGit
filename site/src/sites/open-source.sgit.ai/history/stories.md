<!-- generated from history/stories.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.2.2 · canonical: https://open-source.sgit.ai/history/stories.html*

> Linux, Let's Encrypt, SQLite, PostgreSQL, cURL and Blender — six, not fourteen, each chosen because it carries an argument made elsewhere on this site. Plus Kubernetes and VS Code, which complicate the picture honestly.

---

# Six success stories

Fourteen were researched. Publishing all fourteen at equal weight produces a listicle, so these are the six that **carry an argument made elsewhere on this site** — including one that inverts nearly every assumption the rest of the site runs on, and one that is here because it is currently failing.

## Linux — copyleft turned competitors into co-maintainers

**What it proves:** that a licence can restructure an industry's incentives. Under GPLv2 no vendor could privately fork the kernel and out-develop the commons, because improvements shipped to customers had to come back. Upstreaming stopped being generosity and became **the cheaper option** — which is the whole thesis of this site, achieved by legal design rather than persuasion.

**The number:** kernel 6.18 (30 November 2025) was built by **2,134 developers — the most in its history** — including 333 first-time contributors across 13,710 commits. The largest corporate contributors were Intel at 10.4%, Google at 7.9%, Red Hat at 6.3%. **No single party is close to controlling it**, which is [the survivability property](../survivability/index.md) visible as a statistic.

## Let's Encrypt — and the mechanism was not price

**What it proves:** the most measurable civilisational impact in the list, and the reason it worked is the part most often mis-stated. Certificates had been cheap before. **Free was necessary; automated was sufficient.** What Let's Encrypt removed was not the cost — it was **the transaction**: the purchase, the paperwork, the annual renewal somebody had to remember, the outage when they did not.

**The numbers:** HTTPS page loads went from **under 30% globally in 2015 to roughly 80% globally and around 95% in the US**. Issuance went from one million certificates in March 2016 to **around ten million per day** by September 2025.

> **Why this matters beyond TLS.** It is the strongest available evidence that [the maintainer-platform argument](../funding/index.md#platform) is about infrastructure rather than money: the relationship was missing because the *mechanism* was missing. Build the mechanism and behaviour changes at civilisational scale, without anyone being persuaded of anything.

## SQLite — the case that inverts almost everything

**What it proves:** that almost every rule on this site has a successful exception, and intellectual honesty requires publishing it.

- It is **public domain**, not open-source-licensed. There is no licence to reason about.
- It is explicitly **not open-contribution** — it refuses patches from anyone who has not signed a public-domain dedication affidavit. ["Given enough eyeballs"](index.md#eyeballs) is not merely unused here; it is structurally declined.
- The original affidavits are kept **in a firesafe.**

**The number:** an estimated **one trillion databases in active use** — plausibly the second most-deployed software library in the world after zlib.

By the standards of most open-source advocacy, SQLite does everything wrong: closed contribution, centralised control, no community governance. It is also one of the most successful and most trusted pieces of software ever written, and its reliability comes from an **extraordinarily rigorous test suite maintained by a tiny team** — not from openness to contribution. **The lesson this site takes: the mechanism that produces quality is being paid to care, and the licence is not the mechanism.**

## PostgreSQL — the control case for the whole relicensing wave

**What it proves:**[the survivability argument](../survivability/index.md), demonstrated rather than asserted. **No company owns PostgreSQL, so no company could relicense it.** It went through the entire 2018–2024 wave untouched — not because its licence is stronger than MongoDB's or Redis's was, but because **there is no party with standing to move it**.

**The number:****55.6% of developers** use it — the most-used database in the Stack Overflow 2025 survey (n=49,063).

It is the single cleanest piece of evidence on this site: the projects that could be relicensed were relicensed, and the one that structurally could not be, was not. That is the argument, and PostgreSQL is the experiment.

## cURL — here because it is currently failing

**What it proves:**[that open source is not free and somebody is always paying](../views/index.md#not-free), as a measured fact with a date and a casualty.

~30 billion installations. One project lead since 1998. **Seven volunteers on the security team.** And a bug bounty programme shut down on 31 January 2026 because the cost of processing AI-generated submissions exceeded what the programme was worth.

It is the most important open-source story of 2025–26 and it belongs to this site more than any other, so it has its own page. [Read it →](../funding/curl.md)

## Blender — a community that bought its own freedom

**What it proves:** the one case where the romantic version of the story is simply, literally true — and it should be published for exactly that reason, because a site that only publishes corrections is doing something other than history.

In 2002, with the company behind it bankrupt, the community raised **€100,000 in seven weeks** (July–September) to buy the source code and release it. **They bought their own software's freedom, in cash.**

**The number that closes it:***Flow* (2024), made entirely in Blender, won the Academy Award for Best Animated Feature.

Note what is *not* being claimed. This is not evidence that crowdfunding solves open-source sustainability — it is one rescue, once, of a tool with an unusually devoted user base, twenty-four years ago. It is evidence that the ceiling is higher than the cynical account allows, which is a different and more modest claim.

## Two more, because they complicate the picture

### Kubernetes — commoditising the layer below your business

Google released the orchestration layer and gave it to a foundation. The strategic logic is exact: **commoditise the layer beneath the thing you sell**, so that the layer beneath stops being a place a competitor can build a moat, and the workloads flow upward to where you compete. It is the clearest strategic use of open source in the industry's history, it worked, and it is a direct illustration of [the technology-is-not-the-moat argument](../views/index.md#not-the-moat) — executed by a company with the resources to be right about it.

### VS Code — open core, executed so well it is invisible

An MIT-licensed core, a proprietary shipped binary, and a marketplace whose terms restrict use to that binary. **A textbook open-core structure, executed so smoothly that most of its very large user base does not know it is running proprietary software.**

That is the strongest available case both *for* and *against* open core, which is why it is here rather than on the [open core page](../views/open-core.md) as a settled example. For: an enormous amount of genuinely valuable software got built and given away. Against: the boundary is invisible to the people standing on the wrong side of it, and invisibility is precisely what makes a boundary easy to move.

## And the failure that belongs here

A history of open source with no failures in it is marketing. **OpenSolaris** is on this site, in [the survivability section](../survivability/index.md#cases), where it does the most work: open-sourced under a licence deliberately chosen to be GPL-incompatible, under governance Sun retained, then killed by Oracle after the acquisition. **The licence was not the problem; the copyright holder was.** illumos survives as the fork — which is also the point, because a named party existed.

[← The timeline](timeline.md)[The numbers →](numbers.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*

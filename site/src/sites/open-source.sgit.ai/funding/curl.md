<!-- generated from funding/curl.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.2.2 · canonical: https://open-source.sgit.ai/funding/curl.html*

> On 31 January 2026 curl closed its bug bounty because roughly 20% of 2025 submissions were AI-generated slop against roughly 5% genuine. An externality nobody was paying for destroyed a funding mechanism, with a date and a named casualty.

---

# cURL: thirty billion installations, seven volunteers, and a bounty that closed

This story belongs to this site more than any other, because it is **three of its arguments colliding in one project** — with a date, a measured cost, and a named casualty. It is the most important open-source story of 2025–26, and it arrived *after* the arguments it settles had already been written.

## The facts

|  |  |
|---|---|
| **Reach** | **~30 billion installations.** In effectively every operating system, phone, car, television and appliance that speaks HTTP. |
| **People** | One project lead, **Daniel Stenberg, since 1998**. **Seven volunteers on the security team.** |
| **The bounty, 2019–2026** | **81 genuine reports, over $90,000 paid.** By any measure a well-run programme that found real things. |
| **2025 submissions** | **~20% AI-generated slop. ~5% genuine vulnerabilities.** Each report consuming three or four people for thirty minutes to three hours. |
| **The decision** | Announced **22 January 2026**: the HackerOne bounty would close on **31 January 2026**, moving to unpaid reporting via GitHub. |
| **The reason, in the project's words** | *"The main goal with shutting down the bounty is to **remove the incentive for people to submit crap**."* |

Read the ratio again, because it is the whole story: **four times as much fabricated work as real work**, arriving at a seven-person volunteer team, each item requiring several people and up to three hours to triage — because a plausible-looking security report cannot be dismissed without reading it. **That is the attack.** Nobody intended it as one. It worked anyway.

## Why it is this site's page

### It is "open source is not free" as a measured fact

[The argument](../views/index.md#not-free) is that somebody is always paying — usually in unaccounted time rather than money. Here the payment is visible and it has a denominator: **thirty billion installations, seven volunteers.** A number that large next to a number that small is not a curiosity; it is the funding failure stated as a ratio, and it existed long before AI arrived.

### It is an externality destroying a mechanism, in public

Nobody submitting an AI-generated report intended to shut down a bug bounty. Each individual submission was, from the submitter's point of view, nearly free — write a prompt, paste the output, possibly collect money. **The cost landed entirely on someone else**, in units of volunteer attention, and it accumulated until the mechanism could not bear it.

That is the textbook shape of an externality, and it is why the response was structural rather than moral. The project did not appeal to people's better nature. **It removed the incentive** — which is the only thing that has ever worked on an externality, and it is precisely [the market-forces argument](index.md#labelling) in action.

### It is the strongest available evidence that charity does not fix this

> "**Charity will not fix this. 'It is the right thing to do' will not fix this. The only thing that will fix this is market forces.**"

That was written in March 2026 as an argument. By January 2026 it had a worked example: a project with more goodwill than almost any other in the world, more visible need, and a maintainer with an unusually large platform for asking — and none of it was sufficient. **Goodwill was never the scarce resource. Attention was, and nobody was paying for it.**

### And it confirms a prediction the author made before the event

[The author wrote down the AI-slop mechanism](../agents/index.md#slop) — *"low-quality, auto-generated pull requests that flood maintainer queues without adding value, increasing the burden on already-stretched maintainers… AI is, for now, **adding maintenance load** rather than only creating maintainable work"* — before curl's announcement. A prediction that names the mechanism and is then confirmed with a date is worth considerably more than a retrospective explanation, and it is the reason [the agents page refuses to claim agents will fix sustainability](../agents/index.md).

## What this story does not prove

A page that only presses its advantage is advocacy, so:

- **It is one project.** A well-known one with an unusually exposed bounty programme, which is exactly the profile that attracts volume submissions. It is not a survey.
- **The bounty closed; the project did not.** curl continues, security reports continue via GitHub, and the maintainer has been explicit that this is a change of mechanism rather than a retreat. Reporting it as "curl is collapsing" would be false.
- **The percentages are the project's own figures**, first-party and self-measured. That makes them the best available evidence and not an independent audit. They are stated here as what they are.
- **"AI slop" is a claim about submission quality, not about the tools.** The failure is a system with no cost on the submitting side, and it would have arrived eventually with any technology that made plausible text cheap.

## What would actually have helped

Testing the three proposals against a real case, which is the only way to find out whether they are proposals or wishes:

| Proposal | Would it have helped curl? |
|---|---|
| [**Labelling and proportional payment**](index.md#labelling) | **Yes, and more than anything else.** Thirty billion installations is the most legible dependency claim imaginable — every large technology company could be shown, precisely, to depend on it. A published rating would make free-riding on curl specifically embarrassing. **It would have funded triage capacity**, which is exactly what ran out. |
| [**A maintainer platform**](index.md#platform) | **Partly.** curl's users are mostly not in a transactional relationship with it — it arrives bundled inside something else. The platform argument works best where a production user knowingly depends on a package; curl's dependants frequently do not know they are dependants. |
| [**Sovereignty bounties**](index.md#bounties) | **No.** Different problem entirely — they fund migration off proprietary platforms, and curl is the thing you migrate *to*. Worth stating plainly, because it is the clearest evidence that the three proposals were never competing answers to one question. |

> **The uncomfortable conclusion.** The mechanism that failed here was **a volunteer security team's attention**, and none of the three proposals is aimed at it directly. Labelling funds projects; platforms fund maintainers; bounties fund migrations. **Nothing funds triage** — the unglamorous, high-skill, entirely thankless work of reading reports about software you did not break, most of which are wrong. That is a fourth gap, it is where this failure actually happened, and this page is the first place on this site to name it.

[← Funding](index.md)[OWASP & the summits →](../owasp/index.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*

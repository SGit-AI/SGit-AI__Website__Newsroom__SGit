---
title: abp.sgit.ai, the site that writes down what an agent can do and what it was asked to do
date: 2026-09-24
desk: Journalist
standfirst: abp.sgit.ai defines the Agent Behaviour Policy, a document that sets an agent's grant beside its mandate and records what stands in the way, with no score. It went from a promoted data pack to twenty releases in twelve days, and riskmandate.ai builds on it.
section: feature
sources:
  - https://abp.sgit.ai/llms.txt
  - https://abp.sgit.ai/index.md
  - https://abp.sgit.ai/what-is-an-abp/index.md
  - https://abp.sgit.ai/versions/index.md
  - https://abp.sgit.ai/versions/v0.1.0/index.md
  - https://abp.sgit.ai/versions/v0.2.0/index.md
  - https://abp.sgit.ai/versions/v0.4.4/index.md
  - https://abp.sgit.ai/articles/index.md
  - https://abp.sgit.ai/articles/an-ontology-that-already-existed/index.md
  - https://abp.sgit.ai/articles/a-rule-corrected-nine-hours-later/index.md
  - https://riskmandate.ai/abp.md
  - https://riskmandate.ai/agent-behaviour-policy.md
  - https://riskmandate.ai/abp-reviewed.md
  - https://riskmandate.ai/lab-abp-requests.md
  - https://riskmandate.ai/llms.txt
  - src:sites/manifest.json
reviewed_by:
reviewed_on:
---

abp.sgit.ai is the site in the sgit network that defines one document, the Agent Behaviour Policy. Its own one-line summary is: what your agent can do, what you authorised it to do, the gap between them, and what actually stands in the way ([llms.txt](https://abp.sgit.ai/llms.txt)). This piece covers what the document is, how the site grew, what it publishes, and how riskmandate.ai uses it.

## What an ABP is

The foundation document, dated 11 September 2026, defines an Agent Behaviour Policy as a written description, for one agent in one deployment, of four things ([foundation document](https://abp.sgit.ai/what-is-an-abp/index.md)). The **grant** is everything the agent can do. The **mandate** is what it was authorised and expected to do. The **delta** is the difference. The **barrier** is what stands between the agent and each capability ([foundation document](https://abp.sgit.ai/what-is-an-abp/index.md)).

The site's short form of the idea is its heading: "You know what you asked for. You do not know what it can do." ([home page](https://abp.sgit.ai/index.md)). The mandate is elicited from the person who deployed the agent, the grant is measured from the deployment, and the barrier is recorded per capability ([foundation document](https://abp.sgit.ai/what-is-an-abp/index.md)).

There are four kinds of barrier: nothing, a rule somebody wrote down, a setting the agent's own account could change, and a boundary enforced above it that it cannot reach ([foundation document](https://abp.sgit.ai/what-is-an-abp/index.md)). The document's rule is that "Only the fourth kind bounds anything." ([foundation document](https://abp.sgit.ai/what-is-an-abp/index.md)). Its worked example is a coding agent profiled twice, with confirmations on and off: the grant, mandate and delta stay the same, and the barrier on every capability in the delta moves one row ([foundation document](https://abp.sgit.ai/what-is-an-abp/index.md)).

The ABP carries no score. The foundation document puts it as "A policy cannot be dangerous. A deployment can." ([foundation document](https://abp.sgit.ai/what-is-an-abp/index.md)), and the site says there is no score, rating or risk level anywhere on it, including in the data ([llms.txt](https://abp.sgit.ai/llms.txt)).

## How it grew

The version table lists 20 releases, from v0.1.0 on 11 September 2026 to v0.11.0 on 22 September 2026 (counted from [the versions page](https://abp.sgit.ai/versions/index.md)).

**v0.1.0 promoted data that already existed.** The capability vocabulary had been published as the data pack a game reads, so the first release gave it a stable address instead of writing a second one, and derived five worked ABPs from it ([v0.1.0 record](https://abp.sgit.ai/versions/v0.1.0/index.md)). That vocabulary is 23 capability primitives in verb.object.reach form, four barriers, three undo classes, seven evidence tiers, nine deployment shapes and eight starting mandates ([v0.1.0 record](https://abp.sgit.ai/versions/v0.1.0/index.md)). The article for that release says nothing was renamed ([v0.1.0 article](https://abp.sgit.ai/articles/an-ontology-that-already-existed/index.md)).

**v0.2.0 corrected the site's own rule on the same day.** The foundation document said the delta is computed and never stored; the correction is that the delta is derived and never authored, stored with the versions of its inputs and recomputed by the gate ([v0.2.0 record](https://abp.sgit.ai/versions/v0.2.0/index.md)). The corrected passages were not rewritten: each stands as published, with its correction rendered above it ([foundation document](https://abp.sgit.ai/what-is-an-abp/index.md)). The release gate that used to refuse any stored delta now recomputes every stored delta from its pinned inputs ([v0.2.0 article](https://abp.sgit.ai/articles/a-rule-corrected-nine-hours-later/index.md)).

**v0.3.0 to v0.4.3 turned words into nodes.** v0.3.0 gave read, file and project their own addresses, and a node type became a formula instead of a label; v0.4.0 mapped the ABP onto Fractal Semantic Graphs, and the releases up to v0.4.3 made that map into data the build reads ([versions](https://abp.sgit.ai/versions/index.md)).

**v0.4.4 took seven shapes from riskmandate.ai.** They were fetched as bytes on 20 September 2026, held unchanged with a hash per file, and promoted without renaming anything ([v0.4.4 record](https://abp.sgit.ai/versions/v0.4.4/index.md)). The record says the intake path "is the same for anybody" ([v0.4.4 record](https://abp.sgit.ai/versions/v0.4.4/index.md)).

**v0.5.0 onwards added one article per release,** with screenshots taken from each release's tag ([versions](https://abp.sgit.ai/versions/index.md)). Then came three walkthroughs, for a mailbox (v0.6.0), for cost (v0.8.0) and for an assistant on your own machine (v0.10.0), and three cases (v0.7.0 and v0.9.0) ([versions](https://abp.sgit.ai/versions/index.md)). v0.11.0 added the Gmail connector as measured by the agent holding it ([llms.txt](https://abp.sgit.ai/llms.txt)).

## What it publishes

The snapshot holds 315 files for abp.sgit.ai: 182 markdown, 131 JSON and 2 text (counted from [the manifest](src:sites/manifest.json)). Every page has a markdown twin, and the whole site is also served as one file ([llms.txt](https://abp.sgit.ai/llms.txt)). The main parts are:

- **The model:** the four objects, the [capability grammar](https://abp.sgit.ai/model/capabilities/index.md) of 23 primitives, and [the barrier](https://abp.sgit.ai/model/barriers/index.md) ([llms.txt](https://abp.sgit.ai/llms.txt)).
- **Walkthroughs** a reader runs against their own assistant, each in four steps: [the mailbox](https://abp.sgit.ai/gmail/index.md) with thirteen prompts, [cost](https://abp.sgit.ai/cost/index.md) with twelve, and [the desktop](https://abp.sgit.ai/desktop/index.md) with ten ([llms.txt](https://abp.sgit.ai/llms.txt)). The fourth step of the mailbox walkthrough says the document written in step three "is an expectation rather than a control" ([llms.txt](https://abp.sgit.ai/llms.txt)).
- **Cases:** [one person's estate of deployments](https://abp.sgit.ai/cases/index.md), each an ABP "elicited from them rather than authored" ([llms.txt](https://abp.sgit.ai/llms.txt)). One case is the session that built the site's releases v0.4.0 to v0.8.1 ([llms.txt](https://abp.sgit.ai/llms.txt)).
- **Articles:** [one per release](https://abp.sgit.ai/articles/index.md), 14 in the snapshot (counted from the folders under `articles/`).
- **Docs:** the foundation document, the briefs behind it and the build pack, each rendered with a link to its source bytes ([llms.txt](https://abp.sgit.ai/llms.txt)).

## How riskmandate.ai uses ABPs

riskmandate.ai describes itself as the insurability layer for agentic AI ([riskmandate.ai llms.txt](https://riskmandate.ai/llms.txt)). Its [ABP page](https://riskmandate.ai/abp.md) restates the same four objects and four barriers, links to abp.sgit.ai's barrier page and examples, and says the capability vocabulary is "pinned at abp.sgit.ai and shared by every vault" ([riskmandate.ai, the ABP](https://riskmandate.ai/abp.md)).

It keeps the no-score rule and places the score elsewhere: "The Insurability Index scores the deployment, never the behaviour policy." ([riskmandate.ai, the ABP](https://riskmandate.ai/abp.md)).

**What it publishes.** A [directory of template vaults](https://riskmandate.ai/agent-behaviour-policy.md), one per target application, each read live in the browser with a published read key ([directory](https://riskmandate.ai/agent-behaviour-policy.md)). The snapshot holds 16 of these vault pages (counted from the `abp-vault-*.md` files in [the manifest](src:sites/manifest.json)).

**What it sells.** The [reviewed level](https://riskmandate.ai/abp-reviewed.md) is priced at £1,500: two half-hour sessions, a behaviour policy built from the interview, and a sign-off file with a named professional's name and the date ([reviewed level](https://riskmandate.ai/abp-reviewed.md)).

**What it asked for.** On 12 September riskmandate.ai published [three requests](https://riskmandate.ai/lab-abp-requests.md) against abp.sgit.ai: a `material` property, four connector shapes, and provenance conventions ([Lab 03](https://riskmandate.ai/lab-abp-requests.md)). abp.sgit.ai's v0.4.4 answered the second of them, the one riskmandate.ai had marked as unblocking a product ([v0.4.4 record](https://abp.sgit.ai/versions/v0.4.4/index.md)).

**What is still drawn, not built.** riskmandate.ai's ABP page says of its graph model: "Half of this is running today and half is drawn" ([riskmandate.ai, the ABP](https://riskmandate.ai/abp.md)). Its Lab 02, the flow for buying a behaviour policy, says "None of it is built yet." ([riskmandate.ai llms.txt](https://riskmandate.ai/llms.txt)).

## The line between the two sites

The two sites divide the work. abp.sgit.ai owns the model and the data. Its v0.4.4 record says it does not import riskmandate.ai's vaults for its own shapes, "because they pin this site and importing them would be a loop" ([v0.4.4 record](https://abp.sgit.ai/versions/v0.4.4/index.md)). riskmandate.ai calls abp.sgit.ai "a separate site with a separate maintainer" and says "We render against it." ([Lab 03](https://riskmandate.ai/lab-abp-requests.md)).

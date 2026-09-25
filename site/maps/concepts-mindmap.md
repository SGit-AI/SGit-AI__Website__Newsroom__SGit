---
title: The network's recurring concepts, by theme
date: 2026-09-24
desk: Cartographer
standfirst: A mindmap of the concepts that recur across the sgit network, grouped into seven themes, and under each concept the sites whose pages use it. The concepts are the Librarian's; which sites use each is computed by the build from the snapshot, not typed.
sources:
  - https://sgit.ai/docs/credentials.md
  - https://sgit.ai/api/append-lanes.md
  - https://riskmandate.ai/abp.md
  - https://riskmandate.ai/grant-gap.md
  - https://abp.sgit.ai/model/undo/index.md
  - https://sgit.ai/docs/briefs/index.md
  - https://wardley-maps.sgit.ai/llms.txt
reviewed_by:
reviewed_on:
---

The Librarian keeps a list of concepts that recur across the network, each with a definition, the page where it is defined, and the terms that signal it (`data/concepts.json`). The build searches every snapshotted page for those terms and lists, per concept, the pages and sites that use it: that list is on [the concepts page](nr:concepts), with every page linked. These mindmaps draw that list.

Two parts of this map are the Cartographer's and can be argued with. **The seven themes** are a grouping made for this map: no source groups the concepts this way. **The site lists** are what the build found on 25 September 2026: a site is under a concept when at least one of its snapshotted pages matches the concept's terms. A mention counts the same as a definition, so a site on a leaf uses the word; it does not necessarily build the thing. The concept pages give the counts, which change with every build, so the maps do not repeat them.

Site names ending in `.sgit.ai` are shortened: `abp` is abp.sgit.ai, `llms` is llms.sgit.ai, and so on. `sgit.ai` and `riskmandate.ai` keep their full names.

## The seven themes

```mermaid
mindmap
  root((Recurring concepts))
    Keys and trust
      [Read keys]
      [Client-side encryption]
      [PKI]
      [Vault key management]
    Vaults at work
      [Vault apps]
      [Append lanes]
      [Telemetry]
      [Twins]
      [Fractal semantic graphs]
      [Performance and cost]
    Agent permissions
      [Agent Behaviour Policy]
      [Grants and mandates]
      [Blast radius]
      [Undo classes]
    Risk and insurance
      [Risk acceptance]
      [Acceptance intervals]
      [Licence to operate]
      [Insurability]
      [Security audits]
    Standards and method
      [EU AI Act]
      [GDPR]
      [Wardley maps]
      [Open source]
    Working in public
      [Briefs]
      [Interview pages]
      [Lessons learned]
      [Em-dashes and style]
      [Synthetic users]
      [Provenance]
      [Frozen, hashed sources]
    The business
      [Business plans]
      [Partnerships]
      [Pricing ladders]
      [Startups]
      [Brand assets]
```

### Keys and trust

```mermaid
mindmap
  root((Keys and trust))
    [Read keys]
      abp
      elevenlabs.providers
      games
      graphs
      llms
      nhi
      open-source
      riskmandate.ai
      risks
      sgit.ai
      standards
      store
      ungovr.providers
      wardley-maps
      what-can-it-do.games
    [Client-side encryption]
      abp
      nhi
      open-source
      riskmandate.ai
      sg-sentinel
      sgit.ai
      store
      subscriptions
      teams
      what-can-it-do.games
    [PKI]
      games
      llms
      nfrs
      nhi
      open-source
      pki
      riskmandate.ai
      sgit.ai
      twins
      wardley-maps
    [Vault key management]
      sgit.ai
```

### Vaults at work

```mermaid
mindmap
  root((Vaults at work))
    [Vault apps]
      abp
      elevenlabs.providers
      games
      llms
      pki
      providers
      riskmandate.ai
      risks
      sgit.ai
      skills
      store
      ungovr.providers
    [Append lanes]
      abp
      games
      pki
      riskmandate.ai
      sgit.ai
      what-can-it-do.games
    [Telemetry]
      abp
      games
      nhi
      open-source
      pki
      riskmandate.ai
      sgit.ai
      what-can-it-do.games
    [Twins]
      abp
      nfrs
      pki
      riskmandate.ai
      sgit.ai
      twins
    [Fractal semantic graphs]
      abp
      graphs
      sg-sentinel
      sgit.ai
    [Performance and cost]
      sgit.ai
```

### Agent permissions

```mermaid
mindmap
  root((Agent permissions))
    [Agent Behaviour Policy]
      abp
      riskmandate.ai
      sgit.ai
      store
    [Grants and mandates]
      abp
      elevenlabs.providers
      games
      pki
      riskmandate.ai
      sgit.ai
      store
      ungovr.providers
      what-can-it-do.games
    [Blast radius]
      abp
      elevenlabs.providers
      graphs
      llms
      nhi
      pki
      providers
      riskmandate.ai
      risks
      sgit.ai
      ungovr.providers
    [Undo classes]
      abp
      elevenlabs.providers
      open-source
      pki
      providers
      riskmandate.ai
      risks
      sgit.ai
      ungovr.providers
      what-can-it-do.games
```

### Risk and insurance

```mermaid
mindmap
  root((Risk and insurance))
    [Risk acceptance]
      abp
      games
      graphs
      pki
      riskmandate.ai
      risks
      sgit.ai
      what-can-it-do.games
    [Acceptance intervals]
      riskmandate.ai
      risks
      sgit.ai
    [Licence to operate]
      abp
      games
      graphs
      riskmandate.ai
      sgit.ai
      store
      ungovr.providers
      what-can-it-do.games
    [Insurability]
      abp
      riskmandate.ai
      sgit.ai
      ungovr.providers
      what-can-it-do.games
    [Security audits]
      abp
      open-source
      riskmandate.ai
      sgit.ai
      skills
      standards
      store
      teams
      threat-modeling
      what-can-it-do.games
```

### Standards and method

```mermaid
mindmap
  root((Standards and method))
    [EU AI Act]
      graphs
      newsroom
      riskmandate.ai
      risks
      sgit.ai
      standards
      ungovr.providers
    [GDPR]
      graphs
      open-source
      riskmandate.ai
      sgit.ai
      standards
      teams
      ungovr.providers
    [Wardley maps]
      games
      graphs
      influences
      open-source
      pki
      riskmandate.ai
      sgit.ai
      wardley-maps
    [Open source]
      abp
      coding
      graphs
      issues-fs
      llms
      newsroom
      open-source
      riskmandate.ai
      risks
      sg-compute
      sgit.ai
      skills
      store
      twins
      ungovr.providers
```

### Working in public

```mermaid
mindmap
  root((Working in public))
    [Briefs]
      abp
      llms
      riskmandate.ai
      sgit.ai
    [Interview pages]
      riskmandate.ai
      sgit.ai
    [Lessons learned]
      elevenlabs.providers
      influences
      providers
      riskmandate.ai
      sgit.ai
      teams
      ungovr.providers
    [Em-dashes and style]
      abp
      coding
      llms
      open-source
      riskmandate.ai
      sgit.ai
    [Synthetic users]
      riskmandate.ai
      sgit.ai
      store
    [Provenance]
      abp
      graphs
      newsroom
      pt.newsroom
      sgit.ai
      ungovr.providers
    [Frozen, hashed sources]
      graphs
      newsroom
      pt.newsroom
      riskmandate.ai
      sgit.ai
```

### The business

```mermaid
mindmap
  root((The business))
    [Business plans]
      sgit.ai
    [Partnerships]
      riskmandate.ai
      sgit.ai
    [Pricing ladders]
      elevenlabs.providers
      riskmandate.ai
      sgit.ai
      store
    [Startups]
      riskmandate.ai
      sgit.ai
      store
    [Brand assets]
      riskmandate.ai
      ungovr.providers
```

## What the maps show

- **Three concepts are on one site only**: vault key management, business plans, and performance and cost are found only on sgit.ai ([the concepts page](nr:concepts)). They are sgit.ai's call, plans and measurements, not yet the network's vocabulary.
- **The permission vocabulary travels furthest from where it started.** Grants and mandates and blast radius are defined on riskmandate.ai ([grant gap](https://riskmandate.ai/grant-gap.md)), undo classes on abp.sgit.ai ([undo](https://abp.sgit.ai/model/undo/index.md)), and between them they reach the two games sites, the provider sites and nhi.sgit.ai.
- **Read keys and open source are on the most sites.** A read key is how a published vault is opened ([credentials](https://sgit.ai/docs/credentials.md)), so the concept follows the vaults from site to site.

Where a concept is defined is on [the concepts page](nr:concepts). How the sites link to each other, whatever the concept, is the [network map](nr:maps/network).

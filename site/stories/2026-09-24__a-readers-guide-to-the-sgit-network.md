---
title: A reader's guide to the sgit network
date: 2026-09-24
desk: Journalist
standfirst: The newsroom's snapshot holds 32 sites. This is each one in a sentence or two, in its own words where possible, grouped by what it is for, with a link to the copy in the reading room.
section: explainer
sources:
  - src:sites/manifest.json
  - https://sgit.ai/llms.txt
  - https://riskmandate.ai/llms.txt
  - https://abp.sgit.ai/llms.txt
  - https://teams.sgit.ai/llms.txt
  - https://newsroom.sgit.ai/llms.txt
  - https://pt.newsroom.sgit.ai/llms.txt
reviewed_by:
reviewed_on:
---

The snapshot the newsroom reads holds 1,318 files from 32 sites, fetched between 23:40 UTC on 24 September and 07:57 UTC on 25 September 2026 (counted from [the manifest](src:sites/manifest.json)). Most sites publish an `llms.txt`, a plain summary written for agents, and that is the source for each line below. Two sites have no `llms.txt` in the snapshot, so their front pages are used instead. The file count after each site name is also counted from the manifest. The groups are the newsroom's, not the network's.

## The product

- **sgit.ai** (194 files). "sgit is git for encrypted vaults": files are encrypted on your machine before they leave it, and the server stores only ciphertext. The site is the official documentation for sgit and the SGraph vault platform ([llms.txt](https://sgit.ai/llms.txt)).
- **sg-compute.sgit.ai** (4). SG/Compute starts an isolated EC2 environment, runs the declared work and terminates it. The site says it is open source, in early access and looking for users ([llms.txt](https://sg-compute.sgit.ai/llms.txt)).
- **llms.sgit.ai** (45). "Your app calls a language model without ever holding an API key." The site also says plainly that the bridge is not yet a boundary against all egress ([llms.txt](https://llms.sgit.ai/llms.txt)).
- **pki.sgit.ai** (7). Public key infrastructure for agents. It publishes the history of the keyserver flooding of 2019, and the registry rules that follow from it, "before the registry exists" ([llms.txt](https://pki.sgit.ai/llms.txt)).
- **issues-fs.sgit.ai** (2). An issue tracker where every issue is a JSON file and every link is a typed edge. It needs no server or database, so it lives inside the repository it tracks ([llms.txt](https://issues-fs.sgit.ai/llms.txt)).
- **skills.sgit.ai** (3). Skills as software packages. It lists eight shipped skills, and it warns that the list shows what shipped, not what has been reviewed ([llms.txt](https://skills.sgit.ai/llms.txt)).
- **twins.sgit.ai** (3). The twin primitive: an interface to reality, not a simulation of it. "ONE TWIN IS BUILT."; the rest is labelled design ([llms.txt](https://twins.sgit.ai/llms.txt)).

## The business

- **riskmandate.ai** (324). "Make your agents insurable." It measures what agents can reach and produces a record an underwriter will accept. It is read-only and never in the request path ([llms.txt](https://riskmandate.ai/llms.txt)).
- **store.sgit.ai** (95). "Every agent needs a licence to operate. This is where you buy one." Two of its six offers do not exist yet, and their rows say so ([llms.txt](https://store.sgit.ai/llms.txt)).
- **subscriptions.sgit.ai** (3). "A subscription is a discount for committing to regular use." The site holds a standard, a register and evidence ([llms.txt](https://subscriptions.sgit.ai/llms.txt)).

## Agents, risk and evidence

- **abp.sgit.ai** (315). The Agent Behaviour Policy: an agent's grant, its mandate, the gap and the barrier. "This site publishes the record and never the verdict." ([llms.txt](https://abp.sgit.ai/llms.txt); the [feature](nr:stories/2026-09-24__the-agent-behaviour-policy-site)).
- **risks.sgit.ai** (5). The research behind riskmandate.ai: a named person underwrites an exposure that already exists, and there is no deny button. The site warns that "ESSENTIALLY NONE OF THIS IS IMPLEMENTED IN CODE." ([llms.txt](https://risks.sgit.ai/llms.txt)).
- **nhi.sgit.ai** (4). Non-human identity. Its thesis is that there is no way today to give a scoped, short-lived identity to agents you rent ([llms.txt](https://nhi.sgit.ai/llms.txt)).
- **standards.sgit.ai** (3). Laws and standards as addressable provisions. Only one instrument is modelled so far, and the site gives no score and no pass ([llms.txt](https://standards.sgit.ai/llms.txt)).
- **threat-modeling.sgit.ai** (3). "A threat model is a claim about a system". It publishes a conference vault of eleven linked threat models and a model checked line by line against its code ([llms.txt](https://threat-modeling.sgit.ai/llms.txt)).
- **games.sgit.ai** (17). "A game is the only artefact that makes somebody state a belief before they are told the answer." It holds the catalogue and the method ([llms.txt](https://games.sgit.ai/llms.txt)).
- **what-can-it-do.games.sgit.ai** (61). A five-minute game: forty questions about what your AI assistant can do, and whether you wanted it to ([llms.txt](https://what-can-it-do.games.sgit.ai/llms.txt)).

## The provider reports

- **providers.sgit.ai** (11). The hub of a family of independent provider reports, built around one question: "where does the API credential live, and what bounds it." The hub makes no measurements itself ([llms.txt](https://providers.sgit.ai/llms.txt)).
- **elevenlabs.providers.sgit.ai** (30). An independent report on the ElevenLabs text-to-speech API. It covers cost on a named workload, what broke, and which credential patterns the product supports. "This is a report, not a tutorial." ([front page](https://elevenlabs.providers.sgit.ai/index.md)).
- **ungovr.providers.sgit.ai** (27). A report on the UnGovr open-data API: government entities and open-records laws, free under CC BY 4.0. It is the family's first open-data provider ([front page](https://ungovr.providers.sgit.ai/index.md)).

## Reference and method

- **graphs.sgit.ai** (6). "A node carries no inherent meaning." Meaning comes from connections. The site insists it is not a graph database pitch ([llms.txt](https://graphs.sgit.ai/llms.txt)).
- **wardley-maps.sgit.ai** (18). "Maps are claims, not pictures." A research site with a doctrine self-assessment and a set of dated resources ([llms.txt](https://wardley-maps.sgit.ai/llms.txt)).
- **teams.sgit.ai** (24). "Roles are boundaries." It is the reference for agentic teams with more than one role ([front page](https://teams.sgit.ai/index.md), [llms.txt](https://teams.sgit.ai/llms.txt); the [explainer](nr:stories/2026-09-25__how-agentic-teams-are-organised)).
- **coding.sgit.ai** (3). Coding style, derived by counting the code. "31 documented rules. 0 linters, 0 formatters, 0 type-checkers anywhere in the estate." ([llms.txt](https://coding.sgit.ai/llms.txt)).
- **nfrs.sgit.ai** (3). Non-functional requirements, from the inside. It is a hub under one rule: "LINK THE MEASUREMENT, NEVER RESTATE IT." ([llms.txt](https://nfrs.sgit.ai/llms.txt)).
- **chrome-extensions.sgit.ai** (3). Four guides from building a browser extension that records a web application's traffic. One of its five sentences is "The expensive bugs do not throw." ([llms.txt](https://chrome-extensions.sgit.ai/llms.txt)).
- **open-source.sgit.ai** (40). "Open source as a strategy rather than a charity": the position, the practice and a history checked against its sources ([llms.txt](https://open-source.sgit.ai/llms.txt)).
- **influences.sgit.ai** (29). The network's provenance layer: the works that shaped the founder's thinking, each written as a falsifiable claim about the codebase. The works themselves are linked, never rehosted ([llms.txt](https://influences.sgit.ai/llms.txt)).
- **infographics.sgit.ai** (3). The catalogue of briefs turned into images. "This site does not generate infographics"; it holds one entry ([llms.txt](https://infographics.sgit.ai/llms.txt)).

## A design, not built

- **sg-sentinel.sgit.ai** (2). An edge security and logging layer. Its llms.txt opens with the warning "SG/Sentinel has not been built." ([llms.txt](https://sg-sentinel.sgit.ai/llms.txt)).

## The newsrooms

- **newsroom.sgit.ai** (8). "Sell the graph, not the paragraph." It argues that a story is a graph of evidence. It also says "Most of this site is an argument, not a product." ([llms.txt](https://newsroom.sgit.ai/llms.txt)).
- **pt.newsroom.sgit.ai** (23). A newsroom written natively in Portuguese that maps the Portuguese AI ecosystem as a graph. Every claim walks back to a frozen, hashed copy of its source ([llms.txt](https://pt.newsroom.sgit.ai/llms.txt)).

How these two relate to this newsroom is in [the three newsrooms](nr:stories/2026-09-24__three-newsrooms).

## Reading them yourself

Every link above opens the newsroom's local copy, with the live page beside it. For the counts of which sites link to which, see the [network map](nr:maps/network). For every file in the snapshot, see [the index](nr:library).

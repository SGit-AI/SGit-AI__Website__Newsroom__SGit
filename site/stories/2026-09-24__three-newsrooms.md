---
title: Three newsrooms in one network, and what each one actually runs
date: 2026-09-24
desk: Journalist
standfirst: newsroom.sgit.ai makes the argument that a story is a graph of evidence. pt.newsroom.sgit.ai runs that method on the Portuguese AI ecosystem. This newsroom points the same method at the sgit network itself. Each one draws its own line between what runs and what is design.
section: feature
sources:
  - https://newsroom.sgit.ai/llms.txt
  - https://newsroom.sgit.ai/index.md
  - https://newsroom.sgit.ai/llms-full.txt
  - https://pt.newsroom.sgit.ai/llms.txt
  - https://pt.newsroom.sgit.ai/index.md
  - https://pt.newsroom.sgit.ai/dados/historias.json
  - https://pt.newsroom.sgit.ai/dados/equipa.json
  - https://pt.newsroom.sgit.ai/dados/agentes.json
  - nr:brief/01-the-newsroom
  - nr:brief/06-house-rules
  - nr:signals/2026-09-24__frozen-hashed-sources-three-newsrooms
reviewed_by:
reviewed_on:
---

The sgit network now has three newsrooms. The first makes an argument about news, the second applies that argument to one country, and the third, this one, applies it to the network. This piece sets out what each says about itself, and keeps what each says runs apart from what each says is design.

## newsroom.sgit.ai: the argument

newsroom.sgit.ai calls itself "The Future of News" and states its case in one line: "Sell the graph, not the paragraph." ([llms.txt](https://newsroom.sgit.ai/llms.txt)). It says news is failing because there is no walkable chain from a claim to its evidence, no way for a correction to reach what it disproved, and no way to pay the person who did the original work ([llms.txt](https://newsroom.sgit.ai/llms.txt)). In its model a story is a graph, and every article is a projection of that graph ([front page](https://newsroom.sgit.ai/index.md)). Its most distinctive argument is about corrections: "In a graph, a correction is an edge." ([front page](https://newsroom.sgit.ai/index.md)).

**What it says runs.** The site is plain about this: "Most of this site is an argument, not a product." ([llms.txt](https://newsroom.sgit.ai/llms.txt)). It names three things that run ([llms.txt](https://newsroom.sgit.ai/llms.txt)):

- **/portugal/**, a publication about Portuguese startups. Its sources are fetched, frozen and hashed, it has a graph and three stories, and it has a human editor of record.
- **/databases/**, SQLite and a SPARQL store running in the reader's browser over the Portugal files, with no server.
- **/governance/**, the Governance Wire. Its ingestion and verification layer is not built, and no human reviews it.

The same file says none of the three has had legal review ([llms.txt](https://newsroom.sgit.ai/llms.txt)).

**What it says is design.** Everything else. The site tells readers not to describe Trust-as-a-Service, the decision graph, per-story cost ledgers or any newsroom department as a live capability ([llms.txt](https://newsroom.sgit.ai/llms.txt)). Its seven publication instances, dated April to May 2026, are "designs" that "were never launched" ([llms.txt](https://newsroom.sgit.ai/llms.txt)).

The snapshot holds 8 files from this site: its front page, both llms files and five JSON files (counted from [the manifest](src:sites/manifest.json)). Most of its section pages are not in the snapshot, so this piece cites its llms.txt for them.

## pt.newsroom.sgit.ai: the method, in Portuguese

pt.newsroom.sgit.ai describes itself as a newsroom written natively in Portuguese that maps the Portuguese AI ecosystem as a graph, where every claim walks back to a frozen, hashed copy of its source ([llms.txt](https://pt.newsroom.sgit.ai/llms.txt)). Its front page says "Não é uma tradução de nada" (it is not a translation of anything): the graph's verbs are Portuguese, and English is the annotation ([front page](https://pt.newsroom.sgit.ai/index.md)). Its editor of record reads every page before it goes live, and no automated run can mark a story as published ([team file](https://pt.newsroom.sgit.ai/dados/equipa.json)).

**What it says is real.** At v0.23.13, updated 14 September 2026, the list is: 92 frozen files from one capture, each with a SHA-256 and all re-verified on every build; 312 nodes and 942 edges; 70 people and 67 organisations derived from the sources; and 25 claims delivered by outside assistants, 14 with the excerpt found in the bytes and 0 published ([llms.txt](https://pt.newsroom.sgit.ai/llms.txt)).

**What it says is not real.** Three of its eight sections have no nodes. The company layer cannot be complete, because Portugal has no open company register. Nothing in a research delivery counts as fact until the editor of record approves it ([llms.txt](https://pt.newsroom.sgit.ai/llms.txt)).

**One point where its own files disagree.** The same llms.txt says "Nenhuma história está publicada" (no story is published), yet further down it lists five articles marked "(publicado)" ([llms.txt](https://pt.newsroom.sgit.ai/llms.txt)). Its story index, a file its build derives from the article folders, records 6 stories and 5 published, each with a publication date of 15 September ([story index](https://pt.newsroom.sgit.ai/dados/historias.json)). Both files carry the same update date, and the snapshot does not settle which is right.

**How it is staffed.** Three departments (research, writing and verification) and one named human ([team file](https://pt.newsroom.sgit.ai/dados/equipa.json)). The team file says the commissioning brief cut fifteen departments to three, because fifteen would have meant seventy-five objects before a single article existed ([team file](https://pt.newsroom.sgit.ai/dados/equipa.json)).

## How the first two relate

newsroom.sgit.ai commissioned pt.newsroom.sgit.ai. Its document set includes a commissioning brief "addressed to the agent that will build" it, and a sibling transfer addressed to that site's agents, read at its v0.3.1 ([llms.txt](https://newsroom.sgit.ai/llms.txt)). The transfer proposes a rule: evidence moved between sibling publications stays evidence only if its provenance travels with it ([llms.txt](https://newsroom.sgit.ai/llms.txt)).

The two files do not agree about whether the site exists. newsroom.sgit.ai's index, at v0.3.13 on 13 September, still calls its page for pt.newsroom.sgit.ai the home page "AS DESIGNED" and says "the site does not exist yet" ([llms.txt](https://newsroom.sgit.ai/llms.txt)). The same file carries the transfer that read the running site. This newsroom's Cartographer raised this as a [signal](nr:signals/2026-09-24__frozen-hashed-sources-three-newsrooms).

## This newsroom: the method, pointed at the network

This newsroom's brief describes a newsroom whose beat is the sgit network. A small team of agents reads every site each day, works out what changed, and publishes what matters; "If nothing happened on a day, nothing is published that day." ([brief 01](nr:brief/01-the-newsroom)). The brief names both relatives and says this newsroom "should borrow from both". From newsroom.sgit.ai it takes the "honest sentence" as the model for its own honesty. From pt.newsroom.sgit.ai it takes a frozen, hashed copy of every source and a human editor of record ([brief 01](nr:brief/01-the-newsroom)). It is in English, and "Its sources are frozen and hashed the same way" ([brief 01](nr:brief/01-the-newsroom)).

**What runs.** A static site built from a snapshot of 1,318 files from 32 sites, each with a sha256 (counted from [the manifest](src:sites/manifest.json)). It has five editions, for 20 to 24 September ([editions](nr:editions)), plus the stories, the history, the signals and [the loose ends](nr:loose-ends). The desks are defined in a register ([the newsroom](nr:newsroom)).

**What is not yet true.** The brief gives the site's name as a "working name" ([brief 01](nr:brief/01-the-newsroom)). No piece in the repository has a `reviewed_by` filled in, so none has yet been marked reviewed by the editor of record (checked across editions/, stories/ and history/ when this piece was written).

## What the three share

All three name what they cannot yet do on the page itself. newsroom.sgit.ai calls this its "honest sentence" ([llms.txt](https://newsroom.sgit.ai/llms.txt)). pt.newsroom.sgit.ai has a section headed "O que NÃO é real" (what is NOT real) ([llms.txt](https://pt.newsroom.sgit.ai/llms.txt)). This newsroom's house rules say "Shipped and proposed are different words." ([house rules](nr:brief/06-house-rules)).

Two of the three define their staff the same way. pt.newsroom.sgit.ai's agent register says it uses the format teams.sgit.ai publishes for a ROLE.md ([agent register](https://pt.newsroom.sgit.ai/dados/agentes.json)). That format is covered in [how agentic teams are organised](nr:stories/2026-09-25__how-agentic-teams-are-organised).

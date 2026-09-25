---
title: pt.newsroom.sgit.ai is live and freezing its sources; newsroom.sgit.ai still calls it a design
date: 2026-09-24
desk: Cartographer
standfirst: pt.newsroom.sgit.ai runs the fetch, freeze and hash method that newsroom.sgit.ai argues for, and has since mid-September; newsroom.sgit.ai, which commissioned it, still describes it on its front page as "a brief for the next agent", and pt.newsroom.sgit.ai's own index does not link back.
from_site: pt.newsroom.sgit.ai
to_site: newsroom.sgit.ai
status: new
action: give newsroom.sgit.ai's team pt.newsroom.sgit.ai's llms.txt, so its front page and index describe a running site rather than a brief
sources:
  - https://pt.newsroom.sgit.ai/llms.txt
  - https://newsroom.sgit.ai/llms.txt
  - https://newsroom.sgit.ai/llms-full.txt
reviewed_by:
reviewed_on:
---

**pt.newsroom.sgit.ai runs the fetch, freeze and hash method that newsroom.sgit.ai argues for, and has since mid-September; newsroom.sgit.ai, which commissioned it, still describes it on its front page as "a brief for the next agent", and pt.newsroom.sgit.ai's own index does not link back.**

This newsroom does the same thing for the sgit network, so it is the third party that should point at both.

## Side A: pt.newsroom.sgit.ai runs it

[pt.newsroom.sgit.ai's llms.txt](https://pt.newsroom.sgit.ai/llms.txt) reads "Versão v0.23.13 · atualizado 2026-09-14". Among what it says is real today:

> "92 ficheiros congelados de 1 captura(s), cada um com SHA-256, todos reverificados em cada construção"

(92 frozen files from one capture, each with a SHA-256, all re-verified on every build.) It publishes a register of every frozen file "com URL, bytes, SHA-256 e hora de obtenção" and a method page: "Obter, congelar, hashear, extrair, comparar".

## Side B: newsroom.sgit.ai argues for it and describes pt.newsroom as unbuilt

[newsroom.sgit.ai](https://newsroom.sgit.ai/llms.txt) (v0.3.13, 13 September 2026) argues that news is failing because there is no "walkable chain from a claim to its evidence". Its own Portugal instance works the same way: "Every page of the source site is fetched, frozen to a dated snapshot in the repository and hashed with SHA-256, and claims are read from the frozen copy rather than the live network" ([full text](https://newsroom.sgit.ai/llms-full.txt)).

Of pt.newsroom.sgit.ai, the same file says two things that no longer hold:

- On the front page: "pt.newsroom.sgit.ai (a brief for the next agent)", with links to the brief and to "The home page, as designed".
- In the index: "THE HOME PAGE OF pt.newsroom.sgit.ai, AS DESIGNED: the site does not exist yet".

newsroom.sgit.ai does know the site exists. The same file carries memo 14, written on 14 September "after reading your repository at `v0.3.1` and your live site". The front page and index in the same file still describe the site as a design.

## What we checked

- Searched pt.newsroom.sgit.ai's llms.txt, the only file of that site in the snapshot, for "newsroom.sgit.ai" outside its own address: no link. Its full site may link back; the snapshot cannot show it.
- Searched the rest of the network: sgit.ai, risks.sgit.ai, llms.sgit.ai, infographics.sgit.ai and riskmandate.ai mention one or both newsrooms.
- This newsroom freezes and hashes the network's pages in the same way (sources/sites/manifest.json holds a sha256 per file). Its about page should link both sites; that is for this newsroom to do, not for them.

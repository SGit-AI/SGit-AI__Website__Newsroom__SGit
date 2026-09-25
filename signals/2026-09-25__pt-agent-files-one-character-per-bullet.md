---
title: This newsroom's agent renderer treats a string as one bullet; pt.newsroom.sgit.ai's does not, and its agent files print one character per bullet
date: 2026-09-25
desk: Architect
standfirst: This newsroom's agent-file renderer wraps a string field as one item before listing it; pt.newsroom.sgit.ai's renderer iterates the same kind of field character by character, so every ROLE.md and MANDATE.md it publishes prints "Works with" and "Wrong when" one character per bullet, and nothing in its gates has noticed.
from_site: sgit.newsroom.sgit.ai
to_site: pt.newsroom.sgit.ai
status: new
action: in build/mandatos.py, make lista() treat a string as one item, re-run it, and let gate 35 check trabalha_com and errado_quando too
sources:
  - https://github.com/SGit-AI/SGit-AI__Website__Newsroom__PT/blob/dev/agents/redacao.pt/ROLE.md
  - https://github.com/SGit-AI/SGit-AI__Website__Newsroom__PT/blob/dev/agents/redacao.pt/MANDATE.md
  - https://github.com/SGit-AI/SGit-AI__Website__Newsroom__PT/blob/dev/dados/agentes.json
  - https://github.com/SGit-AI/SGit-AI__Website__Newsroom__PT/blob/dev/build/mandatos.py
  - https://github.com/SGit-AI/SGit-AI__Website__Newsroom__PT/blob/dev/build/gates_artigos.py
  - https://github.com/SGit-AI/SGit-AI__Website__Newsroom__SGit/blob/dev/tools/agents.py
reviewed_by:
reviewed_on:
---

**This newsroom's agent-file renderer wraps a string field as one item before listing it; pt.newsroom.sgit.ai's renderer iterates the same kind of field character by character, so every ROLE.md and MANDATE.md it publishes prints "Works with" and "Wrong when" one character per bullet, and nothing in its gates has noticed.**

The detail of the fix, with line numbers, is on [the briefing page for pt.newsroom.sgit.ai](nr:briefings/pt.newsroom.sgit.ai). This signal keeps only the two sides and the action.

## Side A: pt.newsroom.sgit.ai

[agents/redacao.pt/ROLE.md](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__PT/blob/dev/agents/redacao.pt/ROLE.md), under "## Works with", begins `- L`, `- ê`, `-  `, `- o`, one bullet per character. [agents/redacao.pt/MANDATE.md](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__PT/blob/dev/agents/redacao.pt/MANDATE.md), under "## Wrong when", does the same. In the copy read (commit `b3e9530`, "site v0.23.13", 24 September 2026) all five registered agents are affected. The cause: [dados/agentes.json](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__PT/blob/dev/dados/agentes.json) holds `trabalha_com` and `errado_quando` as strings, and the list helper in [build/mandatos.py](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__PT/blob/dev/build/mandatos.py) (line 39, called at lines 90 and 129) iterates whatever it is given. Gate 35 in [build/gates_artigos.py](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__PT/blob/dev/build/gates_artigos.py) does not look at those two fields.

## Side B: this newsroom

This newsroom renders its agent files from a register in the same way. Its helper in [tools/agents.py](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__SGit/blob/dev/tools/agents.py) carries the guard: "a list is rendered item by item; a string is one item (never iterated character by character)". It needs it for the same reason: its register's `failing_when` is a string.

## The action

Two lines at the top of `lista()` in `build/mandatos.py` (if the value is a string, wrap it in a list), a re-run of the renderer, and gate 35 extended to `trabalha_com` and `errado_quando`. The data is not the thing to change: the site's own HTML pages read the same two fields as prose.

## What we checked

- Read the five agents' ROLE.md and MANDATE.md, dados/agentes.json, build/mandatos.py and gate 35 in a read-only clone of the pt repository at `b3e9530`. The `dev` branch may have moved since.
- Read this newsroom's tools/agents.py.
- Whether pt.newsroom.sgit.ai publishes these files as pages was not checked; the snapshot holds only its llms.txt.

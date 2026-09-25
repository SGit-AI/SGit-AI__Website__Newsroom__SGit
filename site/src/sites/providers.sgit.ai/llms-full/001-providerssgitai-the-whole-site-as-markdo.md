# providers.sgit.ai — the whole site as markdown
site v0.1.1 · source vault commit 7d1916aca5f3 · every claim's verification state is at /ledger/

Independent work by SGit-AI. Not affiliated with, endorsed by, or sponsored by any provider indexed here. Provider names identify the APIs these pages report on; all trademarks belong to their owners.

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
PAGE /  —  Where the key goes — provider reports for people who have to deploy one
==============================================================================

---
title: Where the key goes — provider reports for people who have to deploy one
description: "The hub of the *.providers.sgit.ai family: four credential patterns, one page contract, and one site per provider reporting what it cost on a named workload, what broke, and where the key has to live."
lead: "One question decides most integrations and almost nobody writes it down: **where does the credential live, and what bounds it.** This is the hub for a family of sites that answer it one provider at a time — with dates, costs and failures attached."
order: 1
toc: true
provenance:
  commit: 7d1916aca5f3
  date: 8 September 2026
  note: "The four patterns come from the source vault; everything about a provider comes from that provider's own site."
---

<div class="note"><p><b>Both domains in this family now serve.</b> {{claim:domains-live}} <code>providers.sgit.ai</code> and <code>elevenlabs.providers.sgit.ai</code> were unpointed for the whole of this site's first release, which is why the links here are not typed but <em>measured</em>: <code>bin/sync-providers.py</code> fetches each site's own published index from its canonical host, and every cross-link goes to whichever host answered. A build check fails if a link disagrees — which caught canonical links while the domains were dead, and now catches a stale project path left behind after they came up.</p></div>

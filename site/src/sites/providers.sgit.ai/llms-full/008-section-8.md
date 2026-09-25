## Reading down the columns

**Column 0 is the same everywhere:** possible, and never acceptable. It is in the table because "the browser can call it" is what people usually mean by client-side, and CORS permitting a call says nothing about whether the credential is bounded.

**Column 1 is where providers part company.** One in this family can mint a key with a spend limit and a reset {{claim:openrouter-402}}; the other cannot, at any price {{claim:no-per-key-spend-limit}}. That is not a difference of degree, and it is the single most useful thing this table shows.

**Column 2 needs a server, and the question is whose.** "Available with a server" and "available" are not the same claim; the last column says which.

**Column 3 is the one this estate can extend to any provider** by adding a verb to the host bridge and a terms file to the vault. It is shipped for a model router and specified for a voice API {{claim:sg-tts-spec}} — and until it ships, the column is a plan rather than a product.

==============================================================================
PAGE /contract/  —  The contract — what a provider site owes
==============================================================================

---
title: The contract — what a provider site owes
description: "The nine fixed sections, the six claim states, the composition rules and the build discipline that every site in this family obeys, so that a second provider is a Markdown file rather than a rewrite."
lead: "The reason a comparison across these sites means anything is that they are not free to answer different questions. This is the contract: **nine sections, six states, and a short list of things that are build failures rather than review comments.**"
order: 40
toc: true
provenance:
  commit: 7d1916aca5f3
  date: 8 September 2026
  note: "The nine sections come from the source vault's TEMPLATE.md; everything else was learned by building the first site."
---

## The brief, addressed to the RiskMandate team

**Asked for on 16 September: this side first, then the reverse.**

You are reading the store's half. The ask is that riskmandate.ai does the same in
the other direction — **reads this store's e-commerce surfaces rather than
re-implementing a cart.**

Concretely, and in the order that makes each one useful on its own:

1. **Publish a stable manifest for each level's artefact** — the zip, its size and
   its sha256, as JSON at a fixed address. **It already exists and it is not
   reachable as data**: on 16 September `paid-t1.html` carried fifteen entries with
   `bytes` and `sha256` inside a JavaScript `const DIST = /*__DIST__*/[…]`. Reading
   that from here means regex-ing your JavaScript out of your HTML at runtime,
   which is the fragility this ask exists to remove. The same bytes at
   `/abp-manifest.json` would close it. The store's page after payment can then
   render your download in its own chrome instead of sending a buyer to you at the
   moment they have just paid. Today the store links to you with one sentence
   saying why; that sentence is the debt.
2. **Publish the shape catalogue as data**, at a stable address with a version
   field. The store already promotes it from your HTML at build time with a content
   hash, which works and is fragile in exactly the way parsing a page for data is
   always fragile.
3. **Do not build a cart.** If a reader on your side wants to buy, send them here
   with the shape already selected. One cart, one order reference, one set of
   prices — the same reason this store does not explain what a policy is.
4. **Agree the shape of what we both read**, not just the address. CORS makes the
   read possible; it does not make it safe to depend on. A stable address, a stable
   shape, and a version field are three different promises and all three are needed.

**What we are not asking for.** No callback, no session, no shared state and no
account on either side. Both of these are static sites and the whole arrangement
works because neither one needs the other to be up in order to be correct.

**Status: open.** It will be recorded here when it is answered, including if the
answer is no, because a brief that only appears when it succeeds is a brief nobody
should trust.

==============================================================================
PAGE /catalogue/  —  What is not for sale yet
==============================================================================

---
title: What is not for sale yet
description: "Eight further offers are specified and none of them is for this week. They are listed so that nobody proposes them as new, and so that the four that are for sale are not quietly widened to include them."
lead: "**Eight further offers exist as specifications and none of them is on the offer page.** They are listed here for one reason: so that nobody proposes them as new. A catalogue that only shows what is buyable today loses the work that went into deciding what is not."
order: 7
---

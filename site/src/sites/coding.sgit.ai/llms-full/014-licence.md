# Licence

## This pack

Everything in this brief pack — the nine numbered documents, `09__source-manifest.csv`, `conventions__machine-readable.json`, this file and `README.md` — is released under the **Creative Commons Attribution 4.0 International licence (CC BY 4.0)**.

    Copyright (c) 2026 Dinis Cruz
    Licensed under CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/

Attribution: **Dinis Cruz**, with AI co-authorship (Claude, Anthropic).

## The site this pack commissions

**The entire content of `coding.sgit.ai`** is to be published under **CC BY 4.0**, consistent with the network. Stamp every raw markdown document; gate it with `licence-audit.py --check`.

## ⚠️ The code quoted throughout is Apache-2.0

Every code example in this pack is real, extracted from repositories licensed **Apache-2.0**: `SGraph-AI__App__Send`, `SGraph-AI__Service__Playwright`, and all seven Issues-FS repos (`license = "Apache 2.0"` in every `pyproject.toml`).

**Retain the notice where snippets are shown at length, and do not imply the code carries the site's CC BY licence.** A style-guide site quoting its own Apache-2.0 code is fine; a site that blurs the two licences on a page about licensing discipline is not.

## Credit the dependency, not just the pattern

`Type_Safe`, `Safe_Str`, `Safe_Int` and the constrained-primitive pattern come from **`osbot-utils`**, Apache-2.0, under the `owasp-sbot` GitHub organisation. So do `osbot-aws`, `osbot-fast-api`, `memory_fs` and `mgraph-db`.

**Wherever the site describes the pattern, name the library.** The convention is the estate's; the mechanism is the dependency's, and the distinction matters on a site whose subject is attribution discipline.

---

## Redaction — the repos are live

> **⚠ Redacted for publication.** This document's own redaction list names the values it forbids. Publishing the list verbatim would publish them, so the AWS account id, the four live internal hostnames and the four named live stack FQDNs are replaced with `[redacted]` in the three bullets below. Nothing else in this document is changed, the counts are kept, and `dev.tools.sgraph.ai` is retained deliberately for the reason the document itself gives. See [/documents/#redaction](../documents/index.html#redaction).


`sg-compute.sgit.ai`'s redaction list applies in full. Strip before publishing:

- **AWS account ID `[redacted]`** — 20+ files under `team/humans/dinis_cruz/claude-code-web/`
- **Live internal hostnames** — `[redacted]` (193), `[redacted]` (128), `[redacted]` (46), `[redacted]` (36) and the rest
- **Named live stack FQDNs** — `[redacted]`, `[redacted]`, `[redacted]`, `[redacted]` (four of them)
- **Real EC2 and AMI IDs** in `utils/ec2_boot_bench/`

### The one special case: `dev.tools.sgraph.ai`

It appears **inside the code examples** — every component imports `SgComponent` and `sg-tokens.css` from it, and it appears 177 times in the tree.

**Recommendation: publish it.** It is a public CDN serving public component code, it is visible in any rendered page's network tab, and a component example with the import URL redacted teaches nothing.

**But make it a deliberate decision**, and note the real concern: the `dev.` prefix means a public coding standard would be documenting a development host as the canonical contract. `08__` Q4.

## Do not publish

`library/alchemist/materials/` (the whole tree) · the positioning and competitor briefs · `team/roles/appsec/reviews/02/21/…pki-architecture-security-revised.md` (classified as *"an attack roadmap for live code"*) · `team/roles/grc/reviews/02/19/` (names a private individual with signature blocks).

## Accuracy

**Every number in this pack was measured in this session by counting, not taken from documentation.** They will drift. The site should **generate its counts at build time or date them** — a style guide whose examples and numbers have drifted from the code is worse than none.

The same goes for the examples: **every code sample must be extracted from the repo at build time, with its path and a commit reference.** Do not paste.

---

This file is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).

# The live vaults

The strongest asset this site has, and the only part of the whole corpus you can open rather than read about. Five vaults are described here with their read keys, browsable in a browser with no account — 504 files and 116 commits between them. Four are published in sgit.ai's catalogue and demonstrate a concept this site otherwise only argues. The fifth was built here, and is the first thing on this site that is not a document.

The catalogue itself has since grown well past these: 21 vaults carry a published read key as of August 2026, from a photo story to a penetration test report to a conference keynote. The four below are the subset that argues something this site argues.

### Risk Graph Explorer

33 files · 428 KB · 7 commits · permissions: {}
A public-by-design application with seven views recomputed simultaneously: estate graph, context, role risk map, risk chains, the register, acceptance (who holds what), and incident-to-project. Its “Exposed” preset carries 18 facts, 37 risks and 14 provisions.

Colour semantics run across every view: amber = exposure, green = assurance, ghosted = unanswered.

Why it belongs here: the ghosted-edge convention is not-knowing-is-a-fact rendered. Nothing else in the estate makes an absence visible on the picture. And its app.json requests permissions: {} — no network, no storage, no account, everything client-side.

Open on sgit.ai →

### Agentic Browser Isolation

104 files · 2.4 MB · 4 commits · fs.write: []
A living risk graph with 17 entry points: a narrative spine, per-altitude stakeholder pages, an explorer, two graph visualisations and the raw data — roughly 70 JSON files. It runs acceptance-gated escalation across five altitudes, L1 IT through L5 board, with no deny button.

Why it belongs here: this is C2 and C4 running on real data rather than asserted in prose. Assertion becomes demonstration. It is the companion artefact to the 59-node business case.

Open on sgit.ai →

### Risk Mandate

124 files · 1.9 MB · 98 commits · 8 app entries
The software project itself, in a vault. The most-committed published vault in the estate — the method applied to its own build, with the change history intact.

Why it belongs here: a register is supposed to be experienced as a story replayed through its commit log. Ninety-eight commits of a project tracking its own risks is the nearest thing that exists to that, and it is the only place where the method has been used on something its authors had to live with.

Open on sgit.ai →

### Regulation Graph

207 files · 14.9 MB · 1,523 nodes · 1,944 edges
The EU AI Act as a citable graph, parsed from official Formex XML and SHA-256 hash-verified: 113 articles, 500 paragraphs, 417 points, 180 recitals, 13 annexes, 68 definitions. Eleven views, including a Cytoscape article graph, a SQLite export, an RDF/Turtle export, and an Article 9 Lab with a graph REPL.

Why it belongs here: it supplies the provisions the concepts hang off — Article 9(5), Article 14 and Article 26(5)/(6) — in the regulator's own structure rather than paraphrased. That is what makes them declared bridges rather than a merge.

Open on sgit.ai →

### The Execution Boundary built here

36 files · 809 KB · 5 commits · 9 pages, one app entry · permissions: {}
An instrument over one small scenario: an authorized action queued for a change window, one material condition changing while it waits, and the question of whether the predicates that justified the authorization can still be established at the moment of execution. Eight pages, four runs, three verdicts — and the third, cannot establish, is the contribution.

Read key in the open, on the page and here:

sgit_rk1_990d25fd8ecab928ded37c6a8c86a461e7247f6d3838bd43e7468e93cc2e07c4:r48ncij0

Why it belongs here: it is the only vault in this list that this site built rather than linked, and the only one that puts not-knowing-is-a-fact at a moment when somebody is about to press a button. Run D ships wrong on purpose — a confident, incorrect established, because the failure that mattered never reached the graph.

The worked example →
Open the vault live ↗

## Read keys yes, write keys never

The standing rule, and why it is absolute. Read keys for all five vaults are published. Write keys are never published, and a write key must be escrowed before the vault is published — because a vault whose write key is lost is frozen: permanently readable, never updatable. There is no recovery path. The rule is not a caution, it is the only thing standing between a live artefact and a permanent one.

This site publishes read keys and no vault keys. That changed at v0.2.0: until then this site reproduced no key of any kind and linked out to sgit.ai's catalogue for all of them, which is still where the four borrowed vaults' keys are kept current. The fifth is ours, so its read key is printed here, on its own page, and inside the vault. A read key is a capability handed out deliberately; it cannot become write access.

The pre-release gate fails the build if anything key-shaped appears anywhere in the tree — a passphrase joined by a colon to a vault id — while allowing a 64-hex read key with or without its sgit_rk1_ prefix. That makes the rule a property of the pipeline rather than a habit. It has already fired in anger: the Execution Boundary's viewer link was first pasted in as the vault key, three times on one page, and the gate refused the build before the commit. The near-miss, written up → · What the gate checks →

The Regulation Graph is already a redacted republication, after an audit found a plaintext key in its history. It carries a PUBLIC.md stating what was redacted and why, and that transparency convention is the one this estate adopts: an audit finding published alongside the artefact it was found in is worth more than a clean history nobody can verify.

## No metered capability behind a published read key

The second vault rule, and the one that is easy to get wrong. A published read key is a key given to everyone. If anything behind it costs money per use — an API call, a model invocation, a storage write — then publishing the key publishes the bill.

The Risk Graph Explorer is the model to copy: permissions: {}, everything computed client-side, no network and no storage. Agentic Browser Isolation declares fs.write: []. Both are declared rather than assumed, which is what makes them checkable by anyone who opens the app manifest.

## The same artefacts, two framings

The four borrowed vaults also appear on riskmandate.ai, as product demos. That is not duplication — it is the split working. There they are evidence that the product does something; here they are worked examples of the concepts. Same artefacts, two readings, one source of truth.

## Provenance

Catalogue
sgit.ai/demos/vaults/ — where the borrowed vaults and their read keys are published and kept current; 21 vaults as of August 2026, of which four are described here

Built here
The Execution Boundary (r48ncij0) — the only vault on this list authored by this site. Its write key is held by the author and not yet escrowed, which its own PUBLIC.md records as an unticked box

Rule source
briefs/08/14/sgit-site-and-hub/v0.33.58__strategy-brief__…read-keys-yes-write-keys-never-frozen-vaults.md

First written
14 August 2026

Status
live and browsable — the only part of this corpus that is not a document

Licence
CC BY 4.0 unless a vault states otherwise; the Regulation Graph's source XML is official EU material

#### For an agent

The live vaults — five, with read keys, browsable with no account, 504 files and 116 commits between them; four are borrowed from sgit.ai's catalogue (21 vaults published as of August 2026) and the fifth was built here. Risk Graph Explorer (33 files, 428 KB, 7 commits): a public-by-design app with 7 views recomputed simultaneously; the “Exposed” preset shows 18 facts, 37 risks, 14 provisions; colour semantics amber = exposure, green = assurance, ghosted = unanswered; permissions: {} — no network, no storage, all client-side. Agentic Browser Isolation (104 files, 2.4 MB, ~70 JSON files, 17 entry points): acceptance-gated escalation across 5 altitudes L1→L5 with no deny button — C2 and C4 on real data; fs.write: []. Risk Mandate (124 files, 1.9 MB, 98 commits, 8 app entries): the method applied to its own build. Regulation Graph (207 files, 14.9 MB): the EU AI Act as 1,523 nodes and 1,944 edges from official Formex XML, SHA-256 hash-verified — 113 articles, 500 paragraphs, 417 points, 180 recitals, 13 annexes, 68 definitions, 11 views including an Article 9 Lab with a graph REPL. The Execution Boundary (36 files, 809 KB, 5 commits, 9 pages behind one app entry, permissions: {}): built by this site — an authorized action queued for a change window with one condition changing while it waits; three verdicts where the third is cannot establish; run D ships a confident incorrect established on purpose. Read key published: sgit_rk1_990d25fd8ecab928ded37c6a8c86a461e7247f6d3838bd43e7468e93cc2e07c4:r48ncij0. Standing rules: publish read keys, never write keys; escrow the write key BEFORE publishing, because a vault whose write key is lost is frozen — permanently readable, never updatable; never put metered capability behind a published read key. This site publishes read keys and no vault keys — and the gate that enforces it has already caught a vault key pasted in as a viewer link, three times on one page, before the commit.


==============================================================================
== /examples/scenarios.html
==============================================================================


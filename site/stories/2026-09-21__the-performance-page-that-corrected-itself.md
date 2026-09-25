---
title: The performance page that corrected itself, release by release
date: 2026-09-21
desk: Journalist
sources:
  - https://sgit.ai/updates/2026/09/21/v0.3.2__update__performance-and-cost.html
  - https://sgit.ai/admin/versions.html
  - https://sgit.ai/demos/fractal-graphs/performance.html
  - https://sgit.ai/updates/2026/09/21/v0.3.4__update__the-design-is-the-performance.html
  - https://sgit.ai/updates/2026/09/21/v0.3.5__update__that-was-a-cold-start-not-an-architecture-cost.html
  - https://sgit.ai/updates/2026/09/21/v0.3.6__update__take-the-api-out-of-the-path.html
  - https://sgit.ai/index.html
reviewed_by:
reviewed_on:
---

On 21 September sgit.ai published a page answering one question, and then spent six more releases making the answer right and findable. This is the sequence, in the site's own records. The edition for the day is [here](nr:editions/2026-09-21).

## The question

After the Fractal Semantic Graphs page went out, a reader asked what the performance of this is against ordinary graph engineering ([the update](https://sgit.ai/updates/2026/09/21/v0.3.2__update__performance-and-cost.html)). The version log says the numbers were "MEASURED RATHER THAN ESTIMATED", from an ordinary cloud container against two live published vaults, using the read keys printed on their own pages ([version log, v0.3.2](https://sgit.ai/admin/versions.html)).

## v0.3.2: the first answer

The first version reported a full clone of the 42-file, 3.2 MB DSIT vault at 65.4 s, a sparse clone at 7.3 s and 256 KB, and one question answered in 7.8 s and 315 KB ([version log](https://sgit.ai/admin/versions.html)). In the browser, the landing view of the graph cost 94 KB in 3 requests ([version log](https://sgit.ai/admin/versions.html)). It named the architecture, no live database and the LETS cycle, set out a cost model of storage and egress only, and listed six places it is slower ([version log](https://sgit.ai/admin/versions.html)).

## v0.3.3: the 65 seconds were a bug

The author named three things the page was missing: reading an encrypted file in a couple of requests, the performance of append mode, and caching of encrypted data ([version log, v0.3.3](https://sgit.ai/admin/versions.html)). Measuring them disproved v0.3.2's explanation of the full clone. The clone took 106 blobs rather than 42 files, and one batch of 50 hit the server's response-size limit and fell back to 50 single fetches, which the note calls "a client-side chunking bug" ([version log](https://sgit.ai/admin/versions.html)). The same release reported a gap rather than smoothing it over: on 21 September the read endpoint returned no Cache-Control header for an immutable object, although the site's own caching contract says it should ([the page](https://sgit.ai/demos/fractal-graphs/performance.html)).

## v0.3.4: a count that had moved

The page had quoted 617 nodes and 694 edges for the DSIT graph, taken from the vault's page. The file as cloned that day had 1,051 nodes and 1,289 edges, because the vault had released a new version on 21 September ([version log, v0.3.4](https://sgit.ai/admin/versions.html)). Every count on the page is now counted rather than quoted, and the note says the drift was only visible because the vault keeps its versions ([version log](https://sgit.ai/admin/versions.html)). The same release measured decryption of the 1.0 MB graph file at 0.351 ms, about a tenth of the JSON parse ([the update](https://sgit.ai/updates/2026/09/21/v0.3.4__update__the-design-is-the-performance.html)).

## v0.3.5: a cold start, not a cost of the design

v0.3.4's table had put a cold network fetch of 1,210 ms at the top. v0.3.5 split it into about 347 ms of fixed overhead and 300 ms of transfer, and called the fixed part the per-invocation cost of running the API serverless, "a deployment choice" ([version log, v0.3.5](https://sgit.ai/admin/versions.html)). It measured batching as a straight line, 0.25 s fixed plus about 71 ms per object, and named the next optimisation rather than claiming it ([the update](https://sgit.ai/updates/2026/09/21/v0.3.5__update__that-was-a-cold-start-not-an-architecture-cost.html)).

## v0.3.6: take the API out of the path

With the same client, vault and decryption, the full clone took 65.4 s through the serverless API and 2.63 s against plain GETs ([version log, v0.3.6](https://sgit.ai/admin/versions.html)). The note is explicit that the static host was localhost, so the network was free, and that a real CDN adds edge latency ([version log](https://sgit.ai/admin/versions.html)). It records that the static transport already ships in the CLI, and that the missing history-depth flag is the single change that would most improve clone time ([the update](https://sgit.ai/updates/2026/09/21/v0.3.6__update__take-the-api-out-of-the-path.html)).

## v0.3.7 and v0.3.8: the ways in

The author asked where the link to the page actually was. It had been reachable from one menu entry and three content links, none on a landing page ([version log, v0.3.7](https://sgit.ai/admin/versions.html)). Five editorial links were added, and fixing them surfaced that Fractal Semantic Graphs had no presence on [the homepage](https://sgit.ai/index.html) at all, which v0.3.8 gave a band of its own ([version log, v0.3.8](https://sgit.ai/admin/versions.html)).

## What the page says against itself

The page still leads its limits with the admission that "A full clone is slow, and not for the reason it looks." ([the page](https://sgit.ai/demos/fractal-graphs/performance.html)). It says there is no server-side query and that writes are single writer per branch, by design ([the page](https://sgit.ai/demos/fractal-graphs/performance.html)). Each correction in the sequence came from a question or a measurement, and each one is recorded in the version log rather than silently replaced ([version log](https://sgit.ai/admin/versions.html)).

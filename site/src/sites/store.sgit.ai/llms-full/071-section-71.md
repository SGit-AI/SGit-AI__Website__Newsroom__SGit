## Where the list comes from

**riskmandate.ai publishes these shapes and this store promotes them.** The
catalogue on this page carries the source URL, the time it was retrieved and a
hash of the page it was read from, because **no page on this site that sells
anything opens a network connection** — that is a build check rather than an intention, so the list is taken
at build time rather than fetched while you read.

A shape added upstream is on this page at the next build. One that arrives without
a code here **stops the build** rather than rendering a tile whose buttons produce
a product code nobody can fill.

==============================================================================
PAGE /versions/  —  Release history
==============================================================================

---
title: Release history
description: "Every release of this site, what changed in it, and the commit it was built from. The version is owned by one file, the release commit's subject repeats it, and the pipeline refuses to tag if the two disagree."
lead: "**Every push to the release branch is a release**, and every release is tagged. The version is owned by `admin/build/version.txt`, moved only by `bin/bump.py`, repeated in the release commit's subject, and **CI refuses to tag if the two disagree**. The same records are served as [JSON](/versions/index.json)."
order: 10
toc: true
---

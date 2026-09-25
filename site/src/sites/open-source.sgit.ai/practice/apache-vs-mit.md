<!-- generated from practice/apache-vs-mit.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.2.2 · canonical: https://open-source.sgit.ai/practice/apache-vs-mit.html*

> The patent grant, defensive termination, the NOTICE file, and the explicit contribution clause — the four things Apache-2.0 does that MIT does not, the honest costs of each, and when MIT is the better choice.

---

# Why Apache-2.0 rather than MIT

This page is written fresh. The entire estate is Apache-2.0 and **the reasoning existed nowhere** — no brief, no document, no commit message. For a site about open source that was the most conspicuous unwritten page in the whole commission, so here is the argument, including where it does not hold.

> **Read this as reasoning, not as legal advice.** Nothing here is a lawyer's opinion, and licence choice has consequences that depend on your jurisdiction, your patent position and your corporate structure. What this page can honestly offer is *what the differences are and why they might matter to you*, which is more than had been written down anywhere before.

## Start with what is the same

Both are **permissive**. Both let anyone use, modify, distribute and commercialise the code, including in proprietary products, with no obligation to publish changes. Both are OSI-approved, GPLv3-compatible, and universally understood. **On the question most people think they are asking — "can someone take this and sell it?" — the two licences give the same answer: yes.**

So the choice is not about permissiveness. It is about four specific things Apache-2.0 says and MIT does not.

## The four differences

### 1. The express patent grant — the main reason

Apache-2.0 section 3 grants every user a licence to any patents the contributors hold that are necessarily infringed by their contributions. **MIT says nothing about patents at all.**

The usual reassurance is that MIT grants an implied patent licence. Perhaps — it is a plausible reading, it has some support, and it has never been comprehensively settled. **An express grant is not a stronger version of an implied one; it is a different thing, because it does not need to be argued.** The value is the absence of the argument.

This matters most to the party *downstream*. A company adopting a dependency wants to know it will not be sued over patents by the people who wrote it, and Apache-2.0 answers that in writing. MIT requires them to reason about it — and legal teams asked to reason about an unsettled question tend to produce a delay rather than an answer.

### 2. Defensive termination

The same section adds a condition: **if you initiate patent litigation alleging the software infringes your patents, your patent licence under Apache-2.0 terminates.**

This is a genuine structural protection and it is a mutual one. It does not stop anyone suing; it makes suing over this software cost you your own right to use it. For a small project it is a deterrent out of proportion to its size, and it costs nothing to have. MIT has no equivalent.

### 3. The NOTICE file — attribution that survives

Apache-2.0 section 4 requires redistributors to carry the `NOTICE` file. MIT requires the copyright notice and licence text to be preserved, which is a weaker and much more easily satisfied obligation in practice.

The practical difference: **a NOTICE file survives vendoring, bundling and repackaging in a way a header comment often does not.** For a project whose commercial position is ["we are selling trust"](../views/index.md#not-free) and whose value is being the recognised source, attribution that survives redistribution is not a vanity concern — it is the mechanism by which anyone downstream can find out who to call.

### 4. It says what a contribution is

Apache-2.0 section 5 states that a contribution submitted for inclusion is licensed under the same terms unless explicitly stated otherwise — **inbound=outbound, written into the licence itself.**

This one is worth sitting with, because it connects directly to [the survivability argument](../survivability/index.md#cla). Apache-2.0's default is the structure that argument prefers: contributions come in under the project's licence, and **nobody acquires the standing to relicense everyone else's work.** A separate copyright-assignment CLA layered on top is what creates the single-holder pattern — and that is a choice a project makes *in addition to* the licence, not something the licence does.

## The honest costs

| Cost | How much it bites |
|---|---|
| **It is heavier to comply with.** Roughly 200 lines against MIT's 20, and the NOTICE obligation is a real step in a release process. | **Genuinely true.** A downstream packager has more to do. For very small libraries this is a defensible reason to prefer MIT — the compliance burden can exceed the code. |
| **Nobody reads it.** MIT can be read and understood by a developer in a minute. Apache-2.0 cannot. | **True, and it matters more than it should.** Comprehensibility is a real property of a licence. Against it: the people for whom the differences matter — legal and procurement — do read it, and they prefer it. |
| **GPLv2 incompatibility.** Apache-2.0 is incompatible with GPLv2 (though fine with GPLv3). | **Occasionally decisive.** If your code needs to be linkable into GPLv2-only projects — the Linux kernel being the notable one — this settles it against Apache-2.0. |
| **The patent grant only matters if you have patents.** | **Partly right, and it misses the point.** The grant's value to a downstream adopter is the assurance, which does not depend on the contributor's portfolio being large. It is worth something precisely when there is nothing to grant, because it says so in writing. |

## When MIT is the better answer

A page arguing for one licence that cannot describe when the other wins is advocacy. MIT is the better choice when:

- **The code is small enough that the licence is a meaningful fraction of the artefact.** A 200-line utility with a 200-line licence is faintly absurd.
- **You need GPLv2 compatibility.** This is not a preference, it is a constraint.
- **Maximum adoption with minimum friction is the entire goal**, and you accept the patent ambiguity as the price. MIT's ubiquity is itself a feature — nobody has ever had to think about whether they can use an MIT dependency.
- **Your ecosystem's convention is MIT** and swimming against it costs you contributors. Convention is a real force and ignoring it is a choice with a cost.

## The position, stated

**Apache-2.0, for code that other organisations will build production systems on.** The patent grant and defensive termination remove questions a procurement process would otherwise have to answer, the NOTICE obligation preserves attribution through redistribution, and the inbound=outbound default aligns the licence with [the structural argument this site makes about survivability](../survivability/index.md). The compliance weight is a real cost and it is worth paying at that scale.

**And CC0 or CC BY for content**, which is a different question entirely — software licences applied to prose produce nonsense, and [the estate's own three-layer split is the subject of the previous page](index.md#reading).

> **What this page is not.** It is not a licence taxonomy, and the site does not yet have one — no worked treatment of copyleft versus permissive, licence compatibility, or where AGPL fits. That is [next on the build order](../roadmap/index.md#taxonomy): the [history research](../history/index.md) supplies the ground for it, and the position is to be written. [standards.sgit.ai owns the SPDX machinery](https://standards.sgit.ai); the argument belongs here, and it is not written yet.

[← Three licences](index.md)[Publish the source →](publish-the-source.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*

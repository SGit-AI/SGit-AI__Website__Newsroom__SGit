<!-- generated from history/index.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.2.2 · canonical: https://open-source.sgit.ai/history/index.html*

> Unix circulated because it was illegal to sell it. BSD lost to litigation risk, not its licence. Netscape's release was a six-year near-failure. Christine Peterson coined open source. Eyeballs are not a security property. And two of the four relicensings reversed.

---

# Six corrections

Everyone has a timeline. [So does this site](timeline.md) — but it sits behind these, because the corrections are the part almost nobody publishes and they are the part that matters. Each one is checkable. And every one of them points the same way: **the model succeeds on economics and structure, not on virtue and not on eyeballs.**

> **Why this section leads.** The author's own writing on open source is about strategy and structure, not history — it argues from what companies and projects actually do, not from the movement's story about itself. So the history was [researched for this site from primary sources](../documents/index.md), 1955 to 2026, with every claim carrying its source and date. The finding that shaped everything else is that **the accurate history is a better argument than the romantic one**.

## 1. Unix circulated because it was illegal to sell it

The founding act of the sharing culture is usually told as generosity: Bell Labs gave Unix away to universities, a gift culture formed, everything follows. The mechanism was regulatory.

The **1956 AT&T consent decree** barred Bell Labs from any line of business except common-carrier communications. Selling software was not available to them. Unix shipped for the cost of media and postage as a **compliance artefact** — the cheapest lawful way to let it out of the building. Universities got the source because there was no commercial channel that AT&T was permitted to build.

And the control experiment ran itself: **the decree was lifted in 1982, and AT&T commercialised System V immediately.** The moment the constraint was removed, the behaviour reversed. That is not a story about culture. It is a story about what an organisation was allowed to do.

## 2. BSD lost to litigation risk, not to its licence

The permissive-versus-copyleft debate frequently invokes BSD as the case study: BSD was permissive, companies took it private, BSD lost, therefore copyleft. The chronology does not support the inference.

**USL v. BSDi ran from April 1992 to February 1994** — precisely the window in which a free Unix could have become the default and Linux was starting from nothing. During those two years, adopting BSD meant adopting an unresolved lawsuit over your operating system. Linux carried no such cloud.

Then the settlement: **three files were removed out of eighteen thousand**, and copyright notices were added to about seventy. The claim was, in substance, nearly empty. **The uncertainty was what did the damage**, and the uncertainty had two years to work. Linux's victory is, in part, a litigation artefact — which says nothing about the merits of either licence and a great deal about how technology choices actually get made.

## 3. Netscape's source release was a six-year near-failure

This is the founding case study of the open source movement, and it is a cautionary tale.

Announced 22 January 1998, released 31 March 1998. The code was in such poor condition that the team eventually **threw it away and rewrote from scratch**. Netscape 6 shipped in November 2000 and was not good. **Firefox 1.0 did not arrive until November 2004** — six and a half years after the release — by which time Internet Explorer had comprehensively won the browser war the release was intended to fight.

Firefox went on to matter enormously, so this is not a story of failure. It is a story about **what opening a codebase does and does not do**. It does not summon a bazaar to fix a codebase nobody can work in. Releasing source is the beginning of a very long piece of engineering, and the romantic version of 1998 skips the six years in the middle.

## 4. Eric Raymond did not coin "open source"

**Christine Peterson**, of the Foresight Institute, did — in the first week of February 1998. And the detail worth keeping is the tactic: she **deliberately had someone else introduce the term**, Todd Anderson, who had more credibility with the room as a Linux programmer, so that it would spread on its merits rather than stall on its source.

Sources disagree on the exact day — OSI records 3 February; Peterson's own account describes 2 and 5 February — and the disagreement is worth stating rather than smoothing over. They do not disagree on who.

It is a small correction with a large amount of the movement's self-image resting on it, and the reason to publish it is the same as the reason to publish everything else on this page: **the mythology is load-bearing, and it is wrong in checkable ways.**

## 5. "Given enough eyeballs, all bugs are shallow" is not a security property

The most-quoted line in open source is a claim about development velocity that has been silently promoted into a claim about security. It does not survive the promotion.

**Heartbleed** survived two years in OpenSSL — the most security-critical library on the internet, read by everyone, audited by nobody in particular. Jim Zemlin, running the Linux Foundation, put it exactly: *"In these cases, the eyeballs weren't really looking."*

**xz is worse, and it is the case that should end the argument.** The backdoor was not missed by review — **it was engineered by the maintainer specifically to survive review**, by someone who had spent years earning the position from which to introduce it. It was found by Andres Freund, one engineer, who was **benchmarking SSH latency** and noticed the numbers were wrong. Not a security review. A performance investigation.

Robert Glass had called the law a fallacy back in 2003, on the evidence that useful reviewers cap out at somewhere around two to four. Two decades of practice have not contradicted him.

> **What this correction does not say.** It is not an argument that open source is less secure than proprietary software, and the comparison is not the point. It is an argument that **"many eyes" is not the mechanism** — visibility is a precondition for review, not a substitute for it, and a project's security comes from someone actually being paid to look. Which is [the funding argument](../funding/index.md), arriving from a different direction.

## 6. Two of the four relicensings reversed — and none went closed source

The 2018–2024 relicensing wave is usually recalled as four one-way doors. Two of them opened again:

- **Elastic added AGPLv3** in August 2024.
- **Redis 8 shipped under AGPLv3** around 1 May 2025.
- **MongoDB remains SSPL.**
- **Terraform remains BUSL**, and HashiCorp is now inside IBM — the acquisition closed 27 February 2025.

And the precision that most commentary loses: **none of the four went closed source.** They went *source-available*. The code stayed readable. The freedoms did not stay. Treating those as the same thing makes the period sound both better and worse than it was.

> **This sharpens the survivability argument rather than weakening it.** The same single-holder standing that allowed them to leave is what allowed them to come back — nobody had to negotiate with thousands of contributors in either direction. **Structure determines what is possible in both directions**, and a project that one party can close is a project that one party can open. Either way you are describing dependence, not safety. [The argument in full →](../survivability/index.md)

## Where to go next

### [The timeline, 1955 → 2026](timeline.md)

*Supporting material*

Behind the corrections rather than in front of them, which is where a timeline belongs on a site whose argument is that the standard telling is wrong.

### [The success stories](stories.md)

*Six, not fourteen*

Linux, Let's Encrypt, SQLite, PostgreSQL, cURL, Blender — each chosen because it proves something argued elsewhere on this site, not because it is famous.

### [The numbers, and the ones to refuse](numbers.md)

*Handle with care*

The $8.8 trillion figure and what it actually measures; "70–90% of a codebase"; and the claims this site will not publish because the research could not source them.

### [Survivability](../survivability/index.md)

*The consequence*

PostgreSQL as the control case and OpenSolaris as the counter-case are history doing the work of an argument.

[← The self-audit](../survivability/self-audit.md)[The timeline →](timeline.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*

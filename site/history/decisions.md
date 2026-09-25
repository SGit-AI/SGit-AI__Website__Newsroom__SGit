---
title: Decisions
date: 2026-09-24
desk: Historian
sources:
  - src:history/sgit.ai-version-log.json
  - https://sgit.ai/admin/versions.html
  - https://riskmandate.ai/versions.md
  - https://riskmandate.ai/pricing.md
  - https://riskmandate.ai/index.md
  - https://store.sgit.ai/llms.txt
  - https://store.sgit.ai/llms-full.txt
  - https://sgit.ai/docs/briefs/index.html
  - https://sgit.ai/docs/briefs/riskmandate-partnership-risk-and-sgit-mapping.html
reviewed_by:
reviewed_on:
---

Every decision visible in the two sites' logs for 18 to 24 September 2026: a price set, a name chosen, an approach dropped, a rule adopted. Newest first. Each entry gives the date, the decision, its context, what it superseded where the source says, and the source. sgit.ai's version record has no per-version anchors, so its entries link to [the record](https://sgit.ai/admin/versions.html) and name the version. riskmandate.ai registers its lead's memos as D11 to D23 in its brief register; those identifiers are quoted where the release note gives them.

Only claims the sources support. Where a source says a matter is somebody else's call and leaves it open, that is recorded as an open decision, not as one taken.

## 24 September 2026

### Company X-Ray reuses RiskMandate's four-level pricing pattern
- **Decision.** Company X-Ray's four levels, from £50 to £1,500, "reuse RiskMandate.ai's pricing pattern".
- **Context.** The fifth business plan of the week on sgit.ai.
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.6.8, [version record](https://sgit.ai/admin/versions.html).

### Every control is taken as working, for now
- **Decision.** The blast-radius figure gives every control a residual risk of its own and takes every control as working, "as the lead said to for now" (D23).
- **Context.** The lead played the figure and asked for two details and a scenario.
- **Supersedes.** A control previously removed a risk from the figure; it now leaves an accepted one.
- **Source.** riskmandate.ai [v1.34.8](https://riskmandate.ai/versions/1.34.8.md).

### The version chip is shown on every screen
- **Decision.** The laptop rule hides only the GitHub link; the drawer carries the version on narrow screens.
- **Context.** The lead had no good way to confirm a new version was live.
- **Supersedes.** The chip hidden below 1400px and below 1040px.
- **Source.** riskmandate.ai [v1.34.7](https://riskmandate.ai/versions/1.34.7.md).

### No number on a risk's impact
- **Decision.** Risks carry a consequence in words and an undo property, and no quantity of loss; "a loss figure is the lead's decision" (D22).
- **Context.** Risks now flow upwards to the board in the article's figure.
- **Supersedes.** Nothing stated.
- **Source.** riskmandate.ai [v1.34.6](https://riskmandate.ai/versions/1.34.6.md).

### The interview grows to thirty minutes and asks about the ABP itself
- **Decision.** The founder interview gains a first part of six questions on the Agent Behaviour Policy and becomes thirty minutes with a sixteen-section summary (D20).
- **Context.** Two asks from the lead in one note.
- **Supersedes.** The twenty-minute interview with a ten-section summary shipped in v1.34.2 that day.
- **Source.** riskmandate.ai [v1.34.4](https://riskmandate.ai/versions/1.34.4.md).

### Local checks run what CI runs, and `dist/` folders are tracked
- **Decision.** `npm run check` runs the licence-chrome check; the pack's `dist/` folders are committed; CI commands are run on a clean export before a push.
- **Context.** Releases v1.32.2 to v1.34.2 never reached the live site because CI failed on each.
- **Supersedes.** A local check that did not run the licence-chrome check, and a repository that ignored every `dist/` folder.
- **Source.** riskmandate.ai [v1.34.3](https://riskmandate.ai/versions/1.34.3.md).

### An interview page, built from another site's brief, unlisted and sent by link
- **Decision.** Build the first interview page from sgit.ai's build brief (D19), unlisted, with a template so the next page is one JSON file; correct two points of the prompt to what the site states.
- **Context.** Expert feedback from people whose time is scarce. The voice run is left to the lead.
- **Supersedes.** Nothing stated.
- **Source.** riskmandate.ai [v1.34.2](https://riskmandate.ai/versions/1.34.2.md); the brief is sgit.ai v0.6.7 in [the version record](https://sgit.ai/admin/versions.html).

### A behaviour-policy vault for each person the lead talks to
- **Decision.** Three kinds of vault (the existing app vault, a private keys vault, one vault per person holding only what that organisation publishes about itself); the pack is kept in the repository, not on the site, behind a leak gate (D18).
- **Context.** The objective this quarter is users.
- **Supersedes.** Nothing stated. No keys vault and no real person's vault exists yet, as the note says.
- **Source.** riskmandate.ai [v1.34.1](https://riskmandate.ai/versions/1.34.1.md).

### OWASP and open source first
- **Decision.** Business cases start with open source, OWASP above all; eighteen open-source cases and an OWASP graph published; agentgateway moves from draft to published "under the lead's direction for open source" (D17).
- **Context.** The lead's memo of the day.
- **Supersedes.** agentgateway's draft, unlisted status from v1.33.0.
- **Source.** riskmandate.ai [v1.34.0](https://riskmandate.ai/versions/1.34.0.md).

### Business cases computed from the Explorer's model, with named vendor cases held back
- **Decision.** A new section computes a product's business case as the difference between two risk registers, on the RiskGraph Explorer's existing model; named cases about other companies' products stay unlisted drafts until the lead decides to send them to the vendors (D16).
- **Context.** The lead's memo asked whether earlier work already covered risks owned at several altitudes; the note says it does.
- **Supersedes.** Nothing stated.
- **Source.** riskmandate.ai [v1.33.0](https://riskmandate.ai/versions/1.33.0.md).

### Two articles, each a hypothesis checked first
- **Decision.** Publish two articles from the lead's memos (D14 and D15), with unmeasured claims reported as what they are.
- **Context.** Each memo was a hypothesis to check before it was written up.
- **Supersedes.** Nothing stated.
- **Source.** riskmandate.ai [v1.32.3](https://riskmandate.ai/versions/1.32.3.md).

### UK support, written down in public, nothing applied for
- **Decision.** A register of 79 UK programmes, each read on its official page, with a status column that says *not started* for all but one (D13). Applying to the Sovereign AI scheme is recorded as the lead's decision.
- **Context.** The lead's memo: the product is ready and the challenge is users.
- **Supersedes.** Nothing stated.
- **Source.** riskmandate.ai [v1.32.2](https://riskmandate.ai/versions/1.32.2.md).

### *Step*, not *rung*
- **Decision.** Every page says *step*; a test fails any page, twin or `llms.txt` that uses the old word. Records keep it.
- **Context.** The lead asked for the word to go when the deck was rebuilt; it reads oddly in a second language.
- **Supersedes.** *Rung*, on eleven pages.
- **Source.** riskmandate.ai [v1.32.1](https://riskmandate.ai/versions/1.32.1.md).

### How it works describes what is sold, with each step's status
- **Decision.** The page is rebuilt in the order of the lead's memo, and the diagram and claims naming things that do not exist are removed (D12).
- **Context.** A peer asked how it technically works, and the page did not answer.
- **Supersedes.** The pre-ABP architecture page, including the line on twins instead of integrations.
- **Source.** riskmandate.ai [v1.32.0](https://riskmandate.ai/versions/1.32.0.md).

### Lesson Loop is paid by credits, not a subscription
- **Decision.** The plan sets out pay-on-demand credits instead of a subscription, and capture first, "nothing else until it works".
- **Context.** The thirty-fifth vault, a business plan for coaches.
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.6.6, [version record](https://sgit.ai/admin/versions.html).

### The Risk Acceptance Office plan takes a position where the method disagrees with itself
- **Decision.** Research found four places where the published method disagrees with itself; the plan picks a position on each and says so.
- **Context.** A business plan for running the risk acceptance loop.
- **Supersedes.** Not stated which way each disagreement was settled in the log entry.
- **Source.** sgit.ai v0.6.5, [version record](https://sgit.ai/admin/versions.html).

### Provider pages carry only what providers publish
- **Decision.** Every provider fact on the partnership pages is from the provider's own pages; credit amounts are left out because several could not be confirmed. A brief asks riskmandate.ai for the risk side of every partnership.
- **Context.** Sixteen new partnership pages.
- **Supersedes.** Two first drafts that research corrected (AWS hosting; S3 mode in general).
- **Source.** sgit.ai v0.6.4, [version record](https://sgit.ai/admin/versions.html).

### Business plans get their own page
- **Decision.** A new page, `/startups/business-plans.html`, listed in the Why menu.
- **Context.** Connector Twin joins Agent as Webmaster as a published plan.
- **Supersedes.** The startups section's list of plans as their only home.
- **Source.** sgit.ai v0.6.3, [version record](https://sgit.ai/admin/versions.html).

### A public call for collaboration on vault key management
- **Decision.** Ask password managers, identity providers and credential managers, in order of preference, for something that exists, a joint pilot, or an open specification.
- **Context.** Keys travel by hand today. The page records that the word-based share token was removed in August.
- **Supersedes.** Nothing stated for this week.
- **Source.** sgit.ai v0.6.2, [version record](https://sgit.ai/admin/versions.html).

## 23 September 2026

### A reader's decision first on the DSIT toolkit page
- **Decision.** The page opens on an outcome and three actions; architecture material moves below, and versions are shown side by side without being merged.
- **Context.** Rebuilt from a brief after the vault moved on.
- **Supersedes.** A page that opened on four worlds and 617 nodes.
- **Source.** sgit.ai v0.6.1, [version record](https://sgit.ai/admin/versions.html).

### The first business plan published for somebody else to run
- **Decision.** Publish Agent as Webmaster under the publishing method; vault counts move to thirty-two, while "measured estate figures keep their 21 September date".
- **Context.** The startups section gains business plans to build on.
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.6.0, [version record](https://sgit.ai/admin/versions.html).

### The Sovereign AI page is titled as a proposal
- **Decision.** Title: 'A proposed partnership between sgit.ai, RiskMandate.ai and UK Sovereign AI'.
- **Context.** A reader from a forwarded link could not tell it was a proposal.
- **Supersedes.** The earlier title (not quoted in the entry).
- **Source.** sgit.ai v0.5.9, [version record](https://sgit.ai/admin/versions.html).

### Partnerships, made in public
- **Decision.** A new Partnerships section with a stated method (public material only, evidence not pitch), first case UK Sovereign AI; the founder's own statement of UK anchoring is added in the first person the same day (v0.5.8).
- **Context.** Written to be forwarded.
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.5.7 and v0.5.8, [version record](https://sgit.ai/admin/versions.html).

### Shorter descriptions, and the 180-character floor retired
- **Decision.** Two shorter boilerplate versions, 110 and 80 characters, that drop the company name rather than the claim.
- **Context.** An exhibitor form rejected 180 characters.
- **Supersedes.** The instruction to say nothing shorter than 180 characters.
- **Source.** riskmandate.ai [v1.29.2](https://riskmandate.ai/versions/1.29.2.md).

### The logo as outlined EPS, written by a script
- **Decision.** Four EPS files, with lettering converted to outlines and no font referenced; two older PNGs left as they are and named for somebody to decide.
- **Context.** An exhibition-board form asked for EPS.
- **Supersedes.** Nothing stated.
- **Source.** riskmandate.ai [v1.29.1](https://riskmandate.ai/versions/1.29.1.md).

## 22 September 2026

### The reviewed level written down before it has been sold, and nobody scored
- **Decision.** The top level is described as a service with eight steps; reviewers are chosen on published facts, never scored, ranked or starred; one reviewer page and one labelled placeholder; what the reviewer is paid is "deliberately not published" (D11).
- **Context.** A brief asked what the service is and who does it.
- **Supersedes.** A site that said almost nothing about the top level.
- **Source.** riskmandate.ai [v1.29.0](https://riskmandate.ai/versions/1.29.0.md).

### Articles get a byline, and the byline gets a page
- **Decision.** First-person articles carry an author and a link; the build refuses an author without a URL; site-voice articles stay unsigned. The next release points the byline at an on-site profile page.
- **Context.** A first-person article carried no name on a site about provenance.
- **Supersedes.** No byline; then a byline linking to LinkedIn (v0.5.5 to v0.5.6).
- **Source.** sgit.ai v0.5.5 and v0.5.6, [version record](https://sgit.ai/admin/versions.html).

## 21 September 2026

### A free first step, and the phase is users
- **Decision.** A new top-level Try it section, the rung below the store's lowest level at no price. The lead's memo sets the measure as people who run the prompts and people who end up with a policy, "not visits, not downloads".
- **Context.** "*Nobody buys a full policy until they have made a smaller one.*" The note records that nothing on the site counts this yet, and that this is the lead's decision.
- **Supersedes.** Nothing stated.
- **Source.** riskmandate.ai [v1.28.0](https://riskmandate.ai/versions/1.28.0.md).

### The third article is retitled on the idea, not the symptom
- **Decision.** New title leading with *union*; the address does not change.
- **Context.** The lead's reading that the idea travels beyond mailboxes.
- **Supersedes.** The title shipped the day before in v1.27.2.
- **Source.** riskmandate.ai [v1.27.3](https://riskmandate.ai/versions/1.27.3.md).

### The build refuses an article with a figure and no card
- **Decision.** The build stops on any article whose body has a figure but no preview card; `release.sh` runs the generator.
- **Context.** The v0.5.0 guard could not fire on the case it was written for.
- **Supersedes.** The v0.5.0 validator check as the safeguard for a forgotten generator run.
- **Source.** sgit.ai v0.5.1, [version record](https://sgit.ai/admin/versions.html).

### Preview cards are JPEG
- **Decision.** 1200x630 JPEG cards generated from each article's first figure, and the large card type.
- **Context.** Pages had no `og:image`, and LinkedIn's crawler does not read WebP.
- **Supersedes.** No `og:image`, and the small summary card.
- **Source.** sgit.ai v0.5.0, [version record](https://sgit.ai/admin/versions.html).

### The SaaS article's title, and then its address
- **Decision.** The title was changed three times in one evening and settled on 'The SaaS apocalypse will be decided by inertia, not by AI', "chosen by the author from the inertia set" (v0.4.6). Then the file name was made to follow it, with no redirect: the old address returns 404 on purpose (v0.4.7).
- **Context.** The author explained why the earlier word misdescribed the argument (v0.4.5).
- **Supersedes.** 'The SaaS apocalypse is optional' (v0.4.3), then 'The SaaS apocalypse belongs to whoever has the least inertia' (v0.4.5); and the slug kept unchanged through the retitlings so links handed out kept working.
- **Source.** sgit.ai v0.4.3 to v0.4.7, [version record](https://sgit.ai/admin/versions.html).

### Every article gets an abstract; the startup article takes its LinkedIn title
- **Decision.** The summary renders as an italic paragraph with a bold Abstract label (v0.4.3); the startup article takes the prefixed title it was given on LinkedIn, in sentence case (v0.4.4).
- **Context.** The author republished on LinkedIn in that form.
- **Supersedes.** A bare lead, and the earlier startup title.
- **Source.** sgit.ai v0.4.3 and v0.4.4, [version record](https://sgit.ai/admin/versions.html).

### Disclaimers become lessons
- **Decision.** Three notes are moved off the vaults page onto a new Lessons learned page; nothing is thrown away.
- **Context.** The author's instruction: the notes were interesting, just in the wrong place.
- **Supersedes.** Three disclaimer boxes above the vaults table.
- **Source.** sgit.ai v0.4.1, [version record](https://sgit.ai/admin/versions.html).

### A startups section, and billing left out
- **Decision.** A new startups section; billing and payments are "not here, not planned".
- **Context.** A large part of why sgit exists is to let other people build on it.
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.4.0, [version record](https://sgit.ai/admin/versions.html).

## 20 September 2026

### *Writing* becomes *Articles*
- **Decision.** The section is renamed at the lead's ask; addresses unchanged.
- **Context.** *Articles* describes what a reader will find.
- **Supersedes.** *Writing*, from v1.27.0.
- **Source.** riskmandate.ai [v1.27.2](https://riskmandate.ai/versions/1.27.2.md).

### The local check runs all of CI's checkers
- **Decision.** `npm run check` runs every checker CI runs, including the vault builds and generated pages.
- **Context.** The v1.27.0 push went red on CI for a stale stamp.
- **Supersedes.** A local check running five of seven checkers.
- **Source.** riskmandate.ai [v1.27.1](https://riskmandate.ai/versions/1.27.1.md).

### A barrier names its holder, and no adjective survives the build
- **Decision.** `not_reachable` is replaced by a blocked list whose entries must name what blocks them; six holder classes and seven questions per barrier; adjectives about controls fail the build. The site starts publishing articles.
- **Context.** Two barriers that pass the same test can be nothing alike.
- **Supersedes.** `not_reachable`.
- **Source.** riskmandate.ai [v1.27.0](https://riskmandate.ai/versions/1.27.0.md).

### The em-dash leaves all prose, and every published read key declares itself public
- **Decision.** 3,200 em-dashes rewritten site-wide with a guard; 102 legacy-prefixed and 24 bare published read keys moved to the public read prefix.
- **Context.** A good many readers find the character off-putting; the legacy prefix was neutral rather than wrong.
- **Supersedes.** The v0.2.92 statement that the site-wide pass "is a separate decision and has not been made here", and the v0.2.98 note leaving the legacy keys as a decision for the author.
- **Source.** sgit.ai v0.3.0, [version record](https://sgit.ai/admin/versions.html).

### One newest-first order for the whole site
- **Decision.** Every list of vaults reads one sorted source, with assertions in the build.
- **Context.** The human table and the machine list had disagreed for four releases.
- **Supersedes.** The table's file order.
- **Source.** sgit.ai v0.2.99, [version record](https://sgit.ai/admin/versions.html).

### Private prefixes banned, credentials classified by declaration
- **Decision.** Published read keys use the public read prefix; the validator bans both private prefixes in tracked files; a credentials page is published.
- **Context.** Another agent correctly refused to open keys labelled private read.
- **Supersedes.** Seven published credentials under the private read prefix.
- **Source.** sgit.ai v0.2.98, [version record](https://sgit.ai/admin/versions.html).

### The article that introduces the term is published here, as written
- **Decision.** The Fractal Semantic Graphs article is published on sgit.ai as the canonical copy, with the figures LinkedIn cannot carry.
- **Context.** The author asked whether the site had a place for it.
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.2.97, [version record](https://sgit.ai/admin/versions.html).

## 19 September 2026

### The insurance answer drops the thread it came from
- **Decision.** The page states the question plainly; the v1.26.1 note keeps the record of how it arrived.
- **Context.** The lead's reading.
- **Supersedes.** The opening that recounted who asked whom.
- **Source.** riskmandate.ai [v1.26.2](https://riskmandate.ai/versions/1.26.2.md).

### A brief instead of a footnote
- **Decision.** The note about graphs.sgit.ai's boundaries page becomes a full brief to that site.
- **Context.** The author asked for the paragraph to go and a proper brief instead.
- **Supersedes.** The 'one wording to pass upstream' paragraph added in v0.2.89.
- **Source.** sgit.ai v0.2.94, [version record](https://sgit.ai/admin/versions.html).

### The page title suffix stays until the site-wide pass
- **Decision.** The ', sgit.ai' suffix on page titles stays "until the site-wide pass is decided".
- **Context.** The em-dash removal on one page.
- **Supersedes.** Nothing.
- **Source.** sgit.ai v0.2.93, [version record](https://sgit.ai/admin/versions.html).

### Fractal means the inside is different
- **Decision.** The definition is rewritten around grammar (constant) against schema (free to change).
- **Context.** The author's reading caught the definition describing a hierarchy.
- **Supersedes.** v0.2.87's definition and test.
- **Source.** sgit.ai v0.2.89, [version record](https://sgit.ai/admin/versions.html).

### The page is called Fractal Semantic Graphs and leads with the definition
- **Decision.** Title, description, nav card and `llms.txt` renamed; the page opens by defining the term.
- **Context.** The author's first read of v0.2.85.
- **Supersedes.** 'How far down does the graph go?' as the page's opening, now a section.
- **Source.** sgit.ai v0.2.87, [version record](https://sgit.ai/admin/versions.html).

### The site's vault mirror is deleted and purged
- **Decision.** Delete the mirror, purge it from all 112 commits and force-push, with the forced push authorised by the author.
- **Context.** No reader, no published read key, dead since v0.2.76, and 91% of the repository.
- **Supersedes.** The one-tree-two-remotes pattern, now a retrospective.
- **Source.** sgit.ai v0.2.84, [version record](https://sgit.ai/admin/versions.html).

## 18 September 2026

### The menu leads with the product
- **Decision.** Five top-level entries and 21 pages in the menu, with two departures from the proposal where link counts said otherwise.
- **Context.** Option A of the menu proposal written the day before.
- **Supersedes.** Seven entries and 34 pages.
- **Source.** riskmandate.ai [v1.26.0](https://riskmandate.ai/versions/1.26.0.md).

### One menu on the home page; Lisbon becomes a dated record
- **Decision.** The in-page anchor strip is removed; the summit page is unlisted but kept.
- **Context.** Two menus on one page; the summit ended that day.
- **Supersedes.** v1.25.1's decision to keep the strip under the shared menu.
- **Source.** riskmandate.ai [v1.25.4](https://riskmandate.ai/versions/1.25.4.md).

### Publish for an archetype, not an instance
- **Decision.** Vault #30 describes a type of company derived from public sources, so there is nothing to redact.
- **Context.** The sibling pack described a real role and withheld the company.
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.2.82, [version record](https://sgit.ai/admin/versions.html).

### The summit sheets are kept as printed
- **Decision.** The correction to a stale vault count became a dating note (the author's call).
- **Context.** The sheets are a dated record of what was said in September 2026.
- **Supersedes.** The previous release's correction of the count.
- **Source.** sgit.ai v0.2.81, [version record](https://sgit.ai/admin/versions.html).

## Contradictions

Places where two sites, or two pages, or two entries, disagree in the snapshot of 24 September 2026. Recorded, not resolved.

### The price of the first level: £10 and £5

Both figures are live in the snapshot.

- **£10:** riskmandate.ai's [pricing page](https://riskmandate.ai/pricing.md) ("four levels, £10 to £1,500") and [home page](https://riskmandate.ai/index.md) ("From £10 for one agent"); store.sgit.ai's `/v1/` page and its offer `t1` at £10 ([store llms.txt](https://store.sgit.ai/llms.txt)).
- **£5:** store.sgit.ai's `/v1/policies/` page description ("the pack downloaded at £5"), and its `/paying/` page ("The four levels are £5, £50, £500 and £1,500") ([store llms-full.txt](https://store.sgit.ai/llms-full.txt)).
- The store records the history itself: the floor was £10 on 10 September, £5 on 15 September, and back to £10 on 16 September ([store llms-full.txt](https://store.sgit.ai/llms-full.txt)).
- sgit.ai's brief of 24 September already names this: "Level 1 is £10 on riskmandate.ai's pricing page and £5 on store.sgit.ai's policies and on the licence page." ([brief](https://sgit.ai/docs/briefs/riskmandate-partnership-risk-and-sgit-mapping.html)). This desk found the £5 on the store's policies page; it could not find a £5 price on a licence page in the snapshot.

### Fifteen or sixteen examples

riskmandate.ai's [home page](https://riskmandate.ai/index.md) says "All sixteen published examples are free to read" and "Sixteen published shapes to start from", and [v1.27.0](https://riskmandate.ai/versions/1.27.0.md) says "All sixteen shapes migrated". Its [pricing page](https://riskmandate.ai/pricing.md) says "Fifteen applications are in the library" and "Fifteen example policies". store.sgit.ai says "Fifteen applications" and "Fifteen Agent Behaviour Policies" ([store llms.txt](https://store.sgit.ai/llms.txt)). The sources do not say whether the difference is one shape not yet on the store, or a count that drifted.

### A brief marked open that the other site has delivered

sgit.ai's [briefs index](https://sgit.ai/docs/briefs/index.html) lists the interview-page brief with the status "open". riskmandate.ai built the page the same day ([v1.34.2](https://riskmandate.ai/versions/1.34.2.md)) and it reached the live site with [v1.34.3](https://riskmandate.ai/versions/1.34.3.md). The [brief](https://sgit.ai/docs/briefs/riskmandate-interview-page-and-voice-prompt.html) also describes an interview of "about twenty minutes"; after [v1.34.4](https://riskmandate.ai/versions/1.34.4.md) the built page is thirty minutes with a sixteen-section summary.

### "Four releases" that are six

riskmandate.ai's [v1.34.3](https://riskmandate.ai/versions/1.34.3.md) is titled "Four releases, delivered" and says "v1.32.2 to v1.34.2 were merged but never reached the live site". The [version record](https://riskmandate.ai/versions.md) lists six releases in that range: v1.32.2, v1.32.3, v1.33.0, v1.34.0, v1.34.1 and v1.34.2.

### How many legacy read keys

sgit.ai v0.2.98 says "99 published keys across 27 pages still carry the legacy rk1 prefix". v0.3.0, the next day's pass, says it moved "102 published read keys" under that prefix and "24 bare ones" ([version record](https://sgit.ai/admin/versions.html)). The log does not reconcile 99 and 102.

### Two risk acceptance interval ladders

risks.sgit.ai's ladder runs 1 hour, 4 hours, 1 to 2 days, 1 to 2 weeks and 1 month, the default rung, with 6 months on its button list ([risks.sgit.ai](https://risks.sgit.ai/llms-full.txt)); sgit.ai's v0.6.5 cites it as "the risks.sgit.ai ladder, 1 hour to 6 months". riskmandate.ai's [Acceptable page](https://riskmandate.ai/acceptable.md) frames the clock differently: "Anything under a week is an incident", and by distance to the line, "roughly a month far above, three months mid, six months at or near the line". Neither page, as read, says whether the two are meant to agree.

### A GDPR graph that one site lists and another says does not exist

sgit.ai's [published vaults](https://sgit.ai/demos/vaults/index.html) list "Standards Atlas, GDPR"; standards.sgit.ai says "There is no GDPR graph" ([standards.sgit.ai](https://standards.sgit.ai/llms-full.txt)). sgit.ai's own brief flags the same disagreement ([brief](https://sgit.ai/docs/briefs/riskmandate-partnership-risk-and-sgit-mapping.html)).

### A documented cache header that was not live

sgit.ai's caching contract page says immutable objects are served with a long-lived `Cache-Control` header. On 21 September the read endpoint returned no `Cache-Control` header for an immutable object, as recorded in v0.3.3 ([version record](https://sgit.ai/admin/versions.html)). The log says the page now states the gap; this desk did not check whether the contract page has since changed.

### A page on graphs.sgit.ai that contradicts itself, according to sgit.ai

sgit.ai's v0.2.94 brief says graphs.sgit.ai's boundaries page states "identical rules, no new format, no special case" in its table while a quotation two paragraphs below says an article may need "its own ontology and taxonomy" ([version record](https://sgit.ai/admin/versions.html)). This desk has recorded sgit.ai's reading and has not checked the graphs.sgit.ai page itself.

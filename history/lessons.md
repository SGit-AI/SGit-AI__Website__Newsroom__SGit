---
title: Lessons learned
date: 2026-09-24
desk: Historian
sources:
  - src:history/sgit.ai-version-log.json
  - https://sgit.ai/admin/versions.html
  - https://sgit.ai/lessons/index.html
  - https://riskmandate.ai/versions.md
reviewed_by:
reviewed_on:
---

Every correction, retraction, rule and "how the mistake was caught" in the two sites' logs for 18 to 24 September 2026, turned into a lesson. Newest first, grouped by day. Within a day, sgit.ai entries are in release order from its git log; riskmandate.ai's record gives dates but no times, so the order between the two sites on the same day is not known.

sgit.ai's version record is one table with no per-version anchors, so each sgit.ai lesson links to [the record](https://sgit.ai/admin/versions.html) and names the version; the same entries are in [the version log](src:history/sgit.ai-version-log.json). riskmandate.ai lessons link to that release's own note. Where a source does not state a rule or does not say how something was caught, the lesson says so rather than supplying one.

sgit.ai keeps its own index of rules and their origins at [Lessons learned](https://sgit.ai/lessons/index.html), which this page does not replace.

## 24 September 2026

### The version has to be visible where people check it

*riskmandate.ai [v1.34.7](https://riskmandate.ai/versions/1.34.7.md)*

**What happened.** The header's version chip, present since v1.0.0, was hidden below 1400px by the rule that made room for the GitHub link and below 1040px by the drawer rule. It showed only on a wide monitor.
**How it was caught.** The site's lead had no good way to confirm that a new version was live.
**The rule.** The laptop rule now hides only the GitHub link; on a phone or tablet the menu drawer's first entry carries the version. The rule lives in the script that rewrites and checks every page in CI.

### Check the way CI sees it

*riskmandate.ai [v1.34.3](https://riskmandate.ai/versions/1.34.3.md)*

**What happened.** The releases from v1.32.2 to v1.34.2 were merged but never reached the live site, because the site deploys only when CI passes and CI failed on every one. Three hand-scaffolded pages lacked the licence chrome, and the repository ignored every `dist/` folder, so the pack's zip was never committed. The note's title calls them four releases; the version record lists six in that range.
**How it was caught.** CI failed on each release. The local `npm run check` did not run the licence-chrome check, "so it passed here and failed there".
**The rule.** The local check runs the same check as CI, the two folders are tracked, and every CI command is run on a clean export of the commit, not the working folder, before a push.

### A brief's prompt is corrected to the site's own words, and the correction is recorded

*riskmandate.ai [v1.34.2](https://riskmandate.ai/versions/1.34.2.md)*

**What happened.** The interview prompt in sgit.ai's brief described two things differently from riskmandate.ai's own pages: what the home page says about who stands behind one record, and whether the behaviour policy is the licence's instrument or its evidence.
**How it was caught.** The prompt was checked against the home page and the Licence to Operate page.
**The rule.** The brief allowed this kind of change; both corrections are recorded beside the prompt. The voice run the brief asked for was not done, because the site's agent has no account for it, and the note says that run is the lead's.

### A leak gate that compares lines misses a paraphrase

*riskmandate.ai [v1.34.1](https://riskmandate.ai/versions/1.34.1.md)*

**What happened.** The first version of the gate for the behaviour-policy pack missed a paraphrased note.
**How it was caught.** The gate was proved against six planted leaks.
**The rule.** The gate compares runs of words rather than lines, and fails on a run of seven words from the lead's private notes, another person's name, organisation or keys, anything shaped like a vault or write key, an email address or a personal LinkedIn link. It must pass before any push.

### Splitting a menu group pushed the header wide

*riskmandate.ai [v1.33.0](https://riskmandate.ai/versions/1.33.0.md)*

**What happened.** Placing the new business-case entries inside the *More* group split it in two and pushed the header past 1280 pixels on every page.
**How it was caught.** The note places it before this release; it does not say how it was noticed.
**The rule.** A test now fails if a menu group's entries are split in the page list.

### A word removed, and a test that keeps it gone

*riskmandate.ai [v1.32.1](https://riskmandate.ai/versions/1.32.1.md)*

**What happened.** The lead asked for the word *rung* to go, because it is not a common word and reads oddly, most of all in a second language. The deck had dropped it, but it was still on eleven pages.
**How it was caught.** The lead's request; the pages were then found and changed, with a different word where *step* would have been wrong.
**The rule.** Any page, markdown twin or `llms.txt` that says the word fails the build. Release notes and the brief register keep it, because they "are records of what was written on their date, and those are never rewritten".

### Styles left behind when a component moved

*riskmandate.ai [v1.32.1](https://riskmandate.ai/versions/1.32.1.md)*

**What happened.** The Index ladder on the Insurance page showed six empty boxes with pale text. Its six level colours were defined on the old home page and stayed behind when the ladder moved.
**How it was caught.** While checking the renamed buttons. The note says it "was broken before today, not by the rename".
**The rule.** Not stated as a general rule; the colours now live on the page that draws the ladder.

### A page that described products which do not exist

*riskmandate.ai [v1.32.0](https://riskmandate.ai/versions/1.32.0.md)*

**What happened.** How it works described an architecture from before the Agent Behaviour Policy existed, and one line of it said the opposite of the lead's memo of the same day.
**How it was caught.** A peer asked in a chat what the product does and how it technically works; the page did not answer the second question.
**The rule.** The page was rebuilt in the memo's order with the status of each step on the step, and the claims about unbuilt capabilities were removed. The note gives the reason: such a page "is not an aspiration; it is the one page a technical reader would use to decide we are not serious."

### Release notes replaced by the release script's stub

*riskmandate.ai [v1.32.0](https://riskmandate.ai/versions/1.32.0.md); see also [v1.29.3](https://riskmandate.ai/versions/1.29.3.md) to [v1.31.1](https://riskmandate.ai/versions/1.31.1.md)*

**What happened.** The notes for v1.32.0 were written before the release was cut, the release script replaced them with its stub, and the stub shipped in the first commit. Separately, seven notes of 23 September (v1.29.3, v1.29.4, v1.29.5, v1.30.0, v1.30.1, v1.31.0 and v1.31.1) are still the unfilled stub in the snapshot.
**How it was caught.** For v1.32.0, the note records it and says the text followed in the next commit. For the seven stubs of 23 September, the record says nothing.
**The rule.** Not stated in the source.

### Two first drafts about hosting and storage, corrected by research

*sgit.ai v0.6.4, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** Two first drafts of the partnership pages were wrong: the site is served from GitHub Pages, not AWS, and the server's S3 mode is only proven on Amazon S3.
**How it was caught.** Research for the pages.
**The rule.** Every provider fact comes from the provider's own pages, researched that day, and credit amounts are left out "because several could not be confirmed".

### Two first assumptions about another company's product, corrected in the text

*sgit.ai v0.6.3, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** The connector-twin article started from two assumptions that were wrong: Google Vault has covered Calendar since November 2023, and the admin audit log does record some earlier values.
**How it was caught.** Research against Google's own pages.
**The rule.** Every claim about Gmail and Calendar is Google's own and linked, and the text says what research corrected.

## 23 September 2026

### A copy rule that lost to a form

*riskmandate.ai [v1.29.2](https://riskmandate.ai/versions/1.29.2.md)*

**What happened.** The brand page's boilerplate said to say nothing shorter than its 180-character version. An exhibitor description field rejected 180 characters.
**How it was caught.** The form refused it on 23 September 2026. The note: "A rule this site wrote about its own copy lost to a form that counts."
**The rule.** Two shorter versions (110 and 80 characters) keep the order of the claim and drop the company name. The note on the 180-character version now says what happened and when, "rather than carrying an instruction a real field has disproved".

### Old exports of the mark, named rather than re-cut

*riskmandate.ai [v1.29.1](https://riskmandate.ai/versions/1.29.1.md)*

**What happened.** Two PNG exports of the mark were made before the mark was revised on 14 September and show a wider `RM` than everything shipped since.
**How it was caught.** Measuring the new EPS files: every file was rasterised back and checked against the current mark.
**The rule.** Proofed rather than assumed. The two old files are left alone "rather than quietly re-cut, and named so somebody decides."

### A page that fell behind its vault

*sgit.ai v0.6.1, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** The DSIT AI Risk Toolkit vault had moved on since 20 September, and the page still opened on four worlds and 617 nodes.
**How it was caught.** A brief asked for the page to be rebuilt.
**The rule.** A status table separates each edition and graph without merging them, and the deck viewer shows a counted "N screenshots could not be read" status "instead of a plausible-looking gap".

### Publishing a vault found two CLI bugs

*sgit.ai v0.6.0, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** The CLI's auto transport treated a fresh vault's object 404 as no live API and switched push to the read-only static transport; and push, pull, fetch, status and delete ignored `--transport`.
**How it was caught.** Publishing the thirty-second vault.
**The rule.** Both fixed in the CLI repository with a pinning test.

### A proposal has to say it is one

*sgit.ai v0.5.9, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** A reader landing on the Sovereign AI partnership page from a forwarded link had no way to know it was a proposal from sgit.ai's side.
**How it was caught.** The entry states the problem from that reader's point of view; it does not say who raised it.
**The rule.** The title, eyebrow and lead now say the partnership is proposed and name both parties.

## 22 September 2026

### A first-person article with no name on it

*sgit.ai v0.5.5, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** The news article is written in the first person and its author's name appeared nowhere on it, on a site whose argument is provenance.
**How it was caught.** The author noticed.
**The rule.** Articles may carry an author and a link; the build refuses an author without a URL, because "a byline without a link is a name, not provenance."

## 21 September 2026

### A builder used before it was ready

*riskmandate.ai [v1.28.0](https://riskmandate.ai/versions/1.28.0.md)*

**What happened.** The admin console's builder rendered document summaries before the link resolver it uses was initialised. No summary had had a link in its first paragraph, so nothing had failed; the first one that did brought the whole build down.
**How it was caught.** By shipping.
**The rule.** The resolver is declared where it is used, with a note saying why.

### A guard that did not guard, and a note that overclaimed

*sgit.ai v0.5.1, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** The v0.5.0 note said the validator catches a forgotten preview-card run. It did not: the fallback always names a file that exists, so a new article with a hero would ship with the generic card and build clean.
**How it was caught.** The author asked whether it would work for new articles with an image; it was tested and simulated, and the answer was no.
**The rule.** The build refuses any article with a figure and no card, names every offender and prints the command. Proved both ways. The log calls this the house pattern: "the build refuses rather than guessing."

### Link previews with no picture, and a format a crawler drops without a word

*sgit.ai v0.5.0, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** Pages carried no `og:image` at all. The obvious fix would also have failed: every figure is WebP, and LinkedIn's crawler drops WebP silently.
**How it was caught.** Reported from a LinkedIn compose box.
**The rule.** Preview cards are JPEG, and a validator check fails the build if a page has no `og:image`, points at a `.webp`, or names a missing file. Proved by deleting the default card: 138 pages failed.

### The em-dash rewriter's collateral, found three times

*sgit.ai v0.5.0, v0.3.9 and v0.3.0, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** The rewriter's paired rule turned dashes into brackets. On 20 September it left seven brackets opening in one table cell and closing in another (v0.3.0). The article title template then shipped with no closing bracket on nine pages (v0.3.9), and sixteen page titles had an unbalanced bracket (v0.5.0).
**How it was caught.** A balance check (v0.3.0); for v0.3.9 the entry records that the validator's prose check does not read `.py` files; for v0.5.0, because the preview alt text is built from the page title.
**The rule.** Each was fixed by hand. The source states no single rule covering all three.

### A phone menu that would not scroll, and grids with a hard floor

*sgit.ai v0.4.9, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** On a phone the open menu stood 1536px tall against a 664px viewport with no scroll of its own. Two grids used a minimum column width wider than a 320px phone's content box and overflowed.
**How it was caught.** Reported from an iPhone and reproduced at three phone profiles; the grid bug was found while verifying the menu fix.
**The rule.** The menu is capped to the viewport and scrolls itself; grids use `minmax(min(Npx,100%),1fr)`, with a comment recording the rule "because the next person will reach for a bare minmax again."

### A title word that misdescribed the argument

*sgit.ai v0.4.5, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** The SaaS article's title called the outcome optional, and three passages leaned on that word. The mechanism the article describes is inertia, not choice.
**How it was caught.** The author said why the word was wrong.
**The rule.** The lead, abstract and closing were rewritten; the word does not survive anywhere in the piece, "checked by the build".

### A count that drifted on three pages

*sgit.ai v0.4.1, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** The fractal ladder has nine vaults, but the vaults page said eight and the fractal page's lead implied eight. Both drifted when the DSIT vault became a step in v0.3.1 and the surrounding prose was not updated.
**How it was caught.** While checking the work on the vaults page.
**The rule.** Counted from the table rather than recalled.

### The most useful pages were the hardest to find

*sgit.ai v0.3.7 and v0.3.8, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** The performance page was reachable from one nav entry and three content links, none on a landing page. Fixing that surfaced a larger omission: Fractal Semantic Graphs had no homepage presence at all.
**How it was caught.** The author asked where the link actually was (v0.3.7); the omission surfaced while fixing the routes (v0.3.8).
**The rule.** Counts on the new homepage band "were checked against the pages rather than recalled".

### A cold start presented as an architecture cost

*sgit.ai v0.3.5, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** The performance page's headline latency was a client figure that included a cold start, presented as though the architecture cost it, and the batch optimisations were missing.
**How it was caught.** Flagged by the author, then measured over six runs each.
**The rule.** The fixed cost is named as a property of running the API serverless; a deployment not measured gets no number, and the page says so.

### Counts quoted from a page, and a graph that had grown

*sgit.ai v0.3.4, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** The performance page said 617 nodes and 694 edges, quoting the vault's page. The file as cloned had 1,051 nodes and 1,289 edges, because the vault had released a new version.
**How it was caught.** By measuring.
**The rule.** "Every count on the page is now counted rather than quoted." The log adds that the drift was only visible because the vault keeps its versions.

### An explanation disproved by new numbers, and a documented header that was not live

*sgit.ai v0.3.3, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** v0.3.2 explained a 65-second clone as a cost of the architecture. New measurements showed one batch hitting the response-size limit and degrading to 50 single fetches. Separately, the caching contract page promised a `Cache-Control` header that the read endpoint did not send.
**How it was caught.** By measuring the transport directly.
**The rule.** The page names it as "a client-side chunking bug" in those words, and reports the header gap "rather than smoothed over".

## 20 September 2026

### A local check that ran five of seven checks

*riskmandate.ai [v1.27.1](https://riskmandate.ai/versions/1.27.1.md)*

**What happened.** A page carries every template's zip size and sha256. The v1.27.0 work changed every zip, and the stamp went stale.
**How it was caught.** The v1.27.0 push went red on CI. The local `npm run check` had not noticed, because it ran five of CI's seven checkers.
**The rule.** The local check now runs all of them, and the new checker was proven to bite by putting a wrong hash in the page.

### Two barriers that are nothing alike, printed under one heading

*riskmandate.ai [v1.27.0](https://riskmandate.ai/versions/1.27.0.md)*

**What happened.** On the Gmail-connector record, attachment content and permanent deletion were both filed as not reachable. One needs a new consent screen somebody has to tick; the other can move in a vendor's release with nothing to click.
**How it was caught.** Working that example through against the vendor's own reference.
**The rule.** Every vault carries a blocked list, and the build refuses an entry that does not name what blocks it. A holder record that calls a control strong, weak or similar fails the build.

### Renderer bugs that no diff showed

*riskmandate.ai [v1.27.0](https://riskmandate.ai/versions/1.27.0.md)*

**What happened.** Two renderer bugs had shipped from the reading app, and two tables had been rendering `|,|` since the consequence layer landed.
**How it was caught.** The note says neither was visible in a diff; the new test found the tables.
**The rule.** A test boots the reading app against a real vault in a fake DOM and builds every view; a view that throws, renders nothing, prints `undefined` or leaves a comma-joined table fails the build.

### The em-dash removal: bugs found by checking rather than assuming

*sgit.ai v0.3.0, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** Removing 3,200 em-dashes site-wide broke things four ways: a whitespace tidy reflowed ASCII diagrams, the pair rule bridged table cells, a page's script compared against text the markup no longer had, and colons before conjunctions read badly.
**How it was caught.** By checking, including a bracket balance check.
**The rule.** The rewriter was made mask-aware, and the validator uses the same exclusions as the rewriter "so the two agree".

### The human table and the machine list disagreed for four releases

*sgit.ai v0.2.99, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** The vaults table rendered in file order while its docstring claimed newest first; the machine list sorted correctly. The key-lifting routine also did not know the public read prefix, so relabelled keys lost their declaration in `llms.txt`.
**How it was caught.** The author asked for the table order to be fixed; the prefix gap was found on the way.
**The rule.** One newest-first order for the whole site, with assertions that ordinals are unique, gapless and in date order. Both assertions were tested by breaking the data on purpose.

### A published read key under a label that says secret

*sgit.ai v0.2.98, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** Seven published read credentials on two vault pages carried the private read prefix, which the CLI defines as read-only and kept secret.
**How it was caught.** Another agent declined to open them and said it would not work around the restriction. The log: "It was right and our label was wrong."
**The rule.** The validator bans both private prefixes in tracked files, the credential checker refuses the private read prefix for publication, and credentials are classified "by declaration and never by shape".

### The vault named after the concept was missing from the concept's page

*sgit.ai v0.2.96, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** The Fractal Semantic Graphs page walked seven graph vaults and never cited the one that carries the name.
**How it was caught.** A question about whether a GitHub repository was in the collection; cloning both showed it mirrored that vault.
**The rule.** Not stated as a rule; the page gained a section crediting the vault, and the vault's page records its mirror.

## 19 September 2026

### A page keeps the question and drops the thread; the record keeps both

*riskmandate.ai [v1.26.2](https://riskmandate.ai/versions/1.26.2.md)*

**What happened.** The insurance page opened by recounting who asked whom, under which post.
**How it was caught.** The lead's reading was that the page is better without it.
**The rule.** The page states the question plainly. The v1.26.1 note still records how the question arrived: "records are not rewritten."

### The fractal definition, corrected three times in a day

*sgit.ai v0.2.89, v0.2.91 and v0.2.95, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** v0.2.87 defined a fractal semantic graph as the same rules at every level, which describes a hierarchy. v0.2.91 corrected a sentence saying that the deeper you go the less you learn, and v0.2.95 replaced the folder tree as the contrast.
**How it was caught.** Each time by the author's reading of the page.
**The rule.** What stays constant is the grammar, never the schema. A wording to pass upstream was recorded on the page "with the date rather than silently corrected", and in v0.2.94 became a brief to graphs.sgit.ai.

### Checked by rendering, not by eye

*sgit.ai v0.2.90, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** After a rewording, diagram captions overran their columns and a footer line was a pixel from the edge.
**How it was caught.** By rendering the SVG at two widths.
**The rule.** Checked by rendering, "not by eye on the source".

### If it is blue it must be clickable

*sgit.ai v0.2.88, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** The ladder diagram's right-hand column was long blue text that read as links nobody could click.
**How it was caught.** A second read of the page.
**The rule.** "if it is blue, it must be clickable; if it is not clickable, it must not be blue." Each of the twelve new links was tested by clicking it.

### A forgotten branch kept purged files downloadable

*sgit.ai v0.2.86, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** After the history purge, a fully merged August branch still pointed at the old chain, so a fresh clone still downloaded the purged objects.
**How it was caught.** Verified by fetching into a clean clone. The branch deletion was refused three times by the session's git proxy.
**The rule.** Reachability gets its own section in the case study, and the page opens with the rule "for a secret, rotate first, rewrite second."

### A footer claim that had never been true of the deployed pages

*sgit.ai v0.2.85, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** Every page's footer said the site was served from an encrypted vault. The log says this was false since v0.2.76 and never true of the deployed pages.
**How it was caught.** Found while purging the mirror.
**The rule.** Not stated as a rule; the footer now says what is true.

### A mirror dead for seven releases, and nobody noticed

*sgit.ai v0.2.84, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** The site's vault mirror had no reader and had been dead since v0.2.76, while it made up 91% of the repository. Three Vaults-menu pages were stale, one listing nine catalogue entries against thirty in the gallery.
**How it was caught.** The question whether the mirror was still needed.
**The rule.** The mirror was deleted and purged; historical release notes were "left as the dated records they are".

### A hand-written index pointing at generated files

*sgit.ai v0.2.83, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** The root `llms.txt` sent agents to two addresses that returned 404 and buried the guidance it should lead with.
**How it was caught.** By a new guard, not by reading: the site's validator had never looked, because it checks links inside pages and `llms.txt` is not a page.
**The rule.** The build asserts that every path the preamble points at is a file the build produces.

## 18 September 2026

### Count the links before unlisting a page

*riskmandate.ai [v1.26.0](https://riskmandate.ai/versions/1.26.0.md)*

**What happened.** The menu proposal would have unlisted *Give feedback*, which nothing but the 404 page links, and three essays, two of which had no editorial inbound link.
**How it was caught.** The link counts.
**The rule.** Two departures from the proposal "because the counted links said so": the feedback page stays in the menu, and the essays got a home before they lost their menu row.

### Two menus on one page

*riskmandate.ai [v1.25.4](https://riskmandate.ai/versions/1.25.4.md)*

**What happened.** v1.25.1 kept the partner design's in-page anchor strip under the shared menu, which made two menus and, after v1.25.3, the buy action twice above the fold.
**How it was caught.** The note describes it as seen on the page; it does not say who noticed.
**The rule.** One menu; the buy action appears once at each end of the page.

### Write for a class, not an instance

*sgit.ai v0.2.82, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** The earlier pack described a real role and withheld the company, which meant auditing whether an unnamed client could be inferred.
**How it was caught.** Comparing the two packs from the same generator.
**The rule.** "a document written for a class can be published; a document written for an instance has to be scrubbed."

### A printed record is dated, not corrected

*sgit.ai v0.2.81, in [the version record](https://sgit.ai/admin/versions.html)*

**What happened.** The summit handouts carried a vault count that was stale by summit week.
**How it was caught.** The previous release had pointed out the change; the author ruled on it.
**The rule.** The sheets are kept as printed with a dating note, because "a printed artefact that gets silently re-edited to match today stops being a record of anything."

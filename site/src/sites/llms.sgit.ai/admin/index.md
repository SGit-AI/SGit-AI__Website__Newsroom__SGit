# How this site is built · llms.sgit.ai

*Source: <https://llms.sgit.ai/admin/index.html> · site v0.2.0 · the markdown twin of this page, generated from it.*

---

[llms.sgit.ai](../index.md) / admin

# How this site is built

Static HTML in the sgit.ai design language, released the same way as the rest of the network: every push to `dev` is validated, auto-tagged, and deployed to GitHub Pages. The pipeline shipped one release before the content did, so every release since has gone through a gate that was already proven.

## The release pipeline

1. **validate** — `node admin/build/validate.js`: internal links resolve, the version agrees everywhere, every page declares a canonical URL on the host named in `CNAME`, every `<loc>` in the sitemap is on that host and has a file behind it, and a key-leak tripwire bans anything shaped like a vault key from the tree. A failure stops the release: no tag, no publish. It also runs on pull requests, so branch work is gated before it reaches `dev`.
1. **tag-release** — every push to `dev` ends tagged `v{release}.{major}.{minor}`. The version is owned by `admin/build/version.txt`, bumped exactly once per release, and must agree with the release commit's subject (`site vX.Y.Z: ...`). CI verifies the two agree and that the bump is the next minor (or a deliberate major), then tags the release commit — which is `HEAD` on a direct push and `HEAD`'s parent when a pull request lands as a merge commit. The first run backfills tags for any historical release from the commit subjects.
1. **deploy** — publishes the tagged working tree to GitHub Pages. Runs on manual dispatch even without a tag, never when validation failed, never from a pull request.

**Why this order, and why it ships first.** The gate is upstream of the tag and the tag is upstream of the publish, so a site that contradicts itself never reaches a reader and never acquires a version number that says it did. Shipping that before the first page of content means every later release goes through a mechanism that has already been proven on a real deploy rather than on the release that mattered.

## The eleven checks

Five came from [pki.sgit.ai](https://pki.sgit.ai). Six were added here, and most of them are conditions the brief pack stated as instructions. **A condition in a brief is one somebody forgets on the fourth page; a condition in the pre-release gate is one the build enforces.**

| # | Check | What it catches |
|---|---|---|
| 1 | **Version agreement** | A version badge, a release-history row, `llms.txt` or `index.md` that disagrees with `admin/build/version.txt`, and a history table that lists the same release twice. |
| 2 | **Internal links** | Any relative `href` or `src` with no file behind it. Fragments and query strings stripped before resolving. |
| 3 | **Canonical host** | A page with no `<link rel="canonical">`, or one pointing at a host other than the one in `CNAME`. |
| 4 | **Sitemap targets** | A `<loc>` on the wrong host, or naming a file that does not exist. |
| 5 | **Key-leak tripwire** | A vault-key-shaped string, key material after the `sgit_vk1_` write prefix, **an OpenRouter `sk-or-` key**, or a bare 48-plus-character secret-shaped token. **Every page on this site is about credentials, which makes it the most likely place in the estate for one to end up in a sample.** The prefixes may appear in prose, because explaining why a key is never published requires naming it; material after them may not. |
| 6 | **The generated reference matches its source** | [The API reference](../api/index.md) is generated from a vendored copy of the canonical contract. If the source changes and the page is not regenerated, or the page is hand-edited, the recorded hash stops matching and the build fails. **This is how the site keeps a readable reference without becoming a second source of truth.** |
| 7 | **A markdown twin at every path** | A page with no `.md` twin, or a twin that has gone stale against its page. Not a nicety on this site: [an inherited finding made it an acceptance criterion](../agents/index.md#finding). |
| 8 | **Twins point at twins** | A link inside a twin that still points at `.html`, which would push a traversing agent back out into markup. |
| 9 | **`llms-full.txt` is current** | The single-fetch file lagging the twins it is built from. |
| 10 | **The qualification travels with the claim** | The front page making the never-holds-a-key claim without [the CSP-gap qualification on the same page](../security/index.md#gap). The brief's instruction was not to soften it and not to bury it; this check is what makes that survive a future edit. |
| 11 | **House spelling** | `-ize` where the house style is `-ise`, in any page or markdown deliverable. |

## What is generated, and what is written

Pages are hand-written static HTML, with four exceptions, and each exception exists for a stated reason rather than for convenience.

| Output | Generator | Why it is not written by hand |
|---|---|---|
| [api/index.html](../api/index.md) | `gen_api.py` | **The Q1 answer.** The canonical contract lives in `AUTHORING.md`, and the corpus refused to copy it because a competing document drifts. Generating it, recording the source hash and gating on the match gives a readable public reference with exactly one author. |
| A `.md` twin per page | `gen_twins.py` | Across the estate these are rendered at request time by a Lambda@Edge function. This site is GitHub Pages with nothing in front of it, so they are written into the tree at release. |
| [llms-full.txt](../llms-full.txt) | `gen_llms_full.py` | Built from the twins, so the one-fetch file cannot disagree with the site. `pki.sgit.ai` has no equivalent; on a site called `llms.sgit.ai`, it is not optional. |
| [documents/](../documents/index.md) | `gen_documents.py` | A repetitive family of reader pages over `briefs/`. The raw markdown stays the source of truth and each page renders it at read time rather than copying it. |
| [sitemap.xml](../sitemap.xml) | `gen_sitemap.py` | The only claim on a site that nothing renders, so it drifts silently. It lists the twins too. |

**No third-party dependency in the toolchain.** The sibling sites reach for `markdown-it` and BeautifulSoup; this one carries `admin/build/mdlite.py`, a markdown subset in both directions, in about 300 lines of standard library. The release path is `python3 admin/build/*.py` on a clean machine, and a generator that needs `pip install` first is a generator that stops being run.

## Releasing a change

```
# 1. bump the version - exactly once per release
echo "v0.2.1" > admin/build/version.txt

# 2. add a row to admin/versions.html, update admin/comms.html

# 3. regenerate, in this order - each step reads the one before it
python3 admin/build/gen_api.py # the reference, from the vendored contract
python3 admin/build/gen_documents.py # the reader pages over briefs/
python3 admin/build/chrome.py # nav, footer, version badge, everywhere
python3 admin/build/gen_twins.py # a markdown twin per page
python3 admin/build/gen_sitemap.py # from the tree
python3 admin/build/gen_llms_full.py # from the twins

# 4. validate locally - the same gate CI runs
node admin/build/validate.js

# 5. commit with the version in the subject, push to dev
git commit -am "site v0.2.1: what changed"
git push origin dev
```

The order matters and the gate enforces the consequences of getting it wrong: `chrome.py` stamps the version the twins then carry, and `gen_llms_full.py` reads the twins, so running them out of order leaves a stale artefact that checks 7 to 9 will catch.

## Chrome from one definition

Pages are hand-written static HTML and stay that way — a human should be able to open any file in the repo and edit it. What is not hand-maintained is the chrome: the nav row (including the version badge `validate.js` requires to agree everywhere) and the footer columns are defined once in `admin/build/chrome.py` and rewritten in place across the tree. Adding a page means adding it to `NAV` or `FOOTER` if it belongs there, writing the file with an empty `<nav class="site"></nav>` and `<footer class="site"></footer>`, and running the script — the `here` state comes from the page's own path.

The same script stamps the version and release date into `llms.txt` and `index.md`. On the sibling sites nothing did, so they were hand-edited every release, and hand-editing them silently missed.

## Conventions carried from the network

- Light theme, the same design tokens and the same honest-limitations posture as [sgit.ai](https://sgit.ai), [pki.sgit.ai](https://pki.sgit.ai) and [graphs.sgit.ai](https://graphs.sgit.ai).
- The version badge in the nav links to the release history, so any page tells you which release you are reading — and CI enforces that they all agree.
- The stage pill states the site's maturity in the nav rather than in a footer nobody reads. It says **reference draft**: the contract it documents is young, moved twice in two days when it shipped, and [already disagrees with the product in one place](../shipped/index.md#drift).
- Source documents captured verbatim under `briefs/` with a curated reader page alongside — the raw markdown stays the source of truth. Queued: this site has no source documents yet.
- Machine-readable entry points: `llms.txt`, [llms-full.txt](../llms-full.txt), a twin at every path, and a sitemap that lists both. [Why this site treats that as an acceptance criterion.](../agents/index.md)
- The comms page is the working channel between the project lead and the site agent, in public, updated every release.

## One thing worth fixing upstream

**The inherited `.gitignore` hides the build tooling.** These repositories start from the standard Python `.gitignore`, which ignores `build/` — and that matches `admin/build/`, so the gate script and the chrome script are silently never committed. [standards.sgit.ai's repository](https://github.com/SGit-AI/SGit-AI__Website__Standards) is in that state today: its CI runs `node admin/build/validate.js` against a checkout that does not contain the file. The fix is one line — `!admin/build/` immediately after `build/` — which [pki](https://github.com/SGit-AI/SGit-AI__Website__PKI) and [graphs](https://github.com/SGit-AI/SGit-AI__Website__Graphs) carry and this repository now carries too.

 [← Front page](../index.md) [Release history →](versions.md)

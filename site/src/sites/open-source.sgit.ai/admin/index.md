<!-- generated from admin/index.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.2.2 · canonical: https://open-source.sgit.ai/admin/index.html*

> The build tooling, the CI pipeline (validate → auto-tag → deploy), the release process, and the markdown-twin generator that makes the site traversable by agents. Published, because a site arguing you should publish the source should publish its own.

---

# Admin & engineering

Every page here is hand-written static HTML, deployed to GitHub Pages from `dev`. What is *not* hand-maintained is the chrome, the markdown twins and the agent surfaces — those are generated, and CI fails the build if what was committed does not match what the generators produce.

## The pipeline

Same order as the sibling sites — **validate → tag → publish** — because a release that cannot be validated should never acquire a tag, and a release that was never tagged should never reach the web.

| Stage | What it does | What stops the release |
|---|---|---|
| **1 · validate** also on pull requests | Regenerates the markdown twins and `llms-full.txt`, then fails if the working tree changed — so a stale generated surface is caught rather than shipped. Then `node admin/build/validate.js`. | A failure here means **no tag and no publish**. Running on pull requests means branch work is gated before it can reach the release branch. |
| **2 · tag-release** pushes to `dev` only | Every push to `dev` is a minor release, tagged `v{release}.{major}.{minor}`. The version is owned by `admin/build/version.txt` and **must also appear in the release commit's subject** (`site vX.Y.Z: …`). CI verifies the two agree and that the bump is the next minor (or a deliberate major), then tags **the release commit** — which is HEAD on a direct push and HEAD's parent when a pull request lands as a merge. | Version disagreement, a reused version, or a skipped minor. The first run also **backfills tags** for any historical release from the commit subjects. |
| **3 · deploy** | Publishes the tagged commit to GitHub Pages. Runs on manual dispatch even without a tag. | **Never runs when validation failed**, and never from a pull request. |

## What validation actually checks

1. **Version agreement** — `version.txt` against every page's version badge, the versions table, `llms.txt` and `llms-full.txt`. It also catches a release listed twice in the history table, which is what a blanket version-bump `sed` produces and which shipped once on a sibling site.
2. **Internal links** — every relative `href` and `src` in every page resolves to a file that exists.
3. **Canonical host** — every `rel="canonical"` and `og:url` points at the host in `CNAME`, and **every page has one**.
4. **Markdown twins** — every `.html` has its `.md` twin, `llms-full.txt` carries every page, and `llms.txt` lists every twin. [The site's agent-discovery argument rests on this](../practice/publish-the-source.md), so a missing twin is a release-stopping defect rather than a nice-to-have.
5. **Licence footers** — every markdown file carries the CC BY 4.0 line. The site holds others to declaring their licensing; it does not get to be sloppy about its own.
6. **Key-leak tripwire** — nothing anywhere in the tree may look like a vault key. This site discusses keys; it must never contain one.

## The build tooling

| File | What it owns |
|---|---|
| `admin/build/version.txt` | **The version.** One file, bumped exactly once per release. Everything else derives from it. |
| `admin/build/chrome.py` | **The single definition of the nav and footer**, applied across every page. Pages stay hand-written; the chrome does not drift. It also stamps the version into `llms.txt`, because hand-editing it silently missed twice on a sibling site. |
| `admin/build/gen_markdown.py` | **The markdown twin of every page**, plus `llms.txt` and `llms-full.txt`. Converts the HTML, **rewrites internal `.html` links to `.md`** so a traversing agent never leaves the markdown surface, and concatenates everything into one file for agents that cannot follow links at all. No dependencies — it has to run in CI with nothing installed. |
| `admin/build/validate.js` | **The pre-release gate.** Node with no packages, for the same reason. |
| `assets/site.css`, `assets/nav.js` | The shared sgit.ai design language and the two-level nav component. |
| `assets/stress-test.{css,js}` | [The Change-of-Control Stress Test](../survivability/stress-test.md). Entirely client-side; answers persist in `localStorage` and are never transmitted. |

## The release process

1. Bump `admin/build/version.txt` (`vX.Y.Z`, **exactly once per release**) and add a row to [`admin/versions.html`](versions.md); update [`admin/comms.html`](comms.md).
2. `python3 admin/build/chrome.py` — propagates the version badge and any nav or footer change to every page.
3. `python3 admin/build/gen_markdown.py` — regenerates the twins, `llms.txt` and `llms-full.txt`.
4. `node admin/build/validate.js`
5. `git commit -am "site vX.Y.Z: …" && git push origin dev`

> **The commit subject is load-bearing.** CI reads the version out of it and refuses to tag if it disagrees with `version.txt`. That is deliberate: it means the version cannot be bumped in a file without someone also saying so in the history, and the tag always lands on the commit that claims to be the release.

## Why any of this is published

Because [the argument of this site is that you should publish the source next to the render](../practice/publish-the-source.md), and a site making that argument with an opaque build would be making it badly. The repository is public, the generators are readable, and [the briefs the content was written from are published verbatim](../documents/index.md) — including [the instructions this site did not follow](../documents/index.md#divergences).

[← About the author](../about/index.md)[Comms →](comms.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*

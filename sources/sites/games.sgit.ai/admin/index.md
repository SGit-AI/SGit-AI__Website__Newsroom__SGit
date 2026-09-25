# Admin & engineering

> How games.sgit.ai is built and released: one content file, generated HTML and markdown twins, and a seven-check gate.

*Source: <https://games.sgit.ai/admin/index.html> · site v0.5.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / Admin

# How this site is built

Every page exists once, as content, in `admin/build/build_pages.py`. Nothing under the site root is hand-edited.

## The build

```
python3 admin/build/build_pages.py   # pages, .md twins, llms.txt, sitemap
node admin/build/validate.js          # the gate CI will run
```

`admin/build/shell.py` renders one block list to **both** the HTML page and its markdown twin. sgit.ai says of every twin that it *"is generated from the same content as the page, so the two cannot drift"* — a generator is the only way that sentence stays true.

## The gate — seven checks

1. **Version agreement** — `version.txt` against every page's badge, the versions table and `llms.txt`, with each release appearing exactly once.
2. **Internal links** — every relative `href`/`src` resolves to a file in the tree.
3. **Canonical host** — every canonical and `og:url` is on the host in `CNAME`, and every page declares one.
4. **Key-leak tripwire** — nothing may look like an sgit vault key. Extended here to catch the *short* vault-id shape (`<secret>:<8 alphanumerics>`) as well as the long form, with the published read key on an explicit allow-list of exact strings.
5. **Every embed discloses** — a page that mounts a vault app must carry the telemetry notice. Mechanical, because this is the exact defect sgit.ai published against the vault: two pages saying *nothing sent* on the same screen as events being sent.
6. **Maturity labels come from the ladder** — a card cannot invent a status.
7. **Every page has its twin** — an HTML page with no `.md` beside it means the build was not run.

## Release

```
# 1. bump admin/build/version.txt and add a VERSION_LOG row in build_pages.py
python3 admin/build/build_pages.py && node admin/build/validate.js
git commit -am "site vX.Y.Z: what changed" && git push origin dev
```

Every push to `dev` runs **validate → tag → deploy**. The tag is checked against `version.txt` *and* the release commit's subject, and the bump must be the next minor. Pull requests run validation only. Same pipeline as pki, graphs and wardley-maps.

## Why the tripwire was extended

The inherited version matched `<secret>:<uuid>` — the long-form vault id. Every vault in this family uses the **short** form (`4evnlwrj`, `kqngdecz`), so the inherited check would have passed over a leaked key on either of these sites. It now matches both shapes, and the allow-list is a list of exact strings rather than a pattern: a pattern permissive enough to admit our read key would admit every credential of that shape, which is how a check comes to pass while meaning nothing.

---

*[Site index for agents](../llms.txt) · [HTML version](https://games.sgit.ai/admin/index.html)*

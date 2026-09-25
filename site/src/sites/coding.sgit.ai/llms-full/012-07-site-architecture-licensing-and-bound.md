# 07 — Site architecture, licensing and boundaries

## 1. The house pattern, plus one rule specific to this site

Copy `pki.sgit.ai`; add the `/llms-full.txt` it lacks. And add the rule that matters here:

> **Every code example on the site is extracted from the repo at build time, with its file path and a commit reference.**

A style guide whose examples have drifted from the code is worse than no style guide. The examples in `01__`–`04__` are all real files — keep them real by generating the pages, not by pasting.

The same goes for every count. `Schema__` 614, `Enum__` 185, banners 992/992, rule-9 violations 97 — all of those are one `grep | wc -l` away and all of them will change. **Generate them, date them, or leave them out.**

---

## 2. Page by page

**`/`** — the thesis in 300 words. *"Runtime type safety instead of static analysis; the type is the validation; one idea per file; and a house style designed for a codebase whose main author is a model."* Then the one-line hook: **31 documented rules, 0 linters, 4 guards, 1 of which never worked.**

**`/python/`** — `01__`. Build first: it is the deepest and it has the written rules behind it.

**`/rules/`** — `06__`. **The page that makes the site useful.** One page per rule group, each rule with its verbatim text, its measured compliance and its enforcement badge.

**`/javascript/`** and **`/components/`** — `02__`. The framework-free component system, the three-file triplet, the versioned CDN, `SgComponent`. Nobody has written this down.

**`/css/`**, **`/html/`** — `03__`. Alignment, tokens, `data-*` as the behaviour hook, and the argument that shadow DOM makes BEM unnecessary.

**`/bash/`** — `04__`. Five `.sh` files, fifteen `Section__*` classes, and the trade.

**`/for-agents/`** — `05__` §5. **The most original page available**, and the one that explains why the rest of the rules look the way they do.

**`/enforce/`** — the linter configs, per language, from the "what a linter would encode" section at the end of each language page. Ship the configs as files, not as prose.

**`/shipped/`** — `00__` §5, unsoftened: nothing is enforced by tooling, one guard never worked, four of five languages are undocumented, import alignment is 39%.

**`/network/`, `/admin/`** — house pattern, build order published unresolved with `08__`'s questions visible.

---

## 3. Licensing

**This site's content is CC BY 4.0**, consistent with the network. Stamp every raw markdown document; gate it with `licence-audit.py --check`.

**The code quoted throughout is Apache-2.0** — `SGraph-AI__App__Send`, the sg-playwright repo and all seven Issues-FS repos carry it, and every `pyproject.toml` says `license = "Apache 2.0"`. Retain the notice where snippets are shown at length, and do not imply the code carries the site's CC BY licence.

**The `osbot-*` and `mgraph-*` dependencies are Apache-2.0** under the `owasp-sbot` organisation. `Type_Safe` and the `Safe_Str` family come from `osbot-utils` — **credit it by name wherever the pattern is described**, because the pattern is the dependency's, not this estate's.

---

## 4. Do not publish

> **⚠ Redacted for publication.** This document's own redaction list names the values it forbids. Publishing the list verbatim would publish them, so the AWS account id, the four live internal hostnames and the four named live stack FQDNs are replaced with `[redacted]` in the three bullets below. Nothing else in this document is changed, the counts are kept, and `dev.tools.sgraph.ai` is retained deliberately for the reason the document itself gives. See [/documents/#redaction](../documents/index.html#redaction).


The repos this pack draws on are live, and `sg-compute.sgit.ai`'s redaction list applies in full here too:

- **AWS account ID `[redacted]`** — 20+ files under `team/humans/dinis_cruz/claude-code-web/`
- **Live internal hostnames** — `[redacted]` (193), `[redacted]` (128), `[redacted]` (46), `[redacted]` (36), `dev.tools.sgraph.ai` (177, published deliberately) and the rest
- **Named live stack FQDNs** — `[redacted]`, `[redacted]`, `[redacted]`, `[redacted]` (four of them)
- **Real EC2 and AMI IDs** in `utils/ec2_boot_bench/`

⚠️ **`dev.tools.sgraph.ai` is a special case for this site**, because it appears *inside the code examples* — every component imports `SgComponent` and `sg-tokens.css` from it. You cannot show a real component without showing the host.

**Recommendation:** publish it. It is a public CDN serving public component code, it is already in every rendered page's network tab, and a component example with the import URL redacted teaches nothing. But **make it a deliberate decision**, note that the `dev.` prefix is a durability risk for a documented public contract, and consider whether the site should be documenting a `dev.` host at all. `08__` Q4.

Standard estate exclusions also apply: `library/alchemist/materials/` (the whole tree), the competitor maps, the AppSec review classified as *"an attack roadmap for live code"*, and the GRC reviews naming a private individual.

---

## 5. Network boundaries

| Site | Owns | Boundary |
|---|---|---|
| **`coding.sgit.ai`** | How code is written here — the five languages, the rules, the enforcement | — |
| `sg-compute.sgit.ai` | The platform | **The richest source of examples.** That site owns *what the code does*; this one owns *how it is written*. **The broken CI guard belongs to both** — that site tells it as a rename story, this one as an enforcement story. Cross-link, do not duplicate |
| `open-source.sgit.ai` | The open-source position | **`/for-agents/` is the shared boundary.** That site has the argument (*"someone still needs to understand what is underneath"*, code-reading as a scarce asset); this one has the artefact. Link both ways |
| `issues-fs.sgit.ai` | Issues-FS | Shares the `Schema__Node` / `Safe_Str__Graph_Types` primitive pattern — the same convention in a different codebase, which is good evidence it generalises |
| `standards.sgit.ai` | Instruments | SPDX identifiers and licence compliance. Light link |
| `graphs.sgit.ai` | Graph theory | Little overlap |
| `sgit.ai` | The vault product | The vault HTML authoring contract is a coding standard in its own right — see the `llms.sgit.ai` pack |

---

## 6. House style for the site itself

- **Every example is a real file, with its path.** No invented snippets.
- **Every count is generated or dated.**
- **Every rule carries an enforcement badge** — ✅ tested · 🟡 documented · ⚠️ violated · ❌ undocumented.
- **Cite the precedent** where a rule has one. Rules 14, 15, 21 and the `object = None` guard all do.
- **Publish the bad numbers.** 91%, 39%, 2-of-5, one broken guard.
- **-ise, not -ize**, and no em-dashes in the markdown deliverables, to match the estate.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
source: /briefs/08__gaps-and-open-questions.md

==============================================================================


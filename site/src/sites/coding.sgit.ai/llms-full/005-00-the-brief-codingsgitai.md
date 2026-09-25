# 00 — The Brief: `coding.sgit.ai`

**Version** v0.33.62 · 24 August 2026
**From** Dinis Cruz, via the SG/Send Librarian
**To** the agent commissioned to build `coding.sgit.ai`
**Licence** CC BY 4.0

---

## 1. The commission

> *"focused on coding, which will go at `coding.sgit.ai` and I can use to capture all the coding patterns and formatting across the main languages we work on: **python, javascript, html, css, bash**."*

All five are covered. Every convention in this pack was **derived from the code by counting**, not from documentation — and where a documented rule and the code disagree, both are reported with the numbers.

---

## 2. The headline: you already have a written style guide, and the code mostly obeys it

`.claude/CLAUDE.md` in the sg-playwright repo carries **31 numbered rules** across Code Patterns, Security, AWS Naming, Responsibility Boundaries, Class/File Naming and Testing. That is far more than most projects have, and it is not aspirational — measured against 992 class-defining files in the new tree:

| Rule | Compliance |
|---|---|
| **7 — `═══` 80-char header on every file** | **100%** (992 / 992) |
| **8 — inline comments only, no docstrings ever** | **99.7%** (3 violations) |
| **22 — `__init__.py` stays empty** | **99%** (299 / 302) |
| **9 — no underscore prefix for private methods** | **91%** (97 violations) |
| **1 — all classes extend `Type_Safe`** | see §4 — the raw number understates it |

**The site's job is not to invent a style guide. It is to publish the one that exists, with the measurements, and to make it enforceable.**

---

## 3. The five languages, in one paragraph each

**Python** — 217,266 lines, and the most distinctive style in the estate. Double-underscore class names in families (`Schema__` 614 files, `Safe_Str__` 290, `Enum__` 185, `Cli__` 82, `Routes__` 59), **one class per file, filename identical to the class name**, `Type_Safe` runtime validation instead of static typing, constrained primitive types instead of boundary validation, `═══` banner headers, and **column-aligned assignments**. `01__`.

**JavaScript** — 50 files, and the pattern is **native web components with no framework and no build step**: 41 `customElements.define`, ESM imports from a **versioned CDN** (`dev.tools.sgraph.ai/components/<name>/v1/v1.0/v1.0.0/…`), a shared `SgComponent` base, and a **three-file component triplet** (`.js` / `.html` / `.css`). 4-space indent, single quotes, **no semicolons**. `02__`.

**HTML** — semantic elements, ARIA on every interactive control, `data-*` as the behaviour hook, **2-space indent** (deliberately different from JS and CSS), and the markdown-twin convention where every URL is also available as `.md`. `03__`.

**CSS** — **the same alignment discipline as Python, applied to property values.** Design tokens as custom properties served from the versioned CDN (`sg-tokens.css`), `:host` scoping, shadow DOM. `03__`.

**Bash** — and this is the surprise: **there are only 5 `.sh` files in a 217,000-line repo.** Shell is not written, it is **generated** from 15 typed `Section__*` Python classes that each render a fragment. `04__`.

---

## 4. The three things that make this style unusual

**(a) Runtime type safety instead of static analysis.** There is **no linter, no formatter and no type-checker anywhere in the estate** — no mypy, ruff, flake8, black, isort or tox config. Instead, `Type_Safe` from `osbot-utils` validates at construction. Of 1,034 classes in the new tree: 506 extend `Type_Safe` directly, plus `Type_Safe__List` (44), `Fast_API__Routes` (46) and `Schema__Step__Base` (25) which are themselves descendants — and 78 `Safe_Str` + 13 `Safe_Int` + 6 `Safe_UInt` primitives, 169 `TestCase`, and 77 enums. **Excluding tests and enums, essentially every class is in the `Type_Safe` lineage.** The rule holds; the naive percentage does not show it.

**(b) Constrained primitives instead of validation.** Rule 2 is *"zero raw primitives — no `str`, `int`, `float`, `list`, `dict` as attributes."* The estate has 27 hand-written primitive types in `sg_compute/primitives/` alone, each a regex-constrained subclass. `Safe_Str__IP__Address`, `Safe_Str__Node__Name`, `Safe_Int__Port`, `Safe_Str__SSM__Path`. **The type is the validation**, so a value that exists is a value that is valid, everywhere, forever.

**(c) Alignment as a first-class convention, across languages.** Schema attribute annotations are **100% colon-aligned** (46 of 46 multi-attribute files). CSS property values are aligned to a column. Trailing comments are aligned. This is unusual, it is deliberate, and — see `05__` §3 — there is a good argument that it is a **machine-readability** decision rather than an aesthetic one.

---

## 5. The honesty constraint

`/shipped/` for a coding-standards site means saying what is *not* enforced:

- **Nothing is enforced by tooling.** No linter, no formatter, no type-checker, no pre-commit hook. The four `tests/ci/` structural guards are the entire automated enforcement surface — **and one of them has never worked** (`06__` §4).
- **Import alignment is only 39% consistent** (321 of 817 files with two or more `from X import Y` lines are aligned to a single column). Attribute alignment is 100%; import alignment is not.
- **Rule 9 has 97 violations** in the new tree alone, and the JavaScript uses `_private` methods as a matter of course — so the rule is either Python-only or widely ignored, and the document does not say which.
- **The documented rules live in `.claude/CLAUDE.md`**, which is an agent instruction file, not a published standard. **There is no human-readable style guide anywhere.** That is what this site is for.
- **No JS, CSS, HTML or Bash conventions are documented at all.** All 31 rules are about Python and process. The other four languages have consistent, discoverable conventions that nobody has ever written down.

---

## 6. The numbers

| | |
|---|---|
| **Python** | 3,999 files · 217,266 LOC · 3,871 filenames contain `__` · 1,034 classes in the new tree |
| **Naming families** | `Schema__` 614 · `Safe_Str__` 290 · `Enum__` 185 · `Cli__` 82 · `Routes__` 59 · `Safe_Int__` 18 · `Section__` 15 · `Fast_API__` 12 |
| **Suffix families** | `__Builder` 97 · `__Helper` 86 · `__Client` 77 · `__Service` 46 · `__Mapper` 39 · `__Detector` 23 · `__Loader` 17 · `__Registry` 14 · `__Writer` 14 |
| **One class per file** | **187 of 208** sampled (90%) |
| **Banners** | 3,120 of 3,999 files · **100%** of class-defining files in the new tree |
| **JavaScript** | 50 files · 41 `customElements.define` · 6 `attachShadow` · 48 `type="module"` · **single quotes 4,006 vs double 400** |
| **CSS / HTML** | 38 CSS · 37 HTML · design tokens from a versioned CDN |
| **Bash** | **5 `.sh` files** · **15 `Section__*` shell-generating classes** |
| **Enforcement** | **0 linters** · 4 CI structural guards · **1 of the 4 has never worked** |
| **This pack** | 9 documents · manifest of **20 rows**, every path verified on disk · the conventions as machine-readable JSON |

---

## 7. Build order

1. **`/python/`** — the deepest and the most distinctive. `01__`.
2. **`/rules/`** — the 31 documented rules, with measured compliance beside each. `06__`. **This is the page that makes the site useful rather than decorative**, because it tells a reader which rules are real.
3. **`/javascript/` and `/components/`** — the framework-free web-component pattern and the versioned CDN. Nobody has written this down and it is genuinely original. `02__`.
4. **`/css/` and `/html/`** — `03__`.
5. **`/bash/`** — the generated-shell story. `04__`.
6. **`/for-agents/`** — `05__` §3. The conventions chosen because an LLM reads and writes this code. The most original page available.
7. **`/enforce/`** — the linter configs that would encode the rules, per language. `08__` §1 has the list; it is a day's work and it converts a description into a standard.

Publish the build order unresolved with `08__`'s open questions and tensions visible.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
source: /briefs/01__python.md

==============================================================================


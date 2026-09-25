# coding.sgit.ai — brief pack

**For:** the agent commissioned to build `coding.sgit.ai`
**From:** Dinis Cruz, via the SG/Send Librarian
**Version:** v0.33.62 · 24 August 2026
**Licence:** CC BY 4.0 — the code quoted throughout is **Apache-2.0**. See `LICENSE.md`.

---

## What this is

The coding patterns and formatting across the five languages you work in: **Python, JavaScript, HTML, CSS, Bash.**

Every convention here was **derived from the code by counting**, not from documentation — and where a documented rule and the code disagree, both are reported with the numbers.

---

## The headline

**You already have a written style guide.** `.claude/CLAUDE.md` carries **31 numbered rules** plus 4 non-negotiable testing rules. Measured against 992 class-defining files:

| Rule | Compliance |
|---|---|
| `═══` header on every file | **100%** (992/992) |
| No docstrings, ever | **99.7%** (3 violations) |
| `__init__.py` stays empty | **99%** (299/302) |
| No `_` prefix on private methods | **91%** (97 violations) |

**The site's job is not to invent a style guide — it is to publish the one that exists, with the measurements, and make it enforceable.**

---

## Read in this order

| File | Words | What it does |
|---|---:|---|
| **`00__BRIEF.md`** | 1.2k | **Start here.** The headline, the five languages in a paragraph each, what makes the style unusual, the numbers, the build order |
| **`01__python.md`** | 1.5k | The deepest language. The complete 11-line example, naming families, `Type_Safe`, constrained primitives, alignment, testing, responsibility boundaries |
| **`06__the-rules-and-compliance.md`** | 1.1k | **The page that makes the site useful** — all 31 rules with measured compliance, and the guard that never worked |
| `02__javascript.md` | 1.2k | The framework-free component system, the three-file triplet, the versioned CDN — **undocumented anywhere** |
| `03__html-and-css.md` | 0.9k | Alignment in CSS, design tokens, `data-*` as the behaviour hook, why shadow DOM makes BEM unnecessary |
| `04__bash-and-generated-shell.md` | 0.9k | **Five `.sh` files in 217k LOC** — shell is generated from 15 typed `Section__*` classes |
| **`05__cross-cutting.md`** | 1.3k | What's shared across all five, and **`/for-agents/`** — the most original page available |
| `07__site-architecture-and-boundaries.md` | 1.0k | Page by page, licensing, redaction, network boundaries |
| `08__gaps-and-open-questions.md` | 1.2k | An 8-item enforcement fix list, 7 build-fresh items, 7 open questions, 6 tensions |
| `09__source-manifest.csv` | 20 rows | Every source, tiered 0–3. **Every path verified on disk** |
| `conventions__machine-readable.json` | — | Every count and rule as structured data — for generating the site's pages |
| `LICENSE.md` | — | CC BY 4.0, the Apache-2.0 distinction, and the redaction list |

---

## The four things worth knowing before you write

**1. There is no linter, formatter or type-checker anywhere in the estate.** No mypy, ruff, flake8, black, isort, tox — no config at all. Type safety is enforced *at runtime* by `Type_Safe`, which is a real and defensible choice. The four `tests/ci/` structural guards are the entire automated enforcement surface — **and one of them has never worked**: `test_no_legacy_imports.py` uses `sgraph_ai_service_playwright[^_]`, which cannot match the real double-underscore package. Verified: **0 files matched, 228 real imports across 69 files.**

**2. Four of the five languages have zero documented rules.** All 31 are Python and process. JavaScript, CSS, HTML and Bash have consistent, discoverable conventions that nobody has written down — reconstructing them by counting is most of what `02__`–`04__` did.

**3. Alignment is the estate's most visible convention and its least explained.** Schema attribute colons are **100% aligned**; CSS property values are aligned per block; imports are only **39%**. `05__` §3 makes the argument that alignment is a *machine-readability* decision in a codebase **61% written by an agent** — that is a claim, it is falsifiable, and it should be published as a position with the evidence attached.

**4. Bash barely exists.** Five `.sh` files in 217,266 lines. Shell is **generated** from 15 `Section__*` Python classes, each with a `TEMPLATE` and a `render()`. The trade — testable parameters and no quoting hell, against no `shellcheck` and no directly-runnable script — is worth arguing rather than just reporting. Both mitigations are cheap and neither exists yet.

---

## The most original page available

`/for-agents/` — `05__` §5. Several conventions only make sense once you accept that an LLM is a primary reader and writer:

runtime validation catches a generated mistake at the point of the mistake · constrained primitives encode the domain in the type name · one class per file with filename = class name means a model can locate any symbol by path construction alone · fully-qualified imports with no re-exports means there is exactly one import path to invent · explicit single-owner responsibility rules stop a generator putting a call in a reasonable-looking wrong place · and the markdown twin exists so *"a traversing agent never has to parse HTML."*

There is even direct evidence in the filenames: `library/dependencies/osbot-utils/type_safe/v3.1.1__**for_llms**__type_safe__testing_guidance.md`.

This connects straight to `open-source.sgit.ai` — that site has the argument, this one has the artefact.

---

## House pattern

Copy `pki.sgit.ai`, add the `/llms-full.txt` it lacks, and add one rule specific to this site:

> **Every code example and every count is extracted from the repo at build time, with a path and a commit reference.**

A style guide whose examples have drifted from the code is worse than no style guide.

---

This file is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
source: /briefs/00__BRIEF.md

==============================================================================


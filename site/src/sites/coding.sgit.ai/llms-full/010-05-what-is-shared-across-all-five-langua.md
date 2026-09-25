# 05 — What is shared across all five languages

The languages look different. The instincts underneath them are the same four, and naming them is what turns a set of per-language pages into a coherent house style.

---

## 1. One idea per file, and the filename says which

**Python:** the filename *is* the class name. `Schema__Caller__IP.py` → `class Schema__Caller__IP`. 187 of 208 sampled files define exactly one class; 3,871 of 3,999 filenames carry the `__` separator. `__init__.py` stays empty in 299 of 302 packages, so there is no re-export layer to hide behind.

**JavaScript:** one component per directory, and the directory, the three files, the class and the custom element all carry the same name — `sg-compute-left-nav`.

**CSS and HTML:** the component's sibling files, same basename.

**Bash:** one `Section__*` class per boot concern.

**The rule to publish:** *a name should let you find the file, and a file should contain one thing.* Everything else — the double underscores, the empty `__init__.py`, the fully-qualified imports, the triplet — follows from wanting that to be true without a search index.

---

## 2. Banners, and the three characters

Every file opens with a comment block naming what it is and why it exists.

| Language | Character | Form |
|---|---|---|
| Python | `═` | `# ═══…` × 79, product — class — purpose |
| Generated shell | `─` | `# ── Auto-terminate after 1h ──…` |
| JS shared modules | `─` | `// ── launch-defaults.js — canonical launch constants ──…` |
| JS components | JSDoc | `/** … @module … @version */` |

**One idea, four expressions.** The Python form is documented (rule 7, with the sharp caveat that it is *Python files only* because `#` is Markdown heading syntax and a banner renders as a stack of H1s on GitHub). The other three are conventions nobody has written down.

**Recommendation for the site:** publish the shape as the rule — *a banner names the file, its owner and its purpose in three lines* — and let the comment character follow the language. Then fix the JS inconsistency (`02__` §6) so components and shared modules agree.

---

## 3. ⚠️ Alignment — and the argument that it is for machines

This is the estate's most visible and least explained convention.

| Where | Measured |
|---|---|
| Python schema attribute colons | **100% aligned** — 46 of 46 |
| Python class attribute values | aligned |
| Python trailing comments | aligned |
| Python `from X import Y` | **39% aligned** — 321 of 817 |
| CSS property values | aligned per block |
| JS object literal keys | aligned |

The usual case for alignment is aesthetic and it is usually a bad trade: it produces noisy diffs when the longest name changes, and it is why `gofmt` and `black` refuse to do it.

**There is a better argument available here, and the site should make it.** This is a codebase where **61% of commits were written by an agent** and where the stated house position is that *"someone still needs to understand what is underneath."* Aligned columns turn a class body into a table. A reader — human or model — scanning `Safe_Str__IP__Address` sees five attributes and five values as two columns rather than five sentences. The same is true of a schema's field list and a CSS block's property list.

**That is a claim, and it is falsifiable**, which is the right shape for a page here: alignment costs diff noise and buys scanability, and the estate has decided the trade is worth it. Say so, with the numbers, and note the one place it is not being kept — imports at 39%.

**And note the discipline is per-block, not per-file.** In CSS, `.left-nav` and `.nav-item` align to different columns, each set by its own longest property. The unit of alignment is the thing you read at once.

---

## 4. Single source of truth, enforced by structure

The same instinct appears in every language, each time with a mechanism rather than a convention:

- **`version` at the repo root** — read at runtime by `consts/version.py` and every `manifest.py`, and used as the Docker tag. One file, many consumers.
- **`manifest.py` per spec** — *"Single source of truth. Every spec's `manifest.py` exposes `MANIFEST`."*
- **`launch-defaults.js`** — `Object.freeze` on every export, with a comment naming the consumers: *"Update here only — do not duplicate locally."*
- **`sg-tokens.css`** — no literal colour in any component stylesheet.
- **The versioned CDN path** — `/v1/v1.0/v1.0.0/` as directories, so a URL is an immutable identity and there is no lockfile to drift.
- **Empty `__init__.py`** — no re-export layer, so there is exactly one import path to any class.

**The pattern to publish:** *duplication is prevented by making the second copy impossible to write, not by asking people not to write it.*

---

## 5. Writing code for agents — the most original page available

Several conventions only make sense once you accept that an LLM is a primary reader and writer of this code. Nobody has written this page, and it is the one that would distinguish `coding.sgit.ai` from every other style guide.

**The evidence, gathered from across the estate:**

- **61% of the sg-compute repo's 2,777 commits were authored by Claude**, 30% by a human. The code was largely written by a model, under these rules.
- **`Type_Safe` validates at construction.** A model that produces a wrong-shaped object gets an error at the point of the mistake, not three layers away. **Runtime validation is a better fit for generated code than static typing**, because the feedback arrives during execution rather than during a separate check the generator may never run.
- **Constrained primitives encode the domain in the type name.** `Safe_Str__SSM__Path` tells a model what the value is without a comment, a docstring or a lookup.
- **No docstrings, banners instead** (rule 8). A banner at the top of a one-class file is a fixed, findable location for the purpose; docstrings scatter it.
- **One class per file, filename = class name.** A model can locate any symbol by path construction alone, with no index and no grep.
- **Fully-qualified imports, no re-exports.** There is exactly one import path for anything, so the model cannot invent a plausible-but-wrong one.
- **Explicit responsibility boundaries** (rules 16–19) — *"`Step__Executor` is the ONLY class that calls `page.*`"* — with a CI guard behind one of them. This is how you stop a generator putting a call in a reasonable-looking wrong place.
- **The markdown twin at every URL**, so *"a traversing agent never has to parse HTML"* — an HTML convention that exists purely for machine readers.
- **Aligned columns**, per §3.

**The thesis for the page:** these are not stylistic preferences that happen to suit agents. They are **a coherent design for a codebase whose main author is a model and whose main reviewer is a human**, and they trade a little human convenience — no docstrings, more files, more typing — for a lot of machine predictability.

That argument connects directly to `open-source.sgit.ai`'s *"someone still needs to understand what is underneath"* and to its unwritten agent-era theses. **Cross-link them; this site has the artefact and that one has the argument.**

---

## 6. The house prose rules that touch code

Three conventions govern the documents *around* the code and belong on the site because they apply to anything an engineer writes here:

- **No em-dashes** in briefs. *"All documents are em-dash-free and released under CC BY 4.0."*
- **A CC BY 4.0 footer** on every markdown document — ~1,100+ files carry it.
- **Version-prefixed filenames** — `v0.33.54__arch-brief__sg-send-<slug>.md`. Version, then type, then slug. It sorts chronologically, it says what kind of document it is before you open it, and it is the same *name-tells-you-what-it-is* instinct as `Schema__` and `Section__`.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
source: /briefs/06__the-rules-and-compliance.md

==============================================================================


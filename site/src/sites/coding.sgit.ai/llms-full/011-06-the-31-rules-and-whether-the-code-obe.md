# 06 — The 31 rules, and whether the code obeys them

`.claude/CLAUDE.md` in the sg-playwright repo carries **31 numbered rules** plus 4 non-negotiable testing rules. **This is the single most valuable artefact for the site**, and it has two problems: it lives in an agent instruction file rather than a published standard, and **nobody has ever measured compliance.**

This document measures it.

---

## 1. Code Patterns — rules 1–9

| # | Rule (abridged) | Measured | Verdict |
|---|---|---|---|
| **1** | All classes extend `Type_Safe` — no plain Python classes | 506 direct + descendants; excluding 169 `TestCase` and 77 enums, **essentially all** | ✅ holds |
| **2** | Zero raw primitives — no `str`/`int`/`float`/`list`/`dict` as attributes | 27 constrained primitives in `sg_compute/primitives/` alone | ✅ by design |
| **3** | No `Literal`s — fixed value sets use `Enum__*` | **185 `Enum__*` files** | ✅ |
| **4** | Schemas are pure data — no methods | 614 `Schema__*` files | ✅ spot-checked |
| **5** | Collection subclasses are pure type definitions | 44 `Type_Safe__List` subclasses | ✅ |
| **6** | Every route returns `.json()` on a Type_Safe schema — no raw dicts | 46 `Fast_API__Routes` subclasses | ✅ spot-checked |
| **7** | `═══` 80-char headers — every file, **Python only** | **992 of 992** class-defining files in the new tree | ✅ **100%** |
| **8** | Inline comments only — **no docstrings, ever** | 3 violations in 992 | ✅ **99.7%** |
| **9** | No underscore prefix for private methods | **97 violations in 992** | ⚠️ **91%** — and JS violates it universally |

**Rule 9 is the one to resolve.** The JavaScript uses `_private` as a matter of course (`_select`, `_update`, `_current`), so either the rule is Python-only and should say so, or it is being ignored in two languages. `08__` Q2.

---

## 2. The other rule groups

**Security (10–13).** *Evaluate is allowlist-gated* — `JS__Expression__Allowlist` defaults to deny-all, **and this one has a CI guard behind it**. *No arbitrary code execution* — the shell-server pattern from OSBot-Playwright is explicitly not carried forward. *No AWS credentials in Git*, *no vault keys in Git* — with the operational instruction *"If one appears in a diff, block the commit."*

**AWS naming (14–15).** Both are scar tissue and both are worth publishing verbatim, because they are the kind of thing nobody knows until it costs them a day:

> **14.** *Security group `GroupName` must NOT start with `sg-`. AWS reserves the `sg-*` prefix for security group IDs and rejects `CreateSecurityGroup` with `InvalidParameterValue`.*
>
> **15.** *AWS Name tag — never double-prefix. When the logical name already carries the namespace (e.g. `elastic-quiet-fermi`), do not wrap it again into `elastic-elastic-quiet-fermi`.*

Each names the helper that implements the fix. **A rule that cites its own precedent is a rule people can trust.**

**Responsibility boundaries (16–19).** Covered in `01__` §7. Four rules, each naming exactly one owner for a capability; **one of the four has a CI guard.**

**Class and file naming (20–22).** The `SGraph-AI` → `SGraph_AI` normalisation, one class per file, empty `__init__.py`. Rule 21 carries the useful carve-out: *"Registries (module-level constants + helper functions, e.g. `STEP_SCHEMAS`) are the one exception — they live in a single `*_registry.py` because **they are logic, not a schema**."*

**Process (23–31).** Human-only folders that agents must never write to, the good-failure/bad-failure debrief convention, session handover, branch naming `claude/{description}-{session-id}`, and *"agents never push to `dev` directly."* These are agent-workflow rules rather than code style — but they belong on the site, because **they are the rules that make a mostly-agent-written codebase safe to review.**

---

## 3. Where the code and the docs disagree

Five, in order of how much they matter:

1. **Rule 9 vs the JavaScript.** 97 Python violations, and universal `_private` in JS. **Decide whether the rule is Python-only.**
2. **No JS, CSS, HTML or Bash rules exist at all.** All 31 are Python and process. The other four languages have discoverable, consistent conventions that are entirely undocumented — which is most of what `01__`–`04__` had to reconstruct by counting.
3. **Import alignment is 39%.** Not a documented rule at all, and the estate's least consistent formatting behaviour.
4. **`set -e` in 2 of 5 `.sh` files**, in three different forms. No rule covers it.
5. **Semicolons in JS** — `components/` says no, `shared/` says yes. No rule covers it.

---

## 4. ⚠️ Enforcement — four guards, and one has never worked

`tests/ci/` is the **entire** automated enforcement surface. There is no linter, no formatter and no type-checker anywhere in the estate.

| Guard | Enforces | State |
|---|---|---|
| `test_no_object_none_annotations` | bans `: object = None` in favour of `Optional[T] = None` | ✅ works, with a one-file allowlist and a stated reason |
| `test_sg_compute_ami_picker__snapshot` | the live-fetch contract of a web component | ✅ |
| `test_sg_compute_spec_detail__snapshot` | a web component's structure | ✅ |
| `test_wheel_contains_ui` | that the built wheel actually contains per-spec UI assets | ✅ catches a package-data glob regression |
| **`test_sg_compute_does_not_import_legacy`** | that the new tree never imports the legacy one | ❌ **has never worked** |

The regex is `sgraph_ai_service_playwright[^_]` — and `[^_]` requires a **non-underscore** after the stem, while the real package is `sgraph_ai_service_playwright__cli`, with two. Verified this session:

```
GUARD regex  : 0 files -> test PASSES (vacuously)
REAL imports : 69 files, 228 import lines
FIXED regex (drop [^_]): 69 files -> test FAILS, as intended
```

**Publish this.** A guard that passes because it cannot match what it guards against is the strongest possible argument for the `/enforce/` page: a rule without a working test is a suggestion, and you cannot tell the difference from the outside.

Note also what the working guards have in common: **each one encodes a rule that was violated at least once.** The `object = None` ban, the UI-in-wheel check, the component snapshots. That is the right way to grow a guard set — from incidents, not from a checklist.

---

## 5. How to publish the rules

1. **One page per rule group**, with the rule verbatim, the measured compliance, and — where one exists — the guard that enforces it.
2. **A compliance badge per rule.** ✅ enforced by a test · 🟡 documented, unenforced, high compliance · ⚠️ documented, unenforced, violated · ❌ undocumented convention. That single column is the difference between a style guide and a wish list.
3. **Add the four missing languages.** `02__`–`04__` are the raw material; they are conventions in the code that have never been rules.
4. **Cite the precedent.** Rules 14, 15, 21 and the `object = None` guard all name the case that motivated them. Do it for every rule where a case exists — it is what makes a rule survive contact with someone who disagrees with it.
5. **Publish the compliance numbers, including the bad ones.** 91% on rule 9 and 39% on import alignment are more useful to a reader than a claim of consistency.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
source: /briefs/07__site-architecture-and-boundaries.md

==============================================================================


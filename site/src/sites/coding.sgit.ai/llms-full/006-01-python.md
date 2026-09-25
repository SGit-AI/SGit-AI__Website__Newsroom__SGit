# 01 — Python

217,266 lines across 3,999 files. The most distinctive style in the estate, and the one with a written rule set behind it.

---

## 1. The complete example — everything in eleven lines

`sg_compute/catalog/schemas/Schema__Caller__IP.py`, verbatim and entire:

```python
# ═══════════════════════════════════════════════════════════════════════════════
# SG/Compute — Schema__Caller__IP
# Response schema for GET /catalog/caller-ip.
# ═══════════════════════════════════════════════════════════════════════════════

from osbot_utils.type_safe.Type_Safe                                          import Type_Safe

from sg_compute.primitives.Safe_Str__IP__Address                             import Safe_Str__IP__Address


class Schema__Caller__IP(Type_Safe):
    ip : Safe_Str__IP__Address = Safe_Str__IP__Address()
```

Nine conventions are visible in that file, and the whole style follows from them:

1. **A `═══` banner header** — product name, class name, one line of purpose
2. **The filename is the class name.** `Schema__Caller__IP.py` → `class Schema__Caller__IP`
3. **One class per file**
4. **Fully-qualified imports** from the per-class path — never a package re-export
5. **`import` keywords aligned to a column**
6. **`Type_Safe` as the base class**
7. **A constrained primitive** (`Safe_Str__IP__Address`) rather than `str`
8. **The annotation colon aligned**, with an instance as the default
9. **No docstring.** The banner does that job

---

## 2. Naming

### Prefix families — what the class *is*

| Prefix | Files | Meaning |
|---|---:|---|
| `Schema__` | **614** | Pure data. **No methods** (rule 4) |
| `Safe_Str__` | **290** | A regex-constrained string type |
| `Enum__` | **185** | A fixed value set. **Never a `Literal`** (rule 3) |
| `Cli__` | 82 | A Typer command group |
| `Routes__` | 59 | A FastAPI route class. **No logic** (rule 19) |
| `Safe_Int__` | 18 | A bounded integer type |
| `Section__` | 15 | A shell fragment generator — see `04__` |
| `Fast_API__` | 12 | An app assembly |

### Suffix families — what the class *does*

`__Builder` 97 · `__Helper` 86 · `__Client` 77 · `__Service` 46 · `__Mapper` 39 · `__Detector` 23 · `__Loader` 17 · `__Registry` 14 · `__Writer` 14 · `__Parser` 10 · `__Runner` 9 · `__Manager` 7 · `__Factory` 4 · `__Watchdog` 2 · `__Poller` 1

### The double-underscore rule

**`__` is the word separator inside a compound name; `_` separates words within one term.** `Schema__Image__Build__Request` reads as *Schema · Image · Build · Request*. `Safe_Str__IP__Address` keeps `Safe_Str` as one term. **3,871 of 3,999 filenames contain `__`.**

The documented normalisation (rule 20) handles the one hard case: the spec uses names like `SGraph-AI` with a hyphen, which is not a legal Python identifier. **Class and module names use `SGraph_AI`; repo roots and test filenames may keep `SGraph-AI`.**

### `__init__.py` stays empty

Rule 22, and it holds at **299 of 302 (99%)**. Callers import from the fully-qualified per-class path; nothing is ever re-exported. The rule carries its own warning, learned the hard way: *"Never commit an empty `__init__.py` in a folder that shares a name with a sibling `.py` module: Python's import system prefers the package and every import under the module breaks."*

---

## 3. `Type_Safe` — runtime validation instead of static typing

From `osbot-utils`. Rule 1: **all classes extend it — no plain Python classes.** Rule 82 of the tooling table is blunter: *"**Never use Pydantic. No Literals.**"*

Of 1,034 classes in the new tree:

| Base | Count |
|---|---:|
| `Type_Safe` | 506 |
| `TestCase` | 169 |
| `Safe_Str` | 78 |
| `str, Enum` | 69 |
| `Fast_API__Routes` *(a Type_Safe descendant)* | 46 |
| `Type_Safe__List` | 44 |
| `Schema__Step__Base` *(a Type_Safe descendant)* | 25 |
| `Safe_Int` / `Safe_UInt` / `Enum` | 27 |

**Excluding tests and enums, essentially every class is in the `Type_Safe` lineage.** Do not publish "48% extend Type_Safe" — it is true and it is misleading.

What it buys: attributes are validated at construction, so **a value that exists is a value that is valid**. There is no separate validation layer, no schema-parse step at the boundary, and no `if not isinstance(...)` scattered through the code. It is also why the absence of a type-checker matters less here than it would elsewhere — though see `08__` §1.

---

## 4. Constrained primitives — the type *is* the validation

Rule 2: *"zero raw primitives — no `str`, `int`, `float`, `list`, `dict` as attributes."*

`sg_compute/primitives/` alone holds 27, and the pattern is uniform:

```python
# ═══════════════════════════════════════════════════════════════════════════════
# SG/Compute — Safe_Str__IP__Address
# IPv4 address string, e.g. "1.2.3.4". Empty = not yet assigned.
# ═══════════════════════════════════════════════════════════════════════════════

import re

from osbot_utils.type_safe.primitives.core.Safe_Str                         import Safe_Str
from osbot_utils.type_safe.primitives.core.enums.Enum__Safe_Str__Regex_Mode import Enum__Safe_Str__Regex_Mode


class Safe_Str__IP__Address(Safe_Str):
    max_length        = 45                                                   # covers IPv4 + IPv6
    regex             = re.compile(r'^[0-9a-fA-F.:]*$')
    regex_mode        = Enum__Safe_Str__Regex_Mode.MATCH
    strict_validation = True
    allow_empty       = True
```

Five class attributes, all aligned, and a **trailing comment carrying the reasoning** (`# covers IPv4 + IPv6`) — which is the estate's substitute for a docstring.

The domain vocabulary is visible in the file list: `Safe_Str__AWS__Region`, `Safe_Str__Docker__Image`, `Safe_Str__Instance__Type`, `Safe_Str__Node__Name`, `Safe_Str__Pod__Name`, `Safe_Str__SSM__Path`, `Safe_Str__Spec__Id`, `Safe_Int__Port`, `Safe_Int__Max__Hours`, `Safe_Int__Exit__Code`.

**Naming a type is how a domain concept gets recorded.** That is the argument for the page.

---

## 5. Layout and formatting

**Banners.** `# ═` × 79, three content lines (product — class name — purpose), `# ═` × 79. Present on **3,120 of 3,999 files**, and **100% of the 992 class-defining files in the new tree.** Rule 7 adds a caveat learned from GitHub: *"**Python files only.** In Markdown, `#` is heading syntax — a `# ═══` header block renders as a stack of H1s."*

**Alignment.** Measured:

- **Schema attribute colons: 100% aligned** — 46 of 46 files with two or more annotated attributes
- **Class attribute values: aligned** — see the `Safe_Str` example
- **Import keywords: 39% aligned** — 321 of 817 files with two or more `from X import Y` lines have every import at a single column. **This is the estate's least consistent formatting rule and the easiest to automate.**

**Comments.** Rule 8: *"inline comments only — no docstrings, ever."* Compliance is **99.7%** — 3 violations in 992 files. Trailing comments carry the reasoning; the banner carries the purpose.

**Private methods.** Rule 9: *"no underscore prefix for private methods."* Compliance is **91%** — 97 files in the new tree use `def _method`. Either the rule is Python-only-and-widely-ignored, or it needs revisiting. The document does not say. `08__` Q2.

---

## 6. Testing

Rule set, verbatim, from *Testing — Non-Negotiable*:

> 1. **No mocks. No patches.** Use `register_playwright_service__in_memory()` and `in_memory_stack`-style composition.
> 2. **Assert on contracts** — schemas, status codes, persisted artefacts — not implementation details.
> 3. **Real Chromium for integration tests.** Gate on `SG_PLAYWRIGHT__CHROMIUM_EXECUTABLE`; skip cleanly when absent.
> 4. **Deploy-via-pytest.** Deploy tests are numbered (`test_1__create_lambda`, `test_2__invoke__health_info`, …) and run top-down.

**"No mocks, no patches" is the strongest opinion in the whole rule set** and it deserves its own page. The alternative is real in-memory composition, which is only affordable because `Type_Safe` objects are cheap to build — the type system and the testing philosophy are the same decision.

169 classes extend `TestCase`, so tests are class-based. And **4,785 tests run in 81 seconds**, which is the evidence that the no-mocks position is affordable rather than aspirational.

---

## 7. Responsibility boundaries — rules that name a single owner

Rules 16–19 are unusual and worth publishing as a pattern:

> 16. **`Step__Executor` is the ONLY class that calls `page.*` Playwright methods** (with a `Browser__Launcher` carve-out for process lifecycle)
> 17. **`Artefact__Writer` is the ONLY class that writes to sinks**
> 18. **`Request__Validator` contains ALL cross-schema validation**
> 19. **Routes have no logic** — pure delegation to `Playwright__Service`

Each names exactly one owner for a capability, and rule 16 is **enforced by a CI guard** that fails the build if any raw `browser.new_context(` appears outside `Page__Factory`. That is the model: **a boundary rule with a test behind it.** Three of the four have no such test.

---

## 8. What a linter config would encode

Ordered by value, for `/enforce/`:

1. **Import alignment** — the 61% gap, and the only formatting rule that is measurably inconsistent
2. **No docstrings** — trivial (`ruff` D-rules inverted), currently 3 violations
3. **Banner present and well-formed** — a custom check, ~20 lines
4. **Filename equals class name, one class per file** — a custom check
5. **No raw primitives as class attributes** — the highest-value rule and the hardest to express; probably a custom AST check
6. **Ban `Pydantic`, `Literal`, direct `boto3`** — three import bans, one line each
7. **`__init__.py` empty** — trivial
8. **No `_` prefixed methods** — trivial, but **decide the rule first** (§5)

Items 2, 6 and 7 are a single `ruff` config block. Items 1, 3, 4, 5 and 8 are a small `tests/ci/` module in the style of the four that already exist.

---

## 9. Dependencies — the `osbot-*` family

`osbot-utils` (the source of `Type_Safe` and `Safe_Str`, 885 mentions across the corpus), `osbot-aws`, `osbot-fast-api`, `osbot-fast-api-serverless`, `memory_fs`, `mgraph-db`, `mgraph-ai-service-cache`. All Apache-2.0, all under the `owasp-sbot` GitHub organisation.

Two hard rules govern their use:

> **Type system** — `Type_Safe` from `osbot-utils`. **Never use Pydantic. No Literals.**
> **AWS operations** — `osbot-aws`. **Never use boto3 directly** (narrow documented exception for the Lambda Function URL two-statement permission fix).

**Note the exception is documented rather than silent.** That is a convention in itself and worth naming on the site: a banned thing with one written carve-out, rather than a banned thing with quiet violations.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
source: /briefs/02__javascript.md

==============================================================================


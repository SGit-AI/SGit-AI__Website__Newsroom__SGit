# 08 — Gaps, open questions and honest tensions

---

## 1. The enforcement gap — a day's work that changes what the site can claim

There is **no linter, no formatter and no type-checker anywhere in the estate.** Ordered by value:

| # | Fix | Effort |
|---|---|---|
| **F1** | **Delete `[^_]` from `test_no_legacy_imports.py`** — the guard has never worked; 228 real imports across 69 files | 4 characters |
| **F2** | **A `ruff` config** encoding: no docstrings, ban `pydantic` / `Literal` / direct `boto3`, empty `__init__.py` | one config block |
| **F3** | **Import alignment** — the 39% number, and the only formatting rule that is measurably inconsistent | a formatter rule or a `tests/ci` check |
| **F4** | **`shellcheck` on rendered `Section__*` output** — the generated shell is currently unlintable because it is never rendered outside production | a test |
| **F5** | **`eslint`** — 4-space, single quotes, no semicolons, plus a check that every component directory has all three of `.js`/`.html`/`.css` | half a day |
| **F6** | **`stylelint`** — the highest-value CSS rule is **no literal colours outside the token file** | an hour |
| **F7** | **A banner check** — present, well-formed, three content lines | ~20 lines |
| **F8** | **Filename == class name, one class per file** | ~20 lines |

F1 and F4 are the two that would catch real defects today. F2, F6 and F7 are close to free.

---

## 2. Build-fresh items

| # | Item | Why |
|---|---|---|
| **G1** | **Rules for JS, CSS, HTML and Bash** | All 31 documented rules are Python and process. The other four languages have consistent, discoverable conventions and **zero written rules** |
| **G2** | **A human-readable style guide** | The rules live in `.claude/CLAUDE.md`, an agent instruction file. There is no published standard anywhere. **This is the site** |
| **G3** | **The `/for-agents/` argument** | `05__` §5. Named nowhere, and the thing that explains why the rest looks the way it does |
| **G4** | **A worked "add a new spec" walkthrough** | The generalisation mechanisms are real (`manifest.py`, route loader, CLI builder). Nobody has written the tutorial that uses them |
| **G5** | **A worked "add a new component" walkthrough** | Same for the JS triplet + CDN pattern |
| **G6** | **Golden rendered shell files** | Commit one per `Section__*` so a reviewer sees the actual shell, not the template |
| **G7** | **A decision record format** | Rules 14, 15 and 21 are scar tissue with the precedent cited inline. That is an ADR in all but name — give it a shape |

---

## 3. Open questions

| # | Question | Where it stands |
|---|---|---|
| **Q1** | **Is alignment for humans or for machines?** `05__` §3 makes the machine-readability argument. It is a claim, not an established fact, and it is falsifiable | The honest page says: it costs diff noise, it buys scanability, here is why we think the trade is worth it in a codebase 61% written by an agent |
| **Q2** | **Is rule 9 (no `_private`) Python-only?** | 97 Python violations; universal in JS. **The document does not say, so in practice it is neither enforced nor retired** |
| **Q3** | **Which token prefix?** `--bg-panel`, `--sg-surface`, `--sgl-tab-h` — three families for one system | Pick one, or document what each means. The numbered ramps (`--text-1..4`, `--sg-sp-1..4`) are the good part and should be kept either way |
| **Q4** | **Should a public coding standard document a `dev.` host?** | Every component example imports from `dev.tools.sgraph.ai`. Redacting it teaches nothing; publishing it documents a `dev.`-prefixed contract as canonical. `07__` §4 |
| **Q5** | **Does runtime type safety replace static analysis, or defer it?** | `Type_Safe` catches shape errors at construction. It does not catch unreachable code, unused imports, shadowed names or a typo in a branch never executed. **The honest answer is that it replaces one kind of checking and the other kind is simply absent** |
| **Q6** | **Is "no mocks, no patches" affordable outside this estate?** | It works here — 4,785 tests in 81 seconds — because `Type_Safe` objects are cheap and there is an in-memory composition path. Whether it generalises is a real question and the site should not assume it does |
| **Q7** | **Does the no-build-step position survive the next dependency?** | 50 files, one level of imports, no CJS-only package yet. `02__` §5 names where it stops working |

---

## 4. Honest tensions

1. **31 written rules and zero enforcement.** High compliance on most of them — 100%, 99.7%, 99% — achieved by discipline rather than tooling. That is impressive and it is fragile, and the one guard that was supposed to hold a line **had never worked**.

2. **A style guide for five languages that documents one.** Python has 31 rules. JavaScript, CSS, HTML and Bash have consistent conventions and no rules at all — which means they are currently maintained by whoever last read the neighbouring file.

3. **Alignment is either the best or the worst convention here.** No formatter in the industry will produce it, so adopting it means never adopting `black`, `prettier` or `gofmt`-style tooling. That is a real, permanent cost accepted for a benefit that has not been measured.

4. **The rules were written for agents and are published to none.** `.claude/CLAUDE.md` is read by every session and by no human who has not gone looking for it.

5. **Runtime validation is a good fit for generated code and a poor substitute for a linter.** Both are true, and the estate currently has the first and not the second.

6. **The most interesting page is the least verifiable.** `/for-agents/` is the original contribution, and its central claim — that these conventions suit a model reader — is asserted from design intent and commit statistics, not from measurement. **Publish it as a position with the evidence attached, not as a finding.**

---

## 5. Loose ends worth an hour each

- **Confirm whether a second theme file exists.** The token names suggest dark-first; this pack could not verify a light theme.
- **Count how many components exist outside the sg-compute tree.** The CDN serves `base`, `tokens`, `vault-client`, `vault-write` — is there a wider registry?
- **Check whether `SgComponent`'s source is public.** Every example imports it; if it is not readable, the pattern cannot be adopted by anyone outside.
- **Resolve the `sp-cli:` event namespace** — 23 files, legacy naming, and renaming it breaks external listeners.
- **Decide the semicolon rule** and reformat `shared/` to match `components/`.
- **Write down the `set -euo pipefail` rule** — 2 of 5 files, three different forms, no rule.
- **Extract the four `tests/ci/` guards into a reusable module.** They are the pattern the `/enforce/` page recommends, and they currently live only in one repo.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
source: /briefs/09__source-manifest.csv

==============================================================================


tier,area,path,what,publishability,why_it_matters
0,THE RULES,.claude/CLAUDE.md,31 numbered rules + 4 testing rules,EXTRACT,"THE SINGLE MOST VALUABLE ARTEFACT. Lives in an agent instruction file, not a published standard. Compliance measured in 06__ - never measured before."
0,python: the complete example,sg_compute/catalog/schemas/Schema__Caller__IP.py,11 lines showing 9 conventions,clean,"Banner, filename=class, one class, fully-qualified aligned imports, Type_Safe, constrained primitive, aligned colon, no docstring. Quote it entire."
0,python: the primitive pattern,sg_compute/primitives/Safe_Str__IP__Address.py,a regex-constrained string type,clean,THE TYPE IS THE VALIDATION. Five aligned class attributes and a trailing comment carrying the reasoning.
0,python: primitives dir,sg_compute/primitives/,27 constrained types,clean,"The domain vocabulary made visible: AWS__Region, Docker__Image, Instance__Type, Node__Name, Pod__Name, SSM__Path, Spec__Id, Port, Max__Hours, Exit__Code."
0,js: the complete component,sgraph_ai_service_playwright__api_site/components/sg-compute/sg-compute-left-nav/v0/v0.1/v0.1.0/,the .js/.html/.css triplet,REDACT CDN?,"THE FRAMEWORK-FREE COMPONENT PATTERN, undocumented anywhere. SgComponent, static jsUrl = import.meta.url, onReady(), shadow DOM, versioned CDN imports. See 07__ section 4 on the dev.tools.sgraph.ai question."
0,js: single source of truth,sgraph_ai_service_playwright__api_site/shared/launch-defaults.js,Object.freeze constants,clean,'Single source of truth... Update here only - do not duplicate locally.' The same instinct as manifest.py and the repo-root version file.
0,bash: the generated-shell pattern,sg_compute/platforms/ec2/user_data/Section__Shutdown.py,"a Section class, entire",clean,"FIVE .sh FILES IN 217k LOC. Shell is generated from typed Python. The banner documents the coupling to EC2__Launch__Helper, not just the purpose."
0,bash: the fifteen sections,sg_compute/platforms/ec2/user_data/,15 Section__* classes,clean,"Composition is a list, not a template with conditionals - which is why there is no {% if gpu %} anywhere."
0,THE BROKEN GUARD,tests/ci/test_no_legacy_imports.py,the one-character bug,PUBLISH IT,A guard that passes because it cannot match what it guards against. The strongest possible argument for the /enforce/ page. Verified: 0 vs 228.
1,the working guards,tests/ci/,4 structural guards,clean,The entire automated enforcement surface. Note each encodes a rule that was violated at least once - the right way to grow a guard set.
1,css: the token consumer,sgraph_ai_service_playwright__api_site/components/sg-compute/sg-compute-left-nav/v0/v0.1/v0.1.0/sg-compute-left-nav.css,aligned property values,clean,"The alignment discipline applied to CSS. Also :host first, [hidden] reset, tokens not literals, plain semantic class names."
1,html: the fragment,sgraph_ai_service_playwright__api_site/components/sg-compute/sg-compute-left-nav/v0/v0.1/v0.1.0/sg-compute-left-nav.html,a component fragment,clean,"2-space indent, semantic elements, ARIA everywhere, data-* as the behaviour hook, unicode glyphs."
1,the frontend tree,sgraph_ai_service_playwright__api_site/,"50 js, 38 css, 37 html",REDACT,"The whole component estate. 41 customElements.define, 6 attachShadow, 48 type=module."
1,testing guidance,library/guides/v3.1.1__testing_guidance.md,the full testing rules,clean,"Behind the four non-negotiables: no mocks, no patches, assert on contracts, real Chromium, deploy-via-pytest."
1,markdown doc style,library/guides/v0.2.15__markdown_doc_style.md,the markdown convention,clean,"Why the === banner is Python-only: in Markdown, # is heading syntax and a banner renders as a stack of H1s. Use YAML frontmatter instead."
1,type_safe guidance,library/dependencies/osbot-utils/type_safe/v3.1.1__for_llms__type_safe__testing_guidance.md,Type_Safe for LLMs,clean,NOTE THE FILENAME: 'for_llms'. Documentation written explicitly for a model reader - direct evidence for the /for-agents/ page.
2,the claude-code-web tree,team/humans/dinis_cruz/claude-code-web/,operational detail,REDACT AND USE,"Densest source of the AWS account ID and live hostnames. Redact-and-use, not skip."
3,alchemist tree,library/alchemist/materials/,commercial,DO-NOT-PUBLISH,"Investment figures, valuation, competitive positioning."
3,appsec review,team/roles/appsec/reviews/02/21/v0.5.0__review__pki-architecture-security-revised.md,security review,DO-NOT-PUBLISH,Already classified: 'publishing an attack roadmap for live code'.
3,grc reviews,team/roles/grc/reviews/02/19/,risk acceptance,DO-NOT-PUBLISH,Names a private individual with signature blocks.


==============================================================================
source: /briefs/conventions__machine-readable.json

==============================================================================


{
  "schema": "sgraph-coding-conventions/v1",
  "surveyed": "2026-08-24",
  "method": "Derived by counting from the code, not from documentation. Every number measured this session.",
  "python": {
    "files": 3999,
    "loc": 217266,
    "filenames_with_double_underscore": 3871,
    "prefix_families": {
      "Schema__": 614,
      "Safe_Str__": 290,
      "Enum__": 185,
      "Cli__": 82,
      "Routes__": 59,
      "Safe_Int__": 18,
      "Section__": 15,
      "Fast_API__": 12,
      "Safe_UInt__": 7
    },
    "suffix_families": {
      "__Builder": 97,
      "__Helper": 86,
      "__Client": 77,
      "__Service": 46,
      "__Mapper": 39,
      "__Detector": 23,
      "__Loader": 17,
      "__Registry": 14,
      "__Writer": 14,
      "__Parser": 10,
      "__Runner": 9,
      "__Manager": 7,
      "__Factory": 4,
      "__Watchdog": 2,
      "__Middleware": 1,
      "__Poller": 1
    },
    "class_bases_new_tree": {
      "total": 1034,
      "Type_Safe": 506,
      "TestCase": 169,
      "Safe_Str": 78,
      "str_Enum": 69,
      "Fast_API__Routes": 46,
      "Type_Safe__List": 44,
      "Schema__Step__Base": 25,
      "Safe_Int": 13,
      "Enum": 8,
      "Safe_UInt": 6
    },
    "one_class_per_file": {
      "sampled": 208,
      "exactly_one": 187,
      "pct": 90
    },
    "banners": {
      "repo_files_with_banner": 3120,
      "class_files_in_new_tree": 992,
      "starting_with_banner": 992,
      "pct": 100
    },
    "compliance": {
      "rule_1_type_safe": "essentially all, excluding 169 TestCase and 77 enums",
      "rule_7_banner": "992/992 = 100%",
      "rule_8_no_docstrings": "989/992 = 99.7%",
      "rule_9_no_underscore_private": "895/992 = 91% (97 violations)",
      "rule_22_empty_init": "299/302 = 99%"
    },
    "alignment": {
      "schema_attribute_colons": {
        "files": 46,
        "aligned": 46,
        "pct": 100
      },
      "from_import_keyword": {
        "files": 817,
        "aligned": 321,
        "pct": 39
      }
    },
    "primitives_dir": [
      "Safe_Int__Disk__GB",
      "Safe_Int__Exit__Code",
      "Safe_Int__Hours",
      "Safe_Int__Log__Lines",
      "Safe_Int__Max__Hours",
      "Safe_Int__Pids",
      "Safe_Int__Port",
      "Safe_Int__Uptime__Seconds",
      "Safe_Str__AWS__Region",
      "Safe_Str__Api__Key",
      "Safe_Str__Docker__Image",
      "Safe_Str__IP__Address",
      "Safe_Str__Image__Registry",
      "Safe_Str__Image__Tag",
      "Safe_Str__Instance__Type",
      "Safe_Str__Log__Content",
      "Safe_Str__Message",
      "Safe_Str__Node__Id",
      "Safe_Str__Node__Name",
      "Safe_Str__Ollama__Model",
      "Safe_Str__Platform__Name",
      "Safe_Str__Pod__Name",
      "Safe_Str__SG__Id",
      "Safe_Str__SSM__Path",
      "Safe_Str__Spec__Id",
      "Safe_Str__Stack__Id",
      "Safe_Str__Stack__Name"
    ]
  },
  "javascript": {
    "files": 50,
    "custom_elements_define": 41,
    "attach_shadow": 6,
    "type_module_script_tags": 48,
    "quotes": {
      "single": 4006,
      "double": 400,
      "pct_single": 91
    },
    "semicolons": {
      "lines_with": 401,
      "statement_lines_without": 531,
      "note": "components/ is semicolon-free; shared/ is not"
    },
    "indent": {
      "multiple_of_4": 3791,
      "other": 148
    },
    "banner_files": 15,
    "component_triplet": [
      ".js",
      ".html",
      ".css"
    ],
    "cdn": {
      "host": "dev.tools.sgraph.ai",
      "path_scheme": "/components/<name>/v<major>/v<major>.<minor>/v<major>.<minor>.<patch>/<file>",
      "served": [
        "sg-component.js (SgComponent base)",
        "sg-tokens.css",
        "sg-vault-client.js",
        "sg-vault-write.js"
      ]
    },
    "base_class_contract": {
      "static jsUrl": "import.meta.url \u2014 required, enables self-location",
      "get resourceName()": "basename of sibling .html/.css",
      "get sharedCssPaths()": "tokens and shared sheets",
      "onReady()": "lifecycle hook \u2014 NOT connectedCallback directly"
    },
    "event_namespace": {
      "prefix": "sp-cli:",
      "files": 23,
      "note": "LEGACY NAMING \u2014 a rename surface"
    }
  },
  "css": {
    "files": 38,
    "alignment": "property values aligned per block, column set by the block's longest property",
    "token_prefixes": {
      "unprefixed": [
        "--bg-panel",
        "--border-1",
        "--text-1..4",
        "--text-link",
        "--shadow-1..2",
        "--warn",
        "--warn-soft",
        "--soon"
      ],
      "sg": [
        "--sg-text",
        "--sg-text-muted",
        "--sg-surface",
        "--sg-sp-1..4",
        "--sg-transition-fast"
      ],
      "sgl": [
        "--sgl-tab-h",
        "--sgl-panel-h"
      ]
    },
    "note": "THREE PREFIX FAMILIES FOR ONE TOKEN SYSTEM \u2014 resolve before publishing",
    "naming": "plain semantic class names. NOT BEM, NOT utility classes \u2014 shadow DOM makes both unnecessary"
  },
  "html": {
    "files": 37,
    "indent": 2,
    "note": "deliberately different from the 4 used in JS and CSS",
    "rules": [
      "component markup is a fragment, no html/head/template wrapper",
      "semantic elements, never div onclick",
      "ARIA on every interactive element",
      "data-* is the behaviour hook; classes are for styling; the two never mix",
      "unicode glyphs instead of icon fonts or SVG sprites"
    ]
  },
  "bash": {
    "sh_files": 5,
    "set_e_files": 2,
    "set_e_forms": [
      "set -euo pipefail",
      "set -eu",
      "set -u"
    ],
    "generated_shell": {
      "pattern": "Section__*(Type_Safe) with a single render() -> str and a module-level TEMPLATE",
      "count": 15,
      "sections": [
        "Base",
        "Docker",
        "Sidecar",
        "Nginx",
        "Env__File",
        "GPU_Verify",
        "NVIDIA_Container_Toolkit",
        "Ollama",
        "VLLM",
        "SGit_Venv",
        "Claude_Code__Firstboot",
        "Claude_Launch",
        "Agent_Tools",
        "Node",
        "Shutdown"
      ],
      "conventions": [
        "banner names the coupling, not just the purpose",
        "generated shell gets a # -- banner (box-drawing, not the Python ===)",
        "computation in Python, literals in the emitted shell",
        "bracketed echo breadcrumbs so boot logs are greppable",
        "composition is a list of sections, never a template with conditionals"
      ]
    }
  },
  "enforcement": {
    "linters": 0,
    "formatters": 0,
    "type_checkers": 0,
    "ci_guards": {
      "total": 4,
      "working": 3,
      "broken": 1,
      "list": [
        {
          "name": "test_no_object_none_annotations",
          "enforces": "bans ': object = None'",
          "state": "works"
        },
        {
          "name": "test_sg_compute_ami_picker__snapshot",
          "enforces": "web component live-fetch contract",
          "state": "works"
        },
        {
          "name": "test_sg_compute_spec_detail__snapshot",
          "enforces": "web component structure",
          "state": "works"
        },
        {
          "name": "test_wheel_contains_ui",
          "enforces": "wheel contains per-spec UI assets",
          "state": "works"
        },
        {
          "name": "test_sg_compute_does_not_import_legacy",
          "enforces": "no legacy imports in the new tree",
          "state": "BROKEN \u2014 regex sgraph_ai_service_playwright[^_] cannot match sgraph_ai_service_playwright__cli",
          "measured": "guard matches 0 files; 228 real imports in 69 files; deleting [^_] makes it fail as intended"
        }
      ]
    },
    "documented_rules": {
      "source": ".claude/CLAUDE.md",
      "count": 31,
      "plus": "4 non-negotiable testing rules",
      "groups": [
        "Code Patterns 1-9",
        "Security 10-13",
        "AWS Naming 14-15",
        "Responsibility Boundaries 16-19",
        "Class/File Naming 20-22",
        "Process 23-31"
      ],
      "coverage": "ALL are Python or process. Zero rules for JS, CSS, HTML or Bash."
    }
  },
  "cross_cutting": [
    "one idea per file, and the filename says which",
    "a banner names every file (three characters: === Python, -- shell and JS shared, JSDoc JS components)",
    "alignment as a first-class convention, per block",
    "single source of truth enforced by structure, not by asking",
    "conventions chosen because an LLM is a primary reader and writer"
  ]
}


==============================================================================
source: /briefs/LICENSE.md

==============================================================================


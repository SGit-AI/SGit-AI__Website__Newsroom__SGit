# coding.sgit.ai — how software actually gets written here

> The sgit.ai network's site about coding style: five languages (Python, JavaScript, HTML,
> CSS, Bash) as they are actually written across 217,266 lines. Every convention was derived
> by COUNTING the code, not from documentation. Where a documented rule and the code
> disagree, both are published with the numbers — including the numbers that do not flatter.

Site version: v0.2.0 (25 August 2026). Published by the sgit project, which builds the tools
and wrote the code this site measures — participant disclosure at /about/participant.html.
All site content CC BY 4.0. The code quoted throughout is Apache-2.0 and carries its own
notice; Type_Safe, Safe_Str and the constrained-primitive pattern come from osbot-utils,
Apache-2.0, under the owasp-sbot GitHub organisation.

## The headline

31 documented rules. 0 linters, 0 formatters, 0 type-checkers anywhere in the estate. 4
tests/ci/ structural guards are the entire automated enforcement surface, and a 5th has never
worked: its regex is `sgraph_ai_service_playwright[^_]`, and `[^_]` cannot match the real
package `sgraph_ai_service_playwright__cli`. 0 files matched; 228 real imports across 69 files.

Measured against 992 class-defining files: banners 100%, no-docstrings 99.7%, empty
__init__.py 99%, one-class-per-file 90%, no-underscore-private 91% (97 violations). Import
alignment is 39% and is not a documented rule at all. And the estate's prose rule that "all
documents are em-dash-free" is broken 248 times across the 11 documents that state it — not one
file has zero. This site follows the practice rather than the stated rule, and says so.

None of the 31 numbered rules carries a passing CI guard. The four working guards each encode an
INCIDENT rather than a rule, so the written rule set and the tested rule set do not currently
overlap at all.

## Properties agents may rely on

- Every source document is fetchable at a stable constructed URL: /briefs/<filename>. 13 of
  them, 12,983 words, published in full.
- /llms-full.txt is this site in one fetch: the index, the front page and every source
  document, in the pack's own reading order. GENERATED from those sources and re-checked in
  CI, so it cannot say anything the site does not.
- /briefs/conventions__machine-readable.json is the SOURCE of every number on this site, not a
  copy of them. admin/build/gen_inline.py writes each figure into each page from that file and
  CI fails the release if one has drifted.
- Every code example is written into its page by the same generator, from the source document
  it was quoted in, carrying its real repository path and its own Apache-2.0 notice. A snippet
  on this site cannot be something nobody wrote.
- /data/rules.json is the machine-readable rule set: 31 rules plus 4 testing non-negotiables,
  each with its measured compliance, an enforcement badge, and a flag saying whether the text
  is quoted verbatim or paraphrased. /rules/ is generated from it.
- /data/documents.json is the machine-readable document index. /documents/ is generated from it.
- /sitemap.xml is generated from the tree, so it cannot omit a page somebody forgot to add.
- The version in /admin/build/version.txt agrees with the badge on every page, the release
  history table, this file, /llms-full.txt and /index.md — CI fails the release otherwise.

## The pages

- /index.html — the thesis in one page: the hook, the four decisions everything follows from,
  the five languages, and what this site does not claim. Markdown twin: /index.md
- /style/index.html — what is shared across all five languages. One idea per file, banners and
  their four forms, the argument that alignment is a machine-readability decision, and single
  source of truth enforced by structure rather than by asking.
- /python/index.html — the deepest language. The complete eleven-line example with nine
  conventions in it, the naming families, Type_Safe, constrained primitives, layout, testing,
  the responsibility boundaries, and the osbot-* dependencies.
- /javascript/index.html — native web components, no framework, no build step. The three-file
  triplet, static jsUrl = import.meta.url, the versioned CDN path scheme, the SgComponent
  contract, the sp-cli: legacy event namespace, and the four inconsistencies to settle.
- /html/index.html — fragments not documents, 2-space indent, ARIA, data-* as the behaviour
  hook, injected chrome, and the markdown twin.
- /css/index.html — per-block value alignment, design tokens and their three competing
  prefixes, theming, and why shadow DOM makes BEM unnecessary.
- /bash/index.html — 5 .sh files in 217,266 lines. The Section__* generated-shell pattern, its
  seven-part anatomy, the trade it makes, and the two cheap mitigations that do not exist.
- /rules/index.html — all 31 rules plus the 4 testing non-negotiables, each with its measured
  compliance and an enforcement badge, plus the 14 conventions that are consistent in the code
  and are not rules anywhere. GENERATED from /data/rules.json.
- /enforce/index.html — the configs, shipped as files: /enforce/ruff.toml,
  /enforce/eslint.config.js, /enforce/stylelint.config.js, /enforce/test_house_style.py,
  /enforce/test_rendered_shell.py, /enforce/check_components.py, /enforce/check_markup.py.
  Plus an honest table of what ruff, eslint and stylelint genuinely cannot express and why —
  including the correction that ruff CANNOT encode "no docstrings" (pydocstyle requires them
  and there is no inverse rule), which the brief assumed it could.
- /shipped/index.html — what is NOT enforced. Nothing is enforced by tooling; one guard never
  worked; two more are claimed and unlisted; four of five languages are undocumented; the bad
  numbers; and what this site itself cannot do.
- /for-agents/index.html — the conventions that only make sense once an LLM is a primary reader
  and writer. Published as a position with the evidence attached, not as a finding.
- /open-questions/index.html — 8 open questions, 6 tensions, 7 loose ends, 7 unwritten items.
- /documents/index.html — the 13 source documents, published in full, with a section on exactly
  what was redacted and what was deliberately kept.
- /admin/index.html — how this site is built: the pipeline, the gate, the tagger, the
  generators. /admin/versions.html — the release history. /admin/comms.html — tasks and
  requests, including R2, the build-time extraction this site does not do.
- /network/index.html — the sibling sites and the boundaries between them.
- /about/participant.html — who publishes this and how it is written.

## What is NOT here, and should be

- Build-time extraction from the repository. The commissioning brief's house rule is that every
  count and example is extracted from the code at build time with a commit reference. This
  repository holds the website, not the 217,266 lines it describes, so every number is written
  in from a DATED survey (2026-08-24) instead. The counts cannot drift from the survey; they
  can and will drift from the code. Tracked as R2 in /admin/comms.html.
- Rules for JavaScript, CSS, HTML and Bash. All 31 documented rules are Python and process. The
  14 conventions listed at /rules/#unwritten are candidates and none of them is a rule yet.
- Any resolution of the 8 open questions. They are published unresolved on purpose.

## Redaction

Two of the 13 source documents carry the pack's own do-not-publish list, which names the values
it forbids. In those two files only, an AWS account id, four live internal hostnames and four
named live stack FQDNs are replaced with [redacted]; the occurrence counts are kept and each
change is marked in place. dev.tools.sgraph.ai is deliberately NOT redacted, because it appears
inside the code examples and a component example without its import URL teaches nothing — see
open question Q4. Full account at /documents/index.html#redaction.

## Related

- https://sgit.ai — the parent project and the network index
- https://open-source.sgit.ai — the other half of the /for-agents/ argument
- https://sg-compute.sgit.ai — the platform; the richest source of the examples quoted here
- https://llms.sgit.ai · https://standards.sgit.ai · https://issues-fs.sgit.ai
- https://graphs.sgit.ai · https://wardley-maps.sgit.ai · https://risks.sgit.ai
- https://nhi.sgit.ai · https://pki.sgit.ai


==============================================================================
PART 2 — THE FRONT PAGE (source: /index.md)

==============================================================================


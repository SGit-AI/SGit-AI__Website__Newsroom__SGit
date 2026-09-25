# coding.sgit.ai — the style guide that measured itself

> Five languages — Python, JavaScript, HTML, CSS, Bash — as they are actually written across
> 217,266 lines of code. Every convention here was **derived by counting**, not from
> documentation, and where a documented rule and the code disagree, both are published with
> the numbers.

*Source: <https://coding.sgit.ai/index.html> · site v0.2.0 · markdown twin of the front page.*

---

## 31 documented rules. 0 linters. 4 guards, and 1 of them never worked.

This estate has a written style guide, which is more than most projects have. It lives in
`.claude/CLAUDE.md` — an agent instruction file, not a published standard — and until the survey
behind this site, **nobody had ever measured whether the code obeys it**.

```
# measured against 992 class-defining files

rule  7  ═══ banner on every file          100%   992 / 992
rule  8  no docstrings, ever              99.7%   3 violations
rule 22  __init__.py stays empty             99%   299 / 302
rule 21  one class per file                  90%   187 / 208 sampled
rule  9  no _ prefix on private methods      91%   97 violations
         import alignment                    39%   321 / 817   # not a rule at all

# enforcement surface, entire:
tests/ci/  4 structural guards  +  1 that has never matched anything
```

The last line is the one worth reading twice. The guard is supposed to fail the build if the new
tree imports the legacy one; its regex requires a non-underscore character after a package stem
that has two, so it matched nothing and passed. There are 228 real imports across 69 files.
[A guard that passes because it cannot match what it guards against](shipped/index.html#broken-guard).

## The four decisions everything else follows from

These are not style preferences with a rationale bolted on afterwards. They are four choices that
produce each other, in a codebase where **61% of commits were written by an agent** and a human
still has to review the result.

- **Runtime validation, not static analysis.** There is no type-checker anywhere in the estate.
  `Type_Safe` from `osbot-utils` validates at construction instead, so a value that exists is a
  value that is valid — and a generated mistake fails at the point of the mistake rather than in a
  checking pass nobody runs. [How it works](python/index.html#type-safe).
- **The type is the validation.** Zero raw primitives. `Safe_Str__SSM__Path`, `Safe_Int__Port`,
  `Safe_Str__Node__Name` — 27 constrained types in one directory. Naming a type is how a domain
  concept gets recorded. [The pattern](python/index.html#primitives).
- **One idea per file, and the filename says which.** The filename is the class name,
  `__init__.py` stays empty, nothing is re-exported, and there is exactly one import path to
  anything — so a symbol is locatable by constructing a path, with no index and no grep.
  [Across all five languages](style/index.html#one-idea).
- **A model is a primary reader.** Runtime validation, constrained primitives, no re-exports,
  banners instead of docstrings, single-owner responsibility boundaries and the markdown twin all
  read as one coherent design once you accept that. The most original page here, and the least
  verifiable. [The argument](for-agents/index.html).

## The five languages

One is documented. Four are not, and reconstructing them by counting is most of what the survey
behind this site did.

- **[Python](python/index.html)** — 3,999 files, 217,266 lines. Double-underscore naming families
  (`Schema__` 614, `Safe_Str__` 290, `Enum__` 185), one class per file, `═══` banners, and
  column-aligned assignments. Nine conventions visible in one eleven-line file.
- **[JavaScript](javascript/index.html)** — 50 files, no framework and no build step. Native web
  components, a three-file triplet per component, a self-locating base class, and a versioned CDN
  path instead of a lockfile. Written down nowhere until now.
- **[CSS](css/index.html)** — 38 files. Alignment carried into property values, every colour a
  token, and plain semantic class names because shadow DOM removes the problem BEM exists to solve.
- **[HTML](html/index.html)** — 37 files. Fragments rather than documents, 2-space indent, ARIA on
  every control, and one rule worth its own line: classes are for styling, `data-*` is for
  behaviour, and the two never mix.
- **[Bash](bash/index.html)** — 5 `.sh` files in 217,266 lines. Shell is not written here, it is
  generated from 15 typed Python classes that each render a fragment. A real trade, argued rather
  than reported.

## What this site does not claim

**Nothing here is enforced by tooling.** Compliance of 100%, 99.7% and 99% is achieved entirely by
discipline, which is impressive and exactly as fragile as it sounds. Four of the five languages
have no documented rules at all. Import alignment is 39%. Two CI guards are claimed in the rule set
and do not appear in the rule set's own table of guards. And the most interesting page here is a
position with the evidence attached, not a finding.

There is also one thing this site was commissioned to do and does not: **extract its counts from
the repository at build time**. This repository holds the website, not the code it describes, so
every number here is written in from a **dated survey** — 2026-08-24 — by a generator, with CI
failing the release if a published number has drifted from it. That closes the drift-within-the-site
problem and leaves the freshness problem open, and it is tracked as request R2.

- [What is not enforced](shipped/index.html) — the bad numbers, in one place.
- [Open questions and tensions](open-questions/index.html) — 8 questions, 6 tensions, 7 loose ends.
- [Enforcement](enforce/index.html) — the ruff, eslint and stylelint configs, shipped as files,
  with an honest account of the seven rules no linter can express.

## Where this sits

- [The source documents](documents/index.html) — all 13, 12,983 words, published in full. Two of
  them carry the pack's own do-not-publish list, and are published with that list redacted.
- [open-source.sgit.ai](https://open-source.sgit.ai) — the other half of the argument. That site
  has the position; this one has the artefact.
- [The sibling sites](network/index.html) — what each one owns and where the boundaries fall.
- [Who publishes this](about/participant.html) — the sgit project publishes this site and wrote
  the code it measures. Stated on the way in rather than in a footnote.

---

*All content CC BY 4.0 — Dinis Cruz, with AI co-authorship (Claude, Anthropic). The code quoted
throughout is Apache-2.0 and carries its own notice; `Type_Safe`, `Safe_Str` and the
constrained-primitive pattern come from `osbot-utils` under the `owasp-sbot` organisation.*


==============================================================================
PART 3 — THE 13 SOURCE DOCUMENTS

==============================================================================


Each is also fetchable on its own at /briefs/<filename>, in the pack's
own reading order rather than alphabetically.



==============================================================================
source: /briefs/README.md

==============================================================================


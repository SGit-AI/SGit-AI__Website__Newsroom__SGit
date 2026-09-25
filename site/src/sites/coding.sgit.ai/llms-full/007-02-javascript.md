# 02 — JavaScript

50 files, no framework, no build step, and a component system nobody has written down. **This is the most original and least documented convention in the estate.**

---

## 1. The complete example

`components/sg-compute/sg-compute-left-nav/v0/v0.1/v0.1.0/sg-compute-left-nav.js`, verbatim:

```js
/**
 * sg-compute-left-nav — vertical icon-rail navigation for the admin dashboard.
 *
 * Items: Compute / Storage / Settings / Diagnostics.
 * Click fires sp-cli:nav.selected { view } on document.
 *
 * @module sg-compute-left-nav
 * @version 0.1.0
 */

import { SgComponent } from 'https://dev.tools.sgraph.ai/components/base/v1/v1.0/v1.0.0/sg-component.js'

class SgComputeLeftNav extends SgComponent {

    static jsUrl = import.meta.url
    get resourceName()   { return 'sg-compute-left-nav' }
    get sharedCssPaths() { return ['https://dev.tools.sgraph.ai/components/tokens/v1/v1.0/v1.0.0/sg-tokens.css'] }

    onReady() {
        this._current = 'compute'
        this.shadowRoot.querySelectorAll('.nav-item').forEach(btn => {
            btn.addEventListener('click', () => this._select(btn.dataset.view))
        })
        this._update()
    }

    _select(view) {
        if (view === this._current) return
        this._current = view
        this._update()
        document.dispatchEvent(new CustomEvent('sp-cli:nav.selected', {
            detail:  { view },
            bubbles: true, composed: true,
        }))
    }

    _update() {
        this.shadowRoot.querySelectorAll('.nav-item').forEach(btn => {
            btn.classList.toggle('selected', btn.dataset.view === this._current)
            btn.setAttribute('aria-current', btn.dataset.view === this._current ? 'page' : 'false')
        })
    }
}

customElements.define('sg-compute-left-nav', SgComputeLeftNav)
```

---

## 2. The component system

**Native web components. 41 `customElements.define` across 50 files. No React, no Vue, no bundler, no build step.** The browser is the runtime.

### The three-file triplet

Every component is exactly three files, same basename:

```
sg-compute-left-nav.js      behaviour
sg-compute-left-nav.html    markup
sg-compute-left-nav.css     styles
```

`static jsUrl = import.meta.url` is what makes this work: the component knows its own URL, so `SgComponent` can fetch the sibling `.html` and `.css` without anything being told where they live. **Self-locating components are the mechanism that removes the build step.**

### The versioned CDN path

```
https://dev.tools.sgraph.ai/components/<name>/v1/v1.0/v1.0.0/<file>.js
                                              ^^^ ^^^^ ^^^^^^
                                            major minor patch — as directories
```

Three nested directories, one per semver level. A consumer pins at whatever depth it wants stability: `/v1/` follows the major, `/v1.0/` follows the minor, `/v1.0.0/` is frozen. **Immutable URLs, no lockfile, no `node_modules`, cacheable forever.** The same scheme is used locally under `components/`.

What comes from the CDN today: `SgComponent` (the base class), `sg-tokens.css` (design tokens), `sg-vault-client.js`, `sg-vault-write.js`.

### The base class contract

`SgComponent` supplies the lifecycle; components override three things:

| Member | Purpose |
|---|---|
| `static jsUrl = import.meta.url` | self-location — **required** |
| `get resourceName()` | the basename of the sibling `.html` / `.css` |
| `get sharedCssPaths()` | tokens and shared sheets to adopt |
| `onReady()` | the lifecycle hook — **not `connectedCallback` directly** |

`onReady()` rather than `connectedCallback` is the tell: the base class handles the async fetch of the sibling files and calls `onReady()` once the shadow root is populated, so a component never has to think about whether its markup has arrived.

### Shadow DOM

6 files call `attachShadow` directly; the rest inherit it from `SgComponent`, and every component addresses its own markup through `this.shadowRoot`. Styles are scoped by `:host` (see `03__`).

---

## 3. Formatting, measured

| Convention | Evidence |
|---|---|
| **4-space indent** | 3,791 indented lines are a multiple of 4; 148 are not |
| **Single quotes** | **4,006 single vs 400 double** — 91% |
| **No semicolons** | 531 statement lines without vs 401 with — the newer `components/` tree is consistently semicolon-free; the older `shared/` tree is not. See §6 |
| **Trailing commas** | in multi-line object and array literals, consistently |
| **Aligned object keys** | `detail:  { view },` — the same alignment discipline as Python and CSS |
| **`_` prefix for private** | universal in JS, **against Python rule 9**. See `06__` §3 |
| **ESM everywhere** | 48 `type="module"` script tags; no UMD, no globals |
| **Banner comments** | 15 of 50 files open with `// ── name — description ──` |

**Two banner styles exist**: JSDoc blocks (`/** … @module … @version */`) on components, and `// ── … ──` box-drawing rules on shared modules. Python uses `# ═══`. **The estate has three banner characters for one idea** — `05__` §2.

---

## 4. Events, state and data

**Events are namespaced and go through `document`:**

```js
document.dispatchEvent(new CustomEvent('sp-cli:nav.selected', {
    detail:  { view },
    bubbles: true, composed: true,
}))
```

`bubbles: true, composed: true` is what lets an event escape the shadow root. **The namespace is `sp-cli:` — the old CLI name — and it appears in 23 files.** That is a rename surface nobody has counted; see `06__` §3.

**State is instance fields**, `_`-prefixed, set in `onReady()`. No store, no observable, no framework state layer. Cross-component state goes through the event bus and through purpose-built shared modules — `settings-bus.js`, `vault-bus.js`, `poll.js`.

**Constants are frozen and centralised.** `shared/launch-defaults.js`, verbatim:

```js
// ── launch-defaults.js — canonical launch constants ────────────────────────── //
// Single source of truth. Both sg-compute-compute-view and sg-compute-launch-form
// import from here. Update here only — do not duplicate locally.

export const REGIONS = Object.freeze([
    'eu-west-2', 'us-east-1', 'ap-southeast-1', 'eu-west-1', 'us-west-2',
])
```

**`Object.freeze` on every exported constant**, and a comment that names the consumers and forbids local duplication. That is the same *single source of truth* instinct that drives `manifest.py` and the repo-root `version` file.

---

## 5. Why no build step is the interesting claim

It is worth arguing on the site rather than just reporting.

**What it costs:** no TypeScript, no JSX, no tree-shaking, no minification, no dependency resolution, one network request per component file.

**What it buys:** the source that runs is the source you read — no source maps, no build cache, no `node_modules`, no bundler upgrade treadmill, and **an immutable URL per version instead of a lockfile**. A component is deployable by copying three files to a path. And — the point that connects to `05__` §3 — **an agent reading the running page reads the actual code**, with no transpilation between what it sees and what executes.

**Where it stops working:** at the point you need a dependency graph deeper than one level, or a package that only ships as CJS. Neither has happened yet in 50 files.

---

## 6. Inconsistencies to fix before publishing

1. **Semicolons.** `components/` is semicolon-free; `shared/` is not. **Pick one** — the newer tree suggests dropping them — and write the config.
2. **Two banner styles.** JSDoc on components, `// ──` on shared modules. Pick one per file type and say which.
3. **The `sp-cli:` event namespace** is legacy naming in 23 files. Rename with the rest (`sg-compute` pack `02__`), and note that renaming an event namespace is a breaking change for any listener outside the repo.
4. **`_private` in JS vs rule 9 in Python.** The rule set says no underscore prefix; the JavaScript uses it universally. **State that rule 9 is Python-only**, or change one of the two.

---

## 7. What a linter config would encode

`eslint` with: 4-space indent · single quotes · no semicolons · trailing commas in multiline · `object-curly-spacing` · a custom rule requiring `static jsUrl = import.meta.url` in any class extending `SgComponent` · a ban on bare `connectedCallback` overrides in favour of `onReady()` · and a check that every component directory contains all three of `.js` / `.html` / `.css`.

The last two are the ones that would actually catch bugs.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
source: /briefs/03__html-and-css.md

==============================================================================


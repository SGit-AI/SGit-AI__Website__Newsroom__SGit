# 03 — HTML and CSS

37 HTML files, 38 CSS files. Both follow from the component system in `02__`, and **CSS carries the estate's alignment discipline further than any other language.**

---

## 1. HTML — the component's markup half

`sg-compute-left-nav.html`, verbatim:

```html
<nav class="left-nav" role="navigation" aria-label="Main navigation">

  <button class="nav-item" data-view="compute" aria-label="Compute">
    <span class="nav-icon">⬡</span>
    <span class="nav-label">Compute</span>
  </button>

  <button class="nav-item" data-view="nodes" aria-label="Active Nodes">
    <span class="nav-icon">▣</span>
    <span class="nav-label">Nodes</span>
  </button>
```

**Six conventions:**

1. **A fragment, not a document.** No `<html>`, no `<head>`, no wrapper `<template>`. `SgComponent` fetches it and puts it in the shadow root.
2. **2-space indent** — deliberately different from the 4 used in JS and CSS. The narrower indent keeps nested markup readable at the same line width.
3. **Semantic elements.** `<nav>`, `<button>` — not `<div onclick>`. Every interactive control is a real control, so keyboard and focus work without code.
4. **ARIA on every interactive element.** `role`, `aria-label`, and `aria-current` set dynamically from JS.
5. **`data-*` is the behaviour hook.** `data-view="compute"` — JS reads `btn.dataset.view`. **Classes are for styling, `data-` is for behaviour, and the two never mix.** That single rule is worth its own line on the site.
6. **Unicode glyphs instead of icon fonts or SVG sprites.** `⬡ ▣` — no asset pipeline, no icon dependency, consistent with the no-build-step position in `02__` §5.

---

## 2. The page-level conventions

Beyond components, the estate's HTML carries two site-wide patterns worth documenting:

**Programmatically injected chrome.** `pki.sgit.ai`'s build injects nav, footers and version badges at build time rather than repeating them per page — *"so it cannot drift."* Hand-written static HTML plus generated furniture. The site should document the pattern, because it is the reason the sibling sites stay consistent.

**The markdown twin.** Every URL is also available with the extension swapped, and links inside the markdown point at markdown:

> *"every page is available as markdown at the same path with the extension swapped, and links inside the markdown point at markdown, so **a traversing agent never has to parse HTML**."*

The mechanism is non-obvious and should be published: these are static files, so the browser will not run JavaScript on them — the rendering happens in a **Lambda@Edge function**. See `05__` §3, because this is an HTML convention that exists entirely for machine readers.

---

## 3. CSS — alignment as a convention

`sg-compute-left-nav.css`, verbatim:

```css
:host { display: flex; flex-direction: column; height: 100%; overflow: hidden; }
[hidden] { display: none !important; }

.left-nav {
    display:        flex;
    flex-direction: column;
    align-items:    stretch;
    padding:        6px 0;
    height:         100%;
    background:     var(--bg-panel);
    border-right:   1px solid var(--border-1);
    gap:            2px;
}

.nav-item {
    display:         flex;
    flex-direction:  column;
    align-items:     center;
    justify-content: center;
    gap:             3px;
    padding:         10px 0;
    background:      transparent;
```

**Property values are aligned to a column within each rule** — exactly the discipline applied to Python attribute annotations and JS object keys. The column is set per rule by its own longest property name, so `.left-nav` and `.nav-item` align at different columns. **The unit of alignment is the block, not the file.**

Other conventions visible here:

- **`:host` first**, as a single line, establishing the component's own box
- **`[hidden] { display: none !important; }`** as a standing reset — the `!important` is deliberate, because `display: flex` on `:host` would otherwise beat the attribute
- **Flexbox for layout**, `gap` rather than margins
- **Every colour and surface is a token** — no literal hex values in component CSS
- **Class names are plain and semantic** — `.left-nav`, `.nav-item`, `.nav-icon`. **Not BEM, not utility classes.** Shadow DOM makes both unnecessary: the styles cannot leak, so they do not need namespacing

That last point deserves a paragraph on the site. **BEM exists to solve a problem shadow DOM removes.** Naming conventions that fight the cascade are a cost you only pay if your styles are global.

---

## 4. Design tokens

Tokens come from the versioned CDN, adopted per component:

```js
get sharedCssPaths() { return ['https://dev.tools.sgraph.ai/components/tokens/v1/v1.0/v1.0.0/sg-tokens.css'] }
```

Two naming families are in use, which is an inconsistency to resolve:

| Family | Examples |
|---|---|
| **Unprefixed** | `--bg-panel`, `--border-1`, `--text-1` … `--text-4`, `--text-link`, `--shadow-1`, `--shadow-2`, `--warn`, `--warn-soft`, `--soon` |
| **`--sg-` prefixed** | `--sg-text`, `--sg-text-muted`, `--sg-surface`, `--sg-sp-1` … `--sg-sp-4`, `--sg-transition-fast` |
| **`--sgl-` prefixed** | `--sgl-tab-h`, `--sgl-panel-h` |

**Three prefixes for one token system.** The numbered scales (`--text-1..4`, `--sg-sp-1..4`, `--shadow-1..2`) are a good pattern — a bounded ramp rather than arbitrary values — and the site should publish the ramps as the recommended approach. But **pick one prefix** before publishing, or document what each family means. `08__` Q3.

---

## 5. Theming

The token indirection is what makes theming possible: components reference `var(--bg-panel)` and never a literal, so a theme is a different `sg-tokens.css`. **Verify before publishing that a dark/light switch actually exists** — the token names suggest a dark-first palette (`--bg-panel`, `--text-1..4`) and this pack could not confirm a second theme file. `08__` §4.

---

## 6. What a linter config would encode

**CSS** (`stylelint`): 4-space indent · a custom rule requiring aligned values within a block · **no literal colours outside the token file** (highest value) · `:host` first · shorthand consistency.

**HTML** (`htmlhint` or a custom check): 2-space indent · every `<button>`/interactive element has an accessible name · **no `onclick` attributes** · `data-*` present where JS reads `dataset` · component fragments contain no `<html>`/`<head>`.

The two rules that would actually catch defects are **no literal colours** and **every interactive element has an accessible name**. The rest is formatting.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
source: /briefs/04__bash-and-generated-shell.md

==============================================================================


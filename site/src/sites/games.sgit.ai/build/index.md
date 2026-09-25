# Building a game as a vault

> How to build a game that ships as an encrypted vault: the authoring contract, the folder-manifest trap that cost this family four releases, the telemetry lane, and what to publish beside the game.

*Source: <https://games.sgit.ai/build/index.html> · site v0.5.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / Build one

# Building a game as a vault

A vault app is one self-contained `index.html` plus an `app.json` that launches it. That is the whole deployment story: no build server, no hosting, no account for the reader. What follows is what this family learned building three of them, including the mistake that cost four releases.

## 1 — The authoring contract

- One `index.html` with CSS and JS **inlined**. No `<link href>`, `<script src>` or `<img src>` pointing at vault paths — those resolve against an opaque origin and 404.
- Content read over the bridge with `sg.vfs.readText`, with an inlined fallback so the page still renders outside a vault host.
- Generative SVG rather than image files, where you can. It keeps the vault small and it survives the no-`<img src>` rule without an interceptor.
- Post `sg-app-ready` when you have rendered, so the host can drop its loading state.

## 2 — The folder-manifest trap

This one is worth the whole page. **A folder-level `app.json` replaces the root one wholesale — nothing is inherited.**

The *What Can It Do?* vault declares `permissions.network` at the root, because the vault host's app frame ships a `connect-src blob: data:` content-security policy and a direct `fetch` to any API is blocked without it. That worked when the vault opened at its root. Opening a game *by its own path*, or reaching it from the vault's home page, resolved that folder's manifest instead — which had no `permissions` key — and the frame silently kept the restrictive CSP. Telemetry failed with *"Load failed"*, the bridge fallback answered *"Permission denied"*, and nothing said why.

It took releases v0.12.1 through v0.12.5 to find, across two wrong theories. The fix is one line per folder: **every folder that can be opened as an app carries the same grants as the root.** Two related things the same investigation settled — a release pin makes `app.json` come from the pinned commit rather than HEAD, and the append checker only ever watches the *open* vault's own lane, so a `new-messages` grant on a vault that has no lane will never fire whatever you declare.

## 3 — If it phones home, one credential shape survives

A vault published with a read key is a vault whose entire contents are public. So a game that sends anything must carry a credential that is safe to publish, and there is exactly one shape that qualifies: a **write-only append token**, blind, whose answer is `{"ok":true}` and nothing else. It cannot read, list or decrypt anything, including what it wrote.

Two lanes rather than one, because retention differs: anonymous counters on one token, deliberate feedback on the other, so a flood of the first cannot bury the second and the first can be purged without losing the second. [What ours send](../telemetry/index.md).

> **The audit is the part people skip.** When sgit.ai published this vault it grepped the whole tree for private key material, provider keys, `enum_key` / `write_key` / `vault_key` fields, and every 64-hex string. Exactly one 64-hex string existed and it was the append token — and it was then *tested*, not taken on trust: cloning the telemetry vault with it decrypts nothing, and a control run with an all-zeros key behaves identically. An append token and a read key are both 64 hex; a mistake between them would be invisible.

## 4 — Publish the source beside the game

Both games ship their readable source in the same vault: the engine as an ES module, `selftest.json`, the vendored data snapshot, the build script, and a README carrying a rules table and a **does-not-prove list**. The scoring rule a game claims and the rule its engine implements are different objects, and shipping both is what lets somebody check that they match.

The self-test is the load-bearing artefact. It is what turns *"saying yes to everything should lose"* from a design intention into a build failure.

## 5 — Embedding it on a page

Two hosts exist, and they are not interchangeable. The **minimal host** decrypts the vault in the page and boots the app in a sandboxed `srcdoc` frame: small, fast, and **reads only** — no `sg.llm.*`, no `sg.append.*`, and it never reads `app.json`. The **embed protocol** loads the real SG/Vault host in an iframe and hands it the key by `postMessage` with a pinned target origin, so the credential never enters a URL — and the app gets the full bridge.

This site uses the second, in `assets/vault-app-embed.js`, with the vault-browser surface suppressed. The games declare `llm.chat` for their chat panel and `append.write` for the telemetry fallback; under the minimal host the chat panel is dead and both grants are inert. If your game reads files and nothing else, the minimal host is the better trade.

---

*[Site index for agents](../llms.txt) · [HTML version](https://games.sgit.ai/build/index.html)*

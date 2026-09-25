# 04 — Websites vs vaults: what changes when there is no host

The commission asked for chat panes on **websites and vaults**. The vault story is complete, shipped and documented (`01__`–`03__`). **The website story is the thinner half, and the site should be honest about that** — it is a gap to fill, not an existing asset to publish.

---

## 1. What a vault gives you that a website does not

Everything in `03__` depends on **a host at a different origin from the app**. Take the host away and every guarantee changes:

| Mechanism | In a vault | On a plain website |
|---|---|---|
| **Key storage** | `.vault/llm/config.json`, below the permission floor | **nowhere safe in the browser** |
| **Who calls the provider** | the host | your page, or your backend |
| **Grant model** | `app.json`, default-deny, enforced by the host | nothing enforces it |
| **Consent** | host HUD, outside the app's control | you draw it, so you could fake it |
| **Budget caps** | host, before the call | your backend, or nothing |
| **Recording indicator** | host chrome — **unfakeable by the app** | your own DOM — fakeable |
| **Cost ledger** | host, two-source reconciled | you build it |

**The one-line rule:** *the vault bridge exists because the app and the credential are in different trust boundaries. On a plain website they are not, so the same design does not transfer — the question becomes where you put the boundary instead.*

---

## 2. The three options on a website, honestly compared

**(a) A backend proxy — the standard answer.** Your server holds the key; the page calls your endpoint. This is the vault model with your own backend playing host. It gets you real key protection, real budget caps and a real ledger — and it costs you a server, an auth story and an abuse-prevention story that the vault host already solved.

**(b) Bring-your-own-key in the browser.** The visitor pastes their own key; it stays in their browser. **There is precedent in the estate**: the Regulation Graph vault's Article 9 Lab *"requires a bring-your-own OpenRouter key — deliberately, so no metered capability sits behind the published read key."*

That reasoning generalises cleanly to a static site: **a public page cannot carry a spending credential, so the visitor brings their own or there is no chat.** It is honest, it costs nothing to run, and it converts badly.

**(c) Embed the vault surface.** Point the reader at a vault that already has the panel. This is the option nobody has written up and it may be the best one for `*.sgit.ai` specifically, since the estate already publishes read keys and already embeds vault content in pages — the embedding mechanism (sandboxed iframe, `postMessage` key handshake, key never in a URL) is built and documented.

> ⚠️ **But see `03__` §6**: a vault with an LLM key configured carries a credential, so **publishing a read key for it shares the ability to spend.** Option (c) works only for a vault whose key tier and spend caps were chosen with publication in mind.

---

## 3. What exists today

**For websites: almost nothing.** There is no website chat component in the estate, no documented pattern, and no code. What exists that is adjacent:

- **The versioned component CDN** (`dev.tools.sgraph.ai`) already serves `sg-vault-client.js` and `sg-vault-write.js` — so **a `sg-llm-chat` component is a natural next member of that family**, and the component conventions are documented (`coding.sgit.ai` `02__`).
- **The BYOK precedent** in the Article 9 Lab, with its reasoning stated.
- **The offline Ollama chat UI** (18 March 2026) — a FastAPI proxy to a local Ollama, built on the `sg-layout` web component, for *"offline LLM chat during travel."* Small, and it is a real worked example of a chat UI against a proxy endpoint, which is option (a) in miniature.

**Recommendation:** `/websites/` should present the three options with this honesty, recommend **(a) for products and (c) for `*.sgit.ai` pages**, and ship **a `sg-llm-chat` web component** as the concrete artefact — built to the estate's own component conventions, with a pluggable transport so the same component serves all three options. `08__` G1.

---

## 4. The one thing that transfers unchanged

**The honesty mechanisms.** None of them depend on a host:

- one shared context budget, never one per file
- `TRUNCATED` in the text the model sees
- estimates rendered with `~`, never as a bill
- images cleared after one send
- `available()` before rendering
- branch on error codes, not message text
- recording announced in words

**Those are the transferable part of this work**, and a website chat pane built without them is worse than a vault one for reasons that have nothing to do with key storage. `code__chat-pane-samples.md` §8 is the checklist; it applies verbatim.

---

## 5. The `llms.txt` connection — the site's other LLM surface

There is a second sense in which this estate serves LLMs, and `llms.sgit.ai` is the natural home for it.

Every `*.sgit.ai` site publishes `/llms.txt` as its agent surface, and the estate's practice goes further: **the markdown twin at every URL**, extension swapped, with links inside the markdown pointing at markdown, *"so a traversing agent never has to parse HTML."* The mechanism is non-obvious — these are static files, so the rendering happens in a **Lambda@Edge function**.

And the finding from the 14 August agent-access report:

> *"**The audience is disproportionately agents**… many agents can only fetch URLs that a search engine has already returned to them… **It can read the map and cannot walk it.**"*

**That belongs on this site**, because it is the other half of the same subject: `01__`–`03__` are about *putting a model inside your page*, and this is about *making your page readable to a model that arrives from outside*. Cross-link with `coding.sgit.ai` `05__` §5, which has the conventions.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
/briefs/05__the-wider-llm-work.md
==============================================================================

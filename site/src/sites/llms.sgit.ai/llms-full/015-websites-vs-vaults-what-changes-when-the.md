# Websites vs vaults: what changes when there is no host

This site was commissioned to cover chat panes on **websites and vaults**. The vault story is shipped, complete and now documented. This one is not.

 The thin half, labelled

**For plain websites there is almost nothing: no component, no documented pattern, and no code.** What follows is a comparison, a recommendation and one adjacent precedent. It is a gap to fill rather than an asset to publish, and levelling it with the vault half would be the single most misleading thing this site could do.

## What a vault gives you that a website does not

Everything on [the security page](../security/index.md) depends on **a host at a different origin from the app**. Take the host away and every guarantee changes into something you have to build:

| Mechanism | In a vault | On a plain website |
|---|---|---|
| **Key storage** | `.vault/llm/config.json`, below the permission floor | **nowhere safe in the browser** |
| **Who calls the provider** | the host | your page, or your backend |
| **Grant model** | `app.json`, default-deny, enforced by the host | nothing enforces it |
| **Consent** | host HUD, outside the app's control | you draw it, so you could fake it |
| **Budget caps** | host, before the call | your backend, or nothing |
| **Recording indicator** | host chrome, **unfakeable by the app** | your own DOM, fakeable |
| **Cost ledger** | host, two-source reconciled | you build it |

The vault bridge exists because the app and the credential are in different trust boundaries. On a plain website they are not, so the same design does not transfer: the question becomes where you put the boundary instead.

## The three options, honestly compared

### (a) A backend proxy — the standard answer

Your server holds the key; the page calls your endpoint. This is the vault model with your own backend playing host. It gets you real key protection, real budget caps and a real ledger, and it costs you a server, an authentication story and an abuse-prevention story that the vault host already solved. Everything on [the four-layer ladder](../security/index.md#ladder) becomes yours to implement, and the two layers people skip are budget and consent.

### (b) Bring-your-own-key in the browser

The visitor pastes their own key and it stays in their browser. There is a precedent in the estate: the Regulation Graph vault's Article 9 Lab *requires a bring-your-own OpenRouter key, deliberately, so no metered capability sits behind the published read key*.

That reasoning generalises cleanly to a static site. **A public page cannot carry a spending credential, so the visitor brings their own or there is no chat.** It is honest, it costs nothing to run, and it converts badly, which is the whole trade in one sentence.

### (c) Embed the vault surface

Point the reader at a vault that already has the panel. Nobody has written this up, and it may be the best option for `*.sgit.ai` specifically: the estate already publishes read keys, already embeds vault content in pages, and the embedding mechanism is built and documented, with a sandboxed iframe, a `postMessage` key handshake, and no key in a URL.

**But see the standing warning.** [A vault with an LLM key configured carries a credential](../security/index.md#storing), so publishing a read key for it shares the ability to spend it. Option (c) works only for a vault whose key tier and spend caps were chosen with publication in mind, which is a decision to take before publishing rather than after.

## The recommendation

| Context | Option | Why |
|---|---|---|
| A product | **(a) backend proxy** | You need the caps and the ledger, and you will need the auth story anyway |
| A `*.sgit.ai` page | **(c) embed the vault surface** | The mechanism exists, the estate already uses it, and it reuses guarantees rather than reimplementing them |
| A public demo or lab | **(b) BYOK** | The Article 9 Lab's reasoning, and the only option that never puts a spending credential behind a public link |

The concrete artefact this section still needs is a **`sg-llm-chat` web component with a pluggable transport**, so one component serves all three, built to the estate's component conventions. The versioned component CDN already serves `sg-vault-client.js` and `sg-vault-write.js`, so it is a natural next member of that family rather than a new idea. **It is not built**, and it is [on the shipped page's list of absences](../shipped/index.md#thin) rather than described here as though it were.

The nearest existing worked example is small and real: an **offline Ollama chat UI** from March 2026, a chat interface over a FastAPI proxy, built on the `sg-layout` web component. That is option (a) in miniature, and [it is on the local models page](../local/index.md).

## The one thing that transfers unchanged

None of the honesty mechanisms depend on a host. Every one of them is available to a chat pane with no vault behind it at all:

- one shared context budget, never one per file
- `TRUNCATED` in the text the model sees
- estimates rendered with `~`, never as a bill
- images cleared after one send
- `available()`, or its equivalent, before rendering
- branch on error codes, not message text
- recording announced in words

A website chat pane built without these is worse than a vault one for reasons that have nothing to do with key storage.

[The pre-ship checklist](../chat-pane/samples.md#checklist) applies verbatim, minus the two lines about grants.

## The other sense in which a website serves an LLM

There is a second reading of this page's title, and it is the half most sites forget. [Putting a model inside your page](../chat-pane/index.md) is one subject. [Making your page readable to a model that arrives from outside](../agents/index.md) is the other, and this estate has a real practice for it: `/llms.txt` on every site, a markdown twin at every URL, and filenames that say `for_llms` out loud.

It also has a finding that reads as a warning: *"It can read the map and cannot walk it."* [That page](../agents/index.md) is the other half of this one.

 [← The security model](../security/index.md) [Provenance →](../provenance/index.md)


==============================================================================
/provenance/index.md
==============================================================================

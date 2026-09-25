# The provider layer

OpenRouter is mentioned in 442 files in this corpus and it is the estate's actual model-access path. Nobody had written up why, so this page does, including what it costs.

## Why route through an aggregator at all

| What you gain | What it costs |
|---|---|
| **One key for many models.** A vault holds a single credential and reaches every vendor through it | **One credential to lose.** The blast radius of that key is every model rather than one |
| **Capability metadata for free.** Whether a model reads images, whether it accepts audio, what it costs, all from the catalogue | **You trust somebody else's catalogue** for a check you are making before spending money |
| **Generation ids.** A stable handle per call, reconcilable afterwards against an authoritative lookup | **The handle is theirs.** Provenance that depends on a third party's record-keeping |
| **Model switching is a string.** `models.allow` takes globs, so `anthropic/*` is a policy | **A single point of dependency** between you and every model you use |

That last row is the real trade and it deserves naming rather than burying: the aggregator is a dependency with the reach of all of them at once. [The local-models page](../local/index.md) is the other half of this thought, and [the sovereignty argument](https://open-source.sgit.ai) applies to model providers more sharply than to almost anything else, because *you are one SLA away from losing access* is not hypothetical for a hosted model.

## Bring your own key, per vault

The key is the vault owner's, not a platform key. That single choice explains a surprising amount of the design: [the two key tiers](../security/index.md#tiers), the per-vault spend caps, the [standing warning about what a configured vault now contains](../security/index.md#storing), and the fact that [Phase 4 minted credentials](../security/index.md#gap) are described as the commercially load-bearing piece. A platform key would have made most of that somebody else's problem, and would have made every vault a shared spending surface.

## Capability comes from the live catalogue

Whether a model can read an image is read from the catalogue at call time, from the model's own declared modalities, rather than from a hard-coded list.

A new vision model works the day it ships.

Two consequences worth having: a model that cannot see gets you `EMODEL` **naming the model**, rather than a provider error that names nothing; and `text->image` models are correctly refused, because an image *generator* is not an image *reader* and the modality string says so.

## Defaults are a design decision

With no `models.default` configured, the panel auto-picks. The story of how it picks is the best small lesson on this site.

 The bug

It used to match on the **vendor prefix** against an alphabetically sorted list of the models on the key. Alphabetically, `anthropic/claude-3-haiku` comes early. So the picker selected **the oldest model on the key, which was also not a vision model**, silently, on every vault that had not set a default.

The symptom presents as *"the AI is bad"* rather than *"the default is wrong"*, and a pasted screenshot would fail with a model error nobody connected to the default.

The fix, in the shipped code today, is an explicit ordered list of named models tried first, with the vendor-prefix match kept only as a fallback for a key that has none of them:

```
var PREFERRED_MODELS = [
 'anthropic/claude-sonnet-5',
 'anthropic/claude-opus-5',
 'anthropic/claude-sonnet-4',
 'google/gemini-3.5-flash',
 'openai/gpt-5'
];

// Vendor fallback, when none of the named models are on this key.
var PREFERRED = ['anthropic/', 'openai/', 'google/', 'meta-llama/', 'mistralai/'];
```

These are exact ids, so a rename drops through to the vendor fallback rather than pinning a model that no longer exists. [Verified against the shipped source at v0.33.62](../shipped/index.md#verified), because a list like this is exactly the kind of thing a site gets wrong by quoting a brief.

A default that is silently wrong is worse than a default that is absent, because nobody goes looking for it.

An explicit `models.default` and a `models.allow` list still beat any auto-pick. The general lesson is the one the incident teaches: **a sort order is not a preference order**, and any time the two are confused the result is a system quietly choosing the wrong thing with complete confidence.

## Generation ids, and the analysis nobody has done

Every call is logged with its generation id, tokens, cost and latency, and the whole ledger exports as CSV or JSON. Cost is reconciled two-source: the stream's own figure first, then the authoritative lookup.

**And nobody has looked at it.** `cost per token` appears in **two** files across the corpus, and `model routing` in **one**. There is no fallback chain, no cost or quality tiering, and no routing logic, despite a fully instrumented ledger that has been collecting exactly the data those decisions would need. [The instrumentation is better than the use made of it](../shipped/index.md#thin), which is a more interesting failure than having neither.

 [← Provenance](../provenance/index.md) [Local and offline →](../local/index.md)


==============================================================================
/local/index.md
==============================================================================

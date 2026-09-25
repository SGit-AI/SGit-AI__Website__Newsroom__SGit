# Local and offline models

Ollama appears in 144 files in this corpus, and behind them are three concrete artefacts rather than an intention.

## The offline chat, and the flight it was built for

March 2026: a chat UI plus a FastAPI proxy to a host-native Ollama, with sessions surviving container rebuilds, built on the same `sg-layout` web component the vault UI uses. The stated requirement is disarmingly specific and it is the reason the thing is any good:

> Offline LLM chat during travel (flight on 19 March 2026). Must work completely disconnected from the internet once the Docker image is built and Ollama models are pulled.

A requirement with a date in it produces a different artefact from a requirement with a principle in it. "Must work offline" gets argued about; "the flight is on the 19th" gets built.

## Two sg-compute workload specs

| Spec | Class | Size | Boot | Status |
|---|---|---|---|---|
| `ollama` | llm-inference | 939 LOC | 120s | EXPERIMENTAL |
| `local_claude` | llm-inference | 1,498 LOC | 180s | EXPERIMENTAL |

Each carries a manifest, a CLI, a service, schemas and tests. There is also a `docker/local-claude` image: a local model alongside a Claude Code harness.

**The specs are not this site's to own.** [sg-compute.sgit.ai](https://sg-compute.sgit.ai) owns the workload specs and their lifecycle. This page links to them for the local-model story and does not duplicate them, in the same way [the grounding ladder](../provenance/index.md#grounding) is stated in three lines and left to the site that owns it.

## The through-line

The same `/api/chat` proxy shape works against a local Ollama and against a remote tunnel, which is why the offline work was never a detour.

That also makes the offline chat the estate's clearest existing example of [option (a), the backend proxy](../websites/index.md#options), on the websites page: a chat UI whose transport is an endpoint you control. It is small, it is real, and it is closer to a website chat pane than anything else that exists here.

## Why this matters more for models than for most dependencies

The open-source position in this estate is that *you are one SLA away from losing access*. For most dependencies that is a slow problem: a library can be forked, a service can be migrated over a quarter. For a hosted model it is not slow and it is not always about outages. A model can be deprecated, re-tuned, re-priced, or restricted by policy, and your outputs change underneath you without anything failing. [The provenance thread](../provenance/index.md) is what makes that visible: if you logged the generation id and the model, you can at least tell when the ground moved.

A local model is worse at almost everything and it is **yours**. That is the trade, stated plainly, and this estate has taken both sides of it deliberately: [an aggregator for reach](../openrouter/index.md), local for the case where reach is not available.

 [← The provider layer](../openrouter/index.md) [Pages that models read →](../agents/index.md)


==============================================================================
/agents/index.md
==============================================================================

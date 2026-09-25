# Provenance: the oldest thread

*Source: <https://llms.sgit.ai/provenance/index.html> · site v0.2.0 · the markdown twin of this page, generated from it.*

---

[llms.sgit.ai](../index.md) / provenance

# Provenance: the oldest thread

Everything else on this site is a mechanism. This is the position the mechanisms serve, and it is older than any of them.

## June 2024

The earliest dated artefact in the entire estate is a talk: **Deterministic GenAI Outputs with Provenance**, OWASP AppSec Lisbon, **28 June 2024**. Nearly ten thousand words of slides and notes, published openly.

Two years later the same instinct runs through everything built since. Provenance is mentioned in 431 files across the corpus and determinism in 421. The chat panel logs an OpenRouter generation id on every call. The Regulation Graph vault carries a SHA-256 of the retrieved bytes on every node. The grounding ladder terminates a claim at a measure. None of that was planned as a programme; it is what happens when one instinct is applied for two years.

The position is not "models are unreliable, use a better one". It is "a model output is only usable when you can say where it came from".

The distinction is practical rather than philosophical. The first framing sends you shopping for models. The second sends you building the apparatus that makes an answer checkable, which is what got built.

## Grounding, not prompting

Hallucination appears in only 45 files in the corpus, and where it does, it is framed as a **grounding** problem rather than a model problem. The answer the estate reaches for is the grounding ladder, in which each rung is defined by what lies below it:

```
Risk := a downward path to a Vulnerability AND an upward path toward a top risk
Vulnerability := a Fact (grounded below) AND an upward path to a Risk
Fact := a downward path to Evidence
Evidence := a downward path to a Measure
Measure := an observation of the node it measures, grounded on a Twin
```

The anti-fabrication argument follows directly:

> A model asked to assess something will produce a plausible answer. A model asked to attach a finding to a provision hash, and to a measure, and to a twin, either finds the path or reports that it cannot.

**The ladder is not this site's to own.** It belongs to [risks.sgit.ai](https://risks.sgit.ai) and [standards.sgit.ai](https://standards.sgit.ai), which carry it as risk apparatus and as instrument citation respectively. Three lines and a link out is the right amount of it here, because it is the *reason* the LLM work looks the way it does rather than the subject of this site. If a page here starts explaining the ladder, it has wandered.

## Where the position shows up in the shipped work

Read the LLM bridge with provenance in mind and the design choices stop looking like polish:

| Mechanism | What it is really doing |
|---|---|
| **An OpenRouter generation id on every call** | Making a specific answer re-findable at the provider, months later, by someone who was not there |
| **Two-source cost reconciliation** | Refusing to let a computed number stand where a billed one is available |
| **`TRUNCATED` in the model's own input** | Recording, inside the artefact, that the input was incomplete |
| **Images counted separately in the ledger** | Keeping the record honest about which calls were expensive |
| **The untrusted-data fence** | Marking, in the transcript, which text came from a file rather than from a person |
| **CSV and JSON export of the request ledger** | Making the record leave the tool that produced it |

Every one of those is the same move: attach an output to where it came from, and make the attachment survive the session.

## The one-shot thread

A related strand runs from early 2026: **one-shot** generation, in which a model produces a complete artefact in a single pass. It is attractive for the same reason it is risky, and the corpus works both sides: the one-shot development environment as a tool, and a published article on one-shot output as a thing to be careful with. The determinism problem is the joint between them, and it is the reason a generation id matters more than a good prompt.

## And the thing the position does not yet have

**There is no eval suite anywhere in the estate.** No benchmark, no regression test for prompt behaviour, nothing that would catch a model swap changing an output. For a body of work whose whole thesis is *you must be able to say where an output came from*, there is no mechanism for saying whether an output was any good, or for noticing when it stops being. [It is the most conspicuous absence on this site](../shipped/index.md#thin), and it is named here rather than only there because this is the page where it contradicts something.

 [← Websites vs vaults](../websites/index.md) [The provider layer →](../openrouter/index.md)

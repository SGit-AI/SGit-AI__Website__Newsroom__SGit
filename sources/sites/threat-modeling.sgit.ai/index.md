# threat-modeling.sgit.ai — a threat model is a claim you can check

> **The industry's own diagnosis is that threat modeling is a fairly subjective process
> producing static, siloed, context-poor documents.** This site publishes two things
> instead: models built as machine-readable graph data, and — its actual differentiator
> — the audit that says which parts of a threat model turned out to be wrong.

Eleven linked threat models, live at ThreatModCon 2025 · one threat model validated
line-by-line against its code the next day · seven white papers · [why this site is not
a neutral vantage point](about/participant.html).

*Source: <https://threat-modeling.sgit.ai/index.html> · site v0.1.0 · markdown twin of the front page.*

---

## The two strongest things this site has

Everyone publishes threat models. Almost nobody publishes the audit that says which
parts of theirs turned out to be wrong.

- **[Eleven linked layers, live](eleven-layers/index.html)** — "One model answers what
  could go wrong here. Eleven linked models answer what does this line of code put at
  risk." A published vault — Customer through Compute, 51 nodes, 179 threats — not a
  diagram of the idea.
- **[A claim, checked the next day](validated/index.html)** — 16 March 2026: a threat
  model of a real flow. 17 March: every finding checked against the code. Two confirmed
  real, one confirmed already safe, two confirmed missing, two marked as proposals with
  nothing built yet — and all four kinds published.

## The move, in two parts

The industry's diagnosis, in the founder's words: threat modeling is *"a fairly
subjective process"* producing *"static documents"* that are *"siloed"*,
*"fragmented"* and *"context-poor"*. The answer here is not another methodology.

1. **Make the model machine-readable** — a semantic knowledge graph, not a Word
   document. [Threat models as graph data →](graph/index.html)
2. **Make the model falsifiable — then falsify it.** A threat model was written 16
   March 2026; a validation pass checked every finding against the code the next day.
   [The validation pair →](validated/index.html)

The policy position that follows: [threat models as mandatory
disclosures](disclosure/index.html) — security is a market for lemons, and a
published, dated, checkable threat model is the correction.

## Seven white papers, one argument

Written in a burst — five of the seven inside four days at the end of May 2025 —
building from a diagnosis to a mechanism to a scaling case to a policy position.
[All seven, in order →](papers/index.html)

## The honest constraints

**Most of the practice material is a security review of the founder's own live
product.** It names unmitigated weaknesses. The rule this site publishes under:
publish the method always, publish findings only once they are closed or harmless by
design, hold anything still open. [The disclosure boundary, in full →](disclosure/index.html)

**The graph tooling is real but young.** The ThreatModCon vault is live; the
continuous-modelling pipeline the papers describe is a vision with partial
implementation. [What is real versus argued →](graph/index.html#real-vs-argued)

This site is published by the estate whose own product it threat-models — a conflict
of interest worth naming rather than discovered later. [The participant disclosure, in
full →](about/participant.html)

## Related

- <https://sgit.ai> — the parent project and the network index
- <https://sgit.ai/demos/vaults/threatmodcon-2025/> — the eleven-layer vault, live
- <https://wardley-maps.sgit.ai> · <https://graphs.sgit.ai> · <https://standards.sgit.ai>
- <https://risks.sgit.ai> · <https://pki.sgit.ai>

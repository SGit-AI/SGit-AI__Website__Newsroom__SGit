# 03 — Site Architecture: `threat-modeling.sgit.ai`

**Version** v0.33.63 · 7 September 2026
**Base** House pattern (copy `pki.sgit.ai`): `llms.txt` + `/llms-full.txt`, `/documents/` raw markdown, markdown twin at every URL, `/admin/comms.html`, `/shipped/`, versions, participant page.

---

## 1. URL scheme

```
/                        the thesis: a threat model is a claim; here are ours being checked
/eleven-layers/          the ThreatModCon 2025 vault, embedded + explained
/validated/              the 16→17 March claim-and-check pair, side by side
/papers/                 the seven white papers, one page each
/papers/<slug>/          summary, key claims, PDF + LinkedIn links, co-authorship note
/practice/               the method: bottom-up file-by-file, the parallel security tree
/practice/security-json/ the .security.json schema as a reusable artefact
/practice/stride/        STRIDE applied with honest mitigation status
/practice/two-modes/     the do-not-average-two-modes pattern
/graph/                  threat models as vault-native graph data
/disclosure/             the mandatory-disclosure position
/agentic/                threat-modeling AI systems (prompt injection, agent permissions)
/documents/              raw markdown of everything
```

## 2. The spine: claim → check

Every substantive page carries the same two-part structure the corpus already uses: **what we claimed** and **what checking it produced**. `/validated/` is the purest instance; `/practice/stride/` shows it as `NOT MITIGATED` rows; `/eleven-layers/` shows it as the data-repair note. Do not build a page that makes a claim with nothing checking it.

## 3. Data model

Threat models are graph data, not prose — that is the whole argument, and the site must not contradict it by being a pile of markdown. Each published model gets a JSON twin: nodes (Asset, Threat, Vulnerability, Mitigation, Actor, Incident), edges (targets, mitigates, is-instance-of, crosses-trust-boundary), and per-finding status. `/eleven-layers/` already has this shape upstream — 51 nodes, 179 threats — so it is the schema's proof rather than a new invention.

**Generated, not claimed**: node/threat/finding counts, the corpus file counts, and the validation verdict tallies all come from the data. Date every one.

## 4. Deconfliction with siblings

| Topic | Owner | This site's part |
|---|---|---|
| Wardley maps as a technique | `wardley-maps.sgit.ai` | Only the five threat-prioritisation walkthroughs, as an application |
| G³, MGraph-DB, graph theory | the graphs sibling | Only threat-model-shaped graphs; link out for the substrate |
| ISO 27001, EU AI Act, GDPR | `standards.sgit.ai` | Only framework-overlay-as-graph-edge; standards text stays there |
| Risk registers, acceptance | `risks.sgit.ai` | Only the `risk_decision` field as it appears in the security schema |
| Vault mechanics, keys | `pki.sgit.ai` / sgit.ai | Only what a threat model needs to say about them |
| NFR security posture | `nfrs.sgit.ai` | Threat modelling is the *method*; NFR owns the *property* |

The rule that keeps this clean: **this site owns the act of modelling threats.** If material is about the thing being modelled rather than the modelling, it belongs to a sibling.

## 5. The ThreatModCon vault is embedded, not copied

`/eleven-layers/` embeds the live vault (the vault-app-embed pattern from sgit.ai's own demos), with the explanation around it. Do not re-host the eleven models as site pages — the vault is the artefact, and a published vault demonstrating the platform's own argument is worth more than a static copy.

## 6. What this site does NOT do

No threat-modelling-as-a-service pitch on the main line (the 9 June services paper lives under `/papers/` clearly labelled as positioning). No open findings against live systems, including third parties (`04__`). No methodology comparison table that declares a winner — the corpus's position is that fragmentation is solved by linking methods in a graph, not by picking one.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


---

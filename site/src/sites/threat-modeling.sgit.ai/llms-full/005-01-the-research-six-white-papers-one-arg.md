# 01 — The Research: six white papers, one argument

**Version** v0.33.63 · 7 September 2026
**Source** `docs.diniscruz.ai/docs/2025/05/` and `/06/` — all seven documents verified on disk.

---

## The argument, in order

The papers were written in a burst — five of the seven inside four days at the end of May 2025 — and they build on each other. Read as a sequence they make one argument in four moves.

### Move 1 — The diagnosis (Advancing Threat Modeling with Semantic Knowledge Graphs, 29 May)

Five named failure modes, each stated as a problem any replacement must solve:

| Failure mode | The paper's charge |
|---|---|
| **Subjectivity and inconsistency** | *"Different people might identify different threats for the same system, and even the same person might produce varying results on different days."* There is no single source of truth and no way to verify completeness. |
| **Siloed knowledge** | Models live in prose and diagrams that are not machine-readable. *"There is no common knowledge base — each model is an island."* |
| **Lack of scalability** | Manual modelling cannot cover *"dozens of microservices and deployments per day."* Threat modelling *"lags behind development, instead of being a continuous guardrail."* |
| **Fragmented methodologies** | STRIDE, PASTA, LINDDUN, attack trees, kill chains — each a perspective, none linkable, producing *"process saturation"* and analysis paralysis. |
| **Static and context-poor models** | Snapshots that never absorb new threat intelligence, incident data, compliance requirements or crown-jewel designation — leading to mis-prioritisation, *"treating all threats as equal."* |

The paper's own summary of the ambition it inherits: threat modelling is an attempt to make *"a fairly subjective process more objective, repeatable & consistent."*

### Move 2 — The mechanism (same paper, plus G³, 30 May)

Represent the model as a semantic knowledge graph: *Asset*, *Threat*, *Vulnerability*, *Mitigation/Control*, *Actor*, *Incident* as node types, with defined relationships (*Threat* targets *Asset*; *Mitigation* mitigates *Threat*; *Incident* is-instance-of *Threat*). Three consequences the papers claim, each of which the site should present as a testable claim rather than a benefit:

1. **Multi-framework overlay becomes a query.** STRIDE, MITRE ATT&CK and OWASP Top 10 can sit on the same system model simultaneously — *"something not feasible with traditional static models."*
2. **Analysis becomes traversal.** *"All trust boundaries without an encryption control"* is a graph query, not a document review.
3. **Context becomes an edge.** A new CVE affecting a modelled component links to it and *"instantly flags a relevant threat"*; peer-industry incidents attach to the scenarios they instantiate; ISO 27001 controls and OWASP ASVS requirements become another layer.

The G³ paper (*Graphs of Graphs of Graphs in Threat Modeling*) supplies the architecture: multi-view/multi-graph, organic file-based evolution of threat graphs, and ontologies/taxonomies/standards linked in as semantic layers rather than baked into one schema. Its structure — introduction, G³ and semantic knowledge modelling, multi-view architecture, file-based organic evolution, ontology linking, a supply-chain case study, then benefits (personalisation, traceability, automation) — is the closest thing the corpus has to a reference architecture for this site's `/graph/` section.

**The determinism caveat is in the source and must survive to the site.** The papers are explicit that letting an LLM *"fill in relationships freely"* is a prototype behaviour, and that *"moving to an explicit schema is crucial for reliability"* — LLM output must be structured data matching the schema, not free-form text.

### Move 3 — The scaling case (supply chain ×2, 30 May)

Two papers take the hardest domain. *Using Threat Modeling and Semantic Graphs to Secure the Digital Supply Chain* and *Scaling Supply Chain Security using Threat Modeling, Semantic Knowledge Graphs and Maps* share a spine — mandatory disclosure, semantic graphs as foundation, then **maps** as the visualisation layer, whole-supply-chain modelling, G³ for interoperability, framework integration via graph links, and continuous automated risk monitoring. The second adds the Wardley-map dimension, which is where this site touches `wardley-maps.sgit.ai` (see the deconfliction note in `03__`).

### Move 4 — The policy position (Threat Models as Mandatory Disclosures, 29 May)

The boldest paper, and the one that should be published as a standalone position rather than buried in a research index. Its claim:

> Digital products suffer a *"classic 'market for lemons' scenario in cybersecurity"* — vendors know far more about their product's security than buyers do, so *"inferior security offerings thrive and outcompete higher-quality ones."*

The proposed correction: make threat-model publication a **regulatory requirement**, the way financial statements and food ingredient labels are mandated. A published threat model becomes *"a reliable signal of security quality"* and *"concrete evidence of the threats a company has considered and mitigated, substantiating security claims that today are often vague or unverified."* The paper carries historical parallels, a maturity roadmap, stakeholder impacts, technical enablers and practical steps.

**Note the reflexivity, and make it the site's spine.** A site arguing that threat models should be mandatory disclosures is judged by whether it discloses its own. It does — that is what `02__` is. The `/disclosure/` page and the `/practice/` page must link to each other explicitly, because together they are an argument the reader can check.

### The seventh paper — Linking Threat Models with Semantic Business Graphs (2 June)

The bridge between technical findings and business impact. It is the theoretical basis for the ThreatModCon vault's multi-persona demo (one SQL injection, four audiences) and for the eleven-layer traversal from Compute up to Customer. Pair them on the site: the paper is the theory, the vault is the working proof.

### The services paper — Supercharging AppSec Threat Modeling Services with GenAI and Semantic Graphs (9 June)

The commercial framing: GenAI as *"force multiplier"*, semantic graphs as *"a living context layer"*, AI-assisted code understanding, personalised multi-stakeholder deliverables, upskilling AppSec teams, new service offerings, an implementation roadmap. This one belongs on the site but flagged as **positioning, not method** — it is the pitch deck of the set, and mixing it with the research weakens both.

---

## Attribution

Several of these papers credit **"Dinis Cruz and ChatGPT Deep Research"** as co-authors in their front matter. Keep it. The estate's whole position is that AI-assisted work should be legible as such; hiding the co-authorship on the research about making security legible would be self-defeating. Each paper on the site carries its own PDF link, its LinkedIn post reference, and its original tags.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


---

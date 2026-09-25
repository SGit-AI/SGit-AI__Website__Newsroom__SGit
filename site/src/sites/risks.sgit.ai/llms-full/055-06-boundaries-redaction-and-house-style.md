# 06 — Boundaries, Redaction and House Style

---

## 1. The seven-site boundary map

`risks.sgit.ai` is the eighth property in the estate and the second to be carved *out of* an existing site rather than built from a gap. Getting the boundaries right on day one is what stops eight sites becoming eight competing copies of the same argument.

### Genuinely risk's own (risks.sgit.ai)

Everything in §1 concepts C1–C42, specifically: risk acceptance as underwriting; no-deny; the interval ladder; unaccepted-equals-critical; accepted-vs-acceptable; the grounding ladder; node type formulas and ontologies-of-ontologies **as applied to risk**; the register as a graph of graphs; fractal registers and relevance fade; technical vs business owner; Confirmed/Validated/Accepted; the underwriting graph and propagation; cascade and air gaps; not-knowing-is-a-fact; CIA blast-radius expansion; the plug question, plug profile and recoverability; altitude; appetite as a revealed band; the psychology of the physical act; the level ledger; register density; residuals; meta-risks; register health and gaming; three moves; decision-as-node; question-is-not-a-risk; do-not-internalise; the evidence economy's acceptor/certifier split; confidence bands; the two underwritings; observability as a risk dimension; five whys as a domain translator; RAMM; AOMM; the plug-pull maturity model; the harm taxonomy; the agentic incident taxonomy; and every worked example in §4.

### Belongs to **graphs.sgit.ai** (with risks.sgit.ai citing, not owning)

The general graph machinery, independent of risk: directed edges with named inverses and query paths that prevent node explosion (`06/26/semantic-graph-and-query-paths/v0.33.35__arch-brief__...directed-edges...md`); path properties read as language and multi-graph creation paths (`.../v0.33.35__arch-brief__...path-properties...md`); fractal semantic graphs as an agentic operating layer (`07/12/architecture/v0.33.48__arch-brief__...fractal-semantic-graphs...md`); browser-local query engines — Oxigraph/Kuzu/DuckDB WASM (`07/28/regulation-graph-and-acceptability/v0.33.53__arch-brief__...customised-standard...md`); the graph canvas REPL and "never render the whole graph" (`08/02/vault-as-substrate/v0.33.55__arch-brief__...graph-canvas-repl...md`); the 08/09 graphing-text cluster (enrichment and shared anchors, Wikidata as the concept layer, evidence packs attach-never-mutate, index-is-not-a-source, refactoring meaning); and digital twins in their general form (`06/26/digital-twins-and-world-models/`, 4 docs). **The boundary rule:** node type formulas as a *mechanism* are graphs.sgit.ai's; the grounding ladder as a *risk formula* is risks.sgit.ai's, and should cite the mechanism rather than restate it.

### Belongs to **nhi.sgit.ai**

The entire `06/04/nhi-2.0/` series (17 documents, ~50,000 words): agent identity as a startup thesis, cloud permissions per API, living off the land, multiple identities working together, permission granularity, PKI foundations, semantic knowledge graphs of identity, skills-come-with-identity, temporal permissions and time travel, web of trust and agent trust scores, plus the NHI commercial/moat/open-source briefs. Also the agent-mandate ontology's *identity* half (Principal, Agent, AgentTwin, CapabilityCertificate) and the 08/19 service-twin and agent-enrolment briefs. **The one exception:** `06/04/nhi-2.0/v0.32.3__strategy-brief__sg-send-nhi-2.0-risk-management-acceptance-underwriting-roi.md` is risk's origin document and should be *cited* by risks.sgit.ai as the first appearance of "the risk already exists", while living on nhi.sgit.ai.

### Belongs to **pki.sgit.ai**

Attribution, non-repudiation, signing and key topology: `team/roles/appsec/reviews/02/21/v0.5.0__review__pki-architecture-security*.md`; `08/19/briefs/v0.33.60__cross-team-brief__pki-site-review-mandate-is-the-gap-registry-is-the-missing-half.md`; `08/19/briefs/v0.33.60__arch-brief__agent-enrolment-without-borrowed-authority-append-lane-is-the-narrow-door.md`; the vault-authorisation cluster (`08/06/vault-authorisation/`, 6 docs — statecharts, kernel reference monitor, plugins-are-capability-grants, ambient authority as the injection root cause). **Note the tension:** the 19 Aug PKI-site review says *"mandate is the gap, registry is the missing half"* — meaning pki.sgit.ai currently carries mandate material that arguably belongs with risk. Worth a coordinated split.

### Belongs to **sg-sentinel.sgit.ai**

Anything that is **in-line enforcement**, which the risk corpus explicitly refuses. `05/24/sg-sentinel-batch2/v0.27.60__arch-brief__sg-sentinel-agent-governance.md` (reverse-proxy agent governance, controlling what agents do in dev and prod) is the clean case. The risk corpus's own stated boundary, from `07/23/posture-and-core-primitives/v0.33.50__strategy-brief__...never-in-line...md` and the honest-tension table in `07/24/.../v0.33.51__strategy-brief__...ability-to-stop...md`: *"The model rates the ability to stop but does not provide it; a customer who scores badly will ask us to supply the stop button, which is exactly the enforcement role the corpus refuses."* **risks.sgit.ai should state this boundary explicitly** — it measures and evidences; sg-sentinel enforces.

### Belongs to **newsroom.sgit.ai**

The evidence-economy *supply side*: news-backed evidence vaults run as an editorial mini news organisation, news stories as Evidence on the grounding ladder, author micropayments as a consumption-event billing primitive, MyFeeds and Trust-as-a-Service, evidence packs as a service, and paying-the-fact-creator. Files: `07/05/evidence-economy/` (3 docs), `07/31/projects-budgets-and-evidence/v0.33.54__strategy-brief__...paying-the-fact-creator...md`, `05/17/v0.27.55__strategy-brief__myfeeds-*`, `05/17/v0.27.55__arch-brief__myfeeds-website-rebuild-three-primitives.md`, `05/17/v0.27.55__dev-brief__articles-as-vaults-publishing-workflow.md`. **The split:** the *demand* side — force of proof, the risk-acceptor/fact-certifier split, the two prices, and confidence bands driving evidence purchases — is risk's own, because it is generated by accountability. The *supply* side — how evidence is produced, certified, priced and paid for — is the newsroom's.

### Additional boundaries worth naming (not in the brief but present in the corpus)

- **The EU AI Act / canonical-standard work** (`07/31/canonical-act-build/` 5 docs, `07/31/canonical-act-publish-and-product/` 5 docs, `07/28/regulation-graph-and-acceptability/` 4 docs, `07/31/the-act-as-a-measure/` 3 docs) is a substantial thread — ~40,000 words — that is *neither* risk nor graphs. It deserves either its own site (a "regulation graph" or "canonical act" property) or a clearly demarcated section on risks.sgit.ai. Risk's genuine claims within it are narrow and sharp: Article 9(5)'s undefined "acceptable", Article 14 as the plug obligation, Article 26(5)/(6) as the worked example anchor, and obligation-date ≠ liability-date.
- **sgit.ai itself** owns the vault, forge, catalogue and publishing mechanics (`08/14/sgit-site-and-hub/`, 8 docs). risks.sgit.ai should consume the topic-section pattern described there rather than re-argue it.
- **Wardley mapping** (`06/23/wardley-maps/`, `07/28/mvp-and-field-demo/v0.33.53__strategy-brief__...wardley-map-of-the-airgapped-register...md`) is a shared method, not risk's own.

---

---

## 2. Redaction watch-list

**This corpus has the highest redaction load of any pack so far.** It names real vendors critically, contains a live contract draft, and carries investor figures. Run these checks before any bulk publication.

### 9.1 Named real companies assessed critically — highest risk

- **`07/24/sovereignty-and-osmm/v0.33.51__research-brief__sg-send-osmm-assessment-001-[redacted]-level-1-survivability-inversion.md`** — names **two real vendors** [REDACTED · Tier-3 · see PUBLIC.md] (one a Ghent-based startup, described as *"roughly two years old with venture ownership"*), scores both at OSMM Level 1, and concludes the second presents *more* exposure on the axis it markets hardest. The document is scrupulous about its own limits (*"not publicly locatable as of this date"*, *"bounded above, not measured"*, *"re-run after direct enquiry"*), but publishing a critical comparative vendor assessment on a public research site is a legal and relationship exposure. **Do not publish without a legal read and a right-of-reply process.** The OSMM *model* brief in the same folder is clean.
- **`07/12/positioning-and-market/v0.33.48__strategy-brief__sg-send-[redacted]-risk-management-comparison-collaboration-integration-points-mature-governance.md`** and `.../v0.33.48__strategy-brief__...why-the-opportunity-exists-grc-airgapped-from-reality-competitor-map-data-side-threat.md` — competitor maps naming **two large vendors** [REDACTED · Tier-3 · see PUBLIC.md] with dismissive characterisations of their products. Commercial positioning, not research. **Internal-only.**
- **`07/27/outbound-agentic-risk/v0.33.52__research-brief__...agent-escaped-evaluation-sandbox...md`** — names **OpenAI** and **HuggingFace** in an incident analysis. Sourced and cautious, but names two real organisations in a security-failure narrative. **Needs framing and source verification before publication.**
- **`07/28/agentic-risk-research/v0.33.53__research-brief__...has-it-happened-before...md`** — names **Anthropic** (GTG-1002 disclosure), **Check Point**, and **nine Mexican government bodies including the federal tax authority, the civil registry and the electoral institute**. All from published sources with URLs, but naming foreign government agencies as breach victims warrants care. **Needs framing.**
- Other named companies across the risk corpus (counts from `briefs/06`, `07`, `08`): OpenRouter 332, LinkedIn 201, WhatsApp 104, Calendly 66, Salesforce 28, Nokia 22, Replit 20, OpenAI 20, [REDACTED · Tier-3 · see PUBLIC.md] (four Tier-3 vendor names and counts removed), Anthropic 17, Perplexity 14, **Klue 12**, **Vercel 10**, RIMS 7, Check Point 2. **Klue** and **Vercel** appear specifically in breach/failure contexts (`06/28/use-cases-and-risk-acceptance/v0.33.36__research-brief__...klue-breach...md`; the referenced-but-missing v0.33.46 "Vercel allow-all" brief). **Replit** appears as a database-deletion incident example. Each needs an individual publication decision.
- **`06/19/users-product-and-case-study/v0.33.28__research-brief__sg-send-whatsapp-case-study-three-scenarios-blast-radius-qr-full-access-ban-incidents.md`** — a named-platform blast-radius case study. Needs framing.

### 9.2 Codenames that may map to real entities

- **"Odysseus"** (42 mentions across `06/20/odysseus-mandate-analysis/`, 3 docs) reads as a codename for a real agent product or a real engagement. **Verify what it refers to before publishing anything from that folder.** The harm taxonomy inside it is otherwise excellent and generic.

### 9.3 Pricing, commercial terms, and investor material

- **`06/02/v0.31.9__strategy-brief__sg-send-investment-strategy-why-now-alchemist-guidance.md:86`** — illustrative revenue, valuation and exit figures [REDACTED · Tier-3 · see PUBLIC.md]. Explicitly framed as scenarios, not projections. **Internal-only / investor-only.**
- **`07/23/investor-response/v0.33.50__strategy-brief__sg-send-response-to-investor-analysis-...md`** — a direct response to an investor's analysis. **Internal-only**, though its "we are the meta risk" line is quotable if extracted and re-framed.
- **`07/27/first-product-to-market/v0.33.52__contract-draft__sg-send-voice-note-transcription-tool-partnership-[redacted].md`** — an actual **contract draft** with commercial terms [REDACTED · Tier-3 · see PUBLIC.md]. **Internal-only, unambiguously.**
- Competitor pricing quoted verbatim in the 07/23–07/27 briefs: `$29/month`, `$50/month`, `$500/month`, `$100 per named signer per month`, `$125 monthly`. These are third-party price points that will go stale and read as competitive intelligence. **Strip or date-stamp.**
- `07/02/product-roadmap/riskmandate-product-roadmap.{md,svg,pdf}` — internal delivery sequencing with build-state claims. **Needs framing** if published at all; its "already shipped" section is the useful part for a research site's honesty statement.
- `07/17/commercial-model/`, `06/30/partners-market-and-library/`, `07/23/freelance-network-and-tools/`, `07/31/markets-and-field-demo/` — commercial. **Internal-only or heavy framing.**

### 9.4 Named individuals

- **Dinis Cruz** is named as project owner/data controller in `team/roles/appsec/reviews/02/21/v0.5.0__grc-risk__auth-model-transition.md` and throughout the `team/humans/dinis_cruz/` path structure. Presumably fine (it is the founder's own corpus), but note that the **path itself** carries a personal name — if documents are republished with their paths as citations, the name travels with them. Decide deliberately.
- **Art Manion, Jay Jacobs, Michael Roytman** are named in `06/28/ontology-and-definitions/v0.33.36__arch-brief__...manion-jacobs.md`. The treatment is entirely respectful and the document is explicit that it paraphrases (*"Their definitions are paraphrased; see Sources"*), and it cites a LinkedIn post as one source. **Publishable, but confirm the paraphrase is fair and consider notifying them** — this is exactly the kind of bridge document that benefits from a right of reply, and the corpus's own stance (*"Offered to be built on and challenged"*) supports doing so.
- Role titles used throughout (IT Director, Head of GRC, CIO, CPO, CFO, CEO, ML platform lead, head of lending operations, DPO) are **generic and invented** — no redaction needed. The Article 26(5) example explicitly marks every invented element.

### 9.5 Live secrets and operational detail (pre-history)

- **`team/roles/grc/reviews/02/19/v0.4.12__risk-acceptance__deliberate-token-exposure.md`** — documents a **live `linkedin-user` access token**, its status (Active, not rotated), its quota (30 of 50 uses consumed, **20 remaining**), and the branch name where it remains readable in git history. Even though the token value is redacted in the document, the metadata is operational. **Internal-only, absolutely.** Same for `v0.4.16__debrief__INC-004-complete.md` and the `library/sgraph-send/incidents/INC-002…`/`INC-004…` folders.
- **`team/roles/appsec/reviews/02/21/v0.5.0__grc-risk__auth-model-transition.md`** — enumerates **21 unremediated security findings** (KD-1…KD-8, CT-1…CT-8, SP-1…SP-5) deprioritised on the basis of the current operating context, and states plainly that a change in that context reactivates all of them. **Internal-only.** (Ironically, it is also one of the best real illustrations of the "accepted is not acceptable" thesis — if it is ever to be used publicly, it must be abstracted beyond recognition.)
- `team/humans/dinis_cruz/briefs/02/27/v0.7.1__grc__risk-register-sg-send-skill-workflow.md` — names the live delivery chain (n8n, AWS SES, WorkMail, Gmail) and its interception points. **Internal-only.**

### 9.6 Documents already carrying their own disclaimers (good precedent to preserve)

Many of the best risk documents already model the right posture and their disclaimers should be carried across verbatim to risks.sgit.ai rather than stripped: *"Legal points are factual and not legal advice"*; *"The organisation is invented; every invented element is marked"*; *"Generic to the secure-browser and browser-isolation category. No vendor is named"*; *"The scenario is a product deployment example, shortened and illustrative, not any customer's register"*; *"Offered to be built on and challenged"*; and the CC BY 4.0 release line at the foot of nearly every brief — which is what makes public republication straightforward in the first place.

---

## 3. House style, inherited

Full treatment in the graphs pack `06__house-style-and-conventions.md`. Essentials, with the risk-specific emphasis:

- **`/llms.txt` is the whole surface**, and here more than anywhere — the commissioned audience is agents. Each entry carries the concept's single most important fact. `/llms-full.txt` is mandatory, not optional
- **`/documents/` with raw markdown as source of truth**, rendered pages as presentation
- **`/admin/comms.html`** with numbered asks and tasks in explicit states. **Seed with:** N1 the plug correction · N2 RAMM base levels · N3 legal read on the OSMM vendor assessment · N4 the pki.sgit.ai mandate split · N5 verify what "Odysseus" refers to
- **`/admin/versions.html`** · **`/about/participant.html`** · a build order published unresolved with open questions and honest tensions
- **Voice:** short declarative sentences making checkable claims; publish the argument before the implementation and say which is which; name what you got wrong; **no marketing adjectives** — this is the research site, and the contrast with riskmandate.ai is the product
- **Every section serves three readers:** documentation · live demonstration (the four vaults) · **agent guidance**. Here the third is the commission

**Vault rules:** publish read keys, never write keys · escrow the write key *before* publishing, or the vault is frozen · audit before publish and adopt the `PUBLIC.md` convention · **no metered capability behind a published read key** — the Risk Graph Explorer's `permissions: {}` is the model.

**Licence:** CC BY 4.0 per the 21 August decision. `docs.diniscruz.ai` prior art is **CC0** at source — state the source licence per page.

---

## 4. Two demonstrations to build in

1. **Run the site's own risk register in the open.** The corpus argues that a register is a graph, that unaccepted equals critical, and that the register maintains itself because accountability manufactures demand for evidence. A research site that publishes its own register — its open questions as unaccepted risks, with intervals — demonstrates all three at zero cost.
2. **Ship the definitions endpoint.** 42 concepts as JSON: name, one-line definition, canonical source, maturity, related concepts. It is the single highest-value artefact for the commissioned audience, nothing else in the estate has one, and it is a day's work from `01__concepts-index.md`.

---

## 5. Provenance for moved and republished pages

Two classes of source, two rules.

**From riskmandate.ai** — the page moved rather than being copied, so record the move:

```yaml
moved_from:      https://riskmandate.ai/acceptable.html
moved_on:        2026-08-22
leave_behind:    stub published at source, linking here
curation:        edited            # commercial framing removed
```

**From `docs.diniscruz.ai`** — the full provenance contract from the newsroom pack applies: `first_published` is the **original** date, original URL, original co-authors, honest curation label, `source_licence: CC0-1.0`, and `rel="canonical"` for verbatim republication. **Never redirect the source.**

**From the `__Send` repo** — never published, so the version tag is the address:

```yaml
source_repo:      https://github.com/the-cyber-boardroom/SGraph-AI__App__Send
source_repo_path: team/humans/dinis_cruz/briefs/06/28/ontology-and-definitions/v0.33.36__arch-brief__...
source_version:   v0.33.36
first_written:    2026-06-28
source_licence:   CC BY 4.0
```

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).



==============================================================================
== briefs/07__gaps-and-open-questions.md — source document, verbatim
==============================================================================


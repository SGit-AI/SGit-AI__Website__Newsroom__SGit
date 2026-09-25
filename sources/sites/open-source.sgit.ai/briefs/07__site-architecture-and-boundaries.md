# 07 — Site architecture, licensing and boundaries

## 1. The house pattern — and one requirement this site cannot skip

Copy **`pki.sgit.ai`**: `/llms.txt` as the whole agent surface, `/documents/` with raw markdown as source of truth, `/admin/comms.html` numbering asks (N1…) and tasks (T1…), `/admin/versions.html`, `/about/participant.html`, `/shipped/`. Add the `/llms-full.txt` that pki lacks.

**The one thing this site cannot treat as optional** is the agent-discovery ladder from `05__` §4, because a site about open source that agents cannot traverse fails in exactly the way the corpus already diagnosed:

> *"many agents can only fetch URLs that a search engine has already returned to them… **A link listed inside a fetched document did not count as having been seen.** It can read the map and cannot walk it."*

> *"the package registry page, which is a summary written for a different purpose, **becomes the authoritative source by default because it is the only one that ranks**."*

So: get indexed (the real fix), make `/llms.txt` **self-sufficient** rather than a link list (the cheap fix), and ship `/llms-full.txt` as a single-file concatenation (removes link-following entirely). And carry the estate's own practice — **the markdown twin at every URL**, extension swapped, with links inside the markdown pointing at markdown. `02__` §5 has the mechanism, including the Lambda@Edge detail that makes it work on static files.

---

## 2. ⚠️ Resolve the licensing inconsistency before writing a word

Covered fully in `02__` §1. Restated here because it blocks the build:

**The estate runs three licences and the corpus never mentions the third.** Apache-2.0 on code, CC BY 4.0 on ~1,100+ brief footers, and **CC0 1.0 on `docs.diniscruz.ai`** — which nobody has noticed and no document reconciles.

A site *about open source licensing* that carries an unexplained licence mismatch will be caught. Decide first: deliberate layered choice, or drift to be fixed. Then write the page — it is interesting either way.

**And write the missing page:** why Apache-2.0 rather than MIT. The patent grant? The NOTICE file? Defensive termination? The entire estate rests on that choice and the reasoning exists nowhere.

**This site's own content is CC BY 4.0**, consistent with the network. Stamp every raw markdown document and gate it in CI with `licence-audit.py` from the `graphs.sgit.ai` pack.

---

## 3. Quoting other people's material

Different from the sibling sites, because this one quotes the open-source world at length.

| Source | Regime | What the site may do |
|---|---|---|
| **`research__history-and-success-stories.md`** (in this pack) | CC BY 4.0 | Ours. The **sources it cites retain their own licences** — check before reproducing anything beyond a short quotation |
| **Wikipedia** (used heavily in the research) | **CC BY-SA 4.0** | Quote with attribution and a link back. **Do not adapt** — ShareAlike would bind the page. `04__`-style paraphrase-with-citation is fine; wholesale restructuring is not |
| **Project documentation** — curl FAQ, sqlite.org, letsencrypt.org, ASF annual report | Per project; several are permissive, some are ARR | Quote briefly with attribution. **Do not mirror.** The ASF FY2025 report is a PDF — link it, do not rehost |
| **Vendor and analyst reports** — Black Duck OSSRA, CNCF survey, Stack Overflow, Octoverse, StatCounter, W3Techs | **All rights reserved** | Cite the number, the source, the date and the caveat. **Never reproduce their charts.** The research file's evidence table is already in the safe form |
| **HBS WP 24-038** | Academic paper | Cite and link. Quote the method briefly. See `03__` §4 on the $8.8tn figure — never publish it without its definition |
| **`docs.diniscruz.ai` articles** | **CC0 1.0** | Republish freely. Attribute anyway, and keep `rel="canonical"` on the original URL with the recorded first-published date |

**One rule above all of these:** the research file marks several facts *not verified this session* and reports every fetch failure. **Do not publish a marked-unverified fact as established.** The site's credibility position is that it corrects other people's unsourced numbers; shipping one of its own would be self-defeating.

---

## 4. Do not publish

| Path | Reason |
|---|---|
| `library/alchemist/materials/` — **the whole tree** | Investment figures, valuation, revenue model, competitive positioning, pitch decks, named-competitor pricing. **Note the founder profile lives here** — the OWASP board claim in `06__` §1 is sourced from it, and that *fact* is public and quotable while the surrounding document is not |
| `team/humans/dinis_cruz/briefs/07/12/positioning-and-market/` — both files | Names Microsoft and dissects its governance programme as a partnering target; and a competitor map |
| `library/docs/_to_process/secure-send-llm-retention-compliance-gtm.md` | API-credit resale margins, competitive analysis, naming-research admission |
| `team/roles/grc/reviews/03/01/v0.7.19__workstream-proposal__grc.md` | Names a legal entity and enumerates its unfulfilled GDPR obligations; also maps a named third party's alleged violations |
| `team/roles/grc/reviews/02/19/` — both files | Name a **private individual** as risk acceptor, with signature blocks |
| `team/roles/appsec/reviews/02/21/v0.5.0__review__pki-architecture-security-revised.md` | Already classified: *"publishing an attack roadmap for live code"* |
| `library/sgraph-send/dev_packs/v0.32.1__vault-to-vault-append-comms/03__provisioning-and-topologies.md` | Names the driving rollout customer |
| `team/humans/dinis_cruz/briefs/08/06/payments-platform/*` | Pricing, margins, provider endpoint detail |

**Publish with care:** the *"somebody has to be the villagers"* brief is excellent and belongs on the site, but its M&A statistic and seven market figures are loosely attributed (*"reported"*, *"is cited as finding"*) and the brief itself flags that *"much of what circulates is vendor commentary recycling a smaller set of underlying studies."* Re-source or soften.

---

## 5. Naming other people and projects

**Fine, and necessary:** naming projects, foundations, licences, and the public authors of public work — Torvalds, Stallman, Peterson, Raymond, Stenberg, Hipp, Roosendaal, Freund. Recording that curl shut down its bounty on 31 January 2026 and why, with Stenberg's own published words, is factual reporting the community needs.

**Fine:** naming companies in the relicensing history — MongoDB, Elastic, HashiCorp, Redis, IBM, Oracle. These are documented corporate acts with dates and public statements.

**Not fine:** running the Change-of-Control Stress Test on a named commercial competitor and publishing the verdict as a scorecard. **Ship the test; let readers run it.** The one exception is running it on yourself, which `04__` §2 recommends doing publicly.

**Never:** quoting forum, Discord or mailing-list participants without consent, or naming a private individual from the internal corpus.

---

## 6. Network boundaries

| Site | Owns | Boundary |
|---|---|---|
| **`open-source.sgit.ai`** | The open-source position, the practice, the history, survivability, sovereignty, funding, OWASP | — |
| `wardley-maps.sgit.ai` | Mapping technique, Explorer/Villager/Town Planner as a pattern | **Shared: "somebody has to be the villagers".** Wardley owns the PST *pattern*; open-source owns the *NFR market argument*. One canonical copy, cross-linked. Also shared: de-commoditisation, genesis-by-accident |
| `standards.sgit.ai` | Instruments, provisions, crosswalks | **Shared: SPDX as an evidence artefact, and the licence-compliance thesis** (`05__` §5a). Standards owns the machinery; open-source owns the argument |
| `graphs.sgit.ai` | Graph theory, meaning through connectivity | Semantic OWASP and the PBOM sit on the boundary. Open-source owns the *why*, graphs owns the *how* |
| `risks.sgit.ai` | Risk, acceptance, the grounding ladder | Little overlap. Supply-chain risk links both ways |
| `sgit.ai`, `pki.sgit.ai`, `nhi.sgit.ai`, `sg-sentinel.sgit.ai` | Product and domain sites | Should link *here* for the licence and sovereignty argument |
| `riskmandate.ai` | Commercial | References, is not referenced |

---

## 7. Page by page

**`/`** — the thesis in 300 words: *"the power of open source is not for the community… it is not to give back"* and *"open source is not free… what you get is freedom."* Then the six history corrections as a teaser, because they establish that this site checks things.

**`/views/`** — `01__`'s five original pages. The site's identity.

**`/survivability/`** — `04__` §§1–2. **The stress test as a working tool, plus the self-audit.**

**`/history/`** — `03__`. Corrections first, timeline behind them, six success stories not fourteen.

**`/practice/`** — `02__`. The three licences, why Apache-2.0, the read-key discipline, publish-the-source-next-to-the-render, and the compliance gap stated honestly or closed before launch.

**`/agents/`** — `05__`. Dual purpose: the argument *about* agents, and the machine surface *for* them.

**`/owasp/`** — `06__`. **Blocked on the interview.** Ship the summit history and mark the first-person account as pending rather than writing around it.

**`/funding/`** — `04__` §§4–5. Three proposals, the cURL evidence, and a stated position.

**`/shipped/`** — `00__` §7, unsoftened, including the self-audit and the missing SBOM.

**`/admin/`, `/network/`** — house pattern. Publish the build order unresolved with `08__`'s questions and tensions visible.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).

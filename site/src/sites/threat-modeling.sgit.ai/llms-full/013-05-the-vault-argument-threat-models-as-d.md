# 05 — The Vault Argument: threat models as data with a home

**Version** v0.33.63 · 7 September 2026
**Source** `v0.27.45__strategy-brief__appsec-mini-tools-on-top-of-vaults.md` (16 May 2026) and the live vault platform at sgit.ai

---

## 1. The reframe

The AppSec mini-tools brief contains the sharpest commercial sentence in the corpus about this domain, and it deliberately refuses the obvious pitch:

> *"The platform's pitch to an AppSec team is not 'we have better threat modelling than X'; it is 'we have a clean home for all your security artifacts, with tools that work directly on top of them.'"*

The underlying insight, from the founder's voice memo as recorded in the brief: **every AppSec tool has a data-sharing problem; vaults solve it once for all of them.** An AppSec engineer juggles 8–15 tools, each with its own data home. The tool choice is usually fine. The data home is the friction.

## 2. The eight frictions, and the vault answer

The brief tabulates these directly; they map one-to-one onto a threat model's lifecycle:

| The question | The vault answer |
|---|---|
| Where does the threat model live? | In a vault — versioned, owned, exportable |
| How do I share it with auditors? | Read-only vault link, time-limited |
| How do I bring in new data? | Vault content appends; tools read from the vault |
| How do I run offline / air-gapped? | Vault collections are portable; tools run on local SG/Compute |
| How do I correlate findings across tools? | All tools write the same vault structure; findings cross-reference |
| How do I version-control security artifacts? | The vault commit history *is* the version control |
| How do I prove what was reviewed when? | Vault commits are cryptographically signed; auditors verify |
| How do I share without losing control? | Vault sharing with revocation |

Note how many of these are the *mandatory-disclosure* paper's requirements arriving as product features: a signed, dated, revocable, auditor-verifiable artefact is precisely the "reliable signal" that paper says the market lacks. `/graph/` and `/disclosure/` should link to each other for that reason.

## 3. The artefact schema

The brief specifies what a threat-modelling vault holds: *system descriptions, threat lists (STRIDE-categorised), attack trees, DREAD scores, mitigations, Gherkin test cases, evidence.* Two of those deserve the site's attention:

- **Gherkin test cases** — a mitigation expressed as an executable scenario is a threat model that CI can check. This is the strongest available answer to the "static document" failure mode in `01__`, and it is the site's best build spec.
- **Evidence** — the artefact that turns a claim into a disclosure.

## 4. The tool pattern

The productisation template named in the brief: **find a strong open-source tool → host it on our infrastructure → give it our UI and vault integration → contribute back.** The first target is **StrideGPT** (`mrwadams/stride-gpt`) — actively developed, LLM-integrated, supporting STRIDE plus the **OWASP LLM Top 10** and MAESTRO-inspired pattern detection, with two intended modes: pure client-side for air-gapped use, and ephemeral-compute-backed for teams.

**Publish the pattern, and honour the last step.** "Contribute back" is a commitment the site makes visible; `open-source.sgit.ai` holds the founder's position on exactly this, so `/graph/` links there rather than re-arguing it.

The brief lists eight further mini-tools on the same substrate (SBOM analysis, dependency scanning, secrets detection, OWASP Top 10 assessment, compliance evidence, policy management, pentest artefacts, vulnerability disclosure management). Only the threat-modelling one belongs on this site; the rest are a pointer.

## 5. What is real today vs. what is argued

The `/graph/` page must draw this line explicitly, because the gap between the 2025 papers' vision and today's implementation is the site's main honesty risk.

| Real, now | Argued, not built |
|---|---|
| The ThreatModCon vault: 11 linked models, 51 nodes, 179 threats, live and offline-capable | The continuous pipeline that keeps models current as code changes |
| Vault primitives: versioning, signing, revocable read-only sharing, sub-vaults, append lanes | Automated CVE-to-component linking that *"instantly flags"* a new threat |
| MGraph-DB as a memory-first graph store | The multi-ontology overlay (STRIDE × ATT&CK × OWASP) running as a live query over a production model |
| Seven written threat models, one validated against code | Gherkin-executable mitigations checked in CI |
| StrideGPT identified as the first integration target | The integration itself |

An agent reading this site should be able to tell, for any capability, whether it can use it today or is being told a direction. The site's own thesis about falsifiable claims requires nothing less.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


---

# 04 — Disclosure Boundaries: publishing security work about a live product

**Version** v0.33.63 · 7 September 2026

---

## 1. The problem, stated plainly

This site's best material is a security review of the founder's own running platform. It names vulnerabilities by number, locates two of them by file and line, and records several as `NOT MITIGATED` and two controls as `CONFIRMED MISSING`. The source brief itself notes that *"some access tokens have already been leaked in posts."*

Publishing all of that as-is would be a live exploitation guide for SG/Send. Publishing none of it would gut the site and quietly abandon the mandatory-disclosure position in `01__`. Neither is acceptable, so the boundary has to be drawn precisely.

## 2. The rule

**Publish the method always. Publish findings only once they are closed, or once they are harmless by design.**

| Category | Publish? | Reasoning |
|---|---|---|
| The method — bottom-up file-by-file, the parallel security tree, the `.security.json` schema, the STRIDE table format, the two-modes pattern, the validation format | **Yes, in full** | Methods are the transferable asset and expose nothing |
| Findings that are **fixed**, with the fix and its version | **Yes** | This is the disclosure the papers argue for; the version proves closure |
| Findings **mitigated by design** (e.g. server breach → impact None under zero-knowledge) | **Yes** | Publishing an architecture's strength is not exposure — but only where the ZK verification section backs it |
| Findings **still open** on a live system | **No** — hold | Publish the *count* and the *class*, dated, not the location |
| **File-and-line locations** of any unfixed finding | **Never** | The validation report's precision is its value internally and its danger externally |
| Third-party findings (Anthropic log retention, n8n logging, any vendor) | **No** | Not the estate's to disclose; describe the *question* asked, not the answer found |
| The leaked-token history | **Yes, as history** | Already public (`sgit.ai/case-studies/exposed-vault-key.md` tells this class of story); the honest post-mortem is an asset — provided the tokens are dead |

**The dating rule does the heavy lifting.** A finding published as *"open as of 17 March 2026"* and later shown as *"closed in v0.x.y"* is exactly the mandatory-disclosure model working. A finding published as open with no date and no closure is an unmaintained invitation.

## 3. Redaction is a versioned act, not a deletion

When a source document is published in redacted form, the site says so on the page: which categories were held, and why. A silently trimmed threat model is a false memory of the kind `nfrs.sgit.ai` warns about. Every redacted page carries: *"N findings held under the disclosure rule as of <date>; classes: <list>."* The count is generated.

## 4. Before launch: a closure pass

The findings in the corpus are from February and March 2026; this pack is dated September 2026. **Nothing may be published as "open" without re-checking it against current code first.** Two failure modes to avoid, in both directions: publishing a fixed vulnerability as open (defames the product), and publishing a still-open one as fixed (defrauds the reader, and is the exact behaviour the mandatory-disclosure paper condemns). This is comms question Q1.

## 5. Licensing

Site text, schemas, tables and analysis: CC BY 4.0. The white papers are the founder's own and carry their existing co-authorship attribution (several credit *"ChatGPT Deep Research"*). **STRIDE, MITRE ATT&CK, CAPEC, CWE/CVE, OWASP Top 10 and ASVS**: reference by name and link; do not reproduce their content. STRIDE is a Microsoft-originated taxonomy — the six category names are usable as terms of art, but the site publishes *its own* tables under those headings, never a copied framework text. This is the same link-never-rehost boundary as `influences.sgit.ai`.

## 6. Vulnerability disclosure for the site itself

A site publishing threat models must be reachable by anyone who finds a flaw in it. Ship `/.well-known/security.txt` and a disclosure policy page from day one. A threat-modeling site without a disclosure channel would be the discipline's own joke.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


---

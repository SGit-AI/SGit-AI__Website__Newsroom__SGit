---
title: Decisions
date: 2026-09-24
desk: Historian
covers: 2026-06-29 to 2026-09-24
standfirst: Every decision visible in the network's version logs, numbered D-001 onward, oldest first, with its date, context, rationale, the alternatives the source says were rejected, what it superseded and what later superseded it.
sources:
  - src:history/sgit.ai-version-log.json
  - https://sgit.ai/admin/versions.html
  - https://riskmandate.ai/versions.md
  - https://abp.sgit.ai/versions/index.md
  - https://riskmandate.ai/pricing.md
  - https://riskmandate.ai/index.md
  - https://store.sgit.ai/llms.txt
  - https://store.sgit.ai/llms-full.txt
  - https://sgit.ai/docs/briefs/index.html
  - https://sgit.ai/docs/briefs/riskmandate-partnership-risk-and-sgit-mapping.html
reviewed_by:
reviewed_on:
---

A decision here is a choice the sources record: a price set, a name chosen, an approach dropped, a rule adopted. Each entry has the same fields, after the Send project's historian: the date and site, the decision, its context, its rationale, the alternatives rejected (only where the source names them), what it supersedes, what later superseded it, and the source. The log runs oldest first. Within one day, sgit.ai entries come first in release order and riskmandate.ai entries follow in version order; neither site's record gives the order between the two.

**How to read the sources.** sgit.ai's version record is one table with no per-version anchors, so its entries link to [the record](https://sgit.ai/admin/versions.html) and name the version; the same text is in [the version log](src:history/sgit.ai-version-log.json). riskmandate.ai's releases each have a note. The 35 notes before its v1.0.0 are marked *reconstructed* in [its record](https://riskmandate.ai/versions.md), because those builds were made in a vault and are not in the site's repository. riskmandate.ai numbers its lead's memos D1 to D23 in its own brief register; where a note gives one, it is quoted as, for example, *riskmandate.ai's D16*. Those are not this log's numbers.

**What is left out.** Only claims the sources support. Where a source says a matter is somebody else's call and leaves it open, it is recorded as an open question in [the open questions](nr:history/open-questions), not as a decision taken. Where a source gives no rationale beyond the context, the entry says so. Entries D-073 onward were first recorded on 24 September, newest first, and are kept here in the new shape with their links.

## June and July 2026

### D-001: riskmandate.ai ships as a vault app
- **Date.** 29 June 2026 · riskmandate.ai
- **Decision.** The marketing site is delivered as an encrypted SG/Vault HTML app, built to render from one file in three contexts: the SG/App host, the vault preview and a plain static domain.
- **Context.** The first versioned snapshot, with an interactive risk queue where each agent's risk is accepted or sent back for more information.
- **Rationale.** Not stated beyond the three contexts.
- **Supersedes.** Nothing; the first recorded release in the network.
- **Superseded by.** D-047.
- **Source.** riskmandate.ai [v0.1.0](https://riskmandate.ai/versions/0.1.0.md) (reconstructed).

### D-002: Three price tiers, with a published enterprise band
- **Date.** 30 June 2026 · riskmandate.ai
- **Decision.** Pricing is Free, Consumption (metered by usage) and Enterprise at $5K to 15K per month.
- **Context.** A unified menu release.
- **Rationale.** Not stated.
- **Supersedes.** Not stated.
- **Superseded by.** D-003, then D-005.
- **Source.** riskmandate.ai [v0.4.2](https://riskmandate.ai/versions/0.4.2.md) (reconstructed).

### D-003: The risk-acceptance focus, and a certification claim scrubbed from frozen versions
- **Date.** 2 July 2026 · riskmandate.ai
- **Decision.** A new default design around the vision brief: no deny button, risk acceptance for an interval, the mandate defined. The vendor category stack, the unsourced trifecta figures, the value ladder, the certificates and pricing are removed. A "FedRAMP Ready" claim is scrubbed from every shipped version.
- **Context.** The launch post and an Ambassador review had filtered the message; a developer review of v0.4.3 flagged the certification claim as a public-domain blocker.
- **Rationale.** "a false certification-status claim cannot remain publicly served, so this is the documented, intentional exception to delta immutability".
- **Supersedes.** The v0.4 design; D-002 (pricing removed).
- **Superseded by.** D-005 for pricing, within a day.
- **Source.** riskmandate.ai [v0.5.0](https://riskmandate.ai/versions/0.5.0.md) (reconstructed).

### D-004: Versions become a frozen chain of deltas
- **Date.** 3 July 2026 · riskmandate.ai
- **Decision.** Each version folder holds only what it added or changed; building a version layers every folder up to it, and a pin file holds each output's sha256 as a drift tripwire.
- **Context.** A developer review had found that design snapshots were rebuilt from live shared code, so they were not actually frozen. The chain adopts another team's layered-delta review.
- **Rationale.** "rebuilding can no longer rewrite history".
- **Supersedes.** Duplicated source trees per version.
- **Superseded by.** D-047, which dropped the snapshots.
- **Source.** riskmandate.ai [v0.4.5](https://riskmandate.ai/versions/0.4.5.md) (reconstructed).

### D-005: Pricing restored, split by value, enterprise price "Custom"
- **Date.** 3 July 2026 · riskmandate.ai
- **Decision.** The three tiers return as Free, Consumption and Custom, each with three lines on how the tier is operated rather than feature gates. v0.5.0 is unlisted from the switcher.
- **Context.** The release before had dropped pricing.
- **Rationale.** "v0.5.0 over-corrected by dropping pricing entirely."
- **Supersedes.** D-003 (no pricing) and the published band of D-002.
- **Superseded by.** D-062.
- **Source.** riskmandate.ai [v0.5.1](https://riskmandate.ai/versions/0.5.1.md) (reconstructed).

### D-006: A machine-readable surface generated from one source
- **Date.** 3 July 2026 · riskmandate.ai
- **Decision.** `/llms.txt`, `/llms-full.txt` and an agent-content manifest, all generated from one content file, plus a page explaining them.
- **Context.** The pages were rendered by script inside a frame, so an agent fetching a URL saw an empty shell.
- **Rationale.** The Agents page frames it as a product governing agent access publishing "a clean one of its own".
- **Supersedes.** Nothing stated.
- **Source.** riskmandate.ai [v0.5.5](https://riskmandate.ai/versions/0.5.5.md) (reconstructed).

### D-007: Claims cut to what can be defended
- **Date.** 27 July 2026 · riskmandate.ai
- **Decision.** The new plug page ships with no modelled ROI multiple, no invented before-and-after metrics, no named-competitor deficiency claims, no placeholder logos and no dead links, with a test that the retired claims never come back.
- **Context.** The page was adapted from an exploratory MVP.
- **Rationale.** "Claims were cut to what we can defend".
- **Supersedes.** The MVP's claims.
- **Source.** riskmandate.ai [v0.9.1](https://riskmandate.ai/versions/0.9.1.md) (reconstructed).

## August 2026

### D-008: The architecture is called RiskGraph
- **Date.** 3 August 2026 · riskmandate.ai
- **Decision.** SGraph is gone from the site; the diagram reads RISKGRAPH. Frozen versions keep their own wording.
- **Context.** A release adding the accepted-is-not-acceptable page.
- **Rationale.** Not stated beyond "as the immutability model requires" for the frozen versions.
- **Supersedes.** SGraph as the name on the site.
- **Source.** riskmandate.ai [v0.9.2](https://riskmandate.ai/versions/0.9.2.md) (reconstructed).

### D-009: The deck as pre-rendered slides, not an embedded PDF
- **Date.** 3 August 2026 · riskmandate.ai
- **Decision.** The 12 slides are rasterised at build time and shown in a slide viewer, with the PDF one click away.
- **Context.** The embedded PDF showed a broken-document icon: the browser's PDF viewer is not available inside a sandboxed frame.
- **Rationale.** Pre-rendered images "add no third-party library, no CDN dependency and no canvas work at load"; only text selection is lost, and the PDF link covers it.
- **Alternatives rejected.** A runtime PDF renderer, rejected for those reasons.
- **Supersedes.** The embedded PDF.
- **Source.** riskmandate.ai [v0.9.4](https://riskmandate.ai/versions/0.9.4.md) (reconstructed).

### D-010: git tracks the encrypted vault store beside the working tree
- **Date.** 11 August 2026 · sgit.ai
- **Decision.** git tracks the encrypted `.sg_vault` store and excludes only the plaintext `local/` folder, so a git remote doubles as a zero-knowledge mirror of the vault.
- **Context.** Corrects the git integration of the release before.
- **Rationale.** Not stated beyond the mirror property.
- **Supersedes.** v0.1.5's `.gitignore`, which kept `.sg_vault/` out of git.
- **Superseded by.** D-077.
- **Source.** sgit.ai v0.1.6, [version record](https://sgit.ai/admin/versions.html).

### D-011: Every example key is an obviously invalid placeholder
- **Date.** 11 August 2026 · sgit.ai
- **Decision.** All example keys on the site become placeholders that cannot be valid, enforced by a validator rule.
- **Context.** The in-browser terminal release.
- **Rationale.** "format-valid example keys are squattable namespaces".
- **Supersedes.** v0.1.2's "full-strength keys in all examples".
- **Source.** sgit.ai v0.1.10, [version record](https://sgit.ai/admin/versions.html).

### D-012: The tripwire reads the secret from the gitignored tier, and the key is rotated
- **Date.** 12 August 2026 · sgit.ai
- **Decision.** The anti-leak tripwire no longer holds the passphrase; it reads it from the gitignored `local/` tier and scans for it. The key is treated as compromised.
- **Context.** The vault passphrase had been written into a tracked, public validator file as a tripwire regex, present in three commits.
- **Rationale.** So the secret "can never be hardcoded again"; "The key must be treated as compromised and rotated."
- **Supersedes.** The hardcoded tripwire.
- **Source.** sgit.ai v0.1.13, [version record](https://sgit.ai/admin/versions.html).

### D-013: A page nothing links to fails the build
- **Date.** 12 August 2026 · sgit.ai
- **Decision.** Every generated page must be reachable from another page, or the build fails.
- **Context.** v0.1.13 had built a briefs page and never registered it, so nothing linked to it.
- **Rationale.** Not stated beyond the incident.
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.1.14, [version record](https://sgit.ai/admin/versions.html).

### D-014: A freshness window on the mutable ref
- **Date.** 14 August 2026 · sgit.ai
- **Decision.** The HEAD ref is checked at most once every 120 seconds by default, configurable, with a button that forces a fetch.
- **Context.** The ref was the last per-page-view network request.
- **Rationale.** Server load "scales with readers rather than page views"; the cost is a bounded propagation delay.
- **Supersedes.** A ref fetch on every page view.
- **Source.** sgit.ai v0.1.23, [version record](https://sgit.ai/admin/versions.html).

### D-015: The open-source client is the distribution strategy
- **Date.** 14 August 2026 · sgit.ai
- **Decision.** The Why page is rewritten around what sgit makes possible, and its business-model answer says the open-source client "IS the distribution strategy, with services built on top".
- **Context.** The first Why page answered "is there a market" with verticals and a comparison table.
- **Rationale.** "the sharper answer is what sgit makes possible that was not possible before".
- **Supersedes.** v0.1.16's answer that the CLI had "no revenue attached".
- **Source.** sgit.ai v0.1.24, [version record](https://sgit.ai/admin/versions.html).

### D-016: Every page has a markdown twin, and llms.txt is generated
- **Date.** 14 August 2026 · sgit.ai
- **Decision.** Each page gets a `.md` twin from the same content, `llms.txt` is generated from the page registry, and the validator checks twins and their links.
- **Context.** Three changes shipped together with use cases per situation.
- **Rationale.** "so the two cannot drift"; an agent "can traverse the whole site without parsing HTML".
- **Supersedes.** A hand-maintained `llms.txt`.
- **Source.** sgit.ai v0.1.25, [version record](https://sgit.ai/admin/versions.html).

### D-017: The generator refuses to build if a page is missing from the index
- **Date.** 14 August 2026 · sgit.ai
- **Decision.** The `llms.txt` generator fails if any page would be omitted.
- **Context.** The v0.2.0 restructure's new case-studies section was silently absent from the machine index.
- **Rationale.** "a page nothing links to and a page the index does not list are both unpublished."
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.2.1, [version record](https://sgit.ai/admin/versions.html).

### D-018: Republish, don't retrofit
- **Date.** 15 August 2026 · sgit.ai
- **Decision.** A vault that cannot safely publish its read key is republished as a sanitised copy in a fresh vault, with credentials redacted and noted, before a read key is published.
- **Context.** The original strategy vault held its own read-write credential in its content, live delete tokens in bookkeeping, and keys from a low-entropy token.
- **Rationale.** The log calls it "the pattern the page teaches: republish, don't retrofit"; a republish "also sheds the history you cannot publish."
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.2.8, [version record](https://sgit.ai/admin/versions.html).

### D-019: The catalogue's two rules: read keys yes, vault keys never
- **Date.** 15 August 2026 · sgit.ai
- **Decision.** A vault that indexes vaults, including itself, whose schema states "read keys yes, vault keys never" and requires the write key to be escrowed before publishing. Write-key status is a public field per entry.
- **Context.** Ask A of the 14 August briefing pack.
- **Rationale.** Escrow first "because a frozen vault can never be corrected".
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.2.12, [version record](https://sgit.ai/admin/versions.html).

### D-020: CI verifies and tags, and never commits
- **Date.** 16 August 2026 · sgit.ai
- **Decision.** CI checks that the site version matches the release commit's subject and is the next minor, then tags. It authors no commits.
- **Context.** The pipeline was ported from another site whose action has CI commit a version bump.
- **Rationale.** A CI-authored commit "would exist only on the git side, breaking the both-remotes-in-sync invariant".
- **Alternatives rejected.** CI committing the version bump, as the upstream action does.
- **Supersedes.** Nothing stated.
- **Superseded by.** D-031, for what makes a push a release.
- **Source.** sgit.ai v0.2.17, [version record](https://sgit.ai/admin/versions.html).

### D-021: Comparisons as reproducible tests, and the privilege vocabulary first
- **Date.** 17 August 2026 · sgit.ai
- **Decision.** A comparisons section in which each entry is a test with steps, privileges and a re-run method; a seven-property privilege vocabulary published first; results that expire render as UNVERIFIED.
- **Context.** The 16 August comparison brief.
- **Rationale.** The vocabulary is "the part most likely to be argued with and the reason it is published first". One entry records a loss "plainly".
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.2.24, [version record](https://sgit.ai/admin/versions.html).

### D-022: Credential intake becomes a check
- **Date.** 17 August 2026 · sgit.ai
- **Decision.** A script classifies a credential before it touches a page, a catalogue entry or a commit: by prefix for new vaults and by shape for older ones. The release tripwire fires on the write prefix only when a credential character follows it.
- **Context.** A vault key had been submitted for publication as a read key, caught by shape, and only its derived read key published.
- **Rationale.** "The catch depended on somebody looking." Banning the bare prefix had caught its own author three times writing it in prose.
- **Alternatives rejected.** A rule matching the prefix followed by any non-space character "was tried first and failed", because in documentation the prefix is followed by markup.
- **Supersedes.** A habit of checking by eye.
- **Superseded by.** D-084, in part: classification "by declaration and never by shape". See Contradictions.
- **Source.** sgit.ai v0.2.25 and v0.2.26, [version record](https://sgit.ai/admin/versions.html).

### D-023: No metered capability behind a published read key, and the method written down
- **Date.** 17 August 2026 · sgit.ai
- **Decision.** Adopt the Risk Graph Explorer vault's third rule, no metered capability, and publish the seven-step publishing method for another site's agent to follow.
- **Context.** The first vault published as public by design, carrying its own rules.
- **Rationale.** "a published read key in front of an LLM config is an open tab on somebody else's budget"; the rule "is not in our guidance and is the one to adopt."
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.2.28, [version record](https://sgit.ai/admin/versions.html).

### D-024: The lazy-load bypass only when printing
- **Date.** 17 August 2026 · sgit.ai
- **Decision.** Screenshots are fetched ahead only when the page is printed; the print-only source line and landscape hint go; assets carry the site version as a cache-buster.
- **Context.** v0.2.30 had prefetched every screenshot once the page went idle, and a cached stylesheet had produced the bug report.
- **Rationale.** Prefetching for everyone made "every reader pay for images they never scrolled to"; printing "is an uncommon case and did not warrant instructions on the page".
- **Alternatives rejected.** Idle prefetch, called "the wrong trade, and correctly rejected".
- **Supersedes.** v0.2.30's prefetch, source line and landscape hint.
- **Source.** sgit.ai v0.2.31, [version record](https://sgit.ai/admin/versions.html).

### D-025: A release ends by asking the live site its version
- **Date.** 17 August 2026 · sgit.ai
- **Decision.** The release script polls the live URL for up to eight minutes until the version matches, and aborts loudly if it does not.
- **Context.** v0.2.31 and v0.2.32 pushed cleanly, reported success, and never reached the site, because the deploy job died on a rate limit.
- **Rationale.** The cost is up to eight minutes; the alternative is "telling somebody a fix is live when it is not." "a page nothing links to, a page the index omits, and a page the deploy never published are all equally unpublished".
- **Supersedes.** "both remotes in sync" as the end of a release.
- **Source.** sgit.ai v0.2.33, [version record](https://sgit.ai/admin/versions.html).

### D-026: The unshipped step is labelled PROPOSED
- **Date.** 18 August 2026 · sgit.ai
- **Decision.** Seven pages on vault-to-vault messaging and an API reference, from another team's fix pack, with the one unshipped step labelled PROPOSED and two unresolved endpoints listed as unresolved.
- **Context.** Three of the pack's findings did not survive checking, including a primitive the CLI does not use.
- **Rationale.** Publishing a correction for a claim never made "would have put a false statement in this log".
- **Alternatives rejected.** Publishing the draft as written, which "would have told integrators to build against the wrong primitive".
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.2.34, [version record](https://sgit.ai/admin/versions.html).

### D-027: Publishing is adding one file
- **Date.** 19 August 2026 · sgit.ai
- **Decision.** Updates and articles adopt another pipeline's rule verbatim: ordering, permalinks and feeds are derived, and publishing is one file. One divergence: root-relative links are rewritten to depth-relative ones.
- **Context.** Two new sections and a navigation restructure.
- **Rationale.** It "makes an unattended journalist agent safe: two agents publishing on the same day touch two different files and cannot conflict." The divergence exists because pages must also render inside a vault.
- **Supersedes.** Fourteen flat navigation items, now seven groups.
- **Source.** sgit.ai v0.2.35, [version record](https://sgit.ai/admin/versions.html).

### D-028: An audit that stops a publication, and a redacted republication
- **Date.** 20 August 2026 · sgit.ai
- **Decision.** No page for the Regulation Graph vault until it was republished into a new vault with two credentials replaced by visible markers, then re-audited from a fresh clone.
- **Context.** The audit found a live vault key for a different vault in plaintext.
- **Rationale.** Vault objects are content-addressed and immutable, "so a credential committed once may stay reachable from history, the only clean remedy is history that never held it."
- **Alternatives rejected.** Deleting the file, which "would not have been enough".
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.2.37, [version record](https://sgit.ai/admin/versions.html).

### D-029: The grant is not the mandate, and the site does not enforce
- **Date.** 20 August 2026 · riskmandate.ai
- **Decision.** The home page leads with the gap between grant and mandate, states "we define the mandate and map the gap; we do not enforce it", reframes enforcement words (OBSERVE, EXPIRE), and names the brand RiskMandate, one word. The previous home page stays selectable.
- **Context.** A partner-designed home page, and a brief that corrects an earlier claim.
- **Rationale.** "a declared mandate is *instrumentation, not a control*, and you instrument before you enforce."
- **Supersedes.** The 17 July claim that grant equals mandate; ENFORCE & OBSERVE and REVOKE in the partner's copy.
- **Source.** riskmandate.ai [v0.11.0](https://riskmandate.ai/versions/0.11.0.md) (reconstructed).

### D-030: The demos open automatically, over the host's embed protocol
- **Date.** 20 August 2026 · riskmandate.ai
- **Decision.** Embeds use the host's embed mode and handshake, the key held in memory and never in a frame URL; demos open with the page, per the project lead.
- **Context.** The fragment flow lost the key because storage is partitioned inside a cross-site frame.
- **Rationale.** "strictly better than the fragment flow it replaces"; the vault assets are cached and below-the-fold embeds stay idle.
- **Supersedes.** The fragment flow and the click-to-load gate of v0.11.0.
- **Source.** riskmandate.ai [v0.11.1](https://riskmandate.ai/versions/0.11.1.md) (reconstructed).

### D-031: The commit subject decides what is a release
- **Date.** 22 August 2026 · sgit.ai
- **Decision.** A push with no release subject is tagged nothing and published anyway; a push that claims a version is held to a stricter contract.
- **Context.** The tag job failed on two ordinary commits and blocked the deploy for a day.
- **Rationale.** "a missing tag is a bookkeeping gap, a blocked deploy is an outage."
- **Supersedes.** D-020's rule that every push must bump the version.
- **Source.** sgit.ai v0.2.40, [version record](https://sgit.ai/admin/versions.html).

### D-032: A sweep for third-party keys on every candidate vault
- **Date.** 25 August 2026 · sgit.ai
- **Decision.** Every candidate vault is scanned for API-key shapes of other providers, not only sgit's own credentials.
- **Context.** A vault passed the first credential pass clean and was caught only because a screenshot showed a live third-party key file.
- **Rationale.** "a genuine gap in the tooling, not a near miss to be reframed"; third-party keys "leak just as expensively".
- **Supersedes.** A scan built only for sgit credentials.
- **Source.** sgit.ai v0.2.43, [version record](https://sgit.ai/admin/versions.html).

### D-033: The insurability home page, without the market statistics
- **Date.** 25 August 2026 · riskmandate.ai
- **Decision.** A new home page on insurability, whose footer says *Own the mandate*; the mock-up's filing counts, approval rate and form numbers do not ship; web fonts are dropped for the system stack.
- **Context.** The second home-page pivot, ported from a mock-up.
- **Rationale.** The figures "are checkable claims about the real world that we cannot source from here, and a homepage is the worst place to carry a number that ages."
- **Alternatives rejected.** The mock-up's figures, and its footer *Enforce the mandate*.
- **Supersedes.** D-029's home page, kept as a linked page.
- **Superseded by.** D-059.
- **Source.** riskmandate.ai [v0.12.0](https://riskmandate.ai/versions/0.12.0.md) (reconstructed).

### D-034: The network directory leads with the question, in each site's own words
- **Date.** 26 August 2026 · sgit.ai
- **Decision.** The network page opens with seventeen questions mapped to sites, then groups and a table; every thesis is quoted from the site's own heading or lede. Network becomes a top-level group.
- **Context.** The section was built for four sites and there were nineteen.
- **Rationale.** At nineteen, a list of cards is "a directory a reader has to read before it helps them"; quoting means an entry "cannot drift into describing a site that no longer says that".
- **Supersedes.** The list of cards.
- **Source.** sgit.ai v0.2.44, [version record](https://sgit.ai/admin/versions.html).

### D-035: A hold raised, and cleared by the author
- **Date.** 27 August 2026 · sgit.ai
- **Decision.** The AIUC-1 catalogue vault is published as is, with its own disclaimers reproduced in full above the fold.
- **Context.** The vault's own notice says reuse rights for the control text have not been confirmed and that a public republisher should confirm them first.
- **Rationale.** Publishing a read key "is exactly that republication, so the work stopped and asked"; "the author chose to publish as-is."
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.2.49, [version record](https://sgit.ai/admin/versions.html).

## September 2026, before the week

### D-036: A class-coverage gate on every built page
- **Date.** 1 September 2026 · riskmandate.ai
- **Decision.** For every page, the build fails if too many of the classes the markup uses have no rule in its stylesheet.
- **Context.** v0.12.0 shipped with no stylesheet because its own delta listed that stylesheet for removal; another site's agent reported it with the diagnosis.
- **Rationale.** Pins detect drift in shipped versions, "so a brand-new version is pinned to whatever it builds to, including almost nothing."
- **Supersedes.** The v0.10.1 header-style gate, scoped to top-level pages only.
- **Source.** riskmandate.ai [v0.12.1](https://riskmandate.ai/versions/0.12.1.md) (reconstructed).

### D-037: A fork is a second artefact, not a second version
- **Date.** 5 September 2026 · sgit.ai
- **Decision.** The AIUC-1 conformance fork gets its own page and the catalogue page stays as it was; the vaults table carries one row.
- **Context.** The first instinct was to replace the catalogue page.
- **Rationale.** The fork answers "a DIFFERENT question"; "a table of published vaults is a list of things to open, not a changelog."
- **Alternatives rejected.** Replacing the catalogue page.
- **Supersedes.** Nothing.
- **Source.** sgit.ai v0.2.54, [version record](https://sgit.ai/admin/versions.html).

### D-038: The vaults table is generated, and its dates come from git
- **Date.** 6 September 2026 · sgit.ai
- **Decision.** The table is built from a data file; key and open-live columns go; the published date is the commit that first added each vault's page.
- **Context.** On an iPad the key column squeezed the vault id to one character per line.
- **Rationale.** The index "answers 'which of these do I want' and the vault page answers 'how do I open it'."
- **Alternatives rejected.** Update posts and the version log as the date source: the first missed ten vaults and false-matched one, the second had no line for two.
- **Supersedes.** Twenty-five hand-written rows.
- **Source.** sgit.ai v0.2.57, [version record](https://sgit.ai/admin/versions.html).

### D-039: The telemetry brief reversed, and the vault number made permanent
- **Date.** 7 September 2026 · sgit.ai
- **Decision.** The build brief now recommends the append bridge, with the correction in a box above the original; the vaults table's # column becomes a permanent publication ordinal.
- **Context.** The team that owns the append code reviewed the brief line by line and found both things it told a builder to verify were answered wrongly.
- **Rationale.** The direct fetch "is the WRONG fix because it reopens every egress from a frame holding decrypted vault content"; a row number that renumbered on sort "said nothing".
- **Supersedes.** The brief's direct-fetch advice (v0.2.55), and the renumbering column of D-038.
- **Source.** sgit.ai v0.2.58, [version record](https://sgit.ai/admin/versions.html).

### D-040: Proof before mechanism
- **Date.** 7 September 2026 · sgit.ai
- **Decision.** The home page leads with "a vault is a unit of work: data, app, history and sources, shipped as one string" and four real vaults under it; the terminal walkthrough moves down.
- **Context.** It follows a published diagnosis (v0.2.59) that the page led with encryption, which cannot be looked at.
- **Rationale.** Encryption "becomes the subordinate clause, which is where a property nobody can look at belongs".
- **Supersedes.** "the encrypted git for humans and AI agents" as the hero sentence.
- **Source.** sgit.ai v0.2.59 and v0.2.60, [version record](https://sgit.ai/admin/versions.html).

### D-041: The board lives in a vault, and the site reads it
- **Date.** 7 September 2026 · sgit.ai
- **Decision.** The team board's cards move into their own vault with a published read key; the release script pulls the vault before it builds.
- **Context.** Moving a card had cost a full site release.
- **Rationale.** "THE VAULT IS THE TRUTH; THE SITE IS A READER".
- **Supersedes.** Board cards as files in the site repository (v0.2.62).
- **Source.** sgit.ai v0.2.64, [version record](https://sgit.ai/admin/versions.html).

### D-042: The machine surface is generated first, and a voice interview prompt exists
- **Date.** 8 September 2026 · riskmandate.ai
- **Decision.** The llms files are written before the tests that inspect them; a prompt runs a voice-mode feedback interview and leads its debrief with objections.
- **Context.** Agents reading the site got the superseded pitch.
- **Rationale.** A failing test had left the files stale, and the next run "validated yesterday's file".
- **Supersedes.** The old build order.
- **Source.** riskmandate.ai [v0.12.2](https://riskmandate.ai/versions/0.12.2.md) (reconstructed). The interview pattern returns in D-119.

### D-043: A vault decides what is shown, never what the page does
- **Date.** 9 September 2026 · sgit.ai
- **Decision.** Decks and PDFs are read from vaults with the viewer owned by the site; vault content runs in two opaque-origin frames; a decrypted PDF is a download.
- **Context.** The only way to see the vaults' presentations was to open each vault's app.
- **Rationale.** Chrome refuses to render a PDF in a sandboxed frame, tested across every sandbox combination, and an inline PDF "would mean handing vault bytes this origin".
- **Alternatives rejected.** An inline PDF.
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.2.67 and v0.2.69, [version record](https://sgit.ai/admin/versions.html).

### D-044: Everything readable under /docs/, and version everything
- **Date.** 9 September 2026 · sgit.ai
- **Decision.** Fourteen pages move under `/docs/` with no redirects; the front door's first rule is "VERSION EVERYTHING, SHOW THE VERSION, LINK WHAT CHANGED".
- **Context.** Guidance had accumulated across three top-level folders.
- **Rationale.** No redirects "by instruction: the estate is in flux and has few external users."
- **Supersedes.** `/briefs`, `/vault` and `/guidance` as top-level homes.
- **Source.** sgit.ai v0.2.72, [version record](https://sgit.ai/admin/versions.html).

### D-045: The Seal becomes the mark, with the case against it kept
- **Date.** 9 September 2026 · riskmandate.ai
- **Decision.** Concept E, the Seal, replaces the text badge; an internal page records all eight concepts with the argument for and against each.
- **Context.** A brand release.
- **Rationale.** It "signals counter-signature and provenance to the audiences that read our output."
- **Alternatives rejected.** Seven concepts, named on the design record: RM Refined, Interval, Aperture, Index, Containment, Countersign and Record.
- **Supersedes.** The text badge.
- **Source.** riskmandate.ai [v0.13.0](https://riskmandate.ai/versions/0.13.0.md) (reconstructed).

### D-046: *Probably* is not the standard for a credential labelled private
- **Date.** 9 September 2026 · riskmandate.ai
- **Decision.** The AIUC-1 conformance demo is built and held, commented out and with the key removed from the comment; vaults of 3 MB or more wait to be asked; a scoped privacy claim is driven by a flag per vault.
- **Context.** The vault's read key carried the private read prefix, unlike every other key in the catalogue.
- **Rationale.** In the note's words, *probably* "is not the standard for publishing a credential with the word private in it"; an inlined key "ships in the page source whether or not a card renders it".
- **Supersedes.** "nothing you do inside a demo leaves your device", which was false together with a vault that phones home.
- **Source.** riskmandate.ai [v0.14.0](https://riskmandate.ai/versions/0.14.0.md) (reconstructed). sgit.ai relabelled those keys on 20 September (D-084).

### D-047: riskmandate.ai leaves its vault
- **Date.** 11 September 2026 · riskmandate.ai
- **Decision.** The site becomes the repository: each page is the document the server sends, navigation is links, the twelve frozen snapshots are dropped, and CI deploys `site/` with no vault in the path. The vault stays as the historical record.
- **Context.** `index.html` had been a shell loading one snapshot into a frame.
- **Rationale.** "Every page on the site therefore had the same URL. Nothing could be deep-linked, bookmarked, opened in a new tab or indexed."
- **Supersedes.** D-001 (a vault app) and D-004 (the snapshot chain and switcher).
- **Source.** riskmandate.ai [v1.0.0](https://riskmandate.ai/versions/1.0.0.md).

### D-048: The behaviour-policy ontology is promoted out of a game
- **Date.** 11 September 2026 · abp.sgit.ai
- **Decision.** The capability ontology is promoted from the data pack a game already published, rather than authored a second time, and five worked examples are derived from it.
- **Context.** The first version of abp.sgit.ai; its pipeline is copied from the game site.
- **Rationale.** "The capability ontology the ABP needs already existed, published".
- **Supersedes.** Nothing.
- **Source.** abp.sgit.ai [v0.1.0](https://abp.sgit.ai/versions/v0.1.0/index.md).

### D-049: The delta is derived and never authored, and it is stored
- **Date.** 11 September 2026 · abp.sgit.ai
- **Decision.** Every delta is stored with the versions of its inputs pinned, and the release gate recomputes each one; the foundation document is not rewritten but carries a correction notice.
- **Context.** The foundation document said, twice, that the delta is computed and never stored.
- **Rationale.** Storing it "is most of what makes it useful", because whether a control held over a period is a question about a series.
- **Supersedes.** The rule "computed and never stored", published nine hours earlier.
- **Source.** abp.sgit.ai [v0.2.0](https://abp.sgit.ai/versions/v0.2.0/index.md).

### D-050: The policy gets a page, and the page list one home
- **Date.** 12 September 2026 · riskmandate.ai
- **Decision.** The Agent Behaviour Policy becomes a page; `site/pages.json` is the single source of the page list, and a page can be `unlisted` or `private`.
- **Context.** The list was inlined in 24 pages with nothing keeping them in step.
- **Rationale.** The site "had been arguing the Agent Behaviour Policy's contents for months without the artefact having a name".
- **Supersedes.** The inlined page lists.
- **Source.** riskmandate.ai [v1.1.0](https://riskmandate.ai/versions/1.1.0.md).

### D-051: The Lab publishes vendor disagreements unresolved
- **Date.** 12 September 2026 · riskmandate.ai
- **Decision.** A Lab section with four states (finding, mockup, proposal, open question); where a vendor's advertised capability and granted scope disagree, the disagreement is published unresolved.
- **Context.** Work in progress needed a place looser about status and not about sourcing.
- **Rationale.** Settling them "would mean probing somebody else's service, which is out of bounds."
- **Alternatives rejected.** Probing the vendors' services.
- **Supersedes.** Nothing.
- **Source.** riskmandate.ai [v1.2.0](https://riskmandate.ai/versions/1.2.0.md).

### D-052: Every Lab page is also a dated PDF, and none is removed
- **Date.** 12 September 2026 · riskmandate.ai
- **Decision.** Each Lab entry is cut as dated PDF editions that are never rewritten or removed, each with a SHA-256 in a register; an edition is cut only when the argument changes.
- **Context.** Current thinking moves, and a link shows whatever the page says by the time the reader arrives.
- **Rationale.** The earlier reasoning is "exactly the part a business partner needs, because the journey explains the conclusion."
- **Supersedes.** Nothing.
- **Source.** riskmandate.ai [v1.3.0](https://riskmandate.ai/versions/1.3.0.md).

### D-053: A register of every brief, with its digest
- **Date.** 12 September 2026 · riskmandate.ai
- **Decision.** Every document the site is built from is archived as it arrived with its SHA-256, what it produced and what it is still owed.
- **Context.** One brief arrived twice, byte-identical, after three Lab entries had been written from the first copy; the other risk is a document never worked.
- **Rationale.** "Nothing gets worked twice" and "nothing gets quietly dropped"; a received item stays marked received, because "A register that listed only outputs would be a press release."
- **Supersedes.** Nothing.
- **Source.** riskmandate.ai [v1.6.0](https://riskmandate.ai/versions/1.6.0.md).

### D-054: The policy is not sold as a skill, and there is no invented deadline
- **Date.** 12 September 2026 · riskmandate.ai
- **Decision.** The pricing page says the prompt is the free half and the vault the paid one; the front page states a state, not a deadline; British spelling is settled.
- **Context.** Two briefs built in one release.
- **Rationale.** "a distributed skill can carry instructions and cannot carry a constraint"; "There is no deadline and inventing one would break this site's own rule against publishing a verdict."
- **Alternatives rejected.** Selling the behaviour policy as a skill.
- **Supersedes.** A pricing page that described only platform tiers.
- **Source.** riskmandate.ai [v1.7.0](https://riskmandate.ai/versions/1.7.0.md).

### D-055: Never a prohibition without its enforcer
- **Date.** 12 September 2026 · riskmandate.ai
- **Decision.** "never publish a prohibition without publishing what enforces it in the same row."
- **Context.** Lab 06, on network reach, where the grant cannot be enumerated.
- **Rationale.** A prohibition published without its enforcer "establishes foresight without mitigation", which is "a recklessness argument handed to the other side."
- **Supersedes.** Nothing.
- **Source.** riskmandate.ai [v1.8.0](https://riskmandate.ai/versions/1.8.0.md).

### D-056: Questions never name the asker, and the no comes first
- **Date.** 13 September 2026 · riskmandate.ai
- **Decision.** A Questions page of paraphrased, dated questions put in public, with the asker never identified; where the answer is no, it is the first line.
- **Context.** A page for real questions rather than an FAQ.
- **Rationale.** "they asked in a conversation, not for a marketing page".
- **Supersedes.** Nothing.
- **Source.** riskmandate.ai [v1.9.0](https://riskmandate.ai/versions/1.9.0.md).

### D-057: A policy is a draft, and the earlier claim stands in the record
- **Date.** 14 September 2026 · riskmandate.ai
- **Decision.** Three of the four objects can be written by people; only the delta is never authored. The v1.10.0 note is left as it was.
- **Context.** v1.10.0 said "nothing in a behaviour policy is authored except the mandate".
- **Rationale.** "A sentence somebody can disagree with is worth more than a number nobody can argue with, because the disagreement is where the information is." Rewriting the old note "is the one thing the register exists to prevent."
- **Supersedes.** The v1.10.0 claim.
- **Source.** riskmandate.ai [v1.11.0](https://riskmandate.ai/versions/1.11.0.md).

### D-058: Synthetic users read screenshots, not the page source
- **Date.** 15 September 2026 · sgit.ai
- **Decision.** The synthetic-user method hands the agent a screenshot, never the DOM, publishes its protocol in the vault, and keeps fixed findings in the list.
- **Context.** Five invented buyers walked through store.sgit.ai.
- **Rationale.** An agent reading the DOM "finds the buy button every time and therefore finds no confusion"; a list that loses fixed findings "cannot be compared with the next set of runs".
- **Alternatives rejected.** Giving the agent the DOM.
- **Supersedes.** Nothing.
- **Source.** sgit.ai v0.2.77, [version record](https://sgit.ai/admin/versions.html).

### D-059: The home page leads with the policy and says which step is sold
- **Date.** 15 September 2026 · riskmandate.ai
- **Decision.** The policy leads, insurability is the destination, the first rung is marked *what we sell* and the others *design*; three claims of connector-based discovery are rewritten; no price on the home page.
- **Context.** The home page claimed a discovery capability the Questions page disclaims.
- **Rationale.** "you cannot insure what nobody can describe."
- **Supersedes.** D-033's insurability-led home page.
- **Source.** riskmandate.ai [v1.12.0](https://riskmandate.ai/versions/1.12.0.md).

### D-060: Vaults in vaults: one renderer, versioned once
- **Date.** 15 September 2026 · riskmandate.ai
- **Decision.** The renderer moves out of every policy vault into one app vault; each policy vault carries the same small loader.
- **Context.** Nine behaviour-policy vaults built from the model site's shapes.
- **Rationale.** "A buyer's private vault works the same way with no code copied into it."
- **Supersedes.** A renderer copied into each vault.
- **Source.** riskmandate.ai [v1.13.0](https://riskmandate.ai/versions/1.13.0.md).

### D-061: Rules of engagement for agents working in parallel
- **Date.** 15 September 2026 · riskmandate.ai
- **Decision.** Claim a scope per branch, cut the release last after merging, regenerate generated files rather than hand-merge them, never rewrite an append-only record, one owner per surface.
- **Context.** Two and three sessions had been working at once, and the git log recorded what that cost.
- **Rationale.** "`dev` is the live site, so a merge is a deploy".
- **Supersedes.** Nothing stated.
- **Source.** riskmandate.ai [v1.18.0](https://riskmandate.ai/versions/1.18.0.md).

### D-062: The store is linked, and pricing is the four levels
- **Date.** 15 September 2026 · riskmandate.ai
- **Decision.** The site links store.sgit.ai's four levels; the third level is a prompt the customer runs; the Lab leaves the top bar.
- **Context.** The store put its levels up that day.
- **Rationale.** The lead's memo of 15 September says what the £500 level is.
- **Supersedes.** D-005's platform tiers.
- **Superseded by.** D-068, for prices on the site.
- **Source.** riskmandate.ai [v1.19.0](https://riskmandate.ai/versions/1.19.0.md).

### D-063: The £5 sale is a download; the other levels are a follow-up within 24 hours
- **Date.** 15 September 2026 · riskmandate.ai
- **Decision.** The level-1 page is the download, with its hash checked in the browser; levels 2 to 4 promise a person's follow-up within 24 hours.
- **Context.** v1.19.1 had left the file to the store and assumed working-day delivery times.
- **Rationale.** "The lead's answer the same day was simpler".
- **Supersedes.** v1.19.1's email delivery and working days.
- **Source.** riskmandate.ai [v1.19.2](https://riskmandate.ai/versions/1.19.2.md).

### D-064: The after-payment pages are public
- **Date.** 15 September 2026 · riskmandate.ai
- **Decision.** The four post-sale pages become indexable and linked from Pricing and a debrief for the store's team.
- **Context.** They had been unlisted and marked not for indexing.
- **Rationale.** "the aim is a working flow and the first orders".
- **Supersedes.** v1.19.1's unlisted, noindex pages.
- **Source.** riskmandate.ai [v1.19.3](https://riskmandate.ai/versions/1.19.3.md).

### D-065: The home page opens on who is arriving
- **Date.** 15 September 2026 · riskmandate.ai
- **Decision.** Three audience cards and pages; the insurance argument moves in full to its own page; the menu is rebuilt.
- **Context.** A brief from the lead, registered as riskmandate.ai's D10, asked to take content off the home page.
- **Rationale.** The chain: an agent is insurable when authorised in a way that survives examination, which needs a behaviour policy, "So the ABP is what we sell, and nothing above it is dropped."
- **Supersedes.** The insurance content on the home page.
- **Source.** riskmandate.ai [v1.20.0](https://riskmandate.ai/versions/1.20.0.md).

### D-066: A real policy on the front page, held by a test
- **Date.** 15 September 2026 · riskmandate.ai
- **Decision.** The invented company with a score is replaced by a real template's four numbers, checked against its delta file by a test that also refuses a rendered score.
- **Context.** The card sat beside a page saying the site computes no number.
- **Rationale.** "A number on a home page that nothing verifies is how the last one survived."
- **Supersedes.** The sample Index card.
- **Source.** riskmandate.ai [v1.20.1](https://riskmandate.ai/versions/1.20.1.md).

### D-067: Every inline script is parsed by a test
- **Date.** 15 September 2026 · riskmandate.ai
- **Decision.** A test parses every inline script on every page and fails the build if one does not parse.
- **Context.** Two pages had thrown on load while every test passed; a synthetic-user run caught it.
- **Rationale.** Not one existing check "executed or parsed a line of the JavaScript the pages carry."
- **Supersedes.** Nothing.
- **Source.** riskmandate.ai [v1.20.2](https://riskmandate.ai/versions/1.20.2.md).

### D-068: No price anywhere on riskmandate.ai
- **Date.** 16 September 2026 · riskmandate.ai
- **Decision.** Every price leaves the site, and pages name a level by its level; the one £5 kept is in the brief register as a dated record.
- **Context.** The store published a boundary: the store owns the cart, the order reference and the prices.
- **Rationale.** The boundary says riskmandate.ai "never runs a cart, holds a price or issues an order reference". The kept £5 stays because changing it "would be rewriting history rather than correcting it."
- **Supersedes.** D-062's prices on the site, and £5 as the entry price.
- **Superseded by.** D-071.
- **Source.** riskmandate.ai [v1.22.0](https://riskmandate.ai/versions/1.22.0.md).

### D-069: A dual licence for every policy vault
- **Date.** 16 September 2026 · riskmandate.ai
- **Decision.** The published template is CC BY 4.0; a paid copy carries a commercial licence to the named buyer; the build refuses a commercial copy without buyer, order and level.
- **Context.** The Gmail-connector vault taken end to end as the design template.
- **Rationale.** Not stated beyond the licence terms.
- **Supersedes.** Nothing stated.
- **Source.** riskmandate.ai [v1.24.0](https://riskmandate.ai/versions/1.24.0.md).

### D-070: The PDF is the download, not the page
- **Date.** 17 September 2026 · sgit.ai
- **Decision.** The summit sheets are published as HTML pages with the PDF beside them; the pages link the live vault table instead of restating a count.
- **Context.** Four audience sheets handed out at a startup summit.
- **Rationale.** "a PDF is invisible to a search engine, to llms-full.txt and to any agent reading the site"; "A PRINTED ARTEFACT SHOULD POINT AT A COMPUTED ONE FOR ANYTHING THAT MOVES."
- **Supersedes.** Nothing.
- **Source.** sgit.ai v0.2.80, [version record](https://sgit.ai/admin/versions.html).

### D-071: The partner's design, with prices back on the home page
- **Date.** 17 September 2026 · riskmandate.ai
- **Decision.** A partner's home page is built as drawn: the four objects are named reach, mandate, gap and barriers (the files keep the old names), and four prices return, each read from the store with a date.
- **Context.** A design arrived from a business partner that was "better than what was live".
- **Rationale.** Built "as drawn", including "the two that overrule positions this site had taken". The note adds that this "re-opens a boundary the other team wrote down and they should be told."
- **Alternatives rejected.** The design's four-item navigation, left for a deliberate information-architecture decision.
- **Supersedes.** D-068 (no price anywhere).
- **Source.** riskmandate.ai [v1.25.0](https://riskmandate.ai/versions/1.25.0.md).

### D-072: The partner's own HTML, with its fonts served from here
- **Date.** 17 September 2026 · riskmandate.ai
- **Decision.** The reconstruction is replaced by the partner's file, its CSS scoped under its own wrapper and its fonts committed with their licence.
- **Context.** The partner sent the HTML after v1.25.0 had been rebuilt from a picture.
- **Rationale.** "No page on this site calls a third party and the home page is not going to be the first".
- **Alternatives rejected.** Loading the fonts from the font provider, as the partner's file did.
- **Supersedes.** D-071's reconstruction.
- **Source.** riskmandate.ai [v1.25.1](https://riskmandate.ai/versions/1.25.1.md).

## 18 September 2026

### D-073: The summit sheets are kept as printed
- **Date.** 18 September 2026 · sgit.ai
- **Decision.** The correction to a stale vault count becomes a dating note (the author's call).
- **Context.** The previous release had corrected '26 public vaults' to 29.
- **Rationale.** The sheets are "a dated record of what was said in September 2026"; "a printed artefact that gets silently re-edited to match today stops being a record of anything."
- **Supersedes.** The previous release's correction of the count.
- **Source.** sgit.ai v0.2.81, [version record](https://sgit.ai/admin/versions.html).

### D-074: Publish for an archetype, not an instance
- **Date.** 18 September 2026 · sgit.ai
- **Decision.** Vault #30 describes a type of company derived from public sources, so there is nothing to redact.
- **Context.** The sibling pack described a real role and withheld the company.
- **Rationale.** "a document written for a class can be published; a document written for an instance has to be scrubbed."
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.2.82, [version record](https://sgit.ai/admin/versions.html).

### D-075: One menu on the home page; Lisbon becomes a dated record
- **Date.** 18 September 2026 · riskmandate.ai
- **Decision.** The in-page anchor strip is removed; the summit page is unlisted but kept.
- **Context.** Two menus on one page; the summit's second day.
- **Rationale.** On the page the strip made two menus and put the buy action twice above the fold.
- **Supersedes.** v1.25.1's decision to keep the strip under the shared menu (D-072).
- **Source.** riskmandate.ai [v1.25.4](https://riskmandate.ai/versions/1.25.4.md).

### D-076: The menu leads with the product
- **Date.** 18 September 2026 · riskmandate.ai
- **Decision.** Five top-level entries and 21 pages in the menu, with two departures from the proposal where link counts said otherwise.
- **Context.** Option A of the menu proposal written the day before.
- **Rationale.** The menu "was the last part of the site still describing what RiskMandate used to be".
- **Alternatives rejected.** Unlisting *Give feedback*, which would have orphaned it; unlisting three essays before they had another home.
- **Supersedes.** Seven entries and 34 pages.
- **Source.** riskmandate.ai [v1.26.0](https://riskmandate.ai/versions/1.26.0.md).

## 19 September 2026

### D-077: The site's vault mirror is deleted and purged
- **Date.** 19 September 2026 · sgit.ai
- **Decision.** Delete the mirror, purge it from all 112 commits and force-push, with the forced push authorised by the author.
- **Context.** No reader, no published read key, dead since v0.2.76, and 91% of the repository.
- **Rationale.** The purge "is safe for the same reason the mirror was: everything removed was ciphertext under a key that was never in the repository".
- **Supersedes.** D-010, the one-tree-two-remotes pattern, now a retrospective.
- **Source.** sgit.ai v0.2.84, [version record](https://sgit.ai/admin/versions.html).

### D-078: The page is called Fractal Semantic Graphs and leads with the definition
- **Date.** 19 September 2026 · sgit.ai
- **Decision.** Title, description, nav card and `llms.txt` renamed; the page opens by defining the term.
- **Context.** The author's first read of v0.2.85.
- **Rationale.** The first screens must work for a visitor who knows graphs but "has never met the FSG idea".
- **Supersedes.** 'How far down does the graph go?' as the page's opening, now a section.
- **Source.** sgit.ai v0.2.87, [version record](https://sgit.ai/admin/versions.html).

### D-079: Fractal means the inside is different
- **Date.** 19 September 2026 · sgit.ai
- **Decision.** The definition is rewritten around grammar (constant) against schema (free to change).
- **Context.** The author's reading caught the definition describing a hierarchy.
- **Rationale.** Same types, verbs and rules at every level "IS a hierarchy"; it becomes fractal "at the moment zooming in lands you somewhere different".
- **Supersedes.** D-078's definition and test.
- **Source.** sgit.ai v0.2.89, [version record](https://sgit.ai/admin/versions.html).

### D-080: The page title suffix stays until the site-wide pass
- **Date.** 19 September 2026 · sgit.ai
- **Decision.** The ', sgit.ai' suffix on page titles stays "until the site-wide pass is decided".
- **Context.** The em-dash removal on one page.
- **Rationale.** It is a site-wide convention.
- **Supersedes.** Nothing.
- **Source.** sgit.ai v0.2.93, [version record](https://sgit.ai/admin/versions.html).

### D-081: A brief instead of a footnote
- **Date.** 19 September 2026 · sgit.ai
- **Decision.** The note about graphs.sgit.ai's boundaries page becomes a full brief to that site.
- **Context.** The author asked for the paragraph to go and a proper brief instead.
- **Rationale.** The sgit.ai page "is now the fullest worked application of that site's two theses."
- **Supersedes.** The 'one wording to pass upstream' paragraph added in v0.2.89.
- **Source.** sgit.ai v0.2.94, [version record](https://sgit.ai/admin/versions.html).

### D-082: The insurance answer drops the thread it came from
- **Date.** 19 September 2026 · riskmandate.ai
- **Decision.** The page states the question plainly; the v1.26.1 note keeps the record of how it arrived.
- **Context.** The lead's reading.
- **Rationale.** "the question is the thing, and it is asked by everyone the moment AI insurance comes up"; "records are not rewritten."
- **Supersedes.** The opening that recounted who asked whom.
- **Source.** riskmandate.ai [v1.26.2](https://riskmandate.ai/versions/1.26.2.md).

## 20 September 2026

### D-083: The article that introduces the term is published here, as written
- **Date.** 20 September 2026 · sgit.ai
- **Decision.** The Fractal Semantic Graphs article is published on sgit.ai as the canonical copy, with the figures LinkedIn cannot carry.
- **Context.** The author asked whether the site had a place for it.
- **Rationale.** Not stated beyond the missing images.
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.2.97, [version record](https://sgit.ai/admin/versions.html).

### D-084: Private prefixes banned, credentials classified by declaration
- **Date.** 20 September 2026 · sgit.ai
- **Decision.** Published read keys use the public read prefix; the validator bans both private prefixes in tracked files; the checker refuses the private read prefix for publication; a credentials page is published.
- **Context.** Another agent correctly refused to open keys labelled private read.
- **Rationale.** "It was right and our label was wrong"; the private read prefix is refused "because the label says the opposite of what publishing it does."
- **Supersedes.** Seven published credentials under the private read prefix; in part, D-022's classification by shape (not stated by the source; see Contradictions).
- **Source.** sgit.ai v0.2.98, [version record](https://sgit.ai/admin/versions.html).

### D-085: One newest-first order for the whole site
- **Date.** 20 September 2026 · sgit.ai
- **Decision.** Every list of vaults reads one sorted source, with assertions in the build.
- **Context.** The human table and the machine list had disagreed for four releases.
- **Rationale.** The page's own footnote said the two "are generated from the same file and cannot drift".
- **Supersedes.** The table's file order.
- **Source.** sgit.ai v0.2.99, [version record](https://sgit.ai/admin/versions.html).

### D-086: The em-dash leaves all prose, and every published read key declares itself public
- **Date.** 20 September 2026 · sgit.ai
- **Decision.** 3,200 em-dashes rewritten site-wide with a guard; 102 legacy-prefixed and 24 bare published read keys moved to the public read prefix.
- **Context.** A good many readers find the character off-putting; the legacy prefix was neutral rather than wrong.
- **Rationale.** The public prefix "declares the intent".
- **Supersedes.** The v0.2.92 statement that the site-wide pass "is a separate decision and has not been made here", and the v0.2.98 note leaving the legacy keys as a decision for the author.
- **Source.** sgit.ai v0.3.0, [version record](https://sgit.ai/admin/versions.html).

### D-087: A barrier names its holder, and no adjective survives the build
- **Date.** 20 September 2026 · riskmandate.ai
- **Decision.** `not_reachable` is replaced by a blocked list whose entries must name what blocks them; six holder classes and seven questions per barrier; adjectives about controls fail the build. The site starts publishing articles.
- **Context.** Two barriers that pass the same test can be nothing alike.
- **Rationale.** "how much a barrier is worth depends on the deployment it is in."
- **Supersedes.** `not_reachable`.
- **Source.** riskmandate.ai [v1.27.0](https://riskmandate.ai/versions/1.27.0.md).

### D-088: The local check runs all of CI's checkers
- **Date.** 20 September 2026 · riskmandate.ai
- **Decision.** `npm run check` runs every checker CI runs, including the vault builds and generated pages.
- **Context.** The v1.27.0 push went red on CI for a stale stamp.
- **Rationale.** The local check had run "five of CI's seven checkers and not the two that would have" noticed.
- **Supersedes.** A local check running five of seven checkers.
- **Superseded by.** D-120 found a further check the local run did not make.
- **Source.** riskmandate.ai [v1.27.1](https://riskmandate.ai/versions/1.27.1.md).

### D-089: *Writing* becomes *Articles*
- **Date.** 20 September 2026 · riskmandate.ai
- **Decision.** The section is renamed at the lead's ask; addresses unchanged.
- **Context.** Two releases after the section began.
- **Rationale.** "*Writing* described the activity; *Articles* describes what a reader will find."
- **Supersedes.** *Writing*, from v1.27.0.
- **Source.** riskmandate.ai [v1.27.2](https://riskmandate.ai/versions/1.27.2.md).

## 21 September 2026

### D-090: A startups section, and billing left out
- **Date.** 21 September 2026 · sgit.ai
- **Decision.** A new startups section; billing and payments are "not here, not planned".
- **Context.** A large part of why sgit exists is to let other people build on it.
- **Rationale.** The section lists what a founder still has to bring, "which is the section that makes the rest credible".
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.4.0, [version record](https://sgit.ai/admin/versions.html).

### D-091: Disclaimers become lessons
- **Date.** 21 September 2026 · sgit.ai
- **Decision.** Three notes are moved off the vaults page onto a new Lessons learned page; nothing is thrown away.
- **Context.** A first-time visitor met four boxes of process text before a single vault.
- **Rationale.** The author's instruction: the notes were interesting, just in the wrong place; "a rule with no origin is only a preference".
- **Supersedes.** Three disclaimer boxes above the vaults table.
- **Source.** sgit.ai v0.4.1, [version record](https://sgit.ai/admin/versions.html).

### D-092: Every article gets an abstract; the startup article takes its LinkedIn title
- **Date.** 21 September 2026 · sgit.ai
- **Decision.** The summary renders as an italic paragraph with a bold Abstract label (v0.4.3); the startup article takes the prefixed title it was given on LinkedIn, in sentence case (v0.4.4).
- **Context.** The author republished on LinkedIn in that form.
- **Rationale.** The labelled abstract "reads better than a bare lead"; the two versions of the title "should match".
- **Supersedes.** A bare lead, and the earlier startup title.
- **Source.** sgit.ai v0.4.3 and v0.4.4, [version record](https://sgit.ai/admin/versions.html).

### D-093: The SaaS article's title, and then its address
- **Date.** 21 September 2026 · sgit.ai
- **Decision.** The title was changed three times in one evening and settled on 'The SaaS apocalypse will be decided by inertia, not by AI', "chosen by the author from the inertia set" (v0.4.6). Then the file name was made to follow it, with no redirect: the old address returns 404 on purpose (v0.4.7).
- **Context.** The author explained why the earlier word misdescribed the argument (v0.4.5).
- **Rationale.** "AI IS A CONSTANT, AVAILABLE TO BOTH SIDES", so the variable is inertia.
- **Supersedes.** 'The SaaS apocalypse is optional' (v0.4.3), then 'The SaaS apocalypse belongs to whoever has the least inertia' (v0.4.5); and the slug kept unchanged through the retitlings so links handed out kept working.
- **Source.** sgit.ai v0.4.3 to v0.4.7, [version record](https://sgit.ai/admin/versions.html).

### D-094: Preview cards are JPEG
- **Date.** 21 September 2026 · sgit.ai
- **Decision.** 1200x630 JPEG cards generated from each article's first figure, and the large card type.
- **Context.** Pages had no `og:image`.
- **Rationale.** "LinkedIn's crawler does not read WebP. It drops the image without a word".
- **Alternatives rejected.** WebP cards, "the obvious fix", which would not have worked.
- **Supersedes.** No `og:image`, and the small summary card.
- **Source.** sgit.ai v0.5.0, [version record](https://sgit.ai/admin/versions.html).

### D-095: The build refuses an article with a figure and no card
- **Date.** 21 September 2026 · sgit.ai
- **Decision.** The build stops on any article whose body has a figure but no preview card; `release.sh` runs the generator.
- **Context.** The v0.5.0 guard could not fire on the case it was written for.
- **Rationale.** "the build refuses rather than guessing."
- **Supersedes.** The v0.5.0 validator check as the safeguard for a forgotten generator run.
- **Source.** sgit.ai v0.5.1, [version record](https://sgit.ai/admin/versions.html).

### D-096: The third article is retitled on the idea, not the symptom
- **Date.** 21 September 2026 · riskmandate.ai
- **Decision.** New title leading with *union*; the address does not change.
- **Context.** The lead's reading that the idea travels beyond mailboxes.
- **Rationale.** The old title was "only true of mailboxes on a Tuesday"; *union* "is the word the whole argument turns on."
- **Supersedes.** The title shipped the day before in v1.27.2.
- **Source.** riskmandate.ai [v1.27.3](https://riskmandate.ai/versions/1.27.3.md).

### D-097: A free first step, and the phase is users
- **Date.** 21 September 2026 · riskmandate.ai
- **Decision.** A new top-level Try it section, the rung below the store's lowest level at no price. The lead's memo sets the measure as people who run the prompts and people who end up with a policy, "not visits, not downloads".
- **Context.** The offering is built, and what is missing is people who have used it.
- **Rationale.** "*Nobody buys a full policy until they have made a smaller one.*"
- **Supersedes.** Nothing stated. The note records that nothing on the site counts the measure yet, and that this is the lead's decision.
- **Source.** riskmandate.ai [v1.28.0](https://riskmandate.ai/versions/1.28.0.md).

## 22 September 2026

### D-098: Articles get a byline, and the byline gets a page
- **Date.** 22 September 2026 · sgit.ai
- **Decision.** First-person articles carry an author and a link; the build refuses an author without a URL; site-voice articles stay unsigned. The next release points the byline at an on-site profile page.
- **Context.** A first-person article carried no name on a site about provenance.
- **Rationale.** "a byline without a link is a name, not provenance."
- **Supersedes.** No byline; then a byline linking to LinkedIn (v0.5.5 to v0.5.6).
- **Source.** sgit.ai v0.5.5 and v0.5.6, [version record](https://sgit.ai/admin/versions.html).

### D-099: The reviewed level written down before it has been sold, and nobody scored
- **Date.** 22 September 2026 · riskmandate.ai
- **Decision.** The top level is described as a service with eight steps; reviewers are chosen on published facts, never scored, ranked or starred; one reviewer page and one labelled placeholder; what the reviewer is paid is "deliberately not published" (riskmandate.ai's D11).
- **Context.** A brief asked what the service is and who does it.
- **Rationale.** What is published about a person is what that person has published, or what they write and sign off; the pay is "A commercial term, and the lead's call".
- **Supersedes.** A site that said almost nothing about the top level.
- **Source.** riskmandate.ai [v1.29.0](https://riskmandate.ai/versions/1.29.0.md).

## 23 September 2026

### D-100: Partnerships, made in public
- **Date.** 23 September 2026 · sgit.ai
- **Decision.** A new Partnerships section with a stated method (public material only, evidence not pitch), first case UK Sovereign AI; the founder's own statement of UK anchoring is added in the first person the same day (v0.5.8).
- **Context.** Written to be forwarded.
- **Rationale.** The anchoring is stated first-hand "because only the founder can supply it".
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.5.7 and v0.5.8, [version record](https://sgit.ai/admin/versions.html).

### D-101: The Sovereign AI page is titled as a proposal
- **Date.** 23 September 2026 · sgit.ai
- **Decision.** Title: 'A proposed partnership between sgit.ai, RiskMandate.ai and UK Sovereign AI'.
- **Context.** A reader from a forwarded link could not tell it was a proposal.
- **Rationale.** Not stated beyond the context.
- **Supersedes.** The earlier title (not quoted in the entry).
- **Source.** sgit.ai v0.5.9, [version record](https://sgit.ai/admin/versions.html).

### D-102: The first business plan published for somebody else to run
- **Date.** 23 September 2026 · sgit.ai
- **Decision.** Publish Agent as Webmaster under the publishing method; vault counts move to thirty-two, while "measured estate figures keep their 21 September date".
- **Context.** The startups section gains business plans to build on.
- **Rationale.** Not stated beyond the context.
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.6.0, [version record](https://sgit.ai/admin/versions.html).

### D-103: A reader's decision first on the DSIT toolkit page
- **Date.** 23 September 2026 · sgit.ai
- **Decision.** The page opens on an outcome and three actions; architecture material moves below, and versions are shown side by side without being merged.
- **Context.** Rebuilt from a brief after the vault moved on.
- **Rationale.** Not stated beyond the brief.
- **Supersedes.** A page that opened on four worlds and 617 nodes.
- **Source.** sgit.ai v0.6.1, [version record](https://sgit.ai/admin/versions.html).

### D-104: The logo as outlined EPS, written by a script
- **Date.** 23 September 2026 · riskmandate.ai
- **Decision.** Four EPS files, with lettering converted to outlines and no font referenced; two older PNGs left as they are and named for somebody to decide.
- **Context.** An exhibition-board form asked for EPS.
- **Rationale.** "An EPS that *names* a font is an EPS that looks different on somebody else's RIP"; a script makes the next variant "a line of code rather than an afternoon".
- **Supersedes.** Nothing stated.
- **Source.** riskmandate.ai [v1.29.1](https://riskmandate.ai/versions/1.29.1.md).

### D-105: Shorter descriptions, and the 180-character floor retired
- **Date.** 23 September 2026 · riskmandate.ai
- **Decision.** Two shorter boilerplate versions, 110 and 80 characters, that drop the company name rather than the claim.
- **Context.** An exhibitor form rejected 180 characters.
- **Rationale.** "A rule this site wrote about its own copy lost to a form that counts."
- **Supersedes.** The instruction to say nothing shorter than 180 characters.
- **Source.** riskmandate.ai [v1.29.2](https://riskmandate.ai/versions/1.29.2.md).

## 24 September 2026

### D-106: A public call for collaboration on vault key management
- **Date.** 24 September 2026 · sgit.ai
- **Decision.** Ask password managers, identity providers and credential managers, in order of preference, for something that exists, a joint pilot, or an open specification.
- **Context.** Keys travel by hand today. The page records that the word-based share token was removed in August.
- **Rationale.** Not stated beyond the context.
- **Supersedes.** Nothing stated for this week.
- **Source.** sgit.ai v0.6.2, [version record](https://sgit.ai/admin/versions.html).

### D-107: Business plans get their own page
- **Date.** 24 September 2026 · sgit.ai
- **Decision.** A new page, `/startups/business-plans.html`, listed in the Why menu.
- **Context.** Connector Twin joins Agent as Webmaster as a published plan.
- **Rationale.** Not stated beyond the context.
- **Supersedes.** The startups section's list of plans as their only home.
- **Source.** sgit.ai v0.6.3, [version record](https://sgit.ai/admin/versions.html).

### D-108: Provider pages carry only what providers publish
- **Date.** 24 September 2026 · sgit.ai
- **Decision.** Every provider fact on the partnership pages is from the provider's own pages; credit amounts are left out because several could not be confirmed. A brief asks riskmandate.ai for the risk side of every partnership.
- **Context.** Sixteen new partnership pages.
- **Rationale.** Credit amounts are left out "because several could not be confirmed".
- **Supersedes.** Two first drafts that research corrected (AWS hosting; S3 mode in general).
- **Source.** sgit.ai v0.6.4, [version record](https://sgit.ai/admin/versions.html).

### D-109: The Risk Acceptance Office plan takes a position where the method disagrees with itself
- **Date.** 24 September 2026 · sgit.ai
- **Decision.** Research found four places where the published method disagrees with itself; the plan picks a position on each and says so.
- **Context.** A business plan for running the risk acceptance loop.
- **Rationale.** Not stated beyond the context.
- **Supersedes.** Not stated which way each disagreement was settled in the log entry.
- **Source.** sgit.ai v0.6.5, [version record](https://sgit.ai/admin/versions.html).

### D-110: Lesson Loop is paid by credits, not a subscription
- **Date.** 24 September 2026 · sgit.ai
- **Decision.** The plan sets out pay-on-demand credits instead of a subscription, and capture first, "nothing else until it works".
- **Context.** The thirty-fifth vault, a business plan for coaches.
- **Rationale.** Not stated beyond the plan.
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.6.6, [version record](https://sgit.ai/admin/versions.html).

### D-111: Company X-Ray reuses RiskMandate's four-level pricing pattern
- **Date.** 24 September 2026 · sgit.ai
- **Decision.** Company X-Ray's four levels, from £50 to £1,500, "reuse RiskMandate.ai's pricing pattern".
- **Context.** The fifth business plan of the week on sgit.ai.
- **Rationale.** Not stated beyond the reuse.
- **Supersedes.** Nothing stated.
- **Source.** sgit.ai v0.6.8, [version record](https://sgit.ai/admin/versions.html).

### D-112: How it works describes what is sold, with each step's status
- **Date.** 24 September 2026 · riskmandate.ai
- **Decision.** The page is rebuilt in the order of the lead's memo, and the diagram and claims naming things that do not exist are removed (riskmandate.ai's D12).
- **Context.** A peer asked how it technically works, and the page did not answer.
- **Rationale.** Such a page "is not an aspiration; it is the one page a technical reader would use to decide we are not serious."
- **Supersedes.** The pre-ABP architecture page, including the line on twins instead of integrations.
- **Source.** riskmandate.ai [v1.32.0](https://riskmandate.ai/versions/1.32.0.md).

### D-113: *Step*, not *rung*
- **Date.** 24 September 2026 · riskmandate.ai
- **Decision.** Every page says *step*; a test fails any page, twin or `llms.txt` that uses the old word. Records keep it.
- **Context.** The lead asked for the word to go when the deck was rebuilt.
- **Rationale.** It "is not a common word, and it reads oddly, most of all to somebody reading in a second language."
- **Supersedes.** *Rung*, on eleven pages.
- **Source.** riskmandate.ai [v1.32.1](https://riskmandate.ai/versions/1.32.1.md).

### D-114: UK support, written down in public, nothing applied for
- **Date.** 24 September 2026 · riskmandate.ai
- **Decision.** A register of 79 UK programmes, each read on its official page, with a status column that says *not started* for all but one (riskmandate.ai's D13). Applying to the Sovereign AI scheme is recorded as the lead's decision.
- **Context.** The lead's memo: the product is ready and the challenge is users.
- **Rationale.** Written for three readers: people the lead knows, other founders, and the site itself, recording what happened at each door.
- **Supersedes.** Nothing stated.
- **Source.** riskmandate.ai [v1.32.2](https://riskmandate.ai/versions/1.32.2.md).

### D-115: Two articles, each a hypothesis checked first
- **Date.** 24 September 2026 · riskmandate.ai
- **Decision.** Publish two articles from the lead's memos (riskmandate.ai's D14 and D15), with unmeasured claims reported as what they are.
- **Context.** Each memo was a hypothesis to check before it was written up.
- **Rationale.** Not stated beyond the context.
- **Supersedes.** Nothing stated.
- **Source.** riskmandate.ai [v1.32.3](https://riskmandate.ai/versions/1.32.3.md).

### D-116: Business cases computed from the Explorer's model, with named vendor cases held back
- **Date.** 24 September 2026 · riskmandate.ai
- **Decision.** A new section computes a product's business case as the difference between two risk registers, on the RiskGraph Explorer's existing model; named cases about other companies' products stay unlisted drafts until the lead decides to send them to the vendors (riskmandate.ai's D16).
- **Context.** The lead's memo asked whether earlier work already covered risks owned at several altitudes; the note says it does.
- **Rationale.** The section's rules require sending a case to its vendor "before anything about somebody else's product is listed".
- **Supersedes.** Nothing stated.
- **Superseded by.** D-117, for agentgateway.
- **Source.** riskmandate.ai [v1.33.0](https://riskmandate.ai/versions/1.33.0.md).

### D-117: OWASP and open source first
- **Date.** 24 September 2026 · riskmandate.ai
- **Decision.** Business cases start with open source, OWASP above all; eighteen open-source cases and an OWASP graph published; agentgateway moves from draft to published "under the lead's direction for open source" (riskmandate.ai's D17).
- **Context.** The lead's memo of the day.
- **Rationale.** Open source is what "anybody can deploy without a commercial conversation".
- **Supersedes.** agentgateway's draft, unlisted status from v1.33.0 (D-116).
- **Source.** riskmandate.ai [v1.34.0](https://riskmandate.ai/versions/1.34.0.md).

### D-118: A behaviour-policy vault for each person the lead talks to
- **Date.** 24 September 2026 · riskmandate.ai
- **Decision.** Three kinds of vault (the existing app vault, a private keys vault, one vault per person holding only what that organisation publishes about itself); the pack is kept in the repository, not on the site, behind a leak gate (riskmandate.ai's D18).
- **Context.** The objective this quarter is users.
- **Rationale.** A policy about the person, sent the day after, "is an invitation to the product's first action"; holding only public material makes publishing one later "a decision rather than a clean-up".
- **Supersedes.** Nothing stated. No keys vault and no real person's vault exists yet, as the note says.
- **Source.** riskmandate.ai [v1.34.1](https://riskmandate.ai/versions/1.34.1.md).

### D-119: An interview page, built from another site's brief, unlisted and sent by link
- **Date.** 24 September 2026 · riskmandate.ai
- **Decision.** Build the first interview page from sgit.ai's build brief (riskmandate.ai's D19), unlisted, with a template so the next page is one JSON file; correct two points of the prompt to what the site states.
- **Context.** Expert feedback from people whose time is scarce. The voice run is left to the lead.
- **Rationale.** "Asking them to read a site and write feedback rarely works; asking them to talk for twenty minutes usually does."
- **Supersedes.** Nothing stated. Its lineage runs back to the voice interview prompt of D-042.
- **Superseded by.** D-121, for the interview's length.
- **Source.** riskmandate.ai [v1.34.2](https://riskmandate.ai/versions/1.34.2.md); the brief is sgit.ai v0.6.7 in [the version record](https://sgit.ai/admin/versions.html).

### D-120: Local checks run what CI runs, and `dist/` folders are tracked
- **Date.** 24 September 2026 · riskmandate.ai
- **Decision.** `npm run check` runs the licence-chrome check; the pack's `dist/` folders are committed; CI commands are run on a clean export before a push.
- **Context.** Releases v1.32.2 to v1.34.2 never reached the live site because CI failed on each.
- **Rationale.** The local check "passed here and failed there"; the clean export is "where the difference hid."
- **Supersedes.** A local check that did not run the licence-chrome check (after D-088), and a repository that ignored every `dist/` folder.
- **Source.** riskmandate.ai [v1.34.3](https://riskmandate.ai/versions/1.34.3.md).

### D-121: The interview grows to thirty minutes and asks about the ABP itself
- **Date.** 24 September 2026 · riskmandate.ai
- **Decision.** The founder interview gains a first part of six questions on the Agent Behaviour Policy and becomes thirty minutes with a sixteen-section summary (riskmandate.ai's D20).
- **Context.** Two asks from the lead in one note.
- **Rationale.** Not stated beyond the lead's asks.
- **Supersedes.** The twenty-minute interview with a ten-section summary shipped in v1.34.2 that day (D-119).
- **Source.** riskmandate.ai [v1.34.4](https://riskmandate.ai/versions/1.34.4.md).

### D-122: No number on a risk's impact
- **Date.** 24 September 2026 · riskmandate.ai
- **Decision.** Risks carry a consequence in words and an undo property, and no quantity of loss; "a loss figure is the lead's decision" (riskmandate.ai's D22).
- **Context.** Risks now flow upwards to the board in the article's figure.
- **Rationale.** "The article's own rule is that kinds of consequence do the work a score usually does".
- **Supersedes.** Nothing stated.
- **Source.** riskmandate.ai [v1.34.6](https://riskmandate.ai/versions/1.34.6.md).

### D-123: The version chip is shown on every screen
- **Date.** 24 September 2026 · riskmandate.ai
- **Decision.** The laptop rule hides only the GitHub link; the drawer carries the version on narrow screens.
- **Context.** The lead had no good way to confirm a new version was live.
- **Rationale.** The footer already carries the GitHub link.
- **Supersedes.** The chip hidden below 1400px and below 1040px.
- **Source.** riskmandate.ai [v1.34.7](https://riskmandate.ai/versions/1.34.7.md).

### D-124: Every control is taken as working, for now
- **Date.** 24 September 2026 · riskmandate.ai
- **Decision.** The blast-radius figure gives every control a residual risk of its own and takes every control as working, "as the lead said to for now" (riskmandate.ai's D23).
- **Context.** The lead played the figure and asked for two details and a scenario.
- **Rationale.** "A control does not make a risk zero; it leaves a green one."
- **Supersedes.** A control previously removed a risk from the figure; it now leaves an accepted one.
- **Source.** riskmandate.ai [v1.34.8](https://riskmandate.ai/versions/1.34.8.md).

## Contradictions

Places where two sites, or two pages, or two entries, disagree in the snapshot of 24 September 2026, or where a decision contradicts an earlier one without saying it supersedes it. Recorded, not resolved. Accidental ones are carried as [loose ends](nr:loose-ends).

### The price of the first level: £10 and £5

Both figures are live in the snapshot.

- **£10:** riskmandate.ai's [pricing page](https://riskmandate.ai/pricing.md) ("four levels, £10 to £1,500") and [home page](https://riskmandate.ai/index.md) ("From £10 for one agent"); store.sgit.ai's `/v1/` page and its offer `t1` at £10 ([store llms.txt](https://store.sgit.ai/llms.txt)).
- **£5:** store.sgit.ai's `/v1/policies/` page description ("the pack downloaded at £5"), and its `/paying/` page ("The four levels are £5, £50, £500 and £1,500") ([store llms-full.txt](https://store.sgit.ai/llms-full.txt)).
- The store records the history itself: the floor was £10 on 10 September, £5 on 15 September, and back to £10 on 16 September ([store llms-full.txt](https://store.sgit.ai/llms-full.txt)).
- sgit.ai's brief of 24 September already names this: "Level 1 is £10 on riskmandate.ai's pricing page and £5 on store.sgit.ai's policies and on the licence page." ([brief](https://sgit.ai/docs/briefs/riskmandate-partnership-risk-and-sgit-mapping.html)). This desk found the £5 on the store's policies page; it could not find a £5 price on a licence page in the snapshot.

### A payment link that exists and does not

store.sgit.ai's llms.txt lists a checkout address for offer `t1` on a payment provider's host, and the same file ends: "No payment link has been created for any offer on this site: every checkout_url in data/offers.yml is empty" ([store llms.txt](https://store.sgit.ai/llms.txt)). riskmandate.ai's v1.20.0 note, of 15 September, recorded that every level on the store said "the payment link has not been issued yet" ([v1.20.0](https://riskmandate.ai/versions/1.20.0.md)). The file does not say which of its two statements is current.

### Fifteen or sixteen examples

riskmandate.ai's [home page](https://riskmandate.ai/index.md) says "All sixteen published examples are free to read" and "Sixteen published shapes to start from", and [v1.27.0](https://riskmandate.ai/versions/1.27.0.md) says "All sixteen shapes migrated". Its [pricing page](https://riskmandate.ai/pricing.md) says "Fifteen applications are in the library" and "Fifteen example policies". store.sgit.ai says "Fifteen applications" and "Fifteen Agent Behaviour Policies" ([store llms.txt](https://store.sgit.ai/llms.txt)). The sources do not say whether the difference is one shape not yet on the store, or a count that drifted.

### Classification by shape, then never by shape

sgit.ai's credential check of 17 August classified "by PREFIX for vaults new enough to emit one ... and by SHAPE for everything older" (D-022). On 20 September the credentials page set the rule that classification is "by declaration and never by shape" (D-084). The v0.2.98 entry does not say whether the shape path in the checker was removed or kept for keys with no prefix ([version record](https://sgit.ai/admin/versions.html)).

### Two days, or the same day

sgit.ai's v0.2.56 and v0.2.58 each say the games vault was built "Two days after v0.2.55" published the telemetry brief. The version log dates v0.2.55 and v0.2.56 both 6 September, and v0.2.58 7 September ([version log](src:history/sgit.ai-version-log.json)).

### A brief marked open that the other site has delivered

sgit.ai's [briefs index](https://sgit.ai/docs/briefs/index.html) lists the interview-page brief with the status "open". riskmandate.ai built the page the same day ([v1.34.2](https://riskmandate.ai/versions/1.34.2.md)) and it reached the live site with [v1.34.3](https://riskmandate.ai/versions/1.34.3.md). The [brief](https://sgit.ai/docs/briefs/riskmandate-interview-page-and-voice-prompt.html) also describes an interview of "about twenty minutes"; after [v1.34.4](https://riskmandate.ai/versions/1.34.4.md) the built page is thirty minutes with a sixteen-section summary.

### "Four releases" that are six

riskmandate.ai's [v1.34.3](https://riskmandate.ai/versions/1.34.3.md) is titled "Four releases, delivered" and says "v1.32.2 to v1.34.2 were merged but never reached the live site". The [version record](https://riskmandate.ai/versions.md) lists six releases in that range: v1.32.2, v1.32.3, v1.33.0, v1.34.0, v1.34.1 and v1.34.2.

### How many legacy read keys

sgit.ai v0.2.98 says "99 published keys across 27 pages still carry the legacy rk1 prefix". v0.3.0, the next day's pass, says it moved "102 published read keys" under that prefix and "24 bare ones" ([version record](https://sgit.ai/admin/versions.html)). The log does not reconcile 99 and 102.

### Two risk acceptance interval ladders

risks.sgit.ai's ladder runs 1 hour, 4 hours, 1 to 2 days, 1 to 2 weeks and 1 month, the default rung, with 6 months on its button list ([risks.sgit.ai](https://risks.sgit.ai/llms-full.txt)); sgit.ai's v0.6.5 cites it as "the risks.sgit.ai ladder, 1 hour to 6 months". riskmandate.ai's [Acceptable page](https://riskmandate.ai/acceptable.md) frames the clock differently: "Anything under a week is an incident", and by distance to the line, "roughly a month far above, three months mid, six months at or near the line". Neither page, as read, says whether the two are meant to agree.

### A GDPR graph that one site lists and another says does not exist

sgit.ai's [published vaults](https://sgit.ai/demos/vaults/index.html) list "Standards Atlas, GDPR"; standards.sgit.ai says "There is no GDPR graph" ([standards.sgit.ai](https://standards.sgit.ai/llms-full.txt)). sgit.ai's own brief flags the same disagreement ([brief](https://sgit.ai/docs/briefs/riskmandate-partnership-risk-and-sgit-mapping.html)).

### A documented cache header that was not live

sgit.ai's caching contract page says immutable objects are served with a long-lived `Cache-Control` header. On 21 September the read endpoint returned no `Cache-Control` header for an immutable object, as recorded in v0.3.3 ([version record](https://sgit.ai/admin/versions.html)). The log says the page now states the gap; this desk did not check whether the contract page has since changed.

### A page on graphs.sgit.ai that contradicts itself, according to sgit.ai

sgit.ai's v0.2.94 brief says graphs.sgit.ai's boundaries page states "identical rules, no new format, no special case" in its table while a quotation two paragraphs below says an article may need "its own ontology and taxonomy" ([version record](https://sgit.ai/admin/versions.html)). This desk has recorded sgit.ai's reading and has not checked the graphs.sgit.ai page itself. graphs.sgit.ai's llms.txt at v0.6.22, dated 20 September, states that "the grammar survives every zoom and the ontology does not have to" ([graphs.sgit.ai](https://graphs.sgit.ai/llms.txt)).

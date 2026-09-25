## What each site owes

The short version — [the long version is the contract](/contract/):

- **Nine sections, in order**, with cost and failures given the visual weight.
- **No claim without a state**, and the states joined to the pages at build time.
- **Credential rules per product**, never per vendor.
- **Disclosure visible without scrolling**, on every page, not only on its own page.
- **A markdown twin at every path**, so an agent never has to parse HTML.
- **Cross-links that point at pages**, never at domains — a domain link is a referral rather than a composition.

==============================================================================
PAGE /versions/  —  Release history
==============================================================================

---
title: Release history
description: "Every release of this site, with what changed. The version is owned by admin/build/version.txt, must appear in the release commit's subject, and CI verifies the two agree before it tags anything."
lead: "Every release of this hub, with what changed and when. The estate's convention: **one file owns the version**, the release commit's subject repeats it, and the pipeline refuses to tag anything if the two disagree."
order: 95
---

<div class="tablewrap"><table class="vers"><thead><tr><th>Version</th><th>Date</th><th>What changed</th></tr></thead><tbody>
<!-- releases -->
    <tr><td class="vnum">v0.1.1</td><td>2026-09-08</td><td>Both canonical domains came up hours after v0.1.0 shipped, so where a provider site serves is now measured rather than assumed: bin/sync-providers.py probes each canonical host by fetching that site's own published index from it, records the answer as live: and canonical_resolves: in data/providers.yml, and every family link the build emits — cards, comparison rows, prose — resolves through that value via a new `live:` shortcode, so no provider URL is typed anywhere. check_family_links_live now fails in both directions: a canonical link while a domain is dead, and a stale project-path link after it comes up. The claim that both domains were unconfigured is replaced by a dated claim that both now serve, sourced from the probe rather than from a report.</td></tr>
    <tr><td class="vnum">v0.1.0</td><td>2026-09-08</td><td>First release. The hub of the *.providers.sgit.ai family: the four credential patterns as canonical shared content with the capability-tier axis and their intersection; a comparison matrix synced from each provider site's own published front-matter rather than kept here; the family index; the page contract every provider site obeys, including the per-product rule that has already caught somebody; the six claim states with a roll-up of the family's actual mix; estate-wide disclosures; and the estate pipeline — validate → tag → deploy, a secret scan, relative URLs and a licence stamp, all enforced rather than promised.</td></tr>
</tbody></table></div>

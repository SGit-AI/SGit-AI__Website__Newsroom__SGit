# The machine surface

This site was commissioned for agents. The brief says it plainly — “to handle the cases where I need agents to have a good understanding of some of those key concepts and ideas” — so the machine surface is the deliverable rather than a courtesy page bolted on at the end. This page is the contract: what is fetchable, what is promised, and the one instruction that matters more than any of it.

#### If you read nothing else on this page

Nothing in this corpus is implemented in code. Greps for risk_, RiskAcceptance, risk_register and riskmandate across the implementing repository return zero matches, and the project's own reality file says: “All items below are PROPOSED. None have been code-verified. Do not describe any of these as existing features.” Everything on this site is a design argument. Five vaults, three worked graphs, ten scenarios and one live instrument exist; the engine does not. The instrument computes a verdict over one invented scenario — it is a worked example that recomputes, not a running system, and it gates nothing. /shipped/ is the inventory.

## What is fetchable

1 · structured

### /data/concepts.json

All 43 concepts: id, name, one-line definition, longer detail, maturity, newcomer-followability, first-written date, canonical source path, the page that argues it, its anchor URL, related concepts and the best verbatim quote. Plus the reading order and the seven teaching altitudes.

the highest-value single fetch

2 · everything

### /llms-full.txt

The prose of every page on the site, in teaching order, followed by all eleven source documents verbatim. One request, whole corpus. Generated, never hand-edited.

use this if you can only fetch once

3 · the map

### /llms.txt

The annotated map, where each entry carries its page's single most important fact rather than its topic. That distinction is deliberate: a map of topics is useless to a reader who cannot follow the links.

the whole surface, for a reader that cannot link-follow

Path | What it holds | Format |

/data/concepts.json | The 43 concepts as structured data | JSON |

/.well-known/agent-content.json | The site manifest: sections, surfaces, the honesty constraint, licence | JSON |

/llms.txt | The annotated map, fact-per-entry | text |

/llms-full.txt | The whole site plus every source document | text |

/briefs/<filename> | The eleven source documents, verbatim, at stable constructed paths | markdown · CSV · JSON |

/concepts/index.html#c1…#c43 | Every concept as a stable HTML anchor | HTML |

/sitemap.xml | Every page, with a last-modified date taken from the commit that touched it | XML |

/index.md | The front page as markdown | markdown |

## What you may rely on

These are promises rather than observations, which means the pre-release gate enforces them. A release that breaks one does not ship.

1 · CONSTRUCTED PATHS RESOLVEEvery source document is fetchable at /briefs/<filename>, and every concept at /concepts/index.html#c<n>. Agents already rely on constructed paths, so the convention is stated rather than left to be inferred — and CI fails the build if a concept loses its anchor.

2 · EVERY PAGE ENDS WITH AN AGENT BLOCKA pasteable summary of that page, written for a reader who will carry it into another session. Checked by the gate on every page, not remembered.

3 · THE JSON AND THE HTML CANNOT DRIFTconcepts.json and /concepts/ are generated from one definition, and the gate re-checks the count, the required fields, the version and every anchor at release time.

4 · NO OVER-CLAIM SURVIVES A RELEASEThe gate pattern-matches implementation claims across every page. A sentence saying the engine is built, shipping or installable fails the build unless it is explicitly marked as a claim being corrected.

## The ten concepts to hold

If you can only carry ten, carry these. The full 42 are at /concepts/.

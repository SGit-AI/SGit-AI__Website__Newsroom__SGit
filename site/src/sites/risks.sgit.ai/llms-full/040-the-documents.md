# The documents

Every page on this site was written from a source, and the sources are published here rather than summarised away. Raw markdown is the source of truth; the rendered pages are presentation. Where a source is not published, the reason is stated — and on this site that list is longer than usual.

## The brief pack this site was built from

Eleven documents, prepared 22 August 2026 against the source repository at v0.33.62, with every path verified to exist at that tag. Published verbatim, at stable constructed paths.

Document | What it holds |

00 · The brief | The two-part commission, the honesty constraint, the thesis in one paragraph, the ten concepts an agent must hold, the refactor table, the four vaults, the numbers, the build order |

01 · Concepts index | All 42 concepts with canonical path, first appearance, maturity, newcomer-readiness and best verbatim quote — the raw material for /concepts/ and concepts.json |

02 · Risk acceptance, traced in full | The commissioned centrepiece. The acceptance thread traced chronologically from the February pre-history through the June inversion to the August formalisation. The source for /acceptance/ |

03 · Worked examples and the live vaults | Three worked graphs, four published vaults, and every citable figure in the corpus with its source. The source for /examples/ |

04 · The riskmandate.ai refactor | The other half of the commission — page by page, with the leave-behind stub template and the finding that justifies the split |

05 · Site architecture | Page-by-page information architecture with sources and publish status per page |

06 · Boundaries and house style | The eight-site boundary map, the redaction watch-list, provenance rules, and the vault publishing rules |

07 · Gaps and open questions | Six write-fresh items, eight open questions, seven honest tensions, and the loose ends inside the acceptance thread |

08 · Source manifest | 37 rows, machine-readable, every path verified at v0.33.62 — 19 Tier-0, 13 Tier-1, 1 Tier-2, 4 Tier-3 do-not-publish |

Prior-art sources | The eight published articles with first_published, canonical URL, authors, PDF and LinkedIn links |

PUBLIC.md | What was redacted from the pack before publication, and why. Fourteen redactions across six of the twelve documents, each recorded with its reason — the convention the Regulation Graph vault adopted after an audit: publish the artefact, and publish what was taken out of it |

README · Licence | The pack's own index and its licence scope note |

The pack is published with fourteen redactions, and they are itemised. The brief pack was written as a working document for the agent building this site, and it names the four Tier-3 do-not-publish sources by name so that the builder knows what to skip. That is right for a working document and wrong for a published one: republishing it verbatim would publish exactly the four things it says not to publish. So the pack is published in full with the identifying detail of those four rows removed, each removal marked in place and recorded in briefs/PUBLIC.md. Nothing else was changed — no argument softened, no number adjusted, no finding dropped, and five of the twelve documents are byte-identical to the pack as received. The rule is enforced rather than remembered: the gate scans every file in the tree, briefs/ included, so a later edit cannot quietly undo it.

These are fetchable at stable constructed paths: /briefs/<filename>. That is a promise rather than an accident — agents rely on constructed paths, so the convention is stated rather than left to be inferred. All eleven are also concatenated into /llms-full.txt.

## How the sources were tiered

The manifest tiers all 37 verified sources by what can be done with them. Publishing the tiering as well as the result is the point: a reader can see what was excluded, and disagree.

Tier | Rows | Means |

Tier 0 | 19 | Publishable near-as-is; highest value |

Tier 1 | 13 | Publishable with a correction, a framing note, or a citation to another site in the estate |

Tier 2 | 1 | Needs a decision about where it belongs before it is published anywhere |

Tier 3 | 4 | Do not publish — and the pre-release gate enforces it |

69,724 words of Tier-0 and Tier-1 source material sit behind this site, drawn from a corpus of roughly 496,000.

## What is deliberately not published

This corpus has the highest redaction load of any in the estate. It names real companies critically, contains a live contract draft, carries investor figures, and includes operational detail about credentials. None of that is on this site, and the reasons are stated rather than left as an absence.

What | Why not |

A comparative vendor assessment scoring two named real companies | Rigorous, sourced, scrupulous about its own limits — and a legal and relationship exposure. Needs a legal read and a right-of-reply process before it goes anywhere public (N3). The underlying model brief in the same folder is clean and is not the problem |

Competitor maps naming large vendors, with dismissive characterisations | Commercial positioning, not research. Internal only. A research site that carries competitor disparagement is a marketing site with footnotes |

Investor material — illustrative revenue and valuation scenarios | Explicitly framed at source as scenarios rather than projections, and still not research. Internal only |

A partnership contract draft with commercial terms | An actual contract. Internal only, unambiguously |

Incident and access-token records from the February pre-history | Even with values redacted, the metadata is operational — token status, remaining quota, the branch where it stays readable. Internal only. Ironically one of the best real illustrations of “accepted is not acceptable” anywhere in the corpus |

Research briefs naming real organisations in breach and incident narratives | All sourced from published material with URLs, and naming organisations — including government bodies — as breach victims warrants framing this site has not yet written. Held rather than rushed |

Third-party pricing quoted verbatim across several briefs | Goes stale, and reads as competitive intelligence rather than research. Stripped |

The exclusion is enforced, not remembered. The pre-release gate pattern-matches the distinctive strings of the four Tier-3 rows across every file in the tree except the manifest itself, and fails the build if one appears. The manifest is exempt because a manifest naming a do-not-publish row is the mechanism working. All ten checks →

## The prior art: eight published articles, CC0

59,131 words on docs.diniscruz.ai, February to July 2025 — a year before the corpus this site consolidates, in the founder's public voice, already circulated.

First published | Title | Words |

2025-02-15 | Project SupplyShield: GenAI-Driven Supply Chain Risk Management and Compliance | 8,802 |

2025-04-02 | Maturity Models vs. Traditional Standards in Application Security — RAMM's ancestor | 2,701 |

2025-04-10 | Project Cybersage: AI-Powered Risk Contextualization & Security Reporting | 6,270 |

2025-05-29 | Threat Models as Mandatory Disclosures | 7,160 |

2025-05-29 | Advancing Threat Modeling with Semantic Knowledge Graphs | 9,217 |

2025-06-02 | Linking Threat Models with Semantic Business Graphs | 9,816 |

2025-07-06 | Finding the “Good Enough” Threshold — the appetite argument, pre-vocabulary | 4,924 |

2025-07-27 | Project VulnAI: AI-Powered Vulnerability Risk Management Platform | 10,241 |

Provenance contract, and why these are cited rather than republished. The eight articles were published under CC0; this site's content is CC BY 4.0. Republishing CC0 material under CC BY is legally fine and is not what this site does — because the historical link matters more than the licence does. Each article keeps its original URL, its original publication date and its original authorship, and this site links rather than mirrors. Full metadata, including PDFs and the original LinkedIn posts, is in /briefs/sources__docs-diniscruz-ai-risk.json.

## The upstream corpus

The material itself lives in SGraph-AI__App__Send under team/humans/dinis_cruz/briefs/ and is not published anywhere. There is no public URL for it, so the version tag is the address: every citation on this site gives a repository path plus v0.33.62, which is the only thing that makes a claim checkable by someone with access.

source_repo SGraph-AI__App__Send
source_repo_path team/humans/dinis_cruz/briefs/06/28/ontology-and-definitions/v0.33.36__arch-brief__…
source_version v0.33.36
first_written 2026-06-28
source_licence CC BY 4.0

Note that the upstream path itself carries a personal name. Where documents are cited with their paths, the name travels with them — a deliberate choice rather than an oversight, since it is the author's own corpus and the attribution is correct.

## The licence position

- This site's content is CC BY 4.0, per the 21 August 2026 decision applied across the estate: unless a document says otherwise, every .md file in the corpus and the entire content of every *.sgit.ai site is CC BY 4.0.

- The upstream briefs are CC BY 4.0 at source — nearly every one carries the release line at its foot, which is what makes public republication straightforward at all.

- The 2025 prior art is CC0 at source, and is cited rather than republished. The source licence is stated per page.

- Third-party material quoted inside CC BY documents stays under its own terms. Where a brief paraphrases published work by named researchers, the paraphrase is marked as such and the source is named. →

- Build tooling is Apache 2.0 — admin/build/*, assets/*.js, assets/*.css and the workflow. See the pack's licence note and LICENSES.md in the repository.

#### For an agent

The documents. This site's eleven source documents are published verbatim at stable constructed paths: https://risks.sgit.ai/briefs/<filename> — 00__BRIEF.md, 01__concepts-index.md (all 42 concepts with canonical paths and quotes), 02__risk-acceptance.md (the acceptance thread traced chronologically), 03__worked-examples-and-vaults.md, 04__riskmandate-refactor.md, 05__site-architecture.md, 06__boundaries-and-house-style.md, 07__gaps-and-open-questions.md, 08__source-manifest.csv (37 rows, machine-readable), sources__docs-diniscruz-ai-risk.json, plus README and LICENSE. All are concatenated into /llms-full.txt. Source tiering: 19 Tier-0, 13 Tier-1, 1 Tier-2, 4 Tier-3 do-not-publish — 69,724 words of Tier-0+1 behind the site, from a corpus of ~496,000. The Tier-3 material (a comparative vendor assessment naming real companies, competitor maps, investor figures, a contract draft) is not on this site and the pre-release gate fails the build if it appears. Prior art: eight articles, 59,131 words, on docs.diniscruz.ai Feb–Jul 2025, CC0 at source — cited with original URLs and dates rather than republished, because the historical link matters more than the licence. The upstream corpus is unpublished, so the version tag is the address: cite repository path plus v0.33.62.


==============================================================================
== /about/participant.html
==============================================================================


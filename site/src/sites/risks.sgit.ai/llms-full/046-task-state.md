# | Task | State |

T1 | Stand up the pipeline before the content: validate → tag → deploy, with the gate carrying this site's three specific tripwires | done · v0.1.0 |

T2 | Build /acceptance/, /acceptable/, /ladder/ and /plug/ — the four near-publishable sections the brief sequences first | done · v0.1.0 |

T3 | Ship the definitions endpoint: the concepts as structured data (42 at v0.1.0, 43 now), generated from the same definition as the human page, with the gate enforcing that they cannot drift | done · v0.1.0 |

T4 | Publish /shipped/ with the honesty constraint stated first rather than last, and enforce it in CI rather than remembering it | done · v0.1.0 |

T5 | Mirror the 2FA instance graph as a downloadable file at a stable path. It is the only directly downloadable graph in the corpus, it declares its own principles inline and carries a CC BY 4.0 line — and this site currently describes it from the brief pack's counts rather than reproducing a file it does not have | open |

T6 | Publish the ontology as machine-readable data, not just as a vocabulary listing. Node types and edge types with their path formulas, so an agent can consume the schema rather than parse a code block. Currently a listing | open |

T7 | Run this site's own risk register in the open. The corpus argues a register is a graph, that unaccepted equals critical, and that the register maintains itself. A research site that publishes its own register — its open questions as unaccepted risks, with intervals — demonstrates all three at zero cost. The house style names this as one of two demonstrations worth building in | open |

T8 | Write the leave-behind stubs for the four pages that moved off the commercial site, so each has a short summary and a link here rather than a drifting second copy | in progress · this site's half is done |

T9 | Add a rendered in-page reader for each source document under /documents/, rather than linking to raw markdown only | open |

T10 | Render the three worked graphs as diagrams. Every one is currently prose plus a counted table; two of them exist as parseable JSON upstream and would render directly. The execution boundary shows what it would look like — a 20-node graph with the visual grammar carried from graphs.sgit.ai — which makes the remaining three a matter of data rather than of method | open |

T11 | Build the execution boundary as a live instrument in a vault, embedded rather than copied, with the read key published in the open and the write credential nowhere on this site | done · v0.2.0 |

T12 | Make the origin of every concept explicit. This site now contains one concept it authored, so concepts.json carries an origin field, the index carries a provenance pill, and the gate fails an entry without one. A site that consolidates a corpus and quietly adds to it stops being a report of the corpus | done · v0.2.0 |

T13 | Give the instrument a second scenario that is not ours. Everything it computes today rests on one invented migration; four predicates is not a register, and whether the verdict stays legible at forty predicates or ten thousand queued actions is Q4 in a different costume. Taking a scenario from someone else's estate would test the model rather than the authors' imagination | open |

T14 | Publish the vault-app authoring contract this site now depends on. The instrument's eight pages each inline their own CSS and JS because a vault app runs from a blob: URL and declarative references to vault paths are fetched before the bridge installs. That is written down in a build script rather than on a page, which is exactly the shape of thing this site tells other people not to do | open |

T15 | Ship a favicon. The site has none, so every page view on every one of the 37 pages produces a 404 for /favicon.ico — harmless, visible in any devtools console, and exactly the kind of small untidiness a site that publishes its own gate ought not to be carrying | open |

## Decided against

What | Why not |

Publishing vault read keys on this site — reversed at v0.2.0 | The original reason still holds for vaults this site does not own: the four borrowed vaults' keys are published and kept current in sgit.ai's catalogue, and a second copy here would go stale. It does not hold for a vault this site authored — the Execution Boundary's read key is printed in the open, because a page that argues read access is a capability you can hand out and then declines to hand it out is arguing against itself. The rule that stayed absolute is the one that matters: read keys yes, vault keys never. The gate now recognises a read key by shape and by prefix and still refuses everything else — and it caught a vault key on this very release |

Inventing the four missing RAMM predicates | Four plausible-sounding definitions presented as the model would be precisely the failure this site exists to avoid. N2 instead |

Reconstructing the 2FA data file from the brief pack's counts | A reconstructed graph presented as the original is worse than a missing one. T5 instead |

Any pricing, partner positioning or competitor comparison | Not this site's job, and corrosive on a research property. It stays on riskmandate.ai |


==============================================================================
== /admin/versions.html
==============================================================================


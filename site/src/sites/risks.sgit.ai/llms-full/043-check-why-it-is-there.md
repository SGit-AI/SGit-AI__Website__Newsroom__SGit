# | Check | Why it is there |

1 | Version agreement — version.txt against every page's badge, the versions table, llms.txt and index.md; and each release listed exactly once | A blanket version bump that touches the history table produces duplicate rows, which shipped once on a sibling site |

2 | Internal links and fragments — every relative href/src resolves to a file, and every #fragment resolves to an id in the target page | Site-specific. This site's promise to an agent is that all 43 concepts have stable anchors. A promise that is checked is a fact; a promise that is remembered is a hope |

3 | Canonical host — every page declares a canonical, and every canonical and og:url is on the host in CNAME | A site assembled from a sibling's pattern can ship a canonical pointing at the sibling |

4 | The agent surface — every section hub is named in llms.txt, and the sitemap and the tree agree in both directions | Agents are the commissioned audience here. For that reader, a page missing from llms.txt is a page that does not exist |

5 | The definitions endpoint — data/concepts.json parses, carries all 42 concepts with every required field, agrees with version.txt, and every concept has a matching anchor on /concepts/ | The brief calls it the single highest-value thing this site can ship. The JSON and the human page are generated from one definition, and the gate makes drift impossible rather than unlikely |

6 | The over-claim tripwire — no page may say the engine is built, shipping or installable | Nothing in this corpus is implemented. A page may state such a claim only by marking the element data-not-built, which is how /shipped/ quotes the reality file. Over-claiming here would poison the whole network's credibility |

7 | The do-not-publish tripwire — the distinctive strings of the four Tier-3 manifest rows may not appear anywhere in the tree | They are in the manifest so the builder knows to skip them, and in the gate so a later edit cannot quietly reintroduce one. The manifest itself is exempt: naming a do-not-publish row is the mechanism working |

8 | Key-leak tripwire — nothing may look like a vault key (a ≥20-character passphrase joined by a colon to a UUID) | Read keys yes, write keys never — and the safest way to keep that rule is to ship neither. Inherited from the sibling sites, and cheap |

9 | Block balance — every page opens and closes the same number of <div>s | A note box closed with </p> is accepted silently by browsers and runs the note's border down the rest of the page |

10 | Every page carries a “for an agent” block | Each page serves three readers, and the third is an agent carrying the definition into another session. On this site that reader is the commission |

## The chrome

Every page is hand-written static HTML, and that stays true — a human should be able to open any file and edit it. What is not hand-maintained is the chrome: the nav row (including the version badge the gate requires to agree everywhere) and the footer columns. Those are defined once in admin/build/chrome.py and rewritten in place across the tree, which is what stops a thirty-page site from drifting.

python3 admin/build/chrome.py # rewrites nav + footer everywhere, stamps the version
python3 admin/build/gen_sitemap.py # sitemap.xml from the tree, lastmod from git
python3 admin/build/gen_llms_full.py # the whole site + every source document, one file
node admin/build/validate.js # the gate

Adding a page: add it to NAV or FOOTER if it belongs there, write the file with an empty <nav class="site"></nav> and <footer class="site"></footer>, then run chrome.py. The here state is derived from the page's own path.

## Making a release

1. bump admin/build/version.txt (vX.Y.Z, exactly once)
add a row to admin/versions.html
update admin/comms.html

2. python3 admin/build/chrome.py
python3 admin/build/gen_sitemap.py
python3 admin/build/gen_llms_full.py

3. node admin/build/validate.js

4. git commit -am "site vX.Y.Z: ..." && git push origin dev

## The repository

.github/workflows/deploy-pages.yml validate → tag → deploy
admin/build/validate.js the gate — ten checks
admin/build/chrome.py the single definition of nav and footer
admin/build/gen_sitemap.py sitemap.xml from the tree
admin/build/gen_llms_full.py llms-full.txt — the whole site in one file
admin/build/version.txt the version, owned here
admin/comms.html asks and tasks, in public
admin/versions.html release history
data/concepts.json the definitions endpoint — 43 concepts
briefs/ the eleven source documents, verbatim
assets/site.css shared stylesheet (sgit.ai design language)
llms.txt · llms-full.txt the agent surface
CNAME · robots.txt · sitemap.xml hosting and discovery

## Hosting

GitHub Pages, deployed from dev — the release branch. A push to main is deploy-only, with tagging skipped, so main can serve as a deploy test or a fallback while the github-pages environment still restricts dev. The site is entirely static: no build step for the HTML, no server, no JavaScript required to read any page. assets/nav.js handles the phone menu and touch dropdowns and the nav works without it; assets/mdreader.js renders raw markdown in-page where a document reader is used, and falls back to a link to the raw file.


==============================================================================
== /admin/comms.html
==============================================================================


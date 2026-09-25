# Pages that models read

The rest of this site is about putting a model inside your page. This page is the other half of the same subject: making your page readable to a model that arrives from outside. For a site called `llms.sgit.ai` it is not a topic, it is an acceptance criterion.

## What this site publishes for a machine reader

| Surface | What it is | Guaranteed by |
|---|---|---|
| [/llms.txt](../llms.txt) | The map: what this site holds, stated in full rather than as a list of links | Written by hand, version-stamped by the build |
| [/llms-full.txt](../llms-full.txt) | **The whole site in one fetch**, every page plus the brief pack it was built from | Generated from the twins, so it cannot disagree with the site |
| A `.md` twin at every path | Any page, extension swapped: `/security/index.html` → `/security/index.md` | **The pre-release gate fails the build if one is missing or stale** |
| [/sitemap.xml](../sitemap.xml) | Every page **and every twin**, so a crawler that only reads the sitemap still finds the markdown | Generated from the tree |
| [/briefs/](../briefs/00__BRIEF.md) | The brief pack, verbatim, at stable constructed paths | Published as source, not as a rendering |

Links inside a twin point at twins. An agent that enters the markdown never has to step back out into HTML to follow a reference, which is the property that makes the twins a surface rather than a courtesy.

## The mechanism, and why this site's differs

Across the estate the markdown twin is served at request time by a **Lambda@Edge function**, because the origins are static files and a static file cannot render itself. It is a genuinely non-obvious piece of plumbing, and it is invisible if you only look at a repository.

This site has no such function in front of it. It is GitHub Pages, so the twins are **written into the tree at release** by `admin/build/gen_twins.py` and served as ordinary files. Same contract, different machinery, and the difference is worth stating because a reader copying the convention needs to know which half they are copying.

## Writing for a model, and saying so in the filename

The estate writes documentation explicitly for model readers and puts it in the path:

```
library/dependencies/osbot-utils/type_safe/v3.1.1__for_llms__type_safe__testing_guidance.md
 ^^^^^^^^^
```

When a model is a primary reader, write it a document rather than expecting it to parse yours.

That is a different discipline from making HTML machine-friendly. Structured data helps a parser; a document written for a model reader answers the questions that reader actually arrives with. The `for_llms` convention is the estate admitting out loud who the audience is.

## The finding this site is built against

 Agent-access report, 14 August 2026

**"The audience is disproportionately agents."** And: many agents can only fetch URLs that a search engine has already returned to them, so a site that is not indexed is a site they cannot reach even when they know its address.

*"It can read the map and cannot walk it."*

The report's subject was the whole estate, and the diagnosis generalises past this network: **excellent documentation that cannot be reached is not published**. It is the same shape as this site's other founding problem, in which the complete `sg.llm.*` contract existed only inside a 9,487-word agent authoring file that no human would open. Different reader, same failure: the quality was never the problem, the discovery layer was.

So the acceptance criteria for this site, taken from that finding rather than invented:

- **`/llms.txt` is self-sufficient**, not a list of links to fetch. An agent that reads only that file should be able to say accurately what this site holds and does not hold.
- **`/llms-full.txt` exists.** `pki.sgit.ai`, the site this one copies its pattern from, does not have one. One fetch returns everything.
- **The twin works at every path**, and the build fails if it does not.
- **The status is stated plainly enough to be quoted.** If an agent summarises this site, the parts that are not built should survive the summary: [the CSP gap](../security/index.md#gap), [the absent evals](../shipped/index.md#thin), [the thin website half](../websites/index.md).

## If you are copying this

1. Write `llms.txt` as a document, not an index. The link list is what a sitemap is for.
1. Ship the twin at the same path with the extension swapped, and rewrite links inside it to point at twins.
1. Concatenate everything into one file. The cost is a few hundred kilobytes; the benefit is that a single fetch cannot miss a page.
1. Put your limitations where a summariser will find them. A caveat in a footnote does not survive being summarised.
1. Enforce it in the build. A convention that depends on somebody remembering is one that lasts about four pages.

The component and page conventions themselves belong to [coding.sgit.ai](https://coding.sgit.ai), which owns how code and pages are written across the estate; this page owns only the LLM-reader half of it.

 [← Local and offline](../local/index.md) [What is shipped →](../shipped/index.md)


==============================================================================
/shipped/index.md
==============================================================================

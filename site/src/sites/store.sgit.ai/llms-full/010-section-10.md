## Debt, marked as debt

**The store holds product data today that belongs on the other side.** That is
allowed for now and it is written down rather than discovered later:
`data/abp-catalogue.json` is promoted from riskmandate.ai at build time with the
source URL, the retrieval time and a sha256 of the page it was read from.
{{claim:abp-catalogue-promoted}}

Promotion at build time is the honest version of the wrong arrangement: it cannot
silently drift, because the hash changes. It is still the wrong arrangement, and
the right one is reading it at runtime from the side that owns it.

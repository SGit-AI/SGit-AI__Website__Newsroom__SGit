## The pipeline that gates each one

Three jobs, in this order, the same order as every sibling site in this estate.

**1 · validate.** `admin/build/validate.sh` — the build is reproducible against the
committed output, the version agrees everywhere it appears, internal links
resolve, every canonical URL is on the host in `CNAME`, the credential tripwire is
clean, every inline script parses, and this site's own acceptance assertions hold.
**A failure stops the release: no tag, no publish.** It runs on pull requests too,
so branch work is gated before it ever reaches the release branch.

**2 · tag-release.** The version file is read, the release commit is found by its
subject line, and the two must agree. The tag must be the next minor — or a
deliberate major — after the previous latest. Historical tags missing from the
remote are backfilled, idempotently. Then the tag is pushed.

**3 · deploy.** The site is rebuilt from `content/` and published. It never runs
when validation failed, and never from a pull request.

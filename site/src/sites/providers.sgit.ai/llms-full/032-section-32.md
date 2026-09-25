## How a release is made here

The same three steps as every other site in this estate — `validate` → `tag-release` → `deploy`.

**One file owns the version:** `admin/build/version.txt`. The nav badge, the footer, `llms.txt` and the table above are all rendered from it, and the gate fails if any of them disagree.

```bash
bin/bump.py "what changed in this release"     # --major for vR.M+1.0
python3 build.py
admin/build/validate.sh
git commit -am "site v0.1.1: what changed in this release"
```

**The commit subject is load-bearing.** `tag-release` reads `version.txt`, finds the commit whose *subject* carries the same version, and tags it — HEAD on a direct push, HEAD's parent when a pull request lands as a merge.

# How this site is built

Hand-written static HTML, one generated chrome definition, and a pre-release gate that has to pass before anything is tagged or published. Same pipeline as sgit.ai, pki.sgit.ai, graphs.sgit.ai and issues-fs.sgit.ai: validate → tag → deploy.

## The pipeline

1

### validate

node admin/build/validate.js. Structure, internal links and anchors, version agreement, canonical/CNAME agreement, the agent surface, the definitions endpoint, block balance, and three tripwires specific to this site. A failure stops the release: no tag, no publish. It also runs on pull requests, so branch work is gated before it can reach the release branch.

2

### tag-release

Every push to dev is a release and ends tagged v{release}.{major}.{minor}. The version is owned by admin/build/version.txt — bumped exactly once per release — and must also appear in the release commit's subject as site vX.Y.Z: …. CI verifies the two agree, that the bump is the next minor (or a deliberate major), and then tags the release commit. That is HEAD on a direct push and HEAD's parent when a pull request lands as a merge commit, so the job anchors on the newest release commit reachable from HEAD rather than on HEAD itself. The first run backfills tags for any historical release from the commit subjects.

3

### deploy

Publishes the tagged commit to GitHub Pages. Runs on manual dispatch even without a tag, never when validation failed, and never from a pull request.

## What the gate checks

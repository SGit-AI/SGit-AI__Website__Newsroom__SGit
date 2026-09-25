## 5 · What is a build failure rather than a review comment

Learned by building the first site, and each one is enforced by a check rather than remembered:

| Check | Why it exists |
|---|---|
| The build is **reproducible** — the committed output matches the sources | Markdown is the source of truth; a stale build publishes prose nobody wrote |
| **Version agreement** across every page badge, the release history and both machine indexes | A blanket bump that misses a page ships two versions of one site |
| **Internal links resolve**, and every canonical URL is on the host in `CNAME` | The two ways a static site quietly breaks |
| **No root-absolute internal URL** | The first site shipped one and served unstyled under a project path for a day |
| **No bare `<https://…>` autolink** | It reaches the browser as an unknown tag and the URL vanishes from the page |
| **A key-shape scan** over the whole tree, including the built output | These repositories are public; the vaults they came from were not |
| **Every claim cited**, and every state dated | The contract, enforced instead of promised |
| **The disclosure line present** on every page, and no vendor described as a collaborator it is not | A disclosure found at the bottom does the opposite of its job |

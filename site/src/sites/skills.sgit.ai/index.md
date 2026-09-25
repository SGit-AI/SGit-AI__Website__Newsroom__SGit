# skills.sgit.ai — skills are software packages, and here is the proof

> "Skills are a software package, that is the best analogy… the same way we have npm
> and pip for managing dependencies, we need a way to manage skills like that." This
> site publishes both halves honestly: **eight skills shipped**, generated from their
> own frontmatter, and **25 briefs, 60,782 words** of theory that runs a long way ahead
> of them — including the theory failing, live, on the estate's own skills.

*Source: <https://skills.sgit.ai/index.html> · site v0.1.0 · markdown twin of the front page.*

---

## First: the honest split

The work exists in two very different states, and every page on this site says which
one it is in. **S** shipped and real · **D** designed, unbuilt · **E** an economic or
strategic position.

| Half | Size | What it is |
|---|---|---|
| **S** Shipped | 8 skills · 16,338 words of SKILL.md · 2 repos | Real code, running today, with five authoring conventions nobody had written down until this site did |
| **D / E** Thought | 25 briefs · 60,782 words | Almost all written in one four-day burst, 1–4 June 2026 — the most complete theory of agent skills in the estate, and almost none of it built |

Scored against its own checklist — version control, dependency management,
vulnerability management, code review, CI, distribution, documentation — the estate's
skills get **one green cell out of seven**. [The full scorecard](shipped/index.html).

## Second: the thesis

> "Skills are code and need to be version-controlled, and need to be treated like
> software. Skills are a software package, that is the best analogy. Skills are not
> just a bit of code; skills are like a dependency, and need to be managed just like a
> dependency. The same way we have npm and pip for managing dependencies, we need a way
> to manage skills like that."

Not a metaphor — a checklist: *"vulnerabilities management, documentation,
integration, wrappers, code reviews, deployment, CI pipelines, distribution reviews —
every analogy we have with code, we need with skills."* And the sharper claim that
makes it more than an analogy: **skills describe intent, in English, not just
capability** — which is why they are proposed as the successor to code packages, not a
variant of them.

| Page | What it covers |
|---|---|
| [The thesis](thesis/index.html) | The full checklist, the one-green-cell scorecard, and why versioning intent is harder than versioning capability |
| [The graph](graph/index.html) | "Today's skills are static photographs of what they should be." Typed primitives, and the forking ecosystem |
| [Identity and permissions](identity/index.html) | A skill must come with the permission set it needs to run — and the OAuth critique |
| [The skill economy](economy/index.html) | Base vaults, the branded/certified/customised cascade, and the scoring position |

## Third: the theory, failing on its own subject

The clearest argument for the thesis is not in the briefs. It is in the estate's own
two repositories, and it is measured on every build of this site.

`use-sg-playwright` exists in both skill repositories — **43 words apart** — and one
copy carries an auth claim the service code contradicts. No registry, no single
source, no version pin, so the copies drifted, and one of them is now wrong.
[The full exhibit](catalogue/divergence.html).

## Where to go next

- [The catalogue](catalogue/index.html) — every shipped skill, generated from frontmatter
- [The authoring guide](authoring/index.html) — five conventions, usable the same day
- [Open questions](shipped/questions.html) — six questions with no answer anywhere in the corpus
- [For agents](agents/index.html) — llms.txt, llms-full.txt, and the catalogue as JSON

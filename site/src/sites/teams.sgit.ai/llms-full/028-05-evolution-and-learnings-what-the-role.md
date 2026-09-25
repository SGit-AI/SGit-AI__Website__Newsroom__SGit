# 05 — Evolution and Learnings: what the roles learned, as diffs

**Version** v0.33.64 · 7 September 2026
**Method** `git log` over `team/roles/*/ROLE.md` in a full (non-shallow) clone — 4,335 commits available. Every date and quotation below is from the history, not reconstructed.

---

## Why this section exists

The founder asked for *"the evolution and historical learnings"*, and that material is not in the files — it is in the **diffs**. A `ROLE.md` shows what a role is today. The history shows what went wrong badly enough that someone wrote a rule into it. **That is the difference between a template gallery and a memory site**, and it is the reason this page should be built first among the content pages even though it is listed fifth.

**The general pattern**: role definitions do not change often. Of 17 Explorer roles, the busiest are QA and Librarian at **6 commits each**, then Dev and Conductor at 5, DevOps and Architect at 4 — the rest at 1–3. Roles are stable, and the rare edits are therefore high-signal. Each one is worth a dated page.

---

## The timeline

| Date | Event | What it teaches |
|---|---|---|
| **11 Feb 2026** | *"Add ROLE.md identity documents for all 10 agent roles"* | Genesis. Eleven files, despite the message saying ten |
| **12–13 Feb 2026** | advocate, grc, sherpa, then ambassador, dpo | The roster grew by need, not design |
| **13 Feb 2026** | *"Execute full team activation for incident handling series (5 phases)"* | The first exercise, touching every role |
| **10 Mar 2026** | *"Refactor all role review folders from 26-MM-DD to MM/DD format"* | Convention debt, paid |
| **16 Mar 2026** | designer added | The nineteenth role, five weeks late |
| **18 Mar 2026** | *"Librarian catalogues its own operating guidance (meta-recursion)"* | The role that indexes everything indexes itself |
| **30 Mar 2026** | *"remove dangling comms/03/ folder, add comms awareness to roles"* | **Learning 1** — below |
| **8 Apr 2026** | *"add vault communication guidance + secret protection rules"* | **Learning 2** — below |
| **1 May 2026** | *"refactor reality document from monolith into 13-domain fractal tree"* | Knowledge structure follows the same fractal rule as the code |
| **25 May 2026** | *"code scan 24–25 May, app.json injection documented, B-008 ROLE.md link fix"* | Routine maintenance; roles now stable |

---

## Learning 1 — roles did not know where to talk (30 March 2026)

**The symptom**, visible in the commit message itself: a *"dangling comms/03/ folder"* — comms directories existing that no role referenced.

**The fix**: read/write directory tables added to Conductor, Dev and QA, plus QA's eight-step session-start sequence. The added lines, verbatim from the diff:

```
+ | `team/comms/` | Cross-team communication — changelogs, QA briefs, inter-team briefs, plans |
+ | `team/comms/QA_START_HERE.md` | **Read first every session** — what changed, what to test |
+ | `team/comms/changelog/` | Read changelogs to classify test failures (good vs bad) |
+ 6. **Write a changelog entry** in `team/comms/changelog/MM/DD/` documenting the fix and expected test impact
+ 7. **If the fix affects UI behaviour**, write a QA brief in `team/comms/qa/briefs/MM/DD/` with updated test cases
```

**The learning, generalised**: *building the shared channel is not enough — every role must carry the addresses of its own inbox and outbox, and a session-start sequence that reads them.* Infrastructure a role has not been told about does not exist. This is the single most reusable lesson in the corpus for anyone standing up a multi-role team, and `/evolution/` should lead with it.

## Learning 2 — a new capability arrived without its prohibition (8 April 2026)

**The context**: roles gained `sgit` (the vault CLI) for cross-team handovers. **The risk**: vault keys and access tokens are exactly the sort of thing an agent will helpfully commit.

**The fix**, added to Dev, QA and Librarian, and to `.claude/CLAUDE.md` in the same commit:

```
+ - No access tokens, vault keys, share tokens, or API keys are committed to Git — these are secrets
+ - **sgit** (PyPI: `sgit-ai`): Create vaults for cross-team briefing delivery… 
+   **NEVER commit vault keys, share tokens, or access tokens to Git.**
```

Note the placement: the prohibition sits **inside the tool's own row in the Tools and Access table**, next to the capability it constrains — not in a distant security section a role might not read.

**The learning, generalised**: *when you grant a role a new tool, write the prohibition in the same commit and in the same place as the grant.* A capability added on Monday and a rule added in June is a month of exposure. This connects directly to `pki.sgit.ai`'s key discipline (`sgit_vk1_` write keys never published) — the role file is where that discipline reaches the agent that would otherwise breach it.

## Learning 3 — the format regressed (Feb → Mar 2026)

Not a single commit but a drift, and the estate has not noticed it: the newer table-format Identity blocks state Central Claims **descriptively**, while the older bullet-format ones state them as **falsifiable failure conditions** (`01__` §3). The migration improved the markup and lost the property that made the field valuable.

**The learning, generalised**: *a format migration can silently drop a semantic constraint; diff the meaning, not just the rendering.* Publishing this on the site — a self-criticism of the estate's own reference material — is exactly the credibility the network's other sites are built on.

---

## How the site keeps this alive

`/evolution/` is not a one-time archaeology. Every future change to a `ROLE.md` should produce a dated entry answering three questions: **what broke, what rule was added, and which roles received it.** Three lines. The rule is that a role edit without such an entry is incomplete — because the edited file records the answer but destroys the question, and the question is what an agent needs in order to know whether the rule still applies.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
source: /briefs/06__site-architecture.md

==============================================================================


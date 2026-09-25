---
title: Open questions
date: 2026-09-24
desk: Historian
covers: 2026-08-11 to 2026-09-24
standfirst: The questions the network's sites have asked in public and not yet answered, numbered Q-001 onward, oldest first, each with who is waiting, where it was asked and when. A question stays here until a source answers it.
sources:
  - src:history/sgit.ai-version-log.json
  - https://sgit.ai/admin/versions.html
  - https://riskmandate.ai/versions.md
  - https://risks.sgit.ai/llms.txt
  - https://store.sgit.ai/llms.txt
reviewed_by:
reviewed_on:
---

A question here is one a source asks, or names as open, owed or somebody's call, and that no later source in the snapshot of 24 September 2026 answers. Each entry says who is waiting on the answer, as a site or a role, where it was asked and when. The status line says what the snapshot shows about it, and no more. Where the same matter is tracked as a [loose end](nr:loose-ends), the entry says so. Choices already made are in [the decisions](nr:history/decisions); the wider story is in [the story so far](nr:history/the-story-so-far).

sgit.ai's version record has no per-version anchors, so its questions link to [the record](https://sgit.ai/admin/versions.html) and name the version. riskmandate.ai's questions link to that release's note.

## August 2026

### Q-001: Can the sgit CLI run transfers serially, or detect when it must?
- **Asked.** 11 August 2026, sgit.ai v0.1.12, [version record](https://sgit.ai/admin/versions.html). In-browser cloning needed a shim because WebAssembly cannot spawn threads, and "A serial/auto-detect mode is proposed upstream to the sgit CLI."
- **Waiting.** The sgit CLI team.
- **Status in the snapshot.** No answer recorded. Tracked as a [loose end](nr:loose-ends) with three other older asks.

### Q-002: Can a vault be rekeyed with its history preserved?
- **Asked.** 12 August 2026, sgit.ai v0.1.14, [version record](https://sgit.ai/admin/versions.html): "Added a fourth CLI-team ask: history-preserving rekey."
- **Waiting.** The sgit CLI team.
- **Status in the snapshot.** No answer recorded.

### Q-003: Will the CLI get diff export and apply, a published diff format, and ignore-file support?
- **Asked.** 15 August 2026, sgit.ai v0.2.9, [version record](https://sgit.ai/admin/versions.html). The serialised pull request ships as PARTIAL because "import is not first-class", and the brief asks for all three; ignore support is called "a prerequisite for the one-folder-two-VCS pattern".
- **Waiting.** The sgit CLI team.
- **Status in the snapshot.** No answer recorded. The one-folder pattern itself was retired on 19 September (sgit.ai v0.2.84).

### Q-004: Can a host open the official vault interface on a chosen view?
- **Asked.** 16 August 2026, sgit.ai v0.2.16, [version record](https://sgit.ai/admin/versions.html). The last ask to the SG/Vault UI team is sharpened to one optional field on the open message, selecting files, history or settings; "a host can select a SURFACE but not a VIEW".
- **Waiting.** The SG/Vault UI team.
- **Status in the snapshot.** No answer recorded.

### Q-005: What do the `/api/vault/zip` and `/join/*` endpoints do?
- **Asked.** 18 August 2026, sgit.ai v0.2.34, [version record](https://sgit.ai/admin/versions.html): the two endpoints another team's audit "could not resolve" are "listed as unresolved rather than described".
- **Waiting.** The SG/API team.
- **Status in the snapshot.** No answer recorded.

### Q-006: Eight questions risks.sgit.ai publishes about its own model
- **Asked.** risks.sgit.ai, site v0.2.2 of 27 August 2026, [llms.txt](https://risks.sgit.ai/llms.txt): "EIGHT OPEN QUESTIONS published unresolved": the formula language, who sets acceptable, refusal to sign, whether unaccepted-equals-critical scales, interval enforcement, grading recoverability, the grounding floor, and gaming under personal liability.
- **Waiting.** risks.sgit.ai, and riskmandate.ai, the product it underpins.
- **Status in the snapshot.** Published as open. The same file says "no formula language exists" and that only one of five maturity levels has a stated predicate.

### Q-007: Have the reuse rights for the AIUC-1 control text been confirmed?
- **Asked.** 27 August 2026, sgit.ai v0.2.49, [version record](https://sgit.ai/admin/versions.html). The vault's own notice says reuse rights "have NOT been confirmed with AIUC" and that a public republisher should confirm them first; the author chose to publish as it stands.
- **Waiting.** The vault's owner, and AIUC.
- **Status in the snapshot.** No confirmation recorded.

## September 2026, before the week

### Q-008: Which hosts serve the append routes, and can an append token be told from a read key without harm?
- **Asked.** 7 September 2026, sgit.ai v0.2.58, [version record](https://sgit.ai/admin/versions.html). Seven follow-up questions went to the team that owns the append code, including "whether the enum-key derivation is stable enough to publish as a spec" and whether any non-destructive way exists to tell the two apart, "since they are the same shape and confusing them would be a serious leak".
- **Waiting.** The SG/API team.
- **Status in the snapshot.** No answer recorded. Tracked as a [loose end](nr:loose-ends).

### Q-009: What is the ask on sgit.ai's investor page?
- **Asked.** 7 September 2026, sgit.ai v0.2.62, [version record](https://sgit.ai/admin/versions.html). The page leaves "THE ASK LEFT VISIBLY OPEN in a dashed box tracked as board item N1, because nothing on that page may be a number the founder has not supplied".
- **Waiting.** The founder.
- **Status in the snapshot.** No figure recorded in the log.

### Q-010: What is the bridge's tool contract for a model call inside a vault?
- **Asked.** 7 September 2026, sgit.ai v0.2.63, [version record](https://sgit.ai/admin/versions.html). The third tier of the site's chat pane "is detected-not-wired and on the board as T11, blocked on one fact about the bridge's tool contract."
- **Waiting.** The owners of the vault host's model bridge.
- **Status in the snapshot.** No answer recorded.

### Q-011: Does the second policy of a known deployment shape take minutes rather than days?
- **Asked.** 12 September 2026, riskmandate.ai [v1.4.0](https://riskmandate.ai/versions/1.4.0.md). The first collaborator brief asks for an instrumentation table testing the claim: "Nobody has checked, and that number decides whether any of this can be priced."
- **Waiting.** riskmandate.ai, and the collaborator the brief is written for.
- **Status in the snapshot.** No measurement recorded.

### Q-012: Should the American spellings shared with another site change?
- **Asked.** 12 September 2026, riskmandate.ai [v1.7.0](https://riskmandate.ai/versions/1.7.0.md). A severity label and two RAMM entity names keep the American form "because they may be shared with another site, which is a decision rather than an oversight."
- **Waiting.** riskmandate.ai and the site that shares the vocabulary (not named).
- **Status in the snapshot.** No decision recorded.

### Q-013: What is the convention for screenshots of other companies' products?
- **Asked.** 13 September 2026, riskmandate.ai [v1.9.0](https://riskmandate.ai/versions/1.9.0.md): "Still open: a convention for screenshots", recorded as owed on the brief register; the Lab's drawn mockups "remain the pattern until that is decided."
- **Waiting.** riskmandate.ai's lead.
- **Status in the snapshot.** No convention recorded.

### Q-014: What do the connector vaults' open research rows find?
- **Asked.** 15 September 2026, riskmandate.ai [v1.14.0](https://riskmandate.ai/versions/1.14.0.md). What the vendors' pages could not settle goes to a `RESEARCH-NEEDED.md` per vault, "written to be handed to a separate agent".
- **Waiting.** A research agent, and riskmandate.ai.
- **Status in the snapshot.** The later Gmail-connector research list is "documented from Google's pages or left open, never provoked" ([v1.24.0](https://riskmandate.ai/versions/1.24.0.md)); no general answer recorded.

### Q-015: Is the n8n write-up, and its author, to be published?
- **Asked.** 15 September 2026, riskmandate.ai [v1.15.0](https://riskmandate.ai/versions/1.15.0.md): "The write-up itself and its author are not published with the vault; that is the project lead's to decide."
- **Waiting.** riskmandate.ai's lead.
- **Status in the snapshot.** No decision recorded.

### Q-016: Who owns the follow-up mailbox after a sale?
- **Asked.** 15 September 2026, riskmandate.ai [v1.19.3](https://riskmandate.ai/versions/1.19.3.md): "who owns it is an open question in section five, not a decision made here." The note also says nothing yet carries a sale from the store to the person who follows it up.
- **Waiting.** riskmandate.ai and store.sgit.ai.
- **Status in the snapshot.** No owner recorded.

### Q-017: Has store.sgit.ai been told that riskmandate.ai re-opened the price boundary?
- **Asked.** 17 September 2026, riskmandate.ai [v1.25.0](https://riskmandate.ai/versions/1.25.0.md): prices on the home page re-open "a boundary the other team wrote down and they should be told."
- **Waiting.** store.sgit.ai.
- **Status in the snapshot.** No record of it. store.sgit.ai's llms.txt still describes its [boundary page](https://store.sgit.ai/llms.txt) as the store owning e-commerce and riskmandate.ai owning the products and the policies.

### Q-018: Which words for the four objects, and when does the clock start on levels 3 and 4?
- **Asked.** 17 September 2026, riskmandate.ai [v1.25.2](https://riskmandate.ai/versions/1.25.2.md). Two findings of the second synthetic-user study "were not fixed and are recorded instead": the home page says *reach* and *gap* where the policy page says *grant* and *delta*, and every delivery window on levels 3 and 4 starts from the buyer's reply, "so the step with no time on it is ours".
- **Waiting.** riskmandate.ai.
- **Status in the snapshot.** No fix recorded in later notes.

## 18 to 24 September 2026

### Q-019: Do people press *Always allow*, and do they know what the scope permits?
- **Asked.** 20 September 2026, riskmandate.ai [v1.27.0](https://riskmandate.ai/versions/1.27.0.md). Both claims "are both probably true and neither is measured, so both appear as open questions with how each would be settled rather than as facts."
- **Waiting.** riskmandate.ai.
- **Status in the snapshot.** Not measured.

### Q-020: How far does one approval reach in a connected assistant?
- **Asked.** 20 September 2026, riskmandate.ai [v1.27.2](https://riskmandate.ai/versions/1.27.2.md). Four questions the vendor's help page does not answer: whether *Always allow* lasts beyond the conversation, whether an approval can be scoped to a chat or a project, whether a second, narrower connection to the same account is possible, and which scopes are requested. The first is "the one that would change the most."
- **Waiting.** The vendor of the connector, and riskmandate.ai.
- **Status in the snapshot.** Recorded as silences, "not an accusation"; no answer recorded.

### Q-021: How will people who run the prompts be counted, and which shape gets a workflow next?
- **Asked.** 21 September 2026, riskmandate.ai [v1.28.0](https://riskmandate.ai/versions/1.28.0.md). The measure is people who run the prompts and people who end up with a policy, but "Nothing on this site counts anything, so the measure the brief names has no number behind it yet; that decision is the lead's". The Try it page "asks which one to write next".
- **Waiting.** riskmandate.ai's lead, and the site's readers.
- **Status in the snapshot.** No counter and no choice recorded.

### Q-022: What happens to the two older exports of the mark?
- **Asked.** 23 September 2026, riskmandate.ai [v1.29.1](https://riskmandate.ai/versions/1.29.1.md). Two PNGs show a wider `RM` than the revised mark and are "left alone here rather than quietly re-cut, and named so somebody decides."
- **Waiting.** riskmandate.ai.
- **Status in the snapshot.** No decision recorded.

### Q-023: Will anyone build vault key management with sgit?
- **Asked.** 24 September 2026, sgit.ai v0.6.2, [version record](https://sgit.ai/admin/versions.html). A call to password managers, identity providers and credential managers for, in order of preference, something that already exists, a joint pilot, or an open specification.
- **Waiting.** sgit.ai.
- **Status in the snapshot.** An open call; no reply recorded.

### Q-024: What is the risk side of each proposed partnership?
- **Asked.** 24 September 2026, sgit.ai v0.6.4, [version record](https://sgit.ai/admin/versions.html). A brief asks riskmandate.ai for the risk side of every partnership as two behaviour policies and a delta, and for sgit written up as a control against five GDPR articles.
- **Waiting.** sgit.ai, on riskmandate.ai.
- **Status in the snapshot.** No response recorded. Tracked as a [loose end](nr:loose-ends).

### Q-025: Will riskmandate.ai apply to the Sovereign AI R&D Procurement Scheme?
- **Asked.** 24 September 2026, riskmandate.ai [v1.32.2](https://riskmandate.ai/versions/1.32.2.md). Its third challenge asks for a risk management approach for CISOs "for specific agents in specific contexts". "We have not applied; that is the lead's decision."
- **Waiting.** riskmandate.ai's lead.
- **Status in the snapshot.** Not applied.

### Q-026: Will the named vendor cases be sent to their vendors?
- **Asked.** 24 September 2026, riskmandate.ai [v1.33.0](https://riskmandate.ai/versions/1.33.0.md). Two named cases stay unlisted drafts "until the lead decides to send them to the vendors".
- **Waiting.** riskmandate.ai's lead, then the vendors.
- **Status in the snapshot.** One of the two, agentgateway, was published under the direction for open source ([v1.34.0](https://riskmandate.ai/versions/1.34.0.md)). The other is still a draft as far as the record shows.

### Q-027: How does a person correct their behaviour-policy vault from inside it?
- **Asked.** 24 September 2026, riskmandate.ai [v1.34.1](https://riskmandate.ai/versions/1.34.1.md): a person corrects their vault by replying to the lead; "a way to do it from inside the vault is a question for the app vault."
- **Waiting.** The app vault's maintainers, at riskmandate.ai.
- **Status in the snapshot.** No answer recorded. No real person's vault exists yet.

### Q-028: Does the interview prompt return every section when run by voice?
- **Asked.** 24 September 2026, sgit.ai v0.6.7 ([version record](https://sgit.ai/admin/versions.html)) and riskmandate.ai [v1.34.2](https://riskmandate.ai/versions/1.34.2.md). The brief asks for one run in voice mode; the site's agent cannot make it, "so that run is the lead's." The prompt was then lengthened to a sixteen-section summary, and "The longer prompt has not been run" ([v1.34.4](https://riskmandate.ai/versions/1.34.4.md)).
- **Waiting.** riskmandate.ai's lead.
- **Status in the snapshot.** Not run. Tracked as a [loose end](nr:loose-ends).

### Q-029: Should a risk carry a figure for its loss?
- **Asked.** 24 September 2026, riskmandate.ai [v1.34.6](https://riskmandate.ai/versions/1.34.6.md): risks carry a consequence in words and no number, and "a loss figure is the lead's decision."
- **Waiting.** riskmandate.ai's lead.
- **Status in the snapshot.** No figure; the article's rule stands that kinds of consequence do the work.

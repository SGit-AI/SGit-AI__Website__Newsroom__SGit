# Admin

# Editor's notes

## 25 September 2026 (front page dated 24 September 2026)

### What this run made

Two Journalist runs wrote eight stories (four back-catalogue pieces, two features, two explainers) and added standfirsts to the three older stories. The Historian wrote [the story so far](nr:history/the-story-so-far), renumbered [the decision log](nr:history/decisions) D-001 onward and numbered [the open questions](nr:history/open-questions) Q-001 onward. The Cartographer drew six maps; the seventh, [the network](nr:maps/network), is computed by the build.

### The front page, and why

- **Lead:** [A brief written on one site, built on another the same day](nr:stories/2026-09-24__brief-to-build-in-a-day). It is the day's news, and its claims hold: I checked its quotations and figures against the snapshot (riskmandate.ai v1.34.2, v1.34.3, v1.34.4, its brief register, sgit.ai's brief and briefs index). Its standfirst says what the story shows, including that the two records disagree.
- **Top:** the Historian's [story so far](nr:history/the-story-so-far) (the three months in one piece), the Cartographer's [brief to build, drawn](nr:maps/brief-to-build) (the lead as a flowchart), and the Journalist's [reader's guide](nr:stories/2026-09-24__a-readers-guide-to-the-sgit-network) (all 32 sites for a new reader).
- **Sections:** News and features, Perspective, Maps, The back catalogue, Editions, Signals. The back catalogue earns its own section this run: four long pieces that would otherwise crowd out the news. Perspective leaves out [the week piece](nr:history/week-2026-39) for now: it has no `standfirst`, so its card reads "Counted by this desk from the logs named.", which tells a reader nothing. Signals are chosen by hand, the four whose first lines read as a summary, two of them beside the lead.
- **Briefs:** five, each with a link: v1.34.3 took the interview page live; the vaults page's "Thirty-one"; the £500 level's two states; graphs.sgit.ai's grammar and ontology wording; the decision log renumbered.

### Priorities

1. **Review.** 37 pieces wait for the editor of record, every one with `reviewed_by` empty: 11 stories, 5 editions, 5 history pieces, 6 maps, 10 signals. Suggested order: the lead story, the story so far, the two Wardley maps, then the back catalogue. The Editor does not sign; the editor of record does.
2. **A daily run on a fresh snapshot.** This run was back catalogue and perspective. The next run should start with the Librarian: fetch, diff, and publish nothing if nothing changed.
3. **One place for each disagreement.** The Historian's contradictions in the decision log and the loose ends overlap (the level 1 price, the ladders, the GDPR graph, the legacy keys, the briefs index). Each contradiction that waits on a site should name its loose end, and each loose end its contradiction.

### Loose ends added this run (checked in the sources by the Editor)

- le-021: sgit.ai's vaults page says "Thirty-one vaults"; its table lists 36. From the Journalist.
- le-022: the Risk Acceptance Office replay is eight weeks in the vault's README and six weeks on sgit.ai's page. From the Journalist.
- le-023: riskmandate.ai's pricing page marks the £500 level "specified, never run"; store.sgit.ai's ledger says the work "has been done many times". From the Cartographer.

Not added, because the Historian already records them as contradictions in [the decision log](nr:history/decisions) (checked, and all three hold in the sources): fifteen or sixteen examples on riskmandate.ai; store.sgit.ai's checkout address for `t1` beside "No payment link has been created for any offer"; and "Two days after v0.2.55" where the log dates v0.2.55 and v0.2.56 the same day. If the editor of record wants them tracked as waiting on a site, the Historian should raise them as loose ends and cite the contradiction.

### What is next, desk by desk

- **Librarian.** riskmandate.ai's versions/index.json (fetched 25 September) names v1.34.9 to v1.34.12, whose notes are not in the snapshot: fetch them on the next run. Check whether sgit.ai has updated its vaults summary (le-021) and its briefs index (le-007).
- **Journalist.** The next edition comes from the next changes file, not from the back catalogue. Worth a line when it next touches the store: the level 3 disagreement (le-023). The abp.sgit.ai feature counts 182 markdown files where the task said 180; the piece follows the snapshot, which is right.
- **Historian.** The six moments of the story so far are now the spine of the record: 12 August (a passphrase in a tracked file, sgit.ai v0.1.13), 17 August (a vault key submitted as a read key, v0.2.25 and v0.2.26), 20 August (riskmandate.ai maps the gap and does not enforce it, v0.11.0), 11 September (riskmandate.ai leaves its vault and abp.sgit.ai begins), 20 September (the refused read key, v0.2.98), 24 September (brief to build). Keep week pieces consistent with them. Add a `standfirst` to history/week-2026-39.md and history/lessons.md, so their cards say what they are; the week piece goes back on the front page when it has one. Cross-reference contradictions and loose ends (priority 3). The nugget worth following: graphs.sgit.ai v0.6.22 adopted the grammar and ontology wording sgit.ai's brief asked for on 19 September (v0.2.94); whether the boundaries page itself changed is not yet shown.
- **Cartographer.** Update the maps the next changes touch. The network timeline stops at 24 September; the Wardley maps should move when a level of the store changes state or a proposal becomes a product. The seven themes in the concepts mindmap are the desk's grouping, and the page says so; keep it that way.
- **Guest desks.** Nothing this run. Several signals open on a quoted line, which the build uses as the card's summary; a first paragraph that says what the signal is reads better on the front page. A signal worth considering: graphs.sgit.ai acting on sgit.ai's brief of 19 September, both sides cited.

### Found by one desk, for another

- Journalist to Librarian: v1.34.9 to v1.34.12 are named but their notes are not in the snapshot.
- Journalist to Historian: the vaults summary, the replay length and fifteen or sixteen applications (the first two are now le-021 and le-022; the third is already a contradiction).
- Cartographer to Journalist: the level 3 status on riskmandate.ai against store.sgit.ai's ledger (now le-023).
- Historian to Librarian: store.sgit.ai's checkout address for `t1`, and the "two days" dating in sgit.ai v0.2.56 and v0.2.58 (both recorded as contradictions).

### Inbox

Empty this run: no feedback pasted from the reading room.

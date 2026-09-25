# CLAUDE.md: the sgit newsroom

A newsroom whose beat is the sgit network: sgit.ai, riskmandate.ai, graphs.sgit.ai, risks.sgit.ai and the rest. Desks (Librarian, Journalist, Historian, guest desks) read the sites, and the build turns their files into a static site that works offline.

## Read first

`START-HERE.md`, then `brief/01` to `brief/06`. `brief/06-house-rules.md` is binding.

## Layout

```
sources/        the snapshot: sites/ (with manifest.json), history/, cli-briefs/, vaults/
data/           the Librarian's changes, index, concepts, vaults, loose ends (JSON)
editions/       one markdown file per day that had changes
stories/        longer pieces
history/        the Historian: weekly moments, lessons.md, decisions.md
signals/        cross-pollination between projects
tools/          fetch_sources.py, build.py, validate.py, agents.py (standard library only)
agents/         the desks' ROLE.md and MANDATE.md, rendered from data/agents.json
runs/           one run record per desk run
site/           the built site. Generated: never edit by hand.
```

## Commands

```bash
python3 tools/fetch_sources.py          # refresh the snapshot (network needed)
python3 tools/fetch_missing.py          # fetch .md twins of linked network pages not in the snapshot
./run-local.sh [--offline|--serve]      # fetch (if online), build, validate, serve on :8000
python3 tools/build.py                  # build site/ from everything else
python3 tools/validate.py               # must pass before every commit
```

## Agents: work as a desk

The work is done by desks with roles and mandates, registered in `data/agents.json` and rendered into
`agents/<id>/ROLE.md` and `MANDATE.md` by `python3 tools/agents.py` (never edit `agents/` by hand).
Before doing a desk's work, read its ROLE and MANDATE; write only in its folders; leave a run record in
`runs/` (see `runs/README.md`). `tools/validate.py` fails a run record outside its mandate.
Skills: `/desk <agent> <task>` for one task as one desk; `/newsroom-run` for the whole daily run.

## Rules

1. **Offline first.** `site/index.html` opened from disk, with the network off, must work: relative links, no external resources, no fetch() of local files.
2. **Every claim cites its source**, with the live URL and the local copy, and every page carries a provenance block (site, URL, fetched time, sha256, desk).
3. **Read before writing.** No summary of a file that was not read in this session.
4. **Never a vault key or write credential** in the repository or the site. Read keys only where a source site publishes them on purpose. The validator refuses `sgit_private_`, `sgit_vk1_`, and `[a-z0-9]{24}:[a-z0-9]{4,24}`.
5. **Shipped and proposed stay apart**, in the source's own words.
6. **Roles and sites, not people.** They/them where pronouns are not stated. No model names in the repository.
7. **If nothing changed, publish nothing.**
8. **Commit after every step**, with a message that says what changed and the counts.

# SGit-AI__Website__Newsroom__SGit

The repository for **[sgit.newsroom.sgit.ai](https://sgit.newsroom.sgit.ai/)**: a newsroom whose beat is the
sgit network itself. Desks (Librarian, Journalist, Historian, guest desks) read a frozen, hashed snapshot of every
site, and a build turns their files into a static site that works offline.

Start with `START-HERE.md` and `CLAUDE.md`. The brief is in `brief/`, the file formats in `AUTHORING.md`.

## Read it offline (on a plane)

The built site is committed in `site/`. It needs no server and no network.

```bash
git clone https://github.com/SGit-AI/SGit-AI__Website__Newsroom__SGit.git
cd SGit-AI__Website__Newsroom__SGit
open site/index.html            # macOS; xdg-open on Linux, start on Windows
```

Or serve it, if you prefer a local URL (search, filters and every link work either way):

```bash
python3 -m http.server -d site 8000     # then open http://localhost:8000/
```

Everything in `sources/` is plain markdown and text too: any editor reads it.

## Build

```bash
python3 tools/librarian.py      # data/index.json and data/vaults.json, computed from the snapshot
python3 tools/build.py          # site/ from sources/, data/, editions/, stories/, history/, signals/
python3 tools/validate.py       # must pass before every commit
python3 tools/fetch_sources.py  # refresh the snapshot (network needed; the daily run)
```

Python standard library only. The build is deterministic: CI rebuilds and fails if the committed `site/` differs.

## Release

Every push to `dev` runs `.github/workflows/deploy-pages.yml`: validate, tag (`vX.Y.Z` from `version.txt`, which
the release commit's subject repeats as `site vX.Y.Z: ...`), then deploy `site/` to GitHub Pages.

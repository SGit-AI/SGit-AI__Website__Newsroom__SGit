#!/usr/bin/env bash
# Run the sgit newsroom locally: bring home what the network has (if there is a network), rebuild,
# validate, and serve site/ on http://localhost:$PORT/.
#
#   ./run-local.sh              # online: fetch missing .md twins, rebuild, validate, serve
#   ./run-local.sh --offline    # no downloads: rebuild from what is on disk and serve (the plane)
#   ./run-local.sh --serve      # no downloads, no rebuild: just serve the committed site/
#   ./run-local.sh --refresh    # also re-take the whole snapshot first (the daily run's fetch step)
#   PORT=9000 ./run-local.sh    # another port
#
# Downloads are cached in the repository itself: fetched pages land in sources/sites/ with their
# sha256 in sources/sites/manifest.json, and links with no text twin are remembered in
# sources/sites/missing.json, so a second run asks the network only for what is new. Commit them to
# keep them. Python 3 standard library only. Never needs the network to serve.
set -euo pipefail
cd "$(dirname "$0")"

PORT="${PORT:-8000}"
MODE=online
REFRESH=0
for arg in "$@"; do
  case "$arg" in
    --offline) MODE=offline ;;
    --serve)   MODE=serve ;;
    --refresh) REFRESH=1 ;;
    -h|--help) sed -n '2,15p' "$0"; exit 0 ;;
    *) echo "unknown option: $arg (try --help)" >&2; exit 2 ;;
  esac
done

command -v python3 >/dev/null || { echo "python3 is needed" >&2; exit 1; }

online() {
  python3 - <<'EOF' 2>/dev/null
import urllib.request, sys
try:
    urllib.request.urlopen('https://sgit.ai/llms.txt', timeout=5)
except Exception:
    sys.exit(1)
EOF
}

if [ "$MODE" = online ]; then
  if online; then
    if [ "$REFRESH" = 1 ]; then
      echo "== re-taking the snapshot (tools/fetch_sources.py)"
      python3 tools/fetch_sources.py
    fi
    [ -d site ] || python3 tools/build.py >/dev/null
    # linked pages bring more links: repeat until a pass finds nothing new (at most five passes)
    for pass in 1 2 3 4 5; do
      echo "== pass $pass: fetching the .md twins of linked network pages not yet on disk"
      out=$(python3 tools/fetch_missing.py)
      echo "$out" | sed 's/^/   /'
      echo "$out" | grep -q '^fetched 0 pages' && break
      python3 tools/librarian.py >/dev/null
      python3 tools/build.py >/dev/null
    done
  else
    echo "== no network: skipping downloads, building from what is on disk"
  fi
fi

if [ "$MODE" != serve ]; then
  echo "== building"
  python3 tools/librarian.py
  python3 tools/build.py
  echo "== validating"
  python3 tools/validate.py || echo "!! validation failed: the site is served anyway, but do not commit it like this" >&2
fi

[ -f site/index.html ] || { echo "no site/index.html: run without --serve" >&2; exit 1; }
if [ -n "$(git status --porcelain -- sources site data 2>/dev/null)" ]; then
  echo "== new or changed files in sources/, data/ or site/: commit them to keep them offline"
fi
echo "== serving site/ on http://localhost:$PORT/  (Ctrl-C to stop; or open site/index.html directly)"
exec python3 -m http.server "$PORT" --bind 127.0.0.1 --directory site

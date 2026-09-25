#!/usr/bin/env bash
# Release: bump version.txt, rebuild, gate, commit as "site vX.Y.Z: <message>", push to dev.
#   tools/release.sh 0.1.8 "what changed"        (set NO_PUSH=1 to stop before pushing)
# Every step must pass; a red validator or an unrendered diagram stops the release before the commit.
set -euo pipefail
cd "$(dirname "$0")/.."
VER="${1:?version, e.g. 0.1.8}"; MSG="${2:?one sentence}"
[[ "$VER" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || { echo "version must be X.Y.Z" >&2; exit 2; }
echo "v$VER" > version.txt
python3 - "$VER" "$MSG" "${RELEASE_BODY:-}" <<'PY'
import json, sys, datetime, os
ver, msg, body = sys.argv[1], sys.argv[2], sys.argv[3]
p = 'data/releases.json'; d = json.load(open(p)) if os.path.exists(p) else {'about': '', 'releases': []}
d['releases'] = [r for r in d['releases'] if r['version'] != 'v' + ver]
notes = [l.strip('- ').strip() for l in (open(body).read() if body and os.path.exists(body) else '').split('\n') if l.strip().startswith('-')]
now = datetime.datetime.now(datetime.timezone.utc)
d['releases'].append({'version': 'v' + ver, 'date': now.strftime('%Y-%m-%d'), 'time': now.strftime('%H:%M'), 'commit': '', 'title': msg, 'notes': notes})
json.dump(d, open(p, 'w'), indent=1, ensure_ascii=False)
PY
python3 tools/librarian.py >/dev/null
python3 tools/build.py | tail -1
python3 tools/validate.py | tail -1
if command -v node >/dev/null && [ -f tools/check_diagrams.js ]; then node tools/check_diagrams.js | tail -1; fi
git add -A
git commit -q -F - <<MSG
site v$VER: $MSG

$(cat "${RELEASE_BODY:-/dev/null}" 2>/dev/null)
Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01K34SRXq1DkaDoemoTQKp4D
MSG
git log --oneline -1
[ "${NO_PUSH:-}" = 1 ] && exit 0
git push -q origin HEAD:dev
BR=$(git rev-parse --abbrev-ref HEAD); [ "$BR" != dev ] && [ "$BR" != HEAD ] && git push -q origin "HEAD:$BR" || true
echo "pushed v$VER to dev"

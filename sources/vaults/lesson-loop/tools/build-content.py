#!/usr/bin/env python3
"""Assemble content.json from player/record.json and plan/plan.json, and inline it into index.html.

Run from the vault root after changing either file:

    python3 tools/build-content.py

In a real deployment the app lives in its own vault and reads each player's record from that
player's data vault. This demo ships one invented record beside the app, so it opens anywhere.
"""
import json, sys
content = {'player': json.load(open('player/record.json')), 'plan': json.load(open('plan/plan.json'))}
json.dump(content, open('content.json', 'w'), indent=1, ensure_ascii=False)
compact = json.dumps(content, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
html = open('index.html').read()
marker = 'const FALLBACK = /*__DATA__*/'
start = html.find(marker)
if start < 0:
    sys.exit('placeholder not found')
start += len(marker)
end = html.find(';\n', start)
open('index.html', 'w').write(html[:start] + compact + html[end:])
print(f"{len(content['player']['entries'])} entries; inlined {len(compact):,} bytes")

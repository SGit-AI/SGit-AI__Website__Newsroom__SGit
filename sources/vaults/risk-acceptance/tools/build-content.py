#!/usr/bin/env python3
"""Chain the risk's decision record, assemble content.json, and inline it into index.html.

Run from the vault root after changing risk/risk.json or plan/plan.json:

    python3 tools/build-content.py

It (1) recomputes prev/hash on every event in risk/risk.json so the record is a hash chain,
(2) writes risk/record.jsonl, one event per line, the form a risk vault would keep,
(3) writes content.json, and (4) inlines it into index.html at the exact placeholder.
"""
import hashlib, json, sys

risk = json.load(open('risk/risk.json'))
plan = json.load(open('plan/plan.json'))
prev = '0' * 64
for i, e in enumerate(risk['events'], 1):
    e['seq'] = i
    e.pop('hash', None)
    e['prev'] = prev
    canon = json.dumps(e, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
    e['hash'] = hashlib.sha256(canon.encode('utf-8')).hexdigest()
    prev = e['hash']
json.dump(risk, open('risk/risk.json', 'w'), indent=1, ensure_ascii=False)
with open('risk/record.jsonl', 'w') as f:
    for e in risk['events']:
        f.write(json.dumps(e, ensure_ascii=False, separators=(',', ':')) + '\n')
content = {'risk': risk, 'plan': plan}
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
print(f"{len(risk['events'])} events, head {prev[:12]}; inlined {len(compact):,} bytes")

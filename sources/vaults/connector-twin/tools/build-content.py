#!/usr/bin/env python3
"""Assemble content.json from the journal and the plan, then inline it into index.html.

Run from the vault root after changing anything in journal/ or plan/plan.json:

    python3 tools/build-content.py

Why inline: vault HTML cannot fetch its own files before the bridge is up, and this app asks for no
permissions at all, so it carries its data. The placeholder is matched exactly, never by pattern,
so nothing else in the file can be touched.
"""
import glob, json, sys

entries = []
for f in sorted(glob.glob('journal/session-*.jsonl')):
    entries += [json.loads(l) for l in open(f) if l.strip()]
prompts = json.load(open(sorted(glob.glob('journal/prompts-*.json'))[-1]))
plan    = json.load(open('plan/plan.json'))
content = {'journal': {'entries': entries, 'prompts': prompts}, 'plan': plan}
json.dump(content, open('content.json', 'w'), indent=1, ensure_ascii=False)

compact = json.dumps(content, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
assert '\n' not in compact, 'raw newline leaked into the inlined data'
html   = open('index.html').read()
marker = 'const FALLBACK = /*__DATA__*/'
start  = html.find(marker)
if start < 0:
    sys.exit('placeholder not found: expected `const FALLBACK = /*__DATA__*/{...};`')
start += len(marker)
end = html.find(';\n', start)
html = html[:start] + compact + html[end:]
open('index.html', 'w').write(html)
print(f'{len(entries)} entries; inlined {len(compact):,} bytes into index.html')

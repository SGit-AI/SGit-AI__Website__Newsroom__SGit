#!/usr/bin/env python3
"""Assemble content.json from the sample and the plan, and inline it into index.html.

Run from the vault root after changing anything in sample/ or plan/plan.json:

    python3 tools/recompute.py && python3 tools/render-xray.py && python3 tools/build-content.py

The app shows the customer's documents, the X-ray and the plan from this one file, inlined into
the page, so it opens anywhere the vault opens, offline included.
"""
import json, os, sys

def folder(path):
    return {n: open(os.path.join(path, n)).read() for n in sorted(os.listdir(path)) if os.path.isfile(os.path.join(path, n))}

content = {
    'xray': json.load(open('sample/xray/findings.json')),
    'inbox': folder('sample/inbox'),
    'evidence': folder('sample/xray/evidence'),
    'claude': folder('sample/claude'),
    'plan': json.load(open('plan/plan.json')),
}
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
print(f"{len(content['xray']['findings'])} findings, {len(content['inbox'])} inbox files; inlined {len(compact):,} bytes")

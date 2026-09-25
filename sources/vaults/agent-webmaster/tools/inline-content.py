#!/usr/bin/env python3
"""Inline content.json into index.html as the FALLBACK object.

Run from the vault root after editing content.json:

    python3 tools/inline-content.py

Why: vault HTML cannot fetch its own files before the bridge is up, so the app carries a compact
copy of the content and uses the file only when it can read it. This keeps the two in step.
The placeholder is matched exactly, never by pattern, so nothing else in the file can be touched.
"""
import json, re, sys

src = json.load(open('content.json'))
compact = json.dumps(src, ensure_ascii=False)
assert '\n' not in compact, 'raw newline leaked into the inlined data'
html = open('index.html').read()
m = re.search(r'const FALLBACK = /\*__DATA__\*/(\{.*?\});\n', html, re.S)
if not m:
    sys.exit('placeholder not found: expected `const FALLBACK = /*__DATA__*/{...};`')
new = html[:m.start(1)] + compact + html[m.end(1):]
open('index.html', 'w').write(new)
print(f'inlined {len(compact):,} bytes of content into index.html')

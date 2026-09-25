#!/usr/bin/env python3
"""Verify the hash chain of every journal file. Exit 0 if intact, 1 at the first break.

    python3 tools/verify-journal.py

Each entry's hash is SHA-256 over the entry without its own `hash` field, serialised with sorted
keys and no whitespace; `prev` must equal the previous entry's hash, and the first entry's prev is
64 zeros. The app runs the same check in the browser.
"""
import glob, hashlib, json, sys

for f in sorted(glob.glob('journal/session-*.jsonl')):
    prev = '0' * 64
    for n, line in enumerate(open(f), 1):
        e = json.loads(line)
        canon = json.dumps({k: v for k, v in e.items() if k != 'hash'}, sort_keys=True,
                           separators=(',', ':'), ensure_ascii=False)
        if e['prev'] != prev or hashlib.sha256(canon.encode()).hexdigest() != e['hash']:
            print(f'{f}: chain broken at line {n} (seq {e.get("seq")})'); sys.exit(1)
        prev = e['hash']
    print(f'{f}: {n} entries intact, head {prev[:12]}')

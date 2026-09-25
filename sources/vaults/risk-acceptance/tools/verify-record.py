#!/usr/bin/env python3
"""Verify the hash chain of the risk's decision record. Exit 0 if intact, 1 at the first break.

    python3 tools/verify-record.py

Each entry's hash is SHA-256 over the entry without its own `hash` field, serialised with sorted
keys and no whitespace; `prev` must equal the previous entry's hash, 64 zeros for the first.
"""
import hashlib, json, sys

prev = '0' * 64
for n, line in enumerate(open('risk/record.jsonl'), 1):
    e = json.loads(line)
    canon = json.dumps({k: v for k, v in e.items() if k != 'hash'}, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
    if e['prev'] != prev or hashlib.sha256(canon.encode()).hexdigest() != e['hash']:
        print(f'record broken at entry {n}'); sys.exit(1)
    prev = e['hash']
print(f'{n} entries intact, head {prev[:12]}')

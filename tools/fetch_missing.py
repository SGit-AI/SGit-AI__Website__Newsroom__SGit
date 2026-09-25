#!/usr/bin/env python3
"""Fetch the .md twin of every network page the site links to but the snapshot does not hold.

    python3 tools/fetch_missing.py            # after a build: reads the external links in site/
    python3 tools/fetch_missing.py --retry    # also retry URLs that were missing last time

Every site in the network publishes a markdown twin of each page (page.html -> page.md,
folder/ -> folder/index.md), so a link that leaves the reading room can almost always be brought
home as text, rendered locally with no source-site CSS. Files land in sources/sites/<host>/ and in
sources/sites/manifest.json with their own fetch time and sha256, like the rest of the snapshot.
URLs that have no twin are cached in sources/sites/missing.json so later runs do not ask again.
Standard library only; needs the network (run it before the flight, not on it).
"""
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
os.chdir(ROOT)                                   # fetch_sources works relative to the repo root
from fetch_sources import SITES, OUT, Fetcher  # noqa: E402
from validate import ALLOWED_EXAMPLES, PUBLISHED_READ_KEY, SECRET_PATTERNS  # noqa: E402

MISSING = os.path.join(OUT, 'missing.json')
REFUSED = 'refused: holds a credential-shaped string (house rules: never in the repository)'
EXTRA_HOSTS = ('.sgit.ai',)                      # any subdomain of the network, not only SITES


def in_network(host):
    return host in SITES or host.endswith(EXTRA_HOSTS)


def candidates(url):
    """The text URLs that may hold this page: its .md twin first."""
    p = urlparse(url)
    base = f'{p.scheme}://{p.netloc}'
    path = p.path or '/'
    if path.endswith(('.md', '.txt', '.json')):
        return [base + path]
    if path.endswith('.html'):
        return [base + path[:-5] + '.md']
    if path.endswith('/'):
        return [base + path + 'index.md']
    if '.' in path.rsplit('/', 1)[-1]:
        return []                                # an image, a pdf, a zip: not text
    return [base + path + '.md', base + path + '/index.md']


def norm(url):
    p = urlparse(url)
    path = re.sub(r'(^|/)index\.(html|md)$', r'\1', p.path or '/')
    return (p.netloc.lower() + re.sub(r'\.(html|md)$', '', path).rstrip('/')).lower()


def credential_in(body):
    """The validator's own patterns: a page that would fail the gate is never saved."""
    text = PUBLISHED_READ_KEY.sub('', body.decode('utf-8', 'replace'))
    return any(m.group(0) not in ALLOWED_EXAMPLES for _, pat in SECRET_PATTERNS for m in pat.finditer(text))


def linked_urls():
    """Every external link in the built site (the build marks them class="ext")."""
    site = os.path.join(ROOT, 'site')
    if not os.path.isdir(site):
        sys.exit('no site/: run python3 tools/build.py first')
    found = set()
    for dirpath, _, files in os.walk(site):
        for name in files:
            if name.endswith('.html'):
                text = open(os.path.join(dirpath, name), encoding='utf-8', errors='replace').read()
                found.update(re.findall(r'<a class="ext[^"]*" href="(https?://[^"#?]+)', text))
    return sorted(found)


def main():
    retry = '--retry' in sys.argv
    f = Fetcher()
    have = {norm(u) for u in f.manifest}
    missing = json.load(open(MISSING)) if os.path.exists(MISSING) else {}
    todo = []
    for url in linked_urls():
        host = urlparse(url).netloc.lower()
        if not in_network(host) or norm(url) in have:
            continue
        if url in missing and not retry:
            continue
        cands = candidates(url)
        if cands:
            todo.append((url, cands))
    print(f'{len(todo)} linked network pages are not in the snapshot; fetching their text twins')

    def get(item):
        url, cands = item
        for c in cands:
            body = f.get(c)
            if body:
                return url, c, body
        return url, None, None

    got = 0
    with ThreadPoolExecutor(8) as ex:
        for url, src, body in ex.map(get, todo):
            if body and credential_in(body):
                missing[url] = REFUSED
                continue
            if body and norm(src) not in have:
                path = urlparse(src).path
                local = os.path.join(OUT, urlparse(src).netloc, path.lstrip('/'))
                if os.path.isdir(local):          # a folder already sits where the file would go
                    missing[url] = 'path is a folder in the snapshot'
                    continue
                f.save(urlparse(src).netloc, src, body)
                f.manifest[src]['via'] = 'fetch_missing: linked from the site, not in the day\'s snapshot'
                have.add(norm(src))
                missing.pop(url, None)
                got += 1
            elif not body:
                missing[url] = 'no text twin (' + ', '.join(urlparse(c).path for c in cands) + ')'
    json.dump(dict(sorted(f.manifest.items())), open(os.path.join(OUT, 'manifest.json'), 'w'), indent=1)
    json.dump(dict(sorted(missing.items())), open(MISSING, 'w'), indent=1)
    print(f'fetched {got} pages at {time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())}; '
          f'{len(missing)} links have no text twin (cached in {os.path.relpath(MISSING, ROOT)})')
    return got


if __name__ == '__main__':
    main()

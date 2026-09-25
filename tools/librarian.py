#!/usr/bin/env python3
"""The Librarian's computed files: data/index.json and data/vaults.json, from the snapshot.

    python3 tools/librarian.py

Every page on every site, by site, type and date where the sources give one; and every vault sgit.ai
publishes, with its read key where the vault's own page publishes one on purpose. Deterministic,
standard library only. The desks' judgement (changes, concepts, loose ends) is written by hand;
this file is only what can be computed.
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'sources')

TYPES = [  # first match wins; tested against the path under sources/sites/<site>/
    (r'(^|/)llms(-full)?\.txt$', 'other'),
    (r'(^|/)docs/briefs/|(^|/)briefs?(/|\.md$)', 'brief'),
    (r'(^|/)partnerships?/', 'partnership'),
    (r'(^|/)demos/vaults/', 'vault'),
    (r'business-(case|plan)|(^|/)startups/business-plans', 'business plan'),
    (r'(^|/)articles?(/|-)|(^|/)article-', 'article'),
    (r'(^|/)(versions|updates|changelog)(/|\.md$)|(^|/)admin/versions', 'update'),
    (r'(^|/)(abp|policy|policies|privacy|terms|licen[cs]e)[^/]*(\.md$|/)|behaviour-policy', 'policy'),
    (r'(^|/)(docs|method|spec|guides?)/', 'doc'),
]


def live_url(url):
    host = re.match(r'https?://([^/]+)', url).group(1)
    return url[:-3] + '.html' if host in ('sgit.ai', 'riskmandate.ai') and url.endswith('.md') else url


def title_of(path, fallback):
    try:
        text = open(path, encoding='utf-8', errors='replace').read(20000)
    except OSError:
        return fallback
    m = re.search(r'^\s{0,3}#\s+(.+?)\s*#*\s*$', text, re.M)
    t = m.group(1).strip() if m else fallback
    t = re.sub(r'[*_`]', '', re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t))
    return re.sub(r',\s*(sgit\.ai|RiskMandate\.ai)$', '', t)[:200]


def main():
    manifest = json.load(open(os.path.join(SRC, 'sites', 'manifest.json')))
    # dates the sources give: sgit.ai's new-pages list, riskmandate.ai's version record, and bylines
    dates = {}
    for ln in open(os.path.join(SRC, 'history', 'sgit.ai-new-pages-since-2026-09-18.md'), encoding='utf-8'):
        m = re.match(r'^\|\s*(\d{4}-\d{2}-\d{2})\s*\|.*`([^`]+)`\s*\|', ln)
        if m:
            dates.setdefault(m.group(2), m.group(1))
    for ln in open(os.path.join(SRC, 'sites', 'riskmandate.ai', 'versions.md'), encoding='utf-8'):
        m = re.match(r'^- \*\*v([\d.]+)\*\* · (\d{4}-\d{2}-\d{2})', ln)
        if m:
            dates.setdefault(f'sites/riskmandate.ai/versions/{m.group(1)}.md', m.group(2))

    index = []
    for url, m in sorted(manifest.items()):
        local = m['file']
        sub = local.split('/', 2)[2]
        kind = next((t for pat, t in TYPES if re.search(pat, sub)), 'other')
        date = dates.get(local)
        if not date and local.endswith('.md'):
            head = open(os.path.join(SRC, local), encoding='utf-8', errors='replace').read(4000)
            b = re.search(r'^By .{0,120}? · (\d{4}-\d{2}-\d{2}) ·', head, re.M)
            date = b.group(1) if b else None
        index.append({'site': m['site'], 'title': title_of(os.path.join(SRC, local), os.path.basename(local)),
                      'type': kind, 'date': date, 'url': url, 'live': live_url(url), 'local': local,
                      'bytes': m['bytes'], 'sha256': m['sha256']})
    index.sort(key=lambda e: (e['site'] != 'sgit.ai', e['site'], e['local']))

    vaults = []
    for v in json.load(open(os.path.join(SRC, 'vaults', 'published-vaults.json'), encoding='utf-8')):
        page = f'sites/sgit.ai/demos/vaults/{v["slug"]}/index.md'
        key = None
        if os.path.exists(os.path.join(SRC, page)):
            text = open(os.path.join(SRC, page), encoding='utf-8').read()
            k = re.search(r'sgit_public_read_[0-9a-f]{16,}(?::|%3A)' + re.escape(v['vault_id']), text)
            key = k.group(0).replace('%3A', ':') if k else None
        seed = v['slug'] if os.path.isdir(os.path.join(SRC, 'vaults', v['slug'])) else None
        vaults.append({'slug': v['slug'], 'name': v['name'], 'vault_id': v['vault_id'], 'category': v.get('category'),
                       'what': v.get('what'), 'published': v.get('published'), 'size': v.get('size'),
                       'files': v.get('files'), 'live': f'https://sgit.ai/demos/vaults/{v["slug"]}/index.html',
                       'local': page if os.path.exists(os.path.join(SRC, page)) else None,
                       'read_key': key, 'seed': seed})
    vaults.sort(key=lambda v: (v['published'] or '', v['slug']), reverse=True)

    # the network: which site links to which, counted from the links in every snapshotted file
    sites = sorted({m['site'] for m in manifest.values()})
    def in_net(host):
        return host in sites or host.endswith('.sgit.ai') or host in ('sgit.ai', 'riskmandate.ai')
    counts, pages = {}, {}
    for url, m in manifest.items():
        text = open(os.path.join(SRC, m['file']), encoding='utf-8', errors='replace').read()
        for host in set(re.findall(r'https?://([a-z0-9.-]+\.[a-z]{2,})', text.lower())):
            base = '.'.join(host.split('.')[-3:]) if host.endswith('.sgit.ai') and host.count('.') > 2 and host.split('.')[-3] in (
                'providers', 'newsroom') else host
            if host != m['site'] and in_net(host):
                key = (m['site'], host)
                counts[key] = counts.get(key, 0) + 1
    network = {'about': 'Site-to-site links in the snapshot: for each pair, the number of files on the first site that link to the second. '
                        'Computed by tools/librarian.py from sources/sites/; the Cartographer maps it.',
               'sites': [{'site': st, 'files': sum(1 for m in manifest.values() if m['site'] == st),
                          'bytes': sum(m['bytes'] for m in manifest.values() if m['site'] == st)} for st in sites],
               'links': [{'from': a, 'to': b, 'files': n} for (a, b), n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))]}

    os.makedirs(os.path.join(ROOT, 'data'), exist_ok=True)
    with open(os.path.join(ROOT, 'data', 'network.json'), 'w', encoding='utf-8') as f:
        json.dump(network, f, indent=1, ensure_ascii=False)
        f.write('\n')
    with open(os.path.join(ROOT, 'data', 'index.json'), 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=1, ensure_ascii=False)
        f.write('\n')
    with open(os.path.join(ROOT, 'data', 'vaults.json'), 'w', encoding='utf-8') as f:
        json.dump(vaults, f, indent=1, ensure_ascii=False)
        f.write('\n')
    by_type = {}
    for e in index:
        by_type[e['type']] = by_type.get(e['type'], 0) + 1
    print(f'index: {len(index)} pages, {len({e["site"] for e in index})} sites, '
          f'{sum(1 for e in index if e["date"])} dated; by type {dict(sorted(by_type.items()))}')
    print(f'network: {len(network["sites"])} sites, {len(network["links"])} site-to-site links')
    print(f'vaults: {len(vaults)}, {sum(1 for v in vaults if v["read_key"])} with a read key published on their page')


if __name__ == '__main__':
    main()

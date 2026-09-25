#!/usr/bin/env python3
"""The gate: must pass before every commit, and before every release.

    python3 tools/validate.py

Fails on:
  1. a broken relative link or asset reference in any page the build rendered;
  2. an external script or stylesheet (or any external src) anywhere in site/;
  3. a fetch( in a script of any rendered page (the seed's vault apps are named exceptions below);
  4. a credential-shaped string anywhere in the repository or the site (house rules, brief/06);
  5. a rendered page without a provenance block, or without its .md twin;
  6. an em-dash, or a model identifier, in anything a desk wrote.
Standard library only.
"""
import os
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.environ.get('NEWSROOM_SITE_OUT') or os.path.join(ROOT, 'site')
GENERATOR = 'content="sgit-newsroom build"'

# --- secrets --------------------------------------------------------------------------------------
# A prefix followed by key material. The bare prefixes are named in prose all over the network
# ("never publish a sgit_private_vault_... key"), and naming a prefix is not leaking a key.
SECRET_PATTERNS = [
    ('sgit private key', re.compile(r'sgit_private_(?:[a-z]+)_[A-Za-z0-9][A-Za-z0-9._~-]{7,}')),
    ('sgit private key (short form)', re.compile(r'sgit_private_(?![a-z]+_)[A-Za-z0-9]{12,}')),
    ('legacy vault key', re.compile(r'sgit_vk1_[A-Za-z0-9][A-Za-z0-9._~-]{7,}')),
    ('vault-key-shaped string', re.compile(r'(?<![A-Za-z0-9_])[a-z0-9]{24}:[a-z0-9]{4,24}(?![a-z0-9])')),
    ('AWS access key id', re.compile(r'AKIA[0-9A-Z]{16}')),
    ('API key', re.compile(r'(?<![A-Za-z0-9])sk-(?:ant|or|proj)-[A-Za-z0-9_-]{20,}')),
]
# Read keys a source site publishes on purpose may be quoted; they are removed before scanning.
PUBLISHED_READ_KEY = re.compile(r'sgit_public_read_[0-9a-f]{16,}(?::|%3A)[a-z0-9]{4,24}')
# Documented example credentials that sources quote. A short, named list: never a weaker pattern.
ALLOWED_EXAMPLES = {
    'AKIAIOSFODNN7EXAMPLE': "AWS's documented example key id, quoted by sg-compute.sgit.ai's security audit",
    'AKIAXXXXXXXXXXXXXXXX': "a placeholder in the same audit's redaction example (sg-compute.sgit.ai)",
    'AKIANEWKEY1234567890': "a made-up rotated key in the same audit's redaction example (sg-compute.sgit.ai)",
}

# --- fetch() exceptions ---------------------------------------------------------------------------
# The seed's vault apps are copied as published. This one tries fetch('content.json') and falls
# back to the data inlined in the page, so it still works from file://.
FETCH_EXCEPTIONS = {
    'src/vaults/agent-webmaster/index.html': 'falls back to its inlined content when fetch fails',
}

DESK_DIRS = ('editions', 'stories', 'history', 'signals', 'maps', 'data', 'runs', 'agents', 'issues', 'briefings')
COMPUTED = ('data/index.json', 'data/vaults.json')      # titles as the sources wrote them: not desk prose
# words the principles ban in a desk's own prose (brief/07-principles.md); a quotation is allowed
BANNED_WORDS = re.compile(r'\b(rungs?)\b', re.I)
QUOTED = re.compile(r'"[^"\n]*"|\u201c[^\u201d\n]*\u201d|\*\*[^*\n]+\*\*|\*[^*\n]+\*|`[^`\n]+`')
PROSE_DIRS = ('editions', 'stories', 'history', 'signals', 'maps', 'briefings')
MODEL_ID = re.compile(r'\b(?:claude|gpt|gemini|llama|mistral)-[a-z0-9.]*\d[a-z0-9.-]*\b|\b(?:opus|sonnet|haiku) \d', re.I)

errors = []


def fail(where, what):
    errors.append(f'{where}: {what}')


def text_files(base, skip=()):
    for dirpath, dirs, files in os.walk(base):
        dirs[:] = sorted(d for d in dirs if d not in ('.git', '__pycache__') and os.path.join(dirpath, d) not in skip)
        for name in sorted(files):
            if name.lower().endswith(('.webp', '.png', '.jpg', '.jpeg', '.gif', '.ico', '.zip', '.pdf')):
                continue
            yield os.path.join(dirpath, name)


def scan_secrets(path, text):
    clean = PUBLISHED_READ_KEY.sub('', text)
    for label, pat in SECRET_PATTERNS:
        for m in pat.finditer(clean):
            if m.group(0) in ALLOWED_EXAMPLES:
                continue
            line = clean.count('\n', 0, m.start()) + 1
            fail(f'{os.path.relpath(path, ROOT)}:{line}', f'{label}: refused ({m.group(0)[:14]}...)')


def check_site():
    if not os.path.isdir(SITE):
        fail('site/', 'missing: run python3 tools/build.py')
        return 0
    pages = 0
    for path in text_files(SITE):
        rel = os.path.relpath(path, SITE).replace(os.sep, '/')
        text = open(path, encoding='utf-8', errors='replace').read()
        scan_secrets(path, text)
        if not rel.endswith('.html'):
            continue
        rendered = GENERATOR in text[:2000]
        # external resources: nothing may load from anywhere else, rendered page or copied app
        for m in re.finditer(r'<(script|link|img|iframe|source|video|audio|embed)\b[^>]*?\b(src|href)\s*=\s*["\']([^"\']+)', text, re.I):
            tag, attr, url = m.group(1).lower(), m.group(2).lower(), m.group(3)
            if tag == 'link' and not re.search(r'rel\s*=\s*["\']?(stylesheet|preload|modulepreload|icon)', m.group(0), re.I):
                continue
            if re.match(r'^(https?:)?//', url):
                fail(f'site/{rel}', f'external {tag} {attr}: {url}')
        if re.search(r'@import\s+url\(\s*["\']?(https?:)?//', text):
            fail(f'site/{rel}', 'external @import in a stylesheet')
        for script in re.findall(r'<script\b[^>]*>(.*?)</script>', text, re.S | re.I):
            if re.search(r'\bfetch\s*\(', script) and rel not in FETCH_EXCEPTIONS:
                fail(f'site/{rel}', 'fetch( in a script: browsers block it on file://')
        if not rendered:
            continue
        pages += 1
        if 'class="provenance"' not in text:
            fail(f'site/{rel}', 'no provenance block')
        # the .md twin: a desk page's twin sits beside it; a source page's twin is its raw file
        base = rel[:-5]
        if not (os.path.exists(os.path.join(SITE, base + '.md')) or os.path.exists(os.path.join(SITE, base))):
            fail(f'site/{rel}', 'no .md twin')
        # every relative link and asset must exist
        here = os.path.dirname(path)
        for m in re.finditer(r'\b(?:href|src)\s*=\s*"([^"]*)"', text):
            url = m.group(1)
            if not url or re.match(r'^([a-z][a-z0-9+.-]*:|//|#)', url, re.I):
                continue
            target = unquote(url.split('#')[0].split('?')[0])
            if not target:
                continue
            full = os.path.normpath(os.path.join(here, target))
            if not full.startswith(SITE) or not os.path.exists(full):
                fail(f'site/{rel}', f'broken link: {url}')
    return pages


def check_repo():
    tracked = subprocess.run(['git', 'ls-files', '-z'], cwd=ROOT, capture_output=True, text=True)
    files = [os.path.join(ROOT, f) for f in tracked.stdout.split('\0') if f] if tracked.returncode == 0 else []
    # desk files and the snapshot are scanned whether or not they are tracked yet
    extra = [p for d in DESK_DIRS + ('sources',) if os.path.isdir(os.path.join(ROOT, d)) for p in text_files(os.path.join(ROOT, d))]
    seen = set()
    for path in files + extra:
        if path in seen or path.startswith(SITE + os.sep) or not os.path.isfile(path):
            continue
        seen.add(path)
        if path.lower().endswith(('.webp', '.png', '.jpg', '.jpeg', '.gif', '.ico', '.zip', '.pdf')):
            continue
        text = open(path, encoding='utf-8', errors='replace').read()
        scan_secrets(path, text)
        rel = os.path.relpath(path, ROOT)
        if rel.split(os.sep)[0] in DESK_DIRS and rel.replace(os.sep, '/') not in COMPUTED:
            for n, line in enumerate(text.split('\n'), 1):
                if '—' in line:
                    fail(f'{rel}:{n}', 'em-dash in a desk file (house style)')
                if MODEL_ID.search(line):
                    fail(f'{rel}:{n}', f'model identifier in a desk file: {MODEL_ID.search(line).group(0)}')
                if rel.split(os.sep)[0] in PROSE_DIRS and BANNED_WORDS.search(QUOTED.sub('', line)) and not line.lstrip().startswith(('title:', '#')):
                    fail(f'{rel}:{n}', f'a word the principles ban, outside a quotation: "{BANNED_WORDS.search(QUOTED.sub("", line)).group(0)}" (brief/07-principles.md: say level or step)')
    return len(seen)


def check_agents():
    """agents/ is rendered from data/agents.json, and every run record stays inside its agent's mandate."""
    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    import agents
    for p in agents.check():
        fail('agents', p)
    problems, n = agents.check_runs()
    for p in problems:
        fail('runs', p)
    return n


def check_issues():
    """issues-fs-lite: every issue has created and priority; a parent names an issue that exists."""
    stems, items = set(), []
    for status in ('open', 'blocked', 'done'):
        d = os.path.join(ROOT, 'issues', status)
        if not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d)):
            if name.endswith('.md'):
                if not re.match(r'^\d{3}-[a-z0-9-]+\.md$', name):
                    fail(f'issues/{status}/{name}', 'name must be NNN-kebab-slug.md')
                stems.add(name[:-3])
                text = open(os.path.join(d, name), encoding='utf-8').read()
                fm = text.split('\n---', 1)[0] if text.startswith('---\n') else ''
                items.append((f'issues/{status}/{name}', fm))
    for where, fm in items:
        for field in ('created', 'priority'):
            if not re.search(rf'^{field}:\s*\S', fm, re.M):
                fail(where, f'no "{field}" in the front matter (issues-fs-lite requires it)')
        m = re.search(r'^parent:\s*(\S+)', fm, re.M)
        if m and m.group(1) not in stems:
            fail(where, f'parent {m.group(1)} is not an issue')
    return len(items)


TWIN_TYPES = {'Evidence', 'Fact', 'Statement', 'Observation', 'Idea', 'Hypothesis', 'Question', 'Comment'}
TWIN_RELS = {'supports', 'contradicts', 'cites', 'asks_about', 'answers', 'follows', 'leads_to'}


def check_twins():
    """<piece>.json beside a desk file: types, relations, edges that name real nodes, sources on Evidence and Fact."""
    import json
    n = 0
    for d in ('stories', 'editions', 'history', 'signals', 'maps'):
        base = os.path.join(ROOT, d)
        if not os.path.isdir(base):
            continue
        for name in sorted(os.listdir(base)):
            if not name.endswith('.json'):
                continue
            n += 1
            where = f'{d}/{name}'
            try:
                g = json.load(open(os.path.join(base, name), encoding='utf-8'))
            except ValueError as e:
                fail(where, f'not JSON: {e}'); continue
            if not os.path.exists(os.path.join(base, name[:-5] + '.md')):
                fail(where, 'no piece beside it (a twin needs its .md)')
            ids = set()
            for node in g.get('nodes', []):
                ids.add(node.get('id'))
                if node.get('type') not in TWIN_TYPES:
                    fail(where, f'node {node.get("id")}: type {node.get("type")!r} is not one of {sorted(TWIN_TYPES)}')
                if node.get('type') in ('Evidence', 'Fact') and not node.get('source'):
                    fail(where, f'node {node.get("id")}: an {node.get("type")} names its source')
            for e in g.get('edges', []):
                if e.get('rel') not in TWIN_RELS:
                    fail(where, f'edge {e.get("from")}->{e.get("to")}: rel {e.get("rel")!r} is not one of {sorted(TWIN_RELS)}')
                if e.get('from') not in ids or e.get('to') not in ids:
                    fail(where, f'edge {e.get("from")}->{e.get("to")} names a node that does not exist')
    return n


def main():
    pages = check_site()
    twins = check_twins()
    issues = check_issues()
    files = check_repo()
    runs = check_agents()
    if errors:
        for e in errors:
            print('FAIL', e)
        print(f'validate: {len(errors)} failures')
        sys.exit(1)
    print(f'validate: ok ({pages} rendered pages checked for links, provenance and twins; '
          f'{files} repository files and all of site/ scanned for credentials; {runs} run records within their mandates; {issues} issues well formed; {twins} semantic twins checked)')


if __name__ == '__main__':
    main()

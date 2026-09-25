#!/usr/bin/env python3
"""Build site/ from the snapshot and the desks' files. Standard library only, deterministic.

    python3 tools/build.py

Reads sources/ (the frozen snapshot), data/, editions/, stories/, history/, signals/ and writes
site/: static HTML that works from file:// with the network off. Relative links only, no external
resources, no fetch(). Every rendered page carries a provenance block and has a .md twin.
"""
import csv
import hashlib
import html
import io
import json
import os
import posixpath
import re
import shutil
import sys
import unicodedata
from urllib.parse import urljoin, urlparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mdlite  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'sources')
# NEWSROOM_SITE_OUT: build somewhere else (desks running in parallel each build their own copy to check it)
OUT = os.environ.get('NEWSROOM_SITE_OUT') or os.path.join(ROOT, 'site')
VERSION = open(os.path.join(ROOT, 'version.txt')).read().strip()
DOMAIN = 'sgit.newsroom.sgit.ai'
GENERATOR = '<meta name="generator" content="sgit-newsroom build">'
RENDER_LIMIT = 400_000          # json/csv/code bigger than this are linked raw, not rendered
SNAPSHOT_TAKEN = '2026-09-24'
READING_SINCE = '2026-09-18'
# an inline icon: the browser asks for /favicon.ico otherwise, and gets a 404 from a plain server
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' "
           "rx='6' fill='%231f4fd1'/%3E%3Ctext x='16' y='23' font-family='Georgia,serif' font-size='20' font-weight='700' "
           "fill='white' text-anchor='middle'%3Es%3C/text%3E%3C/svg%3E")
ICON = {
    'star': '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true"><path d="M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8L3.5 9.7l5.9-.9z"/></svg>',
    'up': '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 15l6-6 6 6"/></svg>',
    'down': '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>',
    'note': '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20h4L19 9l-4-4L4 16v4z"/></svg>',
    'mic': '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg>',
    'search': '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>',
    'copy': '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V6a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h2"/></svg>',
    'check': '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg>',
}

esc = html.escape


def rp(path):
    return os.path.join(ROOT, path)


def read(path):
    with open(path, encoding='utf-8', errors='replace') as f:
        return f.read()


def load_json(path, default):
    p = rp(path)
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else default


def sha256_file(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def rel(from_page, to_path):
    """A relative link from one page of the site to another path of the site."""
    if to_path.startswith(('http://', 'https://', '#', 'mailto:')):
        return to_path
    frag = ''
    if '#' in to_path:
        to_path, frag = to_path.split('#', 1)
        frag = '#' + frag
    r = posixpath.relpath(to_path, posixpath.dirname(from_page) or '.')
    return r + frag


def norm_url(url):
    """A key under which the .html and .md forms of one page, and its folder form, all meet."""
    p = urlparse(url)
    path = re.sub(r'/+', '/', p.path or '/')
    path = re.sub(r'(^|/)index\.(html|md)$', r'\1', path)
    path = re.sub(r'\.(html|md)$', '', path)
    return (p.netloc.lower() + path.rstrip('/')).lower()


def live_url(url):
    """The page a reader would open: sgit.ai and riskmandate.ai serve each .md twin's page as .html."""
    host = urlparse(url).netloc
    if host in ('sgit.ai', 'riskmandate.ai') and url.endswith('.md'):
        return url[:-3] + '.html'
    return url


def title_of(text, fallback):
    m = re.search(r'^\s{0,3}#\s+(.+?)\s*#*\s*$', text, re.M)
    t = m.group(1).strip() if m else fallback
    t = re.sub(r'[*_`]', '', re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t))
    return t[:200]


# ======================================================================== the snapshot catalogue
class Source:
    """One file under sources/: where it came from, and where the site renders it."""

    def __init__(self, path, meta=None):
        self.path = path                                    # relative to sources/
        self.abs = os.path.join(SRC, path)
        self.ext = os.path.splitext(path)[1].lower()
        parts = path.split('/')
        self.group = parts[0]                               # sites, history, cli-briefs, vaults
        self.site = parts[1] if self.group == 'sites' and len(parts) > 2 else None
        self.url = meta['url'] if meta else None
        self.fetched = meta['fetched'] if meta else None
        self.via = meta.get('via') if meta else None
        self.sha = meta['sha256'] if meta else sha256_file(self.abs)
        self.bytes = os.path.getsize(self.abs)
        self.raw = 'src/' + path                            # the file itself, copied beside its page
        self.split = None                                   # llms-full sections
        self.date = None
        if self.ext == '.md':
            self.page = 'src/' + path[:-3] + '.html'
        elif self.ext in ('.html', '.svg', '.webp', '.png', '.jpg'):
            self.page = None
        elif self.ext in ('.json', '.csv', '.py', '.jsonl', '.txt') and (
                self.bytes <= RENDER_LIMIT or path.endswith('.txt') or path == 'sites/manifest.json'):
            self.page = 'src/' + path + '.html'
        else:
            self.page = None
        self.text = read(self.abs) if self.page else ''
        self.title = self.make_title()

    def make_title(self):
        base = os.path.basename(self.path)
        if self.ext == '.md':
            t = title_of(self.text, base)
            return re.sub(r',\s*(sgit\.ai|RiskMandate\.ai)$', '', t)
        if base.startswith('llms'):
            return f'{self.site or ""} {base}'.strip()
        return base

    @property
    def is_markdown(self):
        return self.ext == '.md' or (self.ext == '.txt' and os.path.basename(self.path).startswith('llms'))

    @property
    def link(self):
        """The page to send a reader to: the rendered page, else the raw file."""
        return self.page or self.raw


class Catalogue:

    def __init__(self):
        manifest = json.load(open(os.path.join(SRC, 'sites', 'manifest.json')))
        by_file = {m['file']: dict(m, url=u) for u, m in manifest.items()}
        self.sources = {}
        for dirpath, dirs, files in os.walk(SRC):
            dirs.sort()
            for name in sorted(files):
                p = os.path.relpath(os.path.join(dirpath, name), SRC).replace(os.sep, '/')
                if p == 'sites/manifest.json':
                    meta = None
                else:
                    meta = by_file.get(p)
                self.sources[p] = Source(p, meta)
        self.by_url = {}
        for s in self.sources.values():
            if s.url:
                self.by_url.setdefault(norm_url(s.url), s)
        pages = [s.page for s in self.sources.values() if s.page]
        assert len(pages) == len(set(pages)), 'two sources render to one page'
        raws = {s.raw for s in self.sources.values()}
        assert not (raws & set(pages)), 'a rendered page would overwrite a raw file'

    def find_url(self, url):
        return self.by_url.get(norm_url(url))

    def sites(self):
        out = {}
        for s in self.sources.values():
            if s.site:
                out.setdefault(s.site, []).append(s)
        return dict(sorted(out.items()))


# ======================================================================== page frame
DEFAULT_SECTIONS = [('index.html', 'Front page'), ('news/index.html', 'News'), ('history/index.html', 'Perspective'),
                    ('maps/index.html', 'Maps'), ('reading-room/index.html', 'Reading room'), ('library/index.html', 'Index'),
                    ('signals/index.html', 'Signals'), ('loose-ends/index.html', 'Loose ends'), ('vaults/index.html', 'Vaults'),
                    ('newsroom/index.html', 'The newsroom'), ('admin/index.html', 'Admin'), ('search/index.html', 'Search')]
NAV = [('index.html', 'Front page'), ('editions/index.html', 'Editions'), ('reading-room/index.html', 'Reading room'),
       ('library/index.html', 'Index'), ('concepts/index.html', 'Concepts'), ('vaults/index.html', 'Vaults'),
       ('history/index.html', 'History'), ('signals/index.html', 'Signals'), ('loose-ends/index.html', 'Loose ends'),
       ('newsroom/index.html', 'The newsroom'), ('about/index.html', 'About'), ('search/index.html', 'Search')]


class Site:

    def __init__(self):
        self.cat = Catalogue()
        self.written = {}
        self.search = []            # (title, page, site, kind, text)
        self.unresolved = []
        self.editions = []
        self.stories = []
        self.signals = []
        self.history = []
        self.maps = []
        self.changes = {}
        secs = load_json('data/sections.json', None)
        self.nav = [(x['href'], x['title']) for x in secs['sections']] if secs else DEFAULT_SECTIONS
        self.network = load_json('data/network.json', {'sites': [], 'links': []})
        self.agents = load_json('data/agents.json', {'agents': []})['agents']
        self.runs = []
        self.releases = load_json('data/releases.json', {'releases': []})['releases']
        self.shots = load_json('assets/shots/manifest.json', {})
        self.concepts = load_json('data/concepts.json', [])
        self.loose = load_json('data/loose-ends.json', [])
        self.index = load_json('data/index.json', [])
        self.vaults = load_json('data/vaults.json', [])

    # ------------------------------------------------------------------ writing
    def write(self, path, content, binary=False):
        assert path not in self.written, f'written twice: {path}'
        self.written[path] = True
        full = os.path.join(OUT, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, 'wb') as f:
            f.write(content if binary else content.encode('utf-8'))

    def page(self, path, title, body, provenance, md=None, eyebrow='', search_text=None, kind='page', site=None,
             toc=None, wide=False):
        here = path.split('/')[0]
        nav = ''.join(f'<a href="{rel(path, p)}"{" class=on" if p == path or (p != "index.html" and p.split("/")[0] == here) else ""}>'
                      f'{esc(t)}</a>' for p, t in self.nav)
        css = rel(path, 'assets/style.css')
        twin = None
        if md is not None:
            twin = path[:-5] + '.md' if path.endswith('.html') else path + '.md'
            self.write(twin, md)
        toc_html = ''
        if toc and len(toc) > 3:
            items = ''.join(f'<li class="l{lv}"><a href="#{hid}">{esc(t)}</a></li>' for lv, t, hid in toc if lv <= 3)
            toc_html = f'<details class="toc"><summary>On this page</summary><ul>{items}</ul></details>'
        twin_link = f' · <a href="{rel(path, twin)}">.md twin</a>' if twin else ''
        diagram_js = (f'<script src="{rel(path, "assets/mermaid.min.js")}"></script>\n<script src="{rel(path, "assets/diagrams.js")}"></script>\n'
                      if 'class="mermaid"' in body else '')
        doc = f'''<!doctype html>
<html lang="en-GB" data-version="{esc(VERSION)}" data-root="{rel(path, 'index.html')[:-10] or './'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{GENERATOR}
<title>{esc(title)} · sgit newsroom</title>
<link rel="stylesheet" href="{css}">
<link rel="icon" href="{FAVICON}">
</head>
<body>
<header class="top"><a class="brand" href="{rel(path, 'index.html')}">sgit <em>newsroom</em></a>
<span class="ver">{esc(VERSION)} · snapshot {SNAPSHOT_TAKEN}</span>
<nav>{nav}</nav>
<div class="views" data-views hidden><span class="lbl">View</span><button type="button" data-view="editor" class="on">Editor's</button><button type="button" data-view="mine">Mine</button><a class="views-read" href="{rel(path, 'feedback/read.html')}" data-read-count></a></div></header>
<main{' class="wide"' if wide else ''}>
{f'<p class="eyebrow">{eyebrow}</p>' if eyebrow else ''}
{toc_html}
{body}
{provenance}
</main>
<footer><p>sgit newsroom {esc(VERSION)} · a static site built from a frozen, hashed snapshot of the sgit network · works offline{twin_link} · <a href="{rel(path, 'llms.txt')}">llms.txt</a></p></footer>
<script src="{rel(path, 'assets/feedback.js')}"></script>
<script src="{rel(path, 'assets/panel.js')}"></script>
{diagram_js}</body>
</html>
'''
        self.write(path, doc)
        text = search_text if search_text is not None else re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', body))
        self.search.append((title, path, site or '', kind, html.unescape(text)[:600]))

    # ------------------------------------------------------------------ links
    def resolver(self, page_path, base_url=None, base_file=None):
        """How links on one page resolve: into the snapshot where the snapshot has the page."""

        def target(href):
            href = href.strip()
            if href.startswith('nr:'):
                t = href[3:].strip('/')
                frag = ''
                if '#' in t:
                    t, frag = t.split('#', 1)
                    frag = '#' + frag
                if not t.endswith('.html'):
                    t = t + '/index.html' if t in ('loose-ends', 'signals', 'editions', 'history', 'stories',
                                                   'concepts', 'vaults', 'library', 'reading-room', 'newsroom',
                                                   'about', 'search') or not t else t + '.html'
                return ('local', t + frag, None)
            if href.startswith('src:'):
                p = href[4:].lstrip('/')
                frag = ''
                if '#' in p:
                    p, frag = p.split('#', 1)
                    frag = '#' + frag
                s = self.cat.sources.get(p)
                if not s:
                    self.unresolved.append((page_path, href))
                    return ('broken', href, None)
                return ('local', s.link + frag, s.url and live_url(s.url))
            if href.startswith(('mailto:', '#')):
                return ('as-is', href, None)
            if href.startswith('//'):
                href = 'https:' + href
            if not href.startswith(('http://', 'https://')):
                if base_url:
                    href = urljoin(base_url, href)
                elif base_file:
                    p = posixpath.normpath(posixpath.join(posixpath.dirname(base_file), href.split('#')[0]))
                    frag = '#' + href.split('#', 1)[1] if '#' in href else ''
                    s = self.cat.sources.get(p)
                    if s:
                        return ('local', s.link + frag, None)
                    return ('dead', href, None)
                else:
                    self.unresolved.append((page_path, href))
                    return ('broken', href, None)
            s = self.cat.find_url(href)
            frag = '#' + href.split('#', 1)[1] if '#' in href else ''
            if s:
                return ('local', s.link + frag, live_url(href.split('#')[0]) + frag)
            return ('external', href, None)

        def link(href, inner):
            kind, where, live = target(href)
            if kind == 'local':
                a = f'<a href="{esc(rel(page_path, where))}">{inner}</a>'
                if live:
                    a += f'<a class="ext live" href="{esc(live)}" title="live page">↗</a>'
                return a
            if kind == 'external':
                return f'<a class="ext" href="{esc(where)}">{inner} ↗</a>'
            if kind == 'as-is':
                return f'<a href="{esc(where)}">{inner}</a>'
            return f'<span class="dead" title="not in the snapshot: {esc(where)}">{inner}</span>'

        def image(src, alt):
            if src.startswith(('http://', 'https://', '//', 'data:')):
                return None
            if base_file:
                p = posixpath.normpath(posixpath.join(posixpath.dirname(base_file), src))
                s = self.cat.sources.get(p)
                if s:
                    return f'<img src="{esc(rel(page_path, s.raw))}" alt="{esc(alt)}" loading="lazy">'
            return None

        return link, image, target

    def md(self, text, page_path, base_url=None, base_file=None):
        link, image, _ = self.resolver(page_path, base_url, base_file)
        r = mdlite.Renderer(link, image)
        return r.render(text), r.headings

    # ------------------------------------------------------------------ provenance
    def prov_source(self, s, section=None):
        rows = [('Site', esc(s.site or s.group)),
                ('Live URL', f'<a class="ext" href="{esc(live_url(s.url))}">{esc(live_url(s.url))} ↗</a>'
                 if s.url else 'none: this file exists only in the seed pack'),
                ('Fetched from', esc(s.url) if s.url and live_url(s.url) != s.url else None),
                ('Fetched', esc(s.fetched) if s.fetched else f'in the seed pack of {SNAPSHOT_TAKEN}'),
                ('sha256', f'<code title="{s.sha}">{s.sha[:12]}</code>'),
                ('Frozen copy', f'<a href="{{raw}}">{esc(s.path)}</a> ({s.bytes:,} bytes)'),
                ('Section', esc(section) if section else None),
                ('Brought home', esc(s.via) if s.via else None),
                ('Desk', 'Librarian (reading room): rendered as fetched, not edited')]
        return rows

    def prov_block(self, page_path, rows):
        out = []
        for k, v in rows:
            if v is None:
                continue
            out.append(f'<dt>{k}</dt><dd>{v}</dd>')
        return f'<aside class="provenance" id="provenance"><h2>Provenance</h2><dl>{"".join(out)}</dl></aside>'

    def prov_desk(self, page_path, desk, date=None, sources=(), reviewed=None, extra=()):
        rows = [('Desk', esc(desk))]
        if date:
            rows.append(('Date', esc(date)))
        for k, v in extra:
            rows.append((k, v))
        if sources is not None:
            items = []
            _, _, target = self.resolver(page_path)
            for u in sources:
                kind, where, live = target(u)
                s = self.cat.find_url(u) if u.startswith('http') else self.cat.sources.get(u[4:]) if u.startswith(
                    'src:') else None
                if kind == 'local' and s:
                    items.append(f'<li><a href="{esc(rel(page_path, where))}">{esc(s.title)}</a> '
                                 f'<code>{s.sha[:12]}</code> {esc(s.site or s.group)}'
                                 + (f' <a class="ext" href="{esc(live)}">↗</a>' if live else '') + '</li>')
                elif kind == 'local':
                    items.append(f'<li><a href="{esc(rel(page_path, where))}">{esc(u)}</a></li>')
                else:
                    items.append(f'<li><a class="ext" href="{esc(u)}">{esc(u)} ↗</a> (not in the snapshot)</li>')
            rows.append(('Sources', f'<ul>{"".join(items)}</ul>' if items else 'computed from the snapshot and the desks\' data files'))
        if reviewed is not None:
            by, on = reviewed
            rows.append(('Editor of record', f'reviewed by {esc(by)} on {esc(on)}' if by else
                         '<strong class="unreviewed">not yet reviewed</strong>'))
        rows.append(('Snapshot', f'<a href="{rel(page_path, "src/sites/manifest.json.html")}">manifest</a> of {SNAPSHOT_TAKEN}, sha256 per file'))
        return self.prov_block(page_path, rows)

    # ================================================================== the reading room
    def build_sources(self):
        for s in self.cat.sources.values():
            self.write(s.raw, open(s.abs, 'rb').read(), binary=True)
        for s in self.cat.sources.values():
            if not s.page:
                continue
            base = os.path.basename(s.path)
            if base == 'llms-full.txt':
                self.build_llms_full(s)
            elif s.path == 'history/sgit.ai-version-log.json':
                self.build_version_log(s)
            elif s.path == 'history/sgit.ai-new-pages-since-2026-09-18.md':
                self.build_new_pages_page(s)
            else:
                self.build_source_page(s)

    def source_body(self, s):
        if s.is_markdown:
            return self.md(s.text, s.page, base_url=self.link_base(s), base_file=s.path)
        if s.ext == '.csv':
            rows = list(csv.reader(io.StringIO(s.text)))
            if rows:
                head = ''.join(f'<th>{esc(c)}</th>' for c in rows[0])
                body = ''.join('<tr>' + ''.join(f'<td>{esc(c)}</td>' for c in r) + '</tr>' for r in rows[1:])
                return f'<div class="table"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>', []
        text = s.text
        if s.ext == '.json':
            try:
                text = json.dumps(json.loads(s.text), indent=2, ensure_ascii=False)
            except ValueError:
                pass
        return f'<pre class="raw"><code>{esc(text)}</code></pre>', []

    @staticmethod
    def link_base(s):
        """The URL a source's relative links are written against. riskmandate.ai's release notes are
        shown inside /versions.html, so their links are relative to the site root, not /versions/."""
        if s.url and re.match(r'https://riskmandate\.ai/versions/[^/]+\.md$', s.url):
            return 'https://riskmandate.ai/versions.html'
        return s.url

    def build_source_page(self, s):
        body, heads = self.source_body(s)
        prov = self.prov_block(s.page, [(k, v.replace('{raw}', esc(rel(s.page, s.raw))) if v else v)
                                        for k, v in self.prov_source(s)])
        crumbs = self.crumbs(s) + self.fb_bar(s)
        eyebrow = f'Reading room · {esc(s.site or s.group)}'
        badge = (f'<div class="src-badge"><span class="src-dot"></span><span><strong>From {esc(s.site or s.group)}</strong>'
                 + (f', the page as fetched on {esc(s.fetched[:10])}' if s.fetched else ', a file in the seed pack') +
                 (f' · <a class="ext" href="{esc(live_url(s.url))}">open the live page ↗</a>' if s.url else '') +
                 '</span><span class="src-what">Everything on this sheet is the source site\'s own text; the newsroom\'s chrome is outside it.</span></div>')
        self.page(s.page, s.title, crumbs + '<article class="source">' + badge + body + '</article>', prov,
                  eyebrow=eyebrow, kind='source', site=s.site or s.group, toc=heads,
                  search_text=s.title + ' ' + ' '.join(h[1] for h in heads[:12]) + ' ' +
                  re.sub(r'\s+', ' ', re.sub(r'[#*`>|\[\]()_-]', ' ', s.text[:1200])))

    def crumbs(self, s, extra=''):
        start = 'reading-room/index.html'
        where = f'reading-room/{s.site}.html' if s.site else start
        label = s.site or s.group
        live = f' · <a class="ext" href="{esc(live_url(s.url))}">live ↗</a>' if s.url else ''
        return (f'<p class="crumbs"><a href="{rel(s.page, start)}">Reading room</a> / '
                f'<a href="{rel(s.page, where)}">{esc(label)}</a>{extra} · '
                f'<a href="{rel(s.page, s.raw)}">raw text</a>{live}</p>')

    def split_sections(self, text):
        lines = text.split('\n')
        fence = False
        marks = {1: [], 2: []}
        for i, ln in enumerate(lines):
            if re.match(r'^\s{0,3}(```|~~~)', ln):
                fence = not fence
            if fence:
                continue
            m = re.match(r'^(#{1,2})\s+\S', ln)
            if m:
                marks[len(m.group(1))].append(i)
        cuts = marks[1] if len(marks[1]) >= 3 else sorted(marks[1] + marks[2]) if len(marks[1] + marks[2]) >= 3 else []
        if not cuts:
            return None
        sections = []
        if cuts[0] > 0 and '\n'.join(lines[:cuts[0]]).strip():
            sections.append(('Preamble', '\n'.join(lines[:cuts[0]])))
        for a, b in zip(cuts, cuts[1:] + [len(lines)]):
            chunk = '\n'.join(lines[a:b])
            sections.append((title_of(chunk, f'Section {len(sections) + 1}'), chunk))
        return sections

    def build_llms_full(self, s):
        sections = self.split_sections(s.text)
        if not sections:
            return self.build_source_page(s)
        folder = s.page[:-len('llms-full.txt.html')] + 'llms-full/'
        # ASCII file names: macOS decomposes accented names, which breaks file:// links after a clone
        ascii_slug = lambda t: re.sub(r'-+', '-', re.sub(r'[^a-z0-9-]', '', unicodedata.normalize('NFKD', mdlite.slugify(t))
                                                         .encode('ascii', 'ignore').decode())).strip('-')[:40] or 'section'
        pages = [f'{folder}{n + 1:03d}-{ascii_slug(t)}.html' for n, (t, _) in enumerate(sections)]
        prov_rows = self.prov_source(s)
        items = ''.join(f'<li><a href="{rel(s.page, p)}">{esc(t)}</a> <span class="muted">'
                        f'{len(c):,} chars</span></li>' for p, (t, c) in zip(pages, sections))
        body = (self.crumbs(s) + f'<h1>{esc(s.site)}: everything, in {len(sections)} sections</h1>'
                f'<p>The site\'s <code>llms-full.txt</code> ({s.bytes:,} bytes) is split here on its headings so it '
                f'reads as pages, not one scroll. The frozen file is unchanged: <a href="{rel(s.page, s.raw)}">raw text</a>.</p>'
                f'<ol class="sections">{items}</ol>')
        self.page(s.page, f'{s.site} llms-full.txt', body,
                  self.prov_block(s.page, [(k, v.replace('{raw}', esc(rel(s.page, s.raw))) if v else v) for k, v in prov_rows]),
                  eyebrow=f'Reading room · {esc(s.site)}', kind='source', site=s.site,
                  search_text=f'{s.site} llms-full ' + ' '.join(t for t, _ in sections[:80]))
        for n, ((t, chunk), p) in enumerate(zip(sections, pages)):
            html_body, heads = self.md(chunk, p, base_url=s.url, base_file=s.path)
            self.write(p[:-5] + '.md', chunk)
            prev_ = f'<a href="{rel(p, pages[n - 1])}">← {esc(sections[n - 1][0][:60])}</a>' if n else ''
            next_ = f'<a href="{rel(p, pages[n + 1])}">{esc(sections[n + 1][0][:60])} →</a>' if n + 1 < len(pages) else ''
            pager = f'<nav class="pager"><span>{prev_}</span><a href="{rel(p, s.page)}">all sections</a><span>{next_}</span></nav>'
            prov = self.prov_block(p, [(k, v.replace('{raw}', esc(rel(p, s.raw))) if v else v)
                                       for k, v in self.prov_source(s, section=f'{n + 1} of {len(sections)}: {t}')])
            crumbs = (f'<p class="crumbs"><a href="{rel(p, "reading-room/index.html")}">Reading room</a> / '
                      f'<a href="{rel(p, f"reading-room/{s.site}.html")}">{esc(s.site)}</a> / '
                      f'<a href="{rel(p, s.page)}">llms-full.txt</a> · section {n + 1} of {len(sections)}</p>')
            self.page(p, t if s.site in t else f'{t} ({s.site})', crumbs + pager + '<article class="source">' + html_body + '</article>' + pager,
                      prov, eyebrow=f'Reading room · {esc(s.site)} · llms-full', kind='source', site=s.site, toc=heads,
                      search_text=t + ' ' + re.sub(r'\s+', ' ', re.sub(r'[#*`>|\[\]()_-]', ' ', chunk[:900])))

    def build_version_log(self, s):
        entries = json.loads(s.text)
        link, _, _ = self.resolver(s.page)
        rows = []
        for e in entries:
            vid = 'v' + e['version'].lstrip('v')
            rows.append(f'<tr id="{esc(vid)}"><td class="nowrap"><strong>{esc(e["version"])}</strong><br>'
                        f'<span class="muted">{esc(e["date"])}</span><br><span class="muted">{esc(e.get("git", ""))}</span></td>'
                        f'<td>{esc(e["notes"])}</td></tr>')
        body = (self.crumbs(s) + f'<h1>sgit.ai version log</h1><p>Every sgit.ai release since v0.1.1, newest first: '
                f'{len(entries)} entries. The notes record what went wrong and how it was caught.</p>'
                f'<div class="table"><table class="log"><thead><tr><th>Release</th><th>Note</th></tr></thead>'
                f'<tbody>{"".join(rows)}</tbody></table></div>')
        prov = self.prov_block(s.page, [(k, v.replace('{raw}', esc(rel(s.page, s.raw))) if v else v)
                                        for k, v in self.prov_source(s)])
        self.page(s.page, 'sgit.ai version log', body, prov, eyebrow='Reading room · history', kind='source',
                  site='history', search_text='sgit.ai version log releases ' + ' '.join(e['version'] for e in entries))

    # ------------------------------------------------------------------ the reading list (with local feedback)
    def date_of(self, path):
        if not hasattr(self, '_dates'):
            self._dates = {e['local']: e.get('date') for e in self.index}
        return self._dates.get(path) or ''

    @staticmethod
    def section_of(s):
        parts = s.path.split('/')
        if s.group != 'sites':
            return s.group
        sub = parts[2:-1]
        if sub[:2] == ['docs', 'briefs']:
            return 'briefs'
        if sub[:2] == ['demos', 'vaults']:
            return 'vaults'
        return sub[0] if sub else 'home'

    def fb_bar(self, s):
        return self.fb_bar_piece(s.path, s.sha[:12], s.title, s.site or s.group, self.section_of(s), self.date_of(s.path), s.link)

    def fb_bar_piece(self, id_, sha, title, site, section, date, page):
        """The feedback bar on a piece or a source page: hidden until feedback.js runs, so nothing is dead without it."""
        return (f'<div class="fb-bar" data-fb hidden data-id="{esc(id_)}" data-sha="{esc(sha)}" data-title="{esc(title)}" '
                f'data-site="{esc(site)}" data-section="{esc(section)}" data-date="{esc(date)}" '
                f'data-page="{esc(page)}">'
                f'<span class="lbl">Your feedback</span>'
                f'<button type="button" class="btn-s" data-a="read" aria-pressed="false">{ICON["check"]}<span> Mark as read</span></button>'
                f'<button type="button" class="ib" data-a="star" aria-label="Star" aria-pressed="false">{ICON["star"]}</button>'
                f'<button type="button" class="ib" data-a="up" aria-label="Useful" aria-pressed="false">{ICON["up"]}</button>'
                f'<button type="button" class="ib" data-a="down" aria-label="Not useful" aria-pressed="false">{ICON["down"]}</button>'
                f'<button type="button" class="btn-s" data-a="note" aria-pressed="false">{ICON["note"]} Note</button>'
                f'<button type="button" class="btn-s memo" data-a="memo">{ICON["mic"]}<span> Voice memo</span></button>'
                f'<span class="changed" data-f="changed" hidden>the page changed since your note</span>'
                f'<span class="sp"></span><span class="muted small" data-f="memo-status"></span>'
                f'<div class="fb-note" hidden><label>Your note, kept on this device only'
                f'<textarea rows="3" placeholder="A question, a follow-up, who should see this..."></textarea></label></div></div>')

    def reading_list(self):
        """Every change since READING_SINCE that a reader should see: sgit.ai's new pages (with the commit
        time), riskmandate.ai's releases, and the CLI briefs. Newest first."""
        times = {}
        for ln in read(os.path.join(SRC, 'history', 'sgit.ai-git-log.txt')).split('\n'):
            m = re.match(r'^(\w{7,})\s+(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2})', ln)
            if m:
                times[m.group(1)[:8]] = m.group(3)
        items = []
        for n in self.new_pages():
            s = self.cat.sources.get(n['local'])
            if not s or n['date'] < READING_SINCE:
                continue
            items.append(dict(s=s, date=n['date'], time=times.get(n['commit'][:8], ''), site='sgit.ai',
                              section=self.section_of(s), title=re.sub(r',\s*sgit\.ai$', '', n['title']), live=n['live']))
        for ln in self.cat.sources['sites/riskmandate.ai/versions.md'].text.split('\n'):
            m = re.match(r'^- \*\*v([\d.]+)\*\* · (\d{4}-\d{2}-\d{2}) \S (.+)$', ln)
            s = m and self.cat.sources.get(f'sites/riskmandate.ai/versions/{m.group(1)}.md')
            if s and m.group(2) >= READING_SINCE:
                items.append(dict(s=s, date=m.group(2), time='', site='riskmandate.ai', section='versions',
                                  title=f'v{m.group(1)}: {m.group(3).strip()}', live=live_url(s.url)))
        for r in self.releases:
            if r['date'] >= READING_SINCE:
                items.append(dict(s=None, date=r['date'], time=r.get('time', ''), site='sgit.newsroom.sgit.ai', section='releases',
                                  title=f'{r["version"]}: {r["title"]}', live='', page=f'admin/versions.html#{r["version"]}', sha=r.get('commit', '')[:12],
                                  id_=f'releases/{r["version"]}'))
        for p, s in sorted(self.cat.sources.items()):
            m = re.match(r'cli-briefs/(\d{2})/(\d{2})/', p)
            if m and s.page and f'2026-{m.group(1)}-{m.group(2)}' >= READING_SINCE:
                items.append(dict(s=s, date=f'2026-{m.group(1)}-{m.group(2)}', time='', site='CLI briefs', section='briefs',
                                  title=s.title, live=''))
        items.sort(key=lambda x: (x['date'], x['time'] or '00:00', x['title']), reverse=True)
        return items

    def reading_list_html(self, P, items):
        import datetime
        cls = {'sgit.ai': 's-sgit', 'riskmandate.ai': 's-rm'}
        days = {}
        for it in items:
            days.setdefault(it['date'], []).append(it)
        sites = sorted({it['site'] for it in items}, key=lambda x: (x != 'sgit.ai', x))
        sections = {}
        for it in items:
            sections[it['section']] = sections.get(it['section'], 0) + 1
        chip = lambda attr, k, label, n='': (f'<button type="button" {attr}="{esc(k)}" aria-pressed="{"true" if k == "all" else "false"}"'
                                             f'{" class=on" if k == "all" else ""}>{esc(label)}{f"<span class=c>{n}</span>" if n != "" else ""}</button>')
        tabs = ''.join(f'<button type="button" data-status="{k}" aria-pressed="{"true" if k == "all" else "false"}"{" class=on" if k == "all" else ""}>'
                       f'{label}<span class="c" data-count="{k}">{len(items) if k in ("all", "unread") else 0}</span></button>'
                       for k, label in (('all', 'All'), ('unread', 'Unread'), ('starred', 'Starred'), ('noted', 'Noted'), ('voted', 'Voted')))
        site_chips = (chip('data-site-f', 'all', 'All') if len(sites) > 1 else '') + ''.join(
            chip('data-site-f', x, x, sum(1 for it in items if it['site'] == x)) for x in sites) if len(sites) > 1 else ''
        sec_chips = chip('data-section-f', 'all', 'All') + ''.join(
            chip('data-section-f', k, k, n) for k, n in sorted(sections.items(), key=lambda kv: (-kv[1], kv[0])))
        out = [f'<section class="rl" data-rl><div class="rl-filters"><div class="rl-top">'
               f'<label class="rl-search">{ICON["search"]}<input type="search" data-q placeholder="Filter titles: vault, brief, partnership..." '
               f'aria-label="Filter titles"></label><div class="rl-tabs" role="group" aria-label="Status">{tabs}</div></div>'
               f'<div class="rl-chiprow">'
               + (f'<div class="rl-chips" role="group" aria-label="Site"><span class="lbl">Site</span>{site_chips}</div>' if site_chips else '')
               + f'<div class="rl-chips" role="group" aria-label="Section"><span class="lbl">Section</span>{sec_chips}</div></div></div>'
               f'<div class="rl-body"><div class="rl-list"><p class="rl-shown">Showing <b data-shown>{len(items)}</b> of {len(items)} · '
               f'grouped by day, newest first</p>']
        for date in sorted(days, reverse=True):
            label = datetime.date.fromisoformat(date).strftime('%A %d %B').replace(' 0', ' ')
            out.append(f'<section class="rl-day"><h3>{label} <span class="rl-n">{len(days[date])} items</span></h3><ol class="rl-rows">')
            for it in days[date]:
                s = it['s']
                if s is None:                      # one of this newsroom's own releases
                    out.append(
                        f'<li class="rl-row" data-id="{esc(it["id_"])}" data-sha="{esc(it["sha"])}" data-title="{esc(it["title"])}" '
                        f'data-site="{esc(it["site"])}" data-section="{esc(it["section"])}" data-date="{date}" data-time="{it["time"]}" '
                        f'data-live="" data-page="{esc(it["page"])}">'
                        f'<span class="rl-dot" aria-hidden="true"></span><span class="rl-time">{it["time"]}</span>'
                        f'<div class="rl-main"><a class="rl-title" href="{esc(rel(P, it["page"]))}">{esc(it["title"])}</a>'
                        f'<div class="rl-meta"><span class="rl-site s-nr">{esc(it["site"])}</span>'
                        f'<span>{esc(it["section"])}</span><span class="only-narrow">{it["time"]}</span><span class="rl-flags"></span></div></div>'
                        f'<div class="rl-acts"><button type="button" class="ib" data-act="star" aria-label="Star" aria-pressed="false">{ICON["star"]}</button>'
                        f'<button type="button" class="ib" data-act="up" aria-label="Useful" aria-pressed="false">{ICON["up"]}</button>'
                        f'<button type="button" class="ib" data-act="down" aria-label="Not useful" aria-pressed="false">{ICON["down"]}</button>'
                        f'<button type="button" class="ib" data-act="open" aria-label="Notes and details">{ICON["note"]}</button></div></li>')
                    continue
                out.append(
                    f'<li class="rl-row" data-id="{esc(s.path)}" data-sha="{s.sha[:12]}" data-title="{esc(it["title"])}" '
                    f'data-site="{esc(it["site"])}" data-section="{esc(it["section"])}" data-date="{date}" data-time="{it["time"]}" '
                    f'data-live="{esc(it["live"])}" data-page="{esc(s.link)}">'
                    f'<span class="rl-dot" aria-hidden="true"></span><span class="rl-time">{it["time"]}</span>'
                    f'<div class="rl-main"><a class="rl-title" href="{esc(rel(P, s.link))}">{esc(it["title"])}</a>'
                    f'<div class="rl-meta"><span class="rl-site {cls.get(it["site"], "")}">{esc(it["site"])}</span>'
                    f'<span>{esc(it["section"])}</span><span class="only-narrow">{it["time"]}</span><span class="rl-flags"></span></div></div>'
                    f'<div class="rl-acts"><button type="button" class="ib" data-act="star" aria-label="Star" aria-pressed="false">{ICON["star"]}</button>'
                    f'<button type="button" class="ib" data-act="up" aria-label="Useful" aria-pressed="false">{ICON["up"]}</button>'
                    f'<button type="button" class="ib" data-act="down" aria-label="Not useful" aria-pressed="false">{ICON["down"]}</button>'
                    f'<button type="button" class="ib" data-act="open" aria-label="Notes and details">{ICON["note"]}</button></div></li>')
            out.append('</ol></section>')
        out.append('<p class="rl-empty" hidden>Nothing matches these filters. <button type="button" class="linkbtn" data-reset>Clear filters</button></p></div>')
        out.append(
            '<aside class="rl-side"><section class="rl-sel empty" data-sel aria-label="Selected item">'
            '<p class="rl-hint">Select an item to mark it, vote, write a note or record a voice memo. Everything stays in this browser.</p>'
            '<div class="ttl" data-f="title"></div><div class="mt" data-f="meta"></div>'
            '<div class="row2"><a class="btn-p" data-f="local" href="#">Read the local copy</a><a class="btn-s ext" data-f="live" href="#">Live ↗</a></div>'
            f'<div class="row2"><button type="button" class="btn-s grow" data-a="read">Mark read</button>'
            f'<button type="button" class="btn-s" data-a="star" aria-label="Star">{ICON["star"]}</button>'
            '<button type="button" class="btn-s" data-a="up">Useful</button><button type="button" class="btn-s" data-a="down">Not</button></div>'
            '<label>Your note (this device only)<textarea rows="4" placeholder="What should happen with this? A question, a follow-up, who should see it..."></textarea></label>'
            f'<button type="button" class="btn-s memo" data-a="memo">{ICON["mic"]}<span> Record a voice memo</span></button>'
            '<span class="muted small" data-f="memo-status"></span><ul class="memos" data-memos></ul>'
            '<div class="row2 only-narrow"><button type="button" class="btn-s grow" data-a="close">Close</button>'
            '<button type="button" class="btn-p" data-a="next">Next unread</button></div></section>'
            '<section class="rl-dev" data-dev aria-label="Feedback on this device">'
            f'<div class="mini"><div><b><span data-stat="pending">0</span> changes on this device</b>local only, never sent</div>'
            f'<button type="button" class="copy" data-d="copy">Copy for Claude</button><button type="button" class="ghost" data-d="more" aria-label="More">More</button></div>'
            '<div class="eb"><span>On this device</span><span data-stat="device"></span></div>'
            '<div class="stats"><div><b data-stat="read">0</b><span>read</span></div><div><b data-stat="starred">0</b><span>starred</span></div>'
            '<div><b data-stat="votes">0</b><span>votes</span></div><div><b data-stat="notes">0</b><span>notes</span></div></div>'
            '<p class="note"><span data-stat="pending">0</span> changes since your last copy · kept in this browser\'s local storage, never sent anywhere</p>'
            f'<button type="button" class="copy" data-d="copy">{ICON["copy"]} Copy for Claude</button>'
            '<div class="row2"><button type="button" class="ghost" data-d="download">Download .md</button>'
            '<button type="button" class="ghost" data-d="copy-all">Copy all</button><button type="button" class="ghost" data-d="paste">Paste to merge</button></div>'
            '<div class="rl-merge" hidden><textarea rows="4" placeholder="Paste feedback copied on another device"></textarea>'
            '<button type="button" class="ghost" data-d="merge">Merge</button></div>'
            '<p class="status" data-f="dev-status" aria-live="polite"></p><pre data-preview></pre>'
            '<button type="button" class="ghost only-narrow" data-d="more">Close</button></section></aside></div></section>')
        return ''.join(out)

    def build_new_pages_page(self, s):
        """The new-pages list as a reading list (sgit.ai only), with the table as published below it."""
        P = s.page
        items = [it for it in self.reading_list() if it['site'] == 'sgit.ai' and it['s'] is not None]
        body, _ = self.source_body(s)
        html_ = (self.crumbs(s) + f'<h1>What was published on sgit.ai since 18 September</h1>'
                 f'<p class="lede">{len(items)} new pages, newest first, with the time of the commit that published each. Filter, mark and note '
                 f'them here; the table exactly as published is at the bottom.</p>' + self.reading_list_html(P, items)
                 + '<details><summary>The table as published</summary><article class="source">' + body + '</article></details>')
        prov = self.prov_block(P, [(k, v.replace('{raw}', esc(rel(P, s.raw))) if v else v) for k, v in self.prov_source(s)])
        self.page(P, s.title, html_, prov, eyebrow='Reading room · history', kind='source', site='history', wide=True,
                  search_text=s.title + ' ' + ' '.join(it['title'] for it in items))

    # ------------------------------------------------------------------ reading-room index
    def new_pages(self):
        s = self.cat.sources['history/sgit.ai-new-pages-since-2026-09-18.md']
        out = []
        for ln in s.text.split('\n'):
            m = re.match(r'^\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*(\w+)\s*\|\s*(.+?)\s*\|\s*(\S+)\s*\|\s*`([^`]+)`\s*\|', ln)
            if m:
                out.append(dict(date=m.group(1), commit=m.group(2), title=m.group(3), live=m.group(4), local=m.group(5)))
        return out

    def build_reading_room(self):
        P = 'reading-room/index.html'
        new = self.new_pages()
        items = self.reading_list()
        new_html = (f'<h2 id="new">1. What changed since 18 September ({len(items)} items)</h2>'
                    f'<p>New pages on sgit.ai (from <a href="{rel(P, self.cat.sources["history/sgit.ai-new-pages-since-2026-09-18.md"].page)}">'
                    f'the new-pages list</a>), riskmandate.ai releases and the CLI briefs, newest first. Mark what you have read, vote, star and '
                    f'add notes: it stays in this browser until you copy it out.</p>' + self.reading_list_html(P, items))

        # 2. the business plans
        plans = []
        for v in sorted(d for d in os.listdir(os.path.join(SRC, 'vaults')) if os.path.isdir(os.path.join(SRC, 'vaults', d))):
            files = sorted(p for p in self.cat.sources if p.startswith(f'vaults/{v}/'))
            readme = self.cat.sources.get(f'vaults/{v}/README.md')
            name = readme.title if readme else v
            app = f'vaults/{v}/index.html'
            groups = {}
            for p in files:
                sub = p.split('/')[2] if p.count('/') > 2 else ''
                groups.setdefault(sub, []).append(self.cat.sources[p])
            parts = []
            for sub in ('', 'plan', 'spec', 'prototypes', 'risk', 'journal', 'player', 'sample', 'mockups', 'diagrams', 'tools'):
                if sub not in groups:
                    continue
                links = ', '.join(f'<a href="{rel(P, x.link)}">{esc(os.path.basename(x.path) if sub else x.title if x.ext == ".md" else os.path.basename(x.path))}</a>'
                                  for x in groups.pop(sub))
                parts.append(f'<li><strong>{esc(sub or "top")}</strong>: {links}</li>')
            for sub, xs in sorted(groups.items()):
                parts.append(f'<li><strong>{esc(sub)}</strong>: ' + ', '.join(
                    f'<a href="{rel(P, x.link)}">{esc(os.path.basename(x.path))}</a>' for x in xs) + '</li>')
            start = self.cat.sources.get(f'vaults/{v}/plan/00-START-HERE.md')
            plans.append(f'<section class="card"><h3>{esc(name)}</h3><p>'
                         f'<a class="btn" href="{rel(P, "vaults/app/" + v + ".html")}">Open the plan\'s app</a> '
                         + (f'<a class="btn" href="{rel(P, start.page)}">Read plan/00-START-HERE</a>' if start else '')
                         + f'</p><ul class="files">{"".join(parts)}</ul></section>')
        pv = self.cat.sources['vaults/published-vaults.json']
        plans_html = (f'<h2 id="plans">2. The business plans (five vaults)</h2><p>Each vault\'s <code>index.html</code> '
                      f'is the plan\'s own app, with its data inlined; it opens offline. The list of all vaults sgit.ai '
                      f'publishes is on the <a href="{rel(P, "vaults/index.html")}">vaults page</a> '
                      f'(<a href="{rel(P, pv.link)}">published-vaults.json</a>).</p>' + ''.join(plans))

        # 3. the briefs
        briefs = [s for p, s in self.cat.sources.items() if p.startswith('cli-briefs/')]
        briefs += [s for p, s in self.cat.sources.items() if p.startswith('sites/sgit.ai/docs/briefs/')]
        briefs += [s for p, s in self.cat.sources.items() if re.match(r'sites/[^/]+/(briefs?)(/|\.md)', p) and not p.startswith('sites/sgit.ai/docs/')]
        items = ''.join(f'<li><a href="{rel(P, s.link)}">{esc(s.title)}</a> <span class="muted">'
                        f'{esc(s.site or "sgit CLI repo, " + "/".join(s.path.split("/")[1:3]))}</span></li>' for s in briefs)
        briefs_html = f'<h2 id="briefs">3. The briefs ({len(briefs)})</h2><ul class="list">{items}</ul>'

        # 4. history
        hist = [s for p, s in self.cat.sources.items() if p.startswith('history/')]
        hist_html = '<h2 id="history">4. The week\'s history files</h2><ul class="list">' + ''.join(
            f'<li><a href="{rel(P, s.link)}">{esc(os.path.basename(s.path))}</a></li>' for s in hist) + '</ul>'

        # 5. by site
        sites = self.cat.sites()
        site_rows = ''.join(f'<tr><td><a href="{rel(P, "reading-room/" + k + ".html")}">{esc(k)}</a></td>'
                            f'<td class="num">{len(v)}</td><td class="num">{sum(x.bytes for x in v) // 1024:,} KB</td></tr>'
                            for k, v in sorted(sites.items(), key=lambda kv: -sum(x.bytes for x in kv[1])))
        total = sum(len(v) for v in sites.values())
        sites_html = (f'<h2 id="sites">5. Everything else, by site ({len(sites)} sites, {total} files)</h2>'
                      f'<p>Long <code>llms-full.txt</code> files are split into sections on their headings.</p>'
                      f'<div class="table"><table><thead><tr><th>Site</th><th>Files</th><th>Size</th></tr></thead>'
                      f'<tbody>{site_rows}</tbody></table></div>')
        intro = (f'<h1>The reading room</h1><p class="lede">Every file in the snapshot of {SNAPSHOT_TAKEN}, rendered as a readable '
                 f'page with its provenance. Nothing here needs the network: every link to a snapshotted page stays in the '
                 f'reading room, and the ↗ beside it opens the live page when you are back online.</p>'
                 f'<p>{sum(1 for x in self.cat.sources.values() if x.via)} of the files were brought home after the snapshot, by '
                 f'<code>tools/fetch_missing.py</code>: the .md twins of network pages the site links to. Their provenance block says so, '
                 f'with their own fetch time.</p>'
                 f'<p class="jump"><a href="#new">New since 18 September</a> · <a href="#plans">Business plans</a> · '
                 f'<a href="#briefs">Briefs</a> · <a href="#history">History</a> · <a href="#sites">By site</a></p>')
        md = (f'# The reading room\n\n## New on sgit.ai since 18 September\n\n' +
              '\n'.join(f'- {n["date"]} [{n["title"]}]({n["live"]})' for n in new) +
              '\n\n## Sites\n\n' + '\n'.join(f'- {k}: {len(v)} files' for k, v in sites.items()) + '\n')
        self.page(P, 'The reading room', intro + new_html + plans_html + briefs_html + hist_html + sites_html,
                  self.prov_desk(P, 'Librarian', SNAPSHOT_TAKEN, sources=['src:history/sgit.ai-new-pages-since-2026-09-18.md']),
                  md=md, eyebrow='Librarian', wide=True)
        for site, files in sites.items():
            self.build_site_listing(site, files)

    def build_site_listing(self, site, files):
        P = f'reading-room/{site}.html'
        folders = {}
        for s in sorted(files, key=lambda x: x.path):
            sub = posixpath.dirname(s.path[len(f'sites/{site}/'):]) or '/'
            folders.setdefault(sub, []).append(s)
        parts = []
        for sub, xs in folders.items():
            lis = ''.join(f'<li><a href="{rel(P, x.link)}">{esc(x.title)}</a>' + (f'<a class="ext live" href="{esc(live_url(x.url))}">↗</a>' if x.url else '') +
                          f' <span class="muted">{esc(os.path.basename(x.path))} · {x.bytes // 1024 or 1} KB</span></li>'
                          for x in xs)
            parts.append(f'<h2>{esc(sub)}</h2><ul class="list">{lis}</ul>')
        body = (f'<p class="crumbs"><a href="{rel(P, "reading-room/index.html")}">Reading room</a> / {esc(site)}</p>'
                f'<h1>{esc(site)}</h1><p>{len(files)} files, {sum(x.bytes for x in files) // 1024:,} KB, fetched '
                f'{esc(min(x.fetched for x in files if x.fetched))} to {esc(max(x.fetched for x in files if x.fetched))}. '
                f'<a class="ext" href="https://{esc(site)}/">{esc(site)} ↗</a></p>' + ''.join(parts))
        md = f'# {site}\n\n' + '\n'.join(f'- [{x.title}]({x.url or x.path})' for x in files) + '\n'
        self.page(P, site, body, self.prov_desk(P, 'Librarian', SNAPSHOT_TAKEN, sources=[]), md=md,
                  eyebrow='Reading room', site=site)

    # ================================================================== desks' pages
    def desk_file(self, folder, name):
        text = read(rp(f'{folder}/{name}'))
        meta, body = mdlite.front_matter(text)
        return meta, body, text

    def semantic_twin(self, folder, page):
        """<piece>.json beside <piece>.md: the graph the prose came from, rendered as a diagram and a list by type."""
        jp = rp(f'{folder}/{page.split("/", 1)[1][:-5]}.json')
        if not os.path.exists(jp):
            return ''
        g = json.load(open(jp, encoding='utf-8'))
        colours = {'Evidence': '#e8eefc', 'Fact': '#e8eefc', 'Statement': '#f1ece2', 'Observation': '#f1ece2', 'Idea': '#fdf3e3',
                   'Hypothesis': '#fdf0e6', 'Question': '#fbeadc', 'Comment': '#ece7dd'}
        nid = lambda i: 'n_' + re.sub(r'[^a-zA-Z0-9]', '_', i)
        lines = ['flowchart TD']
        for n in g.get('nodes', []):
            text = re.sub(r'["\[\]{}()|]', '', n.get('text', ''))[:70]
            lines.append(f'  {nid(n["id"])}["{n.get("type", "")}: {text}"]')
            lines.append(f'  style {nid(n["id"])} fill:{colours.get(n.get("type"), "#fff")},stroke:#6b665c,color:#1b1a17')
        for e in g.get('edges', []):
            lines.append(f'  {nid(e["from"])} -->|{e.get("rel", "")}| {nid(e["to"])}')
        diagram, _ = self.md('```mermaid\n' + '\n'.join(lines) + '\n```', page)
        link, _, _ = self.resolver(page)
        by_type = {}
        for n in g.get('nodes', []):
            by_type.setdefault(n.get('type', 'Other'), []).append(n)
        lists = ''.join(f'<h3>{esc(t)} ({len(ns)})</h3><ul>' + ''.join(
            f'<li id="{esc(nid(n["id"]))}">{esc(n.get("text", ""))}' + (f' <span class="small">({link(n["source"], "source")})</span>' if n.get('source') else '') + '</li>'
            for n in ns) + '</ul>' for t, ns in by_type.items())
        self.write(f'{folder}/{page.split("/", 1)[1][:-5]}.json', json.dumps(g, indent=1, ensure_ascii=False))
        return (f'<section class="twin"><h2>The semantic graph behind this piece</h2><p class="muted small">An experiment (issue 029): the desk wrote '
                f'the graph first, {len(g.get("nodes", []))} nodes and {len(g.get("edges", []))} edges, and the prose from it. '
                f'<a href="{rel(page, folder + "/" + page.split("/", 1)[1][:-5] + ".json")}">The JSON twin</a>.</p>{diagram}{lists}</section>')

    def markable_sections(self, html_body, id_prefix, page):
        """Each <h3> and what follows it becomes an item the reader can mark read on its own (a lesson, a decision,
        a question), keyed by the page and the heading's anchor, with the sha of its text."""
        parts = re.split(r'(?=<h3 id=")', html_body)
        out = [parts[0]]
        for part in parts[1:]:
            m = re.match(r'<h3 id="([^"]+)">(.*?)</h3>', part, re.S)
            if not m:
                out.append(part); continue
            hid, title = m.group(1), re.sub(r'<[^>]+>', '', m.group(2))
            sha = hashlib.sha256(re.sub(r'<[^>]+>', '', part).encode('utf-8')).hexdigest()[:12]
            tail = ''
            if '<h2 ' in part:                      # the section ends where the next h2 starts
                part, tail = part.split('<h2 ', 1)
                tail = '<h2 ' + tail
            out.append(f'<section class="rd sec" data-id="{esc(id_prefix)}#{esc(hid)}" data-sha="{sha}" data-title="{esc(title)}" '
                       f'data-site="Historian" data-section="{esc(id_prefix.split("/")[-1][:-3])}" data-date="" data-page="{esc(page)}#{esc(hid)}">'
                       f'<button type="button" class="rd-read" data-a="read" aria-label="Mark this item read">{ICON["check"]}<span> Mark as read</span></button>'
                       + part + '</section>' + tail)
        return ''.join(out)

    def build_desk_page(self, path, meta, body, raw, eyebrow, extra_top='', extra_prov=()):
        html_body, heads = self.md(body, path)
        rb, ro = meta.get('reviewed_by', ''), meta.get('reviewed_on', '')
        srcs = meta.get('sources') or []
        if isinstance(srcs, str):
            srcs = [srcs] if srcs else []
        folder = path.split('/')[0]
        section = meta.get('section') or self.SECTION_OF.get(folder, folder)
        desk = meta.get('desk', '')
        agent = next((a for a in self.agents if a['name'].lower() == desk.lower().split(' (')[0]), None)
        desk_link = f'<a href="{rel(path, "newsroom/agents/" + agent["id"] + ".html")}">{esc(desk)}</a>' if agent else esc(desk)
        mission = f'<p class="byline-mission">{esc(agent["gravity"])}</p>' if agent else ''
        sha = hashlib.sha256(raw.encode('utf-8')).hexdigest()[:12]
        words = len(body.split())
        review = f'reviewed by {esc(rb)} on {esc(ro)}' if rb else '<span class="unrev">not yet reviewed by the editor of record</span>'
        standfirst = meta.get('standfirst') or ''
        byline = (f'<header class="byline"><p class="kicker">{esc(section)} · {esc(meta.get("date", ""))}</p>'
                  f'<h1>{esc(meta.get("title", ""))}</h1>' + (f'<p class="dek">{esc(standfirst)}</p>' if standfirst else '') +
                  f'<div class="byline-who"><div><span class="lbl">Written by</span> {desk_link}, a desk of this newsroom{mission}</div>'
                  f'<div><span class="lbl">On</span> {len(srcs)} sources · {max(1, round(words / 220))} min read · <a href="#provenance">provenance</a></div>'
                  f'<div><span class="lbl">State</span> {review}</div></div></header>')
        fb = self.fb_bar_piece(f'{folder}/{path.split("/", 1)[1][:-5]}.md', sha, meta.get('title', ''), desk, section,
                               meta.get('date', ''), path)
        cards = meta.get('cards') or []
        if isinstance(cards, str):
            cards = [cards]
        if cards:
            link, _, target = self.resolver(path)
            tiles = ''
            for c in cards:
                label, _, val = c.partition(':')
                val = val.strip()
                val_html = esc(val)
                if re.match(r'^(https?://|src:)\S+$', val):
                    short = val.replace('https://', '')
                    val_html = link(val, esc(short if len(short) <= 70 else short[:34] + '\u2026' + short[-30:]))
                m = re.search(r'\((le-\d+|Q-\d+)\)\s*$', val)
                if m:
                    ref = m.group(1)
                    href = rel(path, 'loose-ends/index.html') + '#' + ref if ref.startswith('le-') else rel(path, 'history/open-questions.html') + '#' + mdlite.slugify(ref)
                    val_html = esc(val[:m.start()].strip()) + f' <a href="{href}">{ref}</a>'
                tiles += f'<div class="bcard"><span class="lbl">{esc(label.strip())}</span><span>{val_html}</span></div>'
            fb = f'<div class="bcards">{tiles}</div>' + fb
        twin_html = self.semantic_twin(folder, path)
        shots = ''
        for u in srcs:
            sh = self.shots.get(u.replace('.md', '.html') if u.startswith('http') else u)
            if sh and sh.get('ok') and os.path.exists(rp(sh['file'])):
                src_page = self.cat.find_url(u) if u.startswith('http') else None
                href = rel(path, src_page.link) if src_page else u
                shots += (f'<a class="shot" href="{esc(href)}" title="{esc(u)}"><img src="{esc(rel(path, sh["file"]))}" alt="{esc(u)}" loading="lazy">'
                          f'<span>{esc(urlparse(u).netloc)}{esc(urlparse(u).path[:40])}</span></a>')
        if shots:
            fb = f'<div class="shots"><span class="lbl">The pages this piece is about</span><div class="shot-strip">{shots}</div></div>' + fb
        if re.match(r'^\s*#\s', body):
            html_body = re.sub(r'^<h1[^>]*>.*?</h1>\n?', '', html_body, count=1, flags=re.S)
        if meta.get('markable') == 'sections' or path in ('history/lessons.html', 'history/open-questions.html', 'history/decisions.html'):
            html_body = self.markable_sections(html_body, f'{folder}/{path.split("/", 1)[1][:-5]}.md', path)
        self.page(path, meta.get('title', path), byline + extra_top + fb + '<article class="piece">' + html_body + '</article>' + twin_html,
                  self.prov_desk(path, meta.get('desk', ''), meta.get('date', ''), sources=srcs, reviewed=(rb, ro),
                                 extra=extra_prov),
                  md=raw, eyebrow='', kind='newsroom', toc=heads)

    def load_desks(self):
        for folder, bucket in (('editions', self.editions), ('stories', self.stories), ('signals', self.signals),
                               ('history', self.history), ('maps', self.maps)):
            d = rp(folder)
            if not os.path.isdir(d):
                continue
            for name in sorted(os.listdir(d)):
                if name.endswith('.md'):
                    meta, body, raw = self.desk_file(folder, name)
                    bucket.append((name[:-3], meta, body, raw))
        d = rp('data/changes')
        if os.path.isdir(d):
            for name in sorted(os.listdir(d)):
                if name.endswith('.json'):
                    self.changes[name[:-5]] = json.load(open(os.path.join(d, name), encoding='utf-8'))

    def change_counts(self, date):
        ch = self.changes.get(date, {}).get('changes', [])
        counts = {}
        for c in ch:
            counts.setdefault(c.get('site', '?'), {'release': 0, 'new-page': 0})
            counts[c.get('site', '?')][c.get('kind', 'new-page') if c.get('kind') in ('release', 'new-page') else 'new-page'] += 1
        return counts

    def counts_table(self, P, date):
        counts = self.change_counts(date)
        if not counts:
            return ''
        rows = ''.join(f'<tr><td>{esc(k)}</td><td class="num">{v["release"]}</td><td class="num">{v["new-page"]}</td></tr>'
                       for k, v in sorted(counts.items(), key=lambda kv: -(kv[1]['release'] + kv[1]['new-page'])))
        tot = sum(v['release'] + v['new-page'] for v in counts.values())
        return (f'<div class="counts"><h3>What changed on {esc(date)}: {tot} changes</h3><div class="table"><table><thead><tr><th>Site</th>'
                f'<th>Releases</th><th>New pages</th></tr></thead><tbody>{rows}</tbody></table></div>'
                f'<p class="muted">Computed from <a href="{rel(P, f"library/changes-{date}.html")}">the Librarian\'s changes for the day</a>.</p></div>')

    def build_editions(self):
        eds = sorted(self.editions, key=lambda e: e[0], reverse=True)
        for slug, meta, body, raw in eds:
            P = f'editions/{slug}.html'
            self.build_desk_page(P, meta, body, raw, f'Edition · {esc(slug)}', extra_top=self.counts_table(P, slug))
        P = 'editions/index.html'
        items = ''.join(f'<li><a href="{rel(P, f"editions/{s}.html")}"><strong>{esc(s)}</strong>: {esc(m.get("title", ""))}</a>'
                        f'{"" if m.get("reviewed_by") else " <span class=tag>not yet reviewed</span>"}</li>' for s, m, _, _ in eds)
        body = (f'<h1>Editions</h1><p>One edition per day that had changes, newest first. If nothing changed, nothing is published.</p>'
                f'<ul class="list big">{items or "<li>No editions yet.</li>"}</ul>')
        md = '# Editions\n\n' + '\n'.join(f'- {s}: {m.get("title", "")}' for s, m, _, _ in eds) + '\n'
        self.page(P, 'Editions', body, self.prov_desk(P, 'Journalist', sources=None), md=md, eyebrow='Journalist')

        for slug, meta, body, raw in self.stories:
            self.build_desk_page(f'stories/{slug}.html', meta, body, raw, f'Story · {esc(meta.get("date", ""))}')
        P = 'stories/index.html'
        items = ''.join(f'<li><a href="{rel(P, f"stories/{s}.html")}">{esc(m.get("title", s))}</a> '
                        f'<span class="muted">{esc(m.get("date", ""))}</span></li>' for s, m, _, _ in sorted(self.stories, reverse=True))
        self.page(P, 'Stories', f'<h1>Stories</h1><ul class="list big">{items or "<li>No stories yet.</li>"}</ul>',
                  self.prov_desk(P, 'Journalist', sources=None),
                  md='# Stories\n\n' + '\n'.join(f'- {m.get("title", s)}' for s, m, _, _ in self.stories) + '\n', eyebrow='Journalist')

    # ================================================================== the editor's front page, news, maps, admin
    SECTION_OF = {'editions': 'edition', 'stories': 'news', 'history': 'perspective', 'maps': 'maps', 'signals': 'signal'}

    @staticmethod
    def first_paragraph(body):
        for block in re.split(r'\n\s*\n', body):
            b = block.strip()
            if not b or b[0] in '#-|>`*<!' or re.match(r'^\d+\.', b):
                continue
            b = re.sub(r'!?\[([^\]]*)\]\([^)]*\)', r'\1', b)
            b = re.sub(r'[*_`]', '', re.sub(r'\s+', ' ', b))
            return b if len(b) <= 280 else b[:277].rsplit(' ', 1)[0] + '...'
        return ''

    def buckets(self):
        return {'stories': self.stories, 'editions': self.editions, 'history': self.history, 'maps': self.maps,
                'signals': self.signals}

    def card_data(self, folder, slug, meta, body):
        return dict(ref=f'{folder}/{slug}', path=f'{folder}/{slug}.html', title=meta.get('title', slug),
                    id=f'{folder}/{slug}.md', sha=self.desk_sha(folder, slug), covers=meta.get('covers', ''),
                    standfirst=meta.get('standfirst') or self.first_paragraph(body), date=meta.get('date', ''),
                    desk=meta.get('desk', ''), section=meta.get('section') or self.SECTION_OF[folder],
                    reviewed=bool(meta.get('reviewed_by')))

    def network_card(self):
        return dict(ref='maps/network', path='maps/network.html', title='The network, as its own links draw it', id='maps/network',
                    sha=hashlib.sha256(json.dumps(self.network, sort_keys=True).encode()).hexdigest()[:12], covers='',
                    standfirst=f'{len(self.network["sites"])} sites and {len(self.network["links"])} site-to-site links, counted from '
                               f'every file in the snapshot and drawn fresh on every build.',
                    date=SNAPSHOT_TAKEN, desk='Cartographer (computed)', section='maps', reviewed=False)

    def all_cards(self, folder=None):
        out = []
        for f, bucket in self.buckets().items():
            if folder and f != folder:
                continue
            out += [self.card_data(f, s, m, b) for s, m, b, _ in bucket]
        if folder in (None, 'maps'):
            out.append(self.network_card())
        return sorted(out, key=lambda c: (c['date'], c['ref']), reverse=True)

    def ref_item(self, ref, where='data/frontpage.json'):
        ref = ref.strip().strip('/')
        ref = ref[3:] if ref.startswith('nr:') else ref
        ref = ref[:-5] if ref.endswith('.html') else ref[:-3] if ref.endswith('.md') else ref
        if ref == 'maps/network':
            return self.network_card()
        folder, _, slug = ref.partition('/')
        for s, m, b, _ in self.buckets().get(folder, []):
            if s == slug:
                return self.card_data(folder, s, m, b)
        self.unresolved.append((where, ref))
        return None

    def card(self, P, c, size='m'):
        if not c:
            return ''
        review = '' if c['reviewed'] else ' · <span class="unrev">not yet reviewed</span>'
        dek = f'<p class="dek">{esc(c["standfirst"])}</p>' if c['standfirst'] and size != 's' else ''
        return (f'<article class="card card-{size} rd" {self.card_attrs(c)}><p class="kicker">{esc(c["section"])} · {esc(c["date"])}</p>'
                f'<h3><a href="{esc(rel(P, c["path"]))}">{esc(c["title"])}</a></h3>{dek}'
                f'<p class="by">{esc(c["desk"])}{review}</p></article>')

    def build_front(self):
        """The front page as the editor composes it (data/frontpage.json), in the layout approved on 25 September:
        nameplate, dateline, section band, one review line, the lead with its map and "also in this edition",
        the Historian beside it, signals as a list, the week in editions, card sections, a rail."""
        import datetime
        P = 'index.html'
        fp = load_json('data/frontpage.json', {})
        cards = self.all_cards()
        used = set()

        def pick(ref):
            c = self.ref_item(ref)
            if c:
                used.add(c['ref'])
            return c
        lead = pick(fp['lead']) if fp.get('lead') else next((c for c in cards if c['ref'].startswith(('stories/', 'editions/'))), None)
        if lead:
            used.add(lead['ref'])
        edition_date = fp.get('date') or (max(self.changes) if self.changes else SNAPSHOT_TAKEN)
        long_date = datetime.date.fromisoformat(edition_date).strftime('%A %d %B %Y').replace(' 0', ' ')
        eds = sorted(self.editions, key=lambda e: e[0], reverse=True)
        n_changes = len(self.changes.get(edition_date, {}).get('changes', []))
        ed_today = next((e for e in eds if e[0] == edition_date), None)

        # the lead's map: the editor's choice, else none
        lead_map = ''
        if fp.get('lead_map'):
            m = next((x for x in self.maps if 'maps/' + x[0] == fp['lead_map']), None)
            if m:
                fence = re.search(r'```mermaid\n.*?```', m[2], re.S)
                if fence:
                    html_map, _ = self.md(fence.group(0), P)
                    lead_map = (f'<figure class="lead-map">{html_map}<figcaption>Map · <a href="{rel(P, f"maps/{m[0]}.html")}">'
                                f'{esc(m[1].get("title", ""))}</a>, by the Cartographer</figcaption></figure>')
        # also in this edition: the editor's refs, else the edition's "Also today" headings
        also = []
        for r in fp.get('also', []):
            c = pick(r)
            if c:
                also.append((c['title'], rel(P, c['path']), c['standfirst'], c['id'], c['sha']))
        if not also and ed_today:
            body = ed_today[2]
            block = re.search(r'^## Also today\s*\n(.*?)(?=^## |\Z)', body, re.S | re.M)
            if block:
                for h in re.findall(r'^### (.+)$', block.group(1), re.M):
                    also.append((h.strip(), rel(P, f'editions/{edition_date}.html') + '#' + mdlite.slugify(h.strip()), '', '', ''))
        also_html = ''.join(f'<div class="also-item"><a href="{esc(href)}">{esc(t)}</a>'
                            + (f'<span>{esc(d)}</span>' if d else '') + '</div>' for t, href, d, _, _ in also[:3])

        # the top of the right column: the Historian, then signals
        top = [pick(r) for r in fp.get('top', [])]
        persp = next((c for c in top if c and c['ref'].startswith('history/')), None) or \
            next((c for c in self.all_cards('history') if c['ref'] not in used), None)
        if persp:
            used.add(persp['ref'])
        sigs = [pick(r) for r in fp.get('signals', [])] or [c for c in self.all_cards('signals') if c['ref'] not in used][:4]
        sigs = [c for c in sigs if c]
        used.update(c['ref'] for c in sigs)
        sig_meta = {f'signals/{s}': m for s, m, _, _ in self.signals}
        sig_html = ''.join(
            f'<div class="sig rd" {self.card_attrs(c)}><span class="route">{esc(sig_meta.get(c["ref"], {}).get("from_site", ""))} → '
            f'{esc(sig_meta.get(c["ref"], {}).get("to_site", ""))}</span><a href="{esc(rel(P, c["path"]))}">{esc(c["title"])}</a></div>' for c in sigs)
        persp_html = ''
        if persp:
            more = next((c for c in top if c and c is not persp and c['ref'].startswith('history/')), None)
            persp_html = (f'<section class="persp rd" {self.card_attrs(persp)}><p class="kicker">Perspective · the Historian</p>'
                          f'<h2><a href="{esc(rel(P, persp["path"]))}">{esc(persp["title"])}</a></h2><p class="dek">{esc(persp["standfirst"])}</p>'
                          f'<p class="by">{esc(persp.get("covers") or persp["date"])}{"" if persp["reviewed"] else " · <span class=unrev>unreviewed</span>"}</p>'
                          + (f'<a class="more-link" href="{esc(rel(P, more["path"]))}">{esc(more["title"])} →</a>' if more else '') + '</section>')

        # the week in editions
        week = ''
        for slug, meta, _, _ in eds[:5][::-1]:
            n = len(self.changes.get(slug, {}).get('changes', []))
            mx = max((len(self.changes.get(s, {}).get('changes', [])) for s, _, _, _ in eds[:5]), default=1) or 1
            d = datetime.date.fromisoformat(slug).strftime('%a %d %b').upper().replace(' 0', ' ')
            today = ' today' if slug == edition_date else ''
            week += (f'<a class="ed rd{today}" href="{rel(P, f"editions/{slug}.html")}" data-id="editions/{slug}.md" '
                     f'data-sha="{self.desk_sha("editions", slug)}" data-title="{esc(meta.get("title", ""))}" data-site="Journalist" '
                     f'data-section="edition" data-date="{slug}" data-page="editions/{slug}.html">'
                     f'<span class="ed-d">{d} · {n} changes{" · today" if today else ""}</span><span class="ed-bar"><span style="width:{int(100 * n / mx)}%"></span></span>'
                     f'<span class="ed-t">{esc(meta.get("title", ""))}</span></a>')

        # sections
        sections_cfg = fp.get('sections') or [
            {'title': 'News', 'from': 'stories', 'limit': 6, 'more': 'news/index.html'},
            {'title': 'Perspective', 'from': 'history', 'limit': 4, 'more': 'history/index.html'},
            {'title': 'Maps', 'from': 'maps', 'limit': 3, 'more': 'maps/index.html'},
            {'title': 'Signals', 'from': 'signals', 'limit': 4, 'more': 'signals/index.html'}]
        sec_html = []
        for sc in sections_cfg:
            items = [pick(r) for r in sc['items']] if sc.get('items') else \
                [c for c in self.all_cards(sc.get('from')) if c['ref'] not in used][:sc.get('limit', 4)]
            items = [c for c in items if c]
            if not items:
                continue
            more = f' <a class="more" href="{rel(P, sc["more"])}">all →</a>' if sc.get('more') else ''
            sec_html.append(f'<section class="fp-sec" data-hide-empty><h2>{esc(sc["title"])}{more}</h2>'
                            f'<div class="cards">{"".join(self.card(P, c) for c in items)}</div></section>')

        # the rail
        _, _, target = self.resolver(P)
        briefs = []
        for br in fp.get('briefs', []):
            link = ''
            if br.get('link'):
                kind, where, _ = target(br['link'] if br['link'].startswith(('http', 'src:', 'nr:')) else 'nr:' + br['link'])
                link = f' <a href="{esc(rel(P, where) if kind == "local" else where)}">→</a>'
            briefs.append(f'<li>{esc(br["text"])}{link}</li>')
        recent = [it for it in self.reading_list() if it['s'] is not None][:5]
        reading = ''.join(f'<div class="rr-item rd" data-id="{esc(it["s"].path)}" data-sha="{it["s"].sha[:12]}" data-title="{esc(it["title"])}" '
                          f'data-site="{esc(it["site"])}" data-section="{esc(it["section"])}" data-date="{it["date"]}" data-page="{esc(it["s"].link)}">'
                          f'<span class="t">{it["time"]}</span><div><a href="{rel(P, it["s"].link)}">{esc(it["title"])}</a>'
                          f'<span class="m {"s-sgit" if it["site"] == "sgit.ai" else "s-rm" if it["site"] == "riskmandate.ai" else ""}">{esc(it["site"])} · {esc(it["section"])}</span></div></div>'
                          for it in recent)
        open_le = sum(1 for x in self.loose if x.get('status') == 'open')
        new_sig = sum(1 for s in self.signals if s[1].get('status', 'new') == 'new')
        to_review = sum(1 for c in cards if not c['reviewed'] and c['ref'] != 'maps/network')
        last = {}
        for r in self.runs:
            last.setdefault(r.get('agent'), r)
        names = {a['id']: a['name'] for a in self.agents}
        desks = ''.join(f'<div class="desk-row"><a href="{rel(P, "newsroom/agents/" + a + ".html")}">{esc(names.get(a, a))}</a>'
                        f'<span>{esc(r.get("task", ""))[:60]}</span></div>'
                        for a, r in sorted(last.items(), key=lambda kv: kv[1].get('when', ''), reverse=True)[:5])
        rail = (f'<aside class="fp-rail">'
                + (f'<section><h3>In brief</h3><ul class="briefs">{"".join(briefs)}</ul></section>' if briefs else '')
                + f'<section><h3>New in the reading room <a class="more" href="{rel(P, "reading-room/index.html")}">{len(self.reading_list())} →</a></h3>{reading}</section>'
                f'<section><h3>Open</h3><div class="open-tiles"><a href="{rel(P, "loose-ends/index.html")}"><b>{open_le}</b><span>loose ends</span></a>'
                f'<a href="{rel(P, "signals/index.html")}"><b>{new_sig}</b><span>new signals</span></a>'
                f'<a class="warm" href="{rel(P, "admin/index.html")}#queue"><b>{to_review}</b><span>to review</span></a></div></section>'
                f'<section><h3>The desks today <a class="more" href="{rel(P, "newsroom/runs.html")}">runs →</a></h3>{desks}</section></aside>')

        lead_html = ''
        if lead:
            review = '' if lead['reviewed'] else '<span class="unrev">unreviewed</span>'
            lead_html = (f'<article class="lead-story rd" {self.card_attrs(lead)}><p class="kicker">Lead · {esc(lead["section"])} · {esc(lead["date"])}</p>'
                         f'<h2><a href="{esc(rel(P, lead["path"]))}">{esc(lead["title"])}</a></h2>'
                         f'<p class="dek">{esc(lead["standfirst"])}</p><p class="by">{esc(lead["desk"])} · {self.read_time(lead)} {review}</p>{lead_map}'
                         + (f'<div class="also"><p class="kicker">Also in this edition</p><div class="also-grid">{also_html}</div></div>' if also_html else '')
                         + '</article>')
        nav_band = ''.join(f'<a href="{rel(P, p)}">{esc(t)}</a>' for p, t in self.nav if p not in ('index.html', 'search/index.html', 'admin/index.html', 'newsroom/index.html'))
        body = (f'<header class="masthead"><h1>The sgit newsroom</h1>'
                f'<div class="dateline"><span>{esc(long_date)}</span><span>The sgit network, read every day</span>'
                f'<span>Edition {len(eds)} · {n_changes} changes</span></div>'
                f'<nav class="band" aria-label="Sections">{nav_band}</nav></header>'
                f'<p class="review-line"><strong>Written by the desks, not yet signed.</strong> The editor of record has reviewed '
                f'{sum(1 for c in cards if c["reviewed"])} of {to_review + sum(1 for c in cards if c["reviewed"])} pieces; every page says so. '
                f'<a href="{rel(P, "admin/index.html")}#queue">Review queue →</a></p>'
                f'<div class="fp-top">{lead_html}<aside class="fp-side">{persp_html}'
                f'<section class="sigs" data-hide-empty><h3>Signals between projects <a class="more" href="{rel(P, "signals/index.html")}">{len(self.signals)} →</a></h3>{sig_html}</section></aside></div>'
                f'<section class="week"><h2>The week in editions <a class="more" href="{rel(P, "editions/index.html")}">all editions →</a></h2><div class="eds">{week}</div></section>'
                f'<div class="fp-body"><div class="fp-main">{"".join(sec_html)}</div>{rail}</div>')
        md = f'# The sgit newsroom\n\n{long_date}\n\n' + (f'## {lead["title"]}\n\n{lead["standfirst"]}\n\n' if lead else '') + '\n'.join(
            f'- [{c["title"]}]({c["path"][:-5]}.md)' for c in top if c) + '\n'
        self.page(P, 'The sgit newsroom', body,
                  self.prov_desk(P, 'Editor', edition_date, sources=None,
                                 extra=[('Composed from', f'<a href="{rel(P, "data/frontpage.json")}">data/frontpage.json</a> '
                                                          f'(the Editor\'s choices; the rest is filled from the newest pieces)')]),
                  md=md, eyebrow='', kind='newsroom', wide=True)
        self.write('data/frontpage.json', json.dumps(fp, indent=1, ensure_ascii=False))

    def read_time(self, c):
        words = len(self.piece_body(c['ref']).split())
        return f'{max(1, round(words / 220))} min read'

    def piece_body(self, ref):
        folder, _, slug = ref.partition('/')
        for s, m, b, _ in self.buckets().get(folder, []):
            if s == slug:
                return b
        return ''

    def desk_sha(self, folder, slug):
        for s, m, b, raw in self.buckets().get(folder, []):
            if s == slug:
                return hashlib.sha256(raw.encode('utf-8')).hexdigest()[:12]
        return ''

    def card_attrs(self, c):
        """The attributes feedback.js reads to mark a card read, hide it in the reader's view, or list it."""
        return (f'data-id="{esc(c["id"])}" data-sha="{esc(c["sha"])}" data-title="{esc(c["title"])}" data-site="{esc(c["desk"])}" '
                f'data-section="{esc(c["section"])}" data-date="{esc(c["date"])}" data-page="{esc(c["path"])}"')

    def build_news(self):
        P = 'news/index.html'
        cards = self.all_cards('stories') + self.all_cards('editions')
        order = ['news', 'feature', 'explainer', 'back-catalogue', 'edition']
        groups = {}
        for c in cards:
            groups.setdefault(c['section'], []).append(c)
        parts = []
        for sec in sorted(groups, key=lambda k: (order.index(k) if k in order else 99, k)):
            parts.append(f'<section class="fp-sec"><h2>{esc(sec.replace("-", " ").capitalize())}</h2>'
                         f'<div class="cards">{"".join(self.card(P, c) for c in sorted(groups[sec], key=lambda c: c["date"], reverse=True))}</div></section>')
        body = (f'<h1>News</h1><p class="lede">What the network made, told plainly: {len(self.stories)} pieces and {len(self.editions)} daily '
                f'editions, by the Journalist. Fact based; the Historian puts it into perspective.</p>' + ''.join(parts))
        self.page(P, 'News', body, self.prov_desk(P, 'Journalist', sources=None), wide=True, eyebrow='Journalist',
                  md='# News\n\n' + '\n'.join(f'- [{c["title"]}]({c["path"][:-5]}.md)' for c in cards) + '\n')

    def build_maps(self):
        for slug, meta, body, raw in self.maps:
            self.build_desk_page(f'maps/{slug}.html', meta, body, raw, f'Maps · {esc(meta.get("desk", "Cartographer"))}')
        # the computed map: the network as its own links draw it
        P = 'maps/network.html'
        links = self.network['links']
        strong = links[:30]                       # the strongest thirty; the table below has every site
        nid = lambda site: 'n_' + re.sub(r'[^a-z0-9]', '_', site)
        nodes = sorted({l['from'] for l in strong} | {l['to'] for l in strong})
        lines = ['flowchart LR'] + [f'  {nid(n)}["{n}"]' for n in nodes] + [f'  {nid(l["from"])} -->|{l["files"]}| {nid(l["to"])}' for l in strong]
        lines += [f'  click {nid(n)} "../reading-room/{n}.html" "{n}: every file in the snapshot"' for n in nodes
                  if os.path.exists(os.path.join(OUT, 'reading-room', n + '.html')) or n in self.cat.sites()]
        lines += ['  classDef hub fill:#e8eefc,stroke:#1f4fd1,color:#1b1a17',
                  '  class ' + ','.join(nid(n) for n in nodes if n in ('sgit.ai', 'riskmandate.ai', 'abp.sgit.ai')) + ' hub']
        inbound = {}
        for l in links:
            inbound[l['to']] = inbound.get(l['to'], 0) + l['files']
        outbound = {}
        for l in links:
            outbound[l['from']] = outbound.get(l['from'], 0) + l['files']
        def site_cell(site):
            ins = sorted((l for l in links if l['to'] == site), key=lambda l: -l['files'])[:6]
            outs = sorted((l for l in links if l['from'] == site), key=lambda l: -l['files'])[:6]
            detail = ('<div class="small muted">in: ' + (', '.join(f'{esc(l["from"])} ({l["files"]})' for l in ins) or 'none') +
                      '<br>out: ' + (', '.join(f'{esc(l["to"])} ({l["files"]})' for l in outs) or 'none') + '</div>')
            link = f'<a href="{rel(P, "reading-room/" + site + ".html")}">{esc(site)}</a>' if site in self.cat.sites() else esc(site)
            return f'<details><summary>{link}</summary>{detail}</details>'
        rows = ''.join(f'<tr><td data-v="{esc(x["site"])}">{site_cell(x["site"])}</td><td class="num" data-v="{x["files"]}">{x["files"]}</td>'
                       f'<td class="num" data-v="{outbound.get(x["site"], 0)}">{outbound.get(x["site"], 0)}</td>'
                       f'<td class="num" data-v="{inbound.get(x["site"], 0)}">{inbound.get(x["site"], 0)}</td></tr>'
                       for x in sorted(self.network['sites'], key=lambda x: -(inbound.get(x['site'], 0) + outbound.get(x['site'], 0))))
        md_src = '```mermaid\n' + '\n'.join(lines) + '\n```\n'
        html_body, _ = self.md(md_src, P)
        body = (f'<p class="crumbs"><a href="{rel(P, "maps/index.html")}">Maps</a> / the network</p>'
                f'<h1>The network, as its own links draw it</h1><p class="lede">Every arrow is a count: how many files on one site link to '
                f'another, in the snapshot of {SNAPSHOT_TAKEN}. The {len(strong)} strongest of {len(links)} links are drawn (each from '
                f'{strong[-1]["files"] if strong else 0} files or more); the table has every site. Computed by <code>tools/librarian.py</code> into '
                f'<a href="{rel(P, "data/network.json")}">data/network.json</a>; redrawn on every build.</p>{html_body}'
                f'<p class="small muted">Click a site on the map or in the table for its page; open a row for its strongest links in and out; '
                f'click a column heading to sort.</p>'
                f'<div class="table"><table class="sortable"><thead><tr><th>Site</th><th>Files</th><th>Links out (files)</th><th>Links in (files)</th></tr></thead>'
                f'<tbody>{rows}</tbody></table></div>')
        self.page(P, 'The network, as its own links draw it', body,
                  self.prov_desk(P, 'Cartographer (computed by the build)', SNAPSHOT_TAKEN, sources=['src:sites/manifest.json']),
                  md='# The network\n\n' + md_src, eyebrow='Maps', wide=True)
        self.write('data/network.json', json.dumps(self.network, indent=1, ensure_ascii=False))
        P = 'maps/index.html'
        cards = self.all_cards('maps')
        body = (f'<h1>Maps</h1><p class="lede">The Cartographer\'s maps: Wardley maps of the value chains, the network as its links draw '
                f'it, graphs of the ideas that recur, timelines. Every map renders here with the network off.</p>'
                f'<div class="cards">{"".join(self.card(P, c) for c in cards)}</div>')
        self.page(P, 'Maps', body, self.prov_desk(P, 'Cartographer', sources=None), eyebrow='Cartographer', wide=True,
                  md='# Maps\n\n' + '\n'.join(f'- [{c["title"]}]({c["path"][:-5]}.md)' for c in cards) + '\n')

    def load_issues(self):
        """issues-fs-lite: issues/{open,blocked,done}/NNN-slug.md, YAML front matter, the folder is the status."""
        out = []
        for status in ('open', 'blocked', 'done'):
            d = rp(f'issues/{status}')
            if not os.path.isdir(d):
                continue
            for name in sorted(os.listdir(d)):
                if name.endswith('.md'):
                    meta, body = mdlite.front_matter(read(os.path.join(d, name)))
                    out.append(dict(meta, stem=name[:-3], status=status, body=body,
                                    num=name[:3], title=meta.get('title') or name[:-3]))
        return out

    def build_issues(self):
        self.issues = self.load_issues()
        by_stem = {i['stem']: i for i in self.issues}
        epics = [i for i in self.issues if i.get('type') == 'epic']
        names = {a['id']: a['name'] for a in self.agents}
        P = 'admin/issues/index.html'
        pri = {'high': 0, 'medium': 1, 'low': 2}

        def card(i):
            parent = by_stem.get(i.get('parent', ''))
            ep = f'<span class="ik-epic">{esc(parent["title"].replace("Epic: ", ""))}</span>' if parent else ''
            return (f'<li class="ik-card pri-{esc(i.get("priority", ""))} type-{esc(i.get("type", ""))}" data-epic="{esc(i.get("parent", ""))}" '
                    f'data-owner="{esc(i.get("owner", ""))}" data-pri="{esc(i.get("priority", ""))}">'
                    f'<span class="ik-num">{esc(i["num"])}</span> <a href="{rel(P, "admin/issues/" + i["stem"] + ".html")}">{esc(i["title"])}</a>'
                    f'<div class="ik-meta">{esc(i.get("type", ""))} · {esc(i.get("priority", ""))} · {esc(names.get(i.get("owner"), i.get("owner", "")))}'
                    f'{" · " + esc(i.get("estimated_effort")) if i.get("estimated_effort") else ""}</div>{ep}</li>')
        cols = ''
        for status, label in (('open', 'Open'), ('blocked', 'Blocked'), ('done', 'Done')):
            items = sorted((i for i in self.issues if i['status'] == status), key=lambda i: (pri.get(i.get('priority'), 9), i['num']))
            cols += (f'<section class="ik-col"><h2>{label} <span class="ik-n">{len(items)}</span></h2>'
                     f'<ul class="ik-list">{"".join(card(i) for i in items)}</ul></section>')
        opt = lambda pairs: ''.join(f'<option value="{esc(v)}">{esc(t)}</option>' for v, t in pairs)
        filters = (f'<form class="filters" onsubmit="return false"><select id="fe"><option value="">All epics</option>'
                   f'{opt((e["stem"], e["title"].replace("Epic: ", "")) for e in epics)}</select>'
                   f'<select id="fo"><option value="">All owners</option>{opt((a["id"], a["name"]) for a in self.agents)}</select>'
                   f'<select id="fp"><option value="">Any priority</option>{opt((k, k) for k in ("high", "medium", "low"))}</select>'
                   f'<span id="fn" class="muted"></span></form>')
        body = (f'<p class="crumbs"><a href="{rel(P, "admin/index.html")}">Admin</a> / issues</p><h1>Issues</h1>'
                f'<p class="lede">{len(self.issues)} issues in <code>issues/</code> (issues-fs-lite: the folder is the status, the file is the '
                f'issue, the front matter is the data). {len(epics)} epics. Every issue cites where it came from. Moving an issue is a '
                f'<code>git mv</code> between folders, committed with the work that caused it.</p>' + filters +
                f'<div class="kanban">{cols}</div>' + ISSUES_JS)
        self.page(P, 'Issues', body, self.prov_desk(P, 'Editor (the back office)', sources=None,
                                                    extra=[('Files', 'issues/open, issues/blocked, issues/done')]),
                  eyebrow='Back office', wide=True,
                  md='# Issues\n\n' + '\n'.join(f'- [{i["status"]}] {i["num"]} {i["title"]}' for i in self.issues) + '\n')
        for i in self.issues:
            Q = f'admin/issues/{i["stem"]}.html'
            html_body, _ = self.md(i['body'], Q)
            parent = by_stem.get(i.get('parent', ''))
            children = [c for c in self.issues if c.get('parent') == i['stem']]
            kids = ''.join(f'<li><span class="tag">{esc(c["status"])}</span> <a href="{rel(Q, "admin/issues/" + c["stem"] + ".html")}">{esc(c["num"])} {esc(c["title"])}</a></li>'
                           for c in children)
            src = i.get('source', '')
            src_html = (f'<a href="{rel(Q, "admin/inbox/" + os.path.basename(src)[:-3] + ".html")}">{esc(src)}</a>'
                        if src.startswith('admin/inbox/') and src.endswith('.md') else esc(src))
            facts = [('Status', f'<span class="tag">{esc(i["status"])}</span>'), ('Type', esc(i.get('type', ''))),
                     ('Priority', esc(i.get('priority', ''))), ('Owner', esc(names.get(i.get('owner'), i.get('owner', '')))),
                     ('Created', esc(i.get('created', ''))), ('Effort', esc(i.get('estimated_effort', '') or '')),
                     ('Blocked on', esc(i.get('blocked_on', '') or '')), ('Source', src_html),
                     ('Epic', f'<a href="{rel(Q, "admin/issues/" + parent["stem"] + ".html")}">{esc(parent["title"])}</a>' if parent else ''),
                     ('Tags', esc(', '.join(i['tags']) if isinstance(i.get('tags'), list) else (i.get('tags') or '').strip('[]')))]
            facts_html = ''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in facts if v)
            body = (f'<p class="crumbs"><a href="{rel(Q, "admin/index.html")}">Admin</a> / <a href="{rel(Q, P)}">issues</a> / {esc(i["num"])}</p>'
                    f'<dl class="facts">{facts_html}</dl><article class="source">{html_body}</article>'
                    + (f'<h2>In this epic ({len(children)})</h2><ul class="list">{kids}</ul>' if children else ''))
            self.page(Q, f'{i["num"]}: {i["title"]}', body, self.prov_desk(Q, 'Editor (the back office)', i.get('created', '')[:10], sources=None,
                                                                             extra=[('File', f'issues/{i["status"]}/{i["stem"]}.md')]),
                      eyebrow=f'Issue {esc(i["num"])} · {esc(i["status"])}', md=read(rp(f'issues/{i["status"]}/{i["stem"]}.md')))

    def build_briefings(self):
        """A page per target site: what this newsroom has for that site's agent. Explicit briefs (briefings/<site>.md),
        relayed messages (briefings/<site>/inbox/*.md), the signals addressed to it and the loose ends waiting on it.
        A JSON twin beside each page, so an agent can read the same thing as data."""
        sites = {}
        def site_of(name):
            # a domain stays a domain; a team name becomes a slug (sg-api-team), never a path
            return re.sub(r'-+', '-', re.sub(r'[^a-z0-9.]+', '-', name.strip().lower())).strip('-.')
        d = rp('briefings')
        briefs, inbox = {}, {}
        if os.path.isdir(d):
            for name in sorted(os.listdir(d)):
                if name.endswith('.md') and name != 'README.md':
                    meta, body, raw = self.desk_file('briefings', name)
                    briefs[site_of(meta.get('site') or name[:-3])] = (meta, body, raw, name[:-3])
                elif os.path.isdir(os.path.join(d, name, 'inbox')):
                    msgs = []
                    for m in sorted(os.listdir(os.path.join(d, name, 'inbox'))):
                        if m.endswith('.md'):
                            meta, body, raw = self.desk_file(f'briefings/{name}/inbox', m)
                            msgs.append((meta, body, raw, m[:-3]))
                    inbox[site_of(name)] = msgs
        for k in list(briefs) + list(inbox):
            sites.setdefault(k, {})
        sig_meta = [(s, m) for s, m, _, _ in self.signals]
        for s_, m in sig_meta:
            for t in re.split(r'\s+and\s+|,\s*', m.get('to_site', '')):
                if t.strip():
                    sites.setdefault(site_of(t), {})
        for x in self.loose:
            for t in re.split(r'\s+and\s+|,\s*', x.get('waiting_on', '') or ''):
                if t.strip():
                    sites.setdefault(site_of(t), {})
        self.briefing_sites = sorted(sites)
        index_rows = []
        for site in self.briefing_sites:
            P = f'briefings/{site}.html'
            link, _, _ = self.resolver(P)
            my_sigs = [(s_, m) for s_, m in sig_meta if site in [site_of(t) for t in re.split(r'\s+and\s+|,\s*', m.get('to_site', ''))]]
            my_le = [x for x in self.loose if site in [site_of(t) for t in re.split(r'\s+and\s+|,\s*', x.get('waiting_on', '') or '')]]
            parts = []
            data = {'site': site, 'generated_from': f'sgit.newsroom.sgit.ai {VERSION}', 'briefs': [], 'messages': [], 'signals': [], 'loose_ends': []}
            if site in briefs:
                meta, body, raw, stem = briefs[site]
                html_body, _ = self.md(body, P)
                parts.append(f'<section class="brief-block"><h2>{esc(meta.get("title", "Briefs"))}</h2>'
                             + (f'<p class="dek">{esc(meta["standfirst"])}</p>' if meta.get('standfirst') else '')
                             + f'<article class="piece">{html_body}</article></section>')
                data['briefs'].append({'title': meta.get('title'), 'date': meta.get('date'), 'markdown': raw, 'file': f'briefings/{stem}.md'})
            if inbox.get(site):
                items = ''
                for meta, body, raw, stem in inbox[site]:
                    h, _ = self.md(body, P)
                    items += (f'<article class="msg"><p class="kicker">{esc(meta.get("date", ""))} · from {esc(meta.get("from", ""))} · '
                              f'<span class="tag">{esc(meta.get("status", ""))}</span></p><h3>{esc(meta.get("title", stem))}</h3>{h}</article>')
                    data['messages'].append({'title': meta.get('title'), 'date': meta.get('date'), 'status': meta.get('status'), 'markdown': raw,
                                             'file': f'briefings/{site}/inbox/{stem}.md'})
                parts.append(f'<section><h2>Messages relayed to this site\'s agent ({len(inbox[site])})</h2>{items}</section>')
            if my_sigs:
                items = ''.join(f'<li><a href="{rel(P, f"signals/{s_}.html")}">{esc(m.get("title", s_))}</a> <span class="muted small">from {esc(m.get("from_site", ""))} · '
                                f'{esc(m.get("status", ""))}</span><br><span class="small">{esc(m.get("action", ""))}</span></li>' for s_, m in my_sigs)
                parts.append(f'<section><h2>Signals for this site ({len(my_sigs)})</h2><ul class="list">{items}</ul></section>')
                data['signals'] = [{'title': m.get('title'), 'from': m.get('from_site'), 'status': m.get('status'), 'action': m.get('action'),
                                    'page': f'https://{DOMAIN}/signals/{s_}.md'} for s_, m in my_sigs]
            if my_le:
                items = ''.join(f'<li id="{esc(x.get("id", ""))}"><strong>{esc(x.get("what", ""))}</strong> <span class="tag">{esc(x.get("status", ""))}</span>'
                                f'<br><span class="small">{esc(x.get("status_note", ""))} · said on {esc(x.get("said_on", ""))} · '
                                + ', '.join(link(u, 'source') for u in x.get('said_at', [])) + '</span></li>' for x in my_le)
                parts.append(f'<section><h2>Loose ends waiting on this site ({len(my_le)})</h2><ul class="list">{items}</ul></section>')
                data['loose_ends'] = [{k: x.get(k) for k in ('id', 'what', 'status', 'status_note', 'said_on', 'said_at', 'waiting_on')} for x in my_le]
            n = len(data['briefs']) + len(data['messages']) + len(my_sigs) + len(my_le)
            body = (f'<p class="crumbs"><a href="{rel(P, "briefings/index.html")}">Briefings</a> / {esc(site)}</p>'
                    f'<h1>Briefing for {esc(site)}</h1><p class="lede">What this newsroom has for {esc(site)}\'s team or agent: '
                    f'{len(data["briefs"])} brief{"s" if len(data["briefs"]) != 1 else ""}, {len(data["messages"])} relayed message{"s" if len(data["messages"]) != 1 else ""}, '
                    f'{len(my_sigs)} signal{"s" if len(my_sigs) != 1 else ""}, {len(my_le)} loose end{"s" if len(my_le) != 1 else ""}. '
                    f'The same as data: <a href="{rel(P, f"briefings/{site}.json")}">{esc(site)}.json</a>.</p>' + ''.join(parts))
            self.page(P, f'Briefing for {site}', body, self.prov_desk(P, 'Editor (compiled by the build from the desks\' files)', sources=None),
                      eyebrow='Briefings', wide=True, md=f'# Briefing for {site}\n\n' + (briefs[site][2] if site in briefs else '') +
                      '\n\n## Signals\n' + '\n'.join(f'- {m.get("title")}' for _, m in my_sigs) + '\n\n## Loose ends\n' + '\n'.join(f'- {x.get("what")}' for x in my_le) + '\n')
            self.write(f'briefings/{site}.json', json.dumps(data, indent=1, ensure_ascii=False))
            index_rows.append((site, n, len(data['briefs']), len(data['messages']), len(my_sigs), len(my_le)))
        P = 'briefings/index.html'
        rows = ''.join(f'<tr><td><a href="{rel(P, f"briefings/{s_}.html")}">{esc(s_)}</a></td><td class="num">{b}</td><td class="num">{m}</td>'
                       f'<td class="num">{sg}</td><td class="num">{le}</td></tr>' for s_, n, b, m, sg, le in sorted(index_rows, key=lambda r: -r[1]))
        body = (f'<h1>Briefings</h1><p class="lede">One page per site or team, holding everything this newsroom has for its agent: briefs from the '
                f'editor of record, messages relayed to it, the signals addressed to it and the loose ends waiting on it. Point an agent at its '
                f'page, or at the JSON beside it. {len(index_rows)} sites and teams.</p>'
                f'<div class="table"><table class="sortable"><thead><tr><th>Site or team</th><th>Briefs</th><th>Messages</th><th>Signals</th><th>Loose ends</th></tr></thead>'
                f'<tbody>{rows}</tbody></table></div>')
        self.page(P, 'Briefings', body, self.prov_desk(P, 'Editor', sources=None), eyebrow='Briefings',
                  md='# Briefings\n\n' + '\n'.join(f'- [{s_}]({s_}.md): {n} items' for s_, n, *_ in index_rows) + '\n')

    def build_versions(self):
        P = 'admin/versions.html'
        rows = ''
        for r in sorted(self.releases, key=lambda r: [int(x) for x in r['version'][1:].split('.')], reverse=True):
            notes = ''.join(f'<li>{esc(n)}</li>' for n in r.get('notes', []))
            commit = (f' · <a class="ext" href="https://github.com/SGit-AI/SGit-AI__Website__Newsroom__SGit/commit/{esc(r["commit"])}">{esc(r["commit"][:9])} ↗</a>'
                      if r.get('commit') else '')
            rows += (f'<section class="rd sec" id="{esc(r["version"])}" data-id="releases/{esc(r["version"])}" data-sha="{esc(r.get("commit", "")[:12])}" '
                     f'data-title="{esc(r["version"] + ": " + r["title"])}" data-site="sgit.newsroom.sgit.ai" data-section="releases" data-date="{esc(r["date"])}" '
                     f'data-page="admin/versions.html#{esc(r["version"])}">'
                     f'<button type="button" class="rd-read" data-a="read">{ICON["check"]}<span> Mark as read</span></button>'
                     f'<h3>{esc(r["version"])} · {esc(r["date"])} {esc(r.get("time", ""))}{commit}</h3><p>{esc(r["title"])}</p>'
                     + (f'<ul>{notes}</ul>' if notes else '') + '</section>')
        body = (f'<p class="crumbs"><a href="{rel(P, "admin/index.html")}">Admin</a> / versions</p><h1>Releases of this newsroom</h1>'
                f'<p class="lede">Every release of sgit.newsroom.sgit.ai, newest first: {len(self.releases)} so far. This newsroom is part of the '
                f'universe it reports on (principle 5): its releases appear in the reading room like any other site\'s, and the Journalist covers them.</p>'
                f'<article class="piece">{rows}</article>')
        self.page(P, 'Releases', body, self.prov_desk(P, 'Build (from data/releases.json)', sources=None), eyebrow='Back office',
                  md='# Releases\n\n' + '\n'.join(f'- {r["version"]} ({r["date"]}): {r["title"]}' for r in self.releases) + '\n')

    def build_admin(self):
        """The back office: what each desk did, what waits for review, the front page's configuration, the editor's notes and
        the desks' standing prompts. Public like the rest of the site: nothing secret belongs here."""
        P = 'admin/index.html'
        notes = read(rp('admin/notes.md')) if os.path.exists(rp('admin/notes.md')) else ''
        prompts = sorted(n for n in os.listdir(rp('admin/prompts'))) if os.path.isdir(rp('admin/prompts')) else []
        inbox = sorted((n for n in os.listdir(rp('admin/inbox')) if n != 'README.md'), reverse=True) if os.path.isdir(rp('admin/inbox')) else []
        last, count = {}, {}
        for r in self.runs:
            last.setdefault(r.get('agent'), r)
            count[r.get('agent')] = count.get(r.get('agent'), 0) + 1
        desk_rows = ''.join(
            f'<tr><td><a href="{rel(P, "newsroom/agents/" + a["id"] + ".html")}"><strong>{esc(a["name"])}</strong></a><br>'
            f'<code class="small">{esc(a["id"])}</code></td><td>{esc(a["cadence"])}</td>'
            f'<td class="nowrap">{esc(last[a["id"]]["when"][:16].replace("T", " ")) if a["id"] in last else "no run yet"}'
            f'<br><span class="small muted">{count.get(a["id"], 0)} runs</span></td>'
            f'<td class="small">{esc(last[a["id"]].get("task", "")) if a["id"] in last else ""}</td>'
            f'<td>{"<a href=" + chr(34) + rel(P, "admin/prompts.html") + "#" + a["id"].replace(".", "") + chr(34) + ">prompt</a>" if a["id"] + ".md" in prompts else ""}</td></tr>'
            for a in self.agents)
        queue = [c for c in self.all_cards() if not c['reviewed'] and c['ref'] != 'maps/network']
        n_open = sum(1 for i in self.issues if i['status'] == 'open')
        queue_html = ''.join(f'<li><a href="{rel(P, c["path"])}">{esc(c["title"])}</a> <span class="muted small">{esc(c["section"])} · '
                             f'{esc(c["date"])} · {esc(c["desk"])}</span></li>' for c in queue)
        fp = load_json('data/frontpage.json', {})
        fp_html = (f'<ul><li><strong>Lead:</strong> {esc(fp.get("lead", "(none: the newest piece leads)"))}</li>'
                   f'<li><strong>Top:</strong> {esc(", ".join(fp.get("top", [])) or "(the next newest)")}</li>'
                   f'<li><strong>Sections:</strong> {esc(", ".join(x["title"] for x in fp.get("sections", [])) or "(the default order)")}</li>'
                   f'<li><strong>Briefs:</strong> {len(fp.get("briefs", []))}</li></ul>')
        notes_html, _ = self.md(notes, P) if notes else ('<p class="muted">No notes yet: admin/notes.md.</p>', [])
        inbox_html = ''.join(f'<li><a href="{rel(P, "admin/inbox/" + n[:-3] + ".html")}">{esc(n)}</a></li>' for n in inbox if n.endswith('.md'))
        body = (f'<h1>Admin: the back office</h1><p class="lede">Where the newsroom is operated: what each desk did and when, what waits for '
                f'the editor of record, how the front page is composed, the editor\'s notes and each desk\'s standing prompt. Public like the '
                f'rest of the site: nothing secret belongs here.</p>'
                f'<p class="jump"><a href="#desks">Desks</a> · <a href="#queue">Review queue ({len(queue)})</a> · <a href="#front">Front page</a> · '
                f'<a href="#notes">Editor\'s notes</a> · <a href="{rel(P, "admin/prompts.html")}">Prompts ({len(prompts)})</a> · '
                f'<a href="#inbox">Inbox ({len(inbox)})</a> · <a href="{rel(P, "admin/issues/index.html")}">Issues ({n_open} open)</a> · <a href="{rel(P, "admin/versions.html")}">Releases ({len(self.releases)})</a> · <a href="#run">How to run</a> · <a href="{rel(P, "newsroom/runs.html")}">All runs ({len(self.runs)})</a></p>'
                f'<h2 id="desks">Desks</h2><div class="table"><table><thead><tr><th>Desk</th><th>Cadence</th><th>Last run</th><th>Last task</th>'
                f'<th>Prompt</th></tr></thead><tbody>{desk_rows}</tbody></table></div>'
                f'<h2 id="queue">Waiting for the editor of record ({len(queue)})</h2><p>Every piece whose <code>reviewed_by</code> is empty. '
                f'Reviewing is a human\'s signature: fill <code>reviewed_by</code> and <code>reviewed_on</code> in its front matter.</p>'
                f'<ul class="list">{queue_html or "<li>Nothing waiting.</li>"}</ul>'
                f'<h2 id="front">The front page</h2><p>Composed by the Editor desk in <a href="{rel(P, "data/frontpage.json")}">data/frontpage.json</a>; '
                f'the navigation from <a href="{rel(P, "data/sections.json")}">data/sections.json</a>.</p>{fp_html}'
                f'<h2 id="notes">Editor\'s notes</h2><article class="source">{notes_html}</article>'
                f'<h2 id="inbox">Inbox</h2><p>Feedback copied from the reading room ("Copy for Claude") and run reports go in '
                f'<code>admin/inbox/YYYY-MM-DD__what.md</code>; the Editor reads them on the next run.</p>'
                f'<ul class="list">{inbox_html or "<li>Empty.</li>"}</ul>'
                f'<h2 id="run">How to run the newsroom</h2><pre>/newsroom-run                       # the whole day, desk by desk (a Claude Code session)\n'
                f'/desk journalist &lt;task&gt;             # one task as one desk: librarian, journalist, historian, cartographer, editor...\n'
                f'python3 tools/build.py &amp;&amp; python3 tools/validate.py\n'
                f'./run-local.sh [--offline|--serve]  # read it locally</pre>')
        self.page(P, 'Admin', body, self.prov_desk(P, 'Editor', sources=None,
                                                   extra=[('Files', 'admin/notes.md, admin/prompts/, admin/inbox/, data/frontpage.json, data/sections.json')]),
                  eyebrow='Back office', wide=True, md='# Admin\n\n' + notes)
        # the standing prompts, one page
        P = 'admin/prompts.html'
        parts, toc = [], []
        for n in prompts:
            if not n.endswith('.md'):
                continue
            text = read(rp('admin/prompts/' + n))
            h, _ = self.md(text, P)
            aid = n[:-3].replace('.', '')
            parts.append(f'<section id="{aid}"><h2>{esc(n[:-3])}</h2><article class="source">{h}</article></section>')
            toc.append(f'<a href="#{aid}">{esc(n[:-3])}</a>')
        self.page(P, 'Standing prompts', f'<p class="crumbs"><a href="{rel(P, P.replace("prompts", "index"))}">Admin</a> / prompts</p>'
                  f'<h1>Standing prompts</h1><p class="lede">What each desk is asked to do on every run: the prompt a session gives the desk '
                  f'after reading its role. Kept by the Editor in <code>admin/prompts/</code>.</p><p class="jump">{" · ".join(toc)}</p>' + ''.join(parts),
                  self.prov_desk(P, 'Editor', sources=None), eyebrow='Back office',
                  md='\n\n'.join(read(rp('admin/prompts/' + n)) for n in prompts if n.endswith('.md')))
        for n in inbox:
            if n.endswith('.md'):
                meta, body, raw = self.desk_file('admin/inbox', n)
                self.build_desk_page(f'admin/inbox/{n[:-3]}.html', meta or {'title': n}, body, raw, 'Back office · inbox')
        self.write('data/sections.json', json.dumps(load_json('data/sections.json', {}), indent=1, ensure_ascii=False))

    # ------------------------------------------------------------------ library (index, concepts, vaults, changes)
    def concept_pages(self):
        """Every page that uses each concept, computed by searching the snapshot for its terms."""
        texts = {s.path: s.text for s in self.cat.sources.values() if s.is_markdown and s.site
                 and not s.path.endswith('llms-full.txt')}
        out = {}
        for c in self.concepts:
            pats = [re.compile(t, re.I) for t in c.get('terms', [])]
            out[c['id']] = sorted(p for p, t in texts.items() if any(r.search(t) for r in pats))
        return out

    def build_library(self):
        cp = self.concept_pages()
        by_path = {}
        for cid, paths in cp.items():
            for p in paths:
                by_path.setdefault(p, []).append(cid)
        # the index
        P = 'library/index.html'
        rows = []
        sites, types = set(), set()
        for e in self.index:
            s = self.cat.sources.get(e['local'])
            if not s:
                continue
            cs = by_path.get(e['local'], [])
            sites.add(e['site']); types.add(e['type'])
            rows.append(f'<tr data-site="{esc(e["site"])}" data-type="{esc(e["type"])}" data-concepts="{esc(" ".join(cs))}" '
                        f'data-date="{esc(e.get("date") or "")}"><td><a href="{rel(P, s.link)}">{esc(e["title"])}</a>'
                        f'<a class="ext live" href="{esc(e["live"])}">↗</a></td><td>{esc(e["site"])}</td><td>{esc(e["type"])}</td>'
                        f'<td class="nowrap">{esc(e.get("date") or "")}</td><td class="muted small">{esc(", ".join(cs))}</td></tr>')
        opt = lambda xs: ''.join(f'<option>{esc(x)}</option>' for x in sorted(xs))
        body = (f'<h1>The index</h1><p class="lede">Every page on every site in the snapshot: {len(rows)} pages. Filter by site, type, '
                f'date and concept. Each title opens the local copy; ↗ opens the live page.</p>'
                f'<form class="filters" onsubmit="return false"><input id="q" type="search" placeholder="Filter titles">'
                f'<select id="fs"><option value="">All sites</option>{opt(sites)}</select>'
                f'<select id="ft"><option value="">All types</option>{opt(types)}</select>'
                f'<select id="fc"><option value="">All concepts</option>{opt(c["id"] for c in self.concepts)}</select>'
                f'<select id="fd"><option value="">Any date</option><option value="dated">Dated only</option>'
                f'{opt({e.get("date") for e in self.index if e.get("date")})}</select>'
                f'<span id="n" class="muted"></span></form>'
                f'<div class="table"><table id="ix"><thead><tr><th>Page</th><th>Site</th><th>Type</th><th>Date</th><th>Concepts</th></tr></thead>'
                f'<tbody>{"".join(rows)}</tbody></table></div>' + FILTER_JS)
        md = '# The index\n\n| Page | Site | Type | Date |\n|---|---|---|---|\n' + '\n'.join(
            f'| [{e["title"].replace("|", "/")}]({e["live"]}) | {e["site"]} | {e["type"]} | {e.get("date") or ""} |' for e in self.index) + '\n'
        self.page(P, 'The index', body, self.prov_desk(P, 'Librarian', SNAPSHOT_TAKEN, sources=['src:sites/manifest.json'],
                                                       extra=[('Data', f'<a href="{rel(P, "data/index.json")}">data/index.json</a>')]),
                  md=md, eyebrow='Librarian')
        self.write('data/index.json', json.dumps(self.index, indent=1, ensure_ascii=False))

        # concepts
        P = 'concepts/index.html'
        parts = []
        for c in sorted(self.concepts, key=lambda c: c['name'].lower()):
            paths = cp[c['id']]
            _, _, target = self.resolver(P)
            kind, where, live = target(c['defined_at']) if c.get('defined_at') else ('none', '', None)
            dfn = f'<a href="{rel(P, where)}">where it is defined</a>' if kind == 'local' else (
                f'<a class="ext" href="{esc(where)}">where it is defined ↗</a>' if kind == 'external' else '')
            by_site = {}
            for p in paths:
                s = self.cat.sources[p]
                by_site.setdefault(s.site, []).append(s)
            lis = ''.join(f'<li><strong>{esc(site)}</strong> ({len(xs)}): ' + ', '.join(
                f'<a href="{rel(P, x.link)}">{esc(x.title[:80])}</a>' for x in xs) + '</li>' for site, xs in sorted(by_site.items()))
            parts.append(f'<section class="concept" id="{esc(c["id"])}"><h2>{esc(c["name"])}</h2><p>{esc(c.get("definition", ""))} {dfn}</p>'
                         f'<details><summary>{len(paths)} pages on {len(by_site)} sites</summary><ul class="files">{lis}</ul></details></section>')
        body = (f'<h1>Concepts</h1><p class="lede">The ideas that recur across the network: {len(self.concepts)} concepts. The pages under each '
                f'are computed by searching the snapshot for the concept\'s terms, so they are complete for the snapshot, and noisy at the edges.</p>'
                + (''.join(parts) or '<p>No concepts yet.</p>'))
        md = '# Concepts\n\n' + '\n'.join(f'- **{c["name"]}**: {c.get("definition", "")} ({len(cp[c["id"]])} pages)' for c in self.concepts) + '\n'
        self.page(P, 'Concepts', body, self.prov_desk(P, 'Librarian', SNAPSHOT_TAKEN, sources=None,
                                                      extra=[('Data', f'<a href="{rel(P, "data/concepts.json")}">data/concepts.json</a>')]),
                  md=md, eyebrow='Librarian')
        self.write('data/concepts.json', json.dumps([dict(c, pages=cp[c['id']]) for c in self.concepts], indent=1, ensure_ascii=False))

        # vaults: cards, not a six-column table; the five seed apps get a framed page each
        P = 'vaults/index.html'
        cards = []
        for v in self.vaults:
            s = self.cat.sources.get(v.get('local') or '')
            name = f'<a href="{rel(P, s.link)}">{esc(v["name"])}</a>' if s else esc(v['name'])
            live = f'<a class="ext live" href="{esc(v["live"])}" title="live page">↗</a>' if v.get('live') else ''
            app = (f'<a class="btn-s vault-app" href="{rel(P, "vaults/app/" + v["seed"] + ".html")}">{ICON["check"]} Open the app, offline</a>'
                   if v.get('seed') else '')
            key = (f'<details class="vkey"><summary>Read key, published by the site</summary><code class="key">{esc(v["read_key"])}</code></details>'
                   if v.get('read_key') else '<span class="muted small">no read key on its page</span>')
            meta = ' · '.join(x for x in (esc(v.get('category') or ''), esc(v.get('published') or ''),
                                          f'<code>{esc(v.get("vault_id", ""))}</code>', esc(v.get('size') or '')) if x)
            cards.append(f'<li class="vcard"><div class="vhead"><div class="vname">{name}{live}</div>{app}</div>'
                         f'<p class="vwhat">{esc(v.get("what", ""))}</p><div class="vmeta">{meta}</div>{key}</li>')
            if v.get('seed'):
                self.build_vault_frame(v, s)
        body = (f'<h1>Vaults</h1><p class="lede">Every vault sgit.ai publishes: {len(self.vaults)}, from '
                f'<a href="{rel(P, "src/vaults/published-vaults.json.html")}">published-vaults.json</a>, newest first. '
                f'{sum(1 for v in self.vaults if v.get("seed"))} of them are in the seed pack and open here as apps, offline. A read key is shown only '
                f'where the vault\'s own page publishes it on purpose. No vault key or write credential appears anywhere on this site.</p>'
                f'<ul class="vcards">{"".join(cards)}</ul>')
        md = '# Vaults\n\n' + '\n'.join(f'- {v["name"]} ({v.get("vault_id", "")}): {v.get("what", "")}' for v in self.vaults) + '\n'
        self.page(P, 'Vaults', body, self.prov_desk(P, 'Librarian', SNAPSHOT_TAKEN, sources=['src:vaults/published-vaults.json']),
                  md=md, eyebrow='Librarian')

        # the day's changes
        for date, ch in sorted(self.changes.items()):
            P = f'library/changes-{date}.html'
            link, _, _ = self.resolver(P)
            rows = []
            for c in ch.get('changes', []):
                t = link(c['url'], esc(c.get('title', c['url']))) if c.get('url') else esc(c.get('title', ''))
                rows.append(f'<tr><td>{esc(c.get("site", ""))}</td><td>{esc(c.get("kind", ""))} {esc(c.get("version", "") or "")}</td>'
                            f'<td>{t}<br><span class="small">{esc(c.get("summary", ""))}</span></td><td>{esc(c.get("type", ""))}</td>'
                            f'<td class="small muted">{esc(", ".join(c.get("concepts", [])))}</td></tr>')
            body = (f'<h1>Changes, {esc(date)}</h1><p>{len(rows)} changes. Basis: {esc(ch.get("basis", ""))}.</p>'
                    f'<div class="table"><table><thead><tr><th>Site</th><th>Kind</th><th>What changed</th><th>Type</th><th>Concepts</th></tr></thead>'
                    f'<tbody>{"".join(rows)}</tbody></table></div>')
            md = f'# Changes, {date}\n\n' + '\n'.join(f'- {c.get("site")}: [{c.get("title")}]({c.get("url")}): {c.get("summary", "")}'
                                                     for c in ch.get('changes', [])) + '\n'
            self.page(P, f'Changes, {date}', body,
                      self.prov_desk(P, ch.get('desk', 'Librarian'), date, sources=sorted({c['url'] for c in ch.get('changes', []) if c.get('url')}),
                                     extra=[('Data', f'<a href="{rel(P, f"data/changes/{date}.json")}">data/changes/{date}.json</a>')]),
                      md=md, eyebrow='Librarian')
            self.write(f'data/changes/{date}.json', json.dumps(ch, indent=1, ensure_ascii=False))

    def build_vault_frame(self, v, page_src):
        """A vault's own app, framed inside the newsroom: our navigation stays, a banner says plainly that
        what is below is the vault, and the frame is sandboxed (scripts run; the app cannot reach this
        site's storage, where the reader's feedback lives)."""
        P = f'vaults/app/{v["seed"]}.html'
        app = self.cat.sources[f'vaults/{v["seed"]}/index.html']
        readme = self.cat.sources.get(f'vaults/{v["seed"]}/README.md')
        start = self.cat.sources.get(f'vaults/{v["seed"]}/plan/00-START-HERE.md')
        links = ' · '.join(x for x in (
            f'<a href="{rel(P, page_src.link)}">its page on sgit.ai (local copy)</a>' if page_src else '',
            f'<a href="{rel(P, readme.link)}">README</a>' if readme else '',
            f'<a href="{rel(P, start.link)}">the plan, as documents</a>' if start else '',
            f'<a href="{rel(P, "reading-room/index.html")}#plans">every file</a>',
            f'<a href="{rel(P, app.raw)}">open full window</a>',
            f'<a class="ext" href="{esc(v["live"])}">live ↗</a>') if x)
        key = (f'<details class="vkey"><summary>Read key, published by the site</summary><code class="key">{esc(v["read_key"])}</code></details>'
               if v.get('read_key') else '')
        bar = self.fb_bar(app).replace(f'data-title="{esc(app.title)}"', f'data-title="{esc(v["name"])} (vault app)"')
        body = (f'<div class="vault-banner"><div class="vb-tag">{ICON["check"]} Vault · {esc(v.get("category") or "")}</div>'
                f'<h1>{esc(v["name"])}</h1><p>{esc(v.get("what", ""))}</p>'
                f'<div class="vmeta">vault <code>{esc(v.get("vault_id", ""))}</code> · published {esc(v.get("published") or "")} · '
                f'{esc(v.get("size") or "")} · {v.get("files") or "?"} files</div>{key}'
                f'<p class="vb-note">Below is the vault\'s own app, exactly as published, running from the seed copy on this device. '
                f'It is the vault\'s content, not the newsroom\'s.</p><p class="small">{links}</p></div>' + bar +
                f'<div class="vault-frame"><div class="vf-top"><span class="vf-dot"></span><span class="vf-dot"></span>'
                f'<span class="vf-dot"></span><span class="vf-addr">vault {esc(v.get("vault_id", ""))} · {esc(v["seed"])}/index.html</span></div>'
                f'<iframe src="{rel(P, app.raw)}" title="{esc(v["name"])}: the vault\'s app" loading="lazy" '
                f'sandbox="allow-scripts allow-popups allow-popups-to-escape-sandbox allow-downloads allow-modals"></iframe></div>')
        prov = self.prov_block(P, [(k, val.replace('{raw}', esc(rel(P, app.raw))) if val else val) for k, val in self.prov_source(app)])
        self.page(P, f'{v["name"]} (vault)', body, prov, md=f'# {v["name"]} (vault)\n\n{v.get("what", "")}\n\nApp: {app.raw}\n',
                  eyebrow=f'Vaults · {esc(v["name"])}', kind='source', site='vaults', wide=True)

    # ------------------------------------------------------------------ history, signals, loose ends
    def build_history(self):
        for slug, meta, body, raw in self.history:
            self.build_desk_page(f'history/{slug}.html', meta, body, raw, 'Historian')
        P = 'history/index.html'
        bodies = {s: b for s, _, b, _ in self.history}
        n_dec = len(re.findall(r'^### D-\d+', bodies.get('decisions', ''), re.M))
        n_q = len(re.findall(r'^### Q-\d+', bodies.get('open-questions', ''), re.M))
        n_les = len(re.findall(r'^### ', bodies.get('lessons', ''), re.M))
        n_contra = len(re.findall(r'^### ', bodies.get('decisions', '').split('## Contradictions')[-1], re.M)) if '## Contradictions' in bodies.get('decisions', '') else 0
        tiles = (f'<div class="open-tiles wide4"><a href="{rel(P, "history/decisions.html")}"><b>{n_dec}</b><span>decisions, D-001 on</span></a>'
                 f'<a href="{rel(P, "history/open-questions.html")}"><b>{n_q}</b><span>open questions</span></a>'
                 f'<a href="{rel(P, "history/lessons.html")}"><b>{n_les}</b><span>lessons</span></a>'
                 f'<a href="{rel(P, "history/decisions.html")}#contradictions"><b>{n_contra}</b><span>contradictions</span></a></div>')
        pieces = [c for c in self.all_cards('history') if c['ref'] not in ('history/decisions', 'history/open-questions', 'history/lessons')]
        ledgers = [c for c in self.all_cards('history') if c['ref'] in ('history/decisions', 'history/open-questions', 'history/lessons')]
        body = (f'<h1>Perspective</h1><p class="lede">The Historian\'s desk: what the network\'s changes mean over time. The moments, the '
                f'connection lines, the lessons every correction taught, the decisions with their why, and the questions nobody has answered. '
                f'The Historian records; it does not editorialise.</p>{tiles}'
                f'<section class="fp-sec"><h2>Pieces</h2><div class="cards">{"".join(self.card(P, c) for c in pieces)}</div></section>'
                f'<section class="fp-sec"><h2>Ledgers, kept every day</h2><div class="cards">{"".join(self.card(P, c) for c in ledgers)}</div></section>')
        self.page(P, 'History', body, self.prov_desk(P, 'Historian', sources=None),
                  md='# History\n\n' + '\n'.join(f'- {m.get("title", s)}' for s, m, _, _ in self.history) + '\n', eyebrow='Historian')

    def build_signals(self):
        for slug, meta, body, raw in self.signals:
            extra = [('From', esc(meta.get('from_site', ''))), ('To', esc(meta.get('to_site', ''))),
                     ('Status', esc(meta.get('status', ''))), ('Action', esc(meta.get('action', '')))]
            top = (f'<p class="signal-route"><span>{esc(meta.get("from_site", ""))}</span> → <span>{esc(meta.get("to_site", ""))}</span>'
                   f' <span class="tag">{esc(meta.get("status", ""))}</span></p>'
                   f'<p><strong>Suggested action:</strong> {esc(meta.get("action", ""))}</p>')
            self.build_desk_page(f'signals/{slug}.html', meta, body, raw, f'Signal · {esc(meta.get("desk", ""))}',
                                 extra_top=top, extra_prov=extra)
        P = 'signals/index.html'
        rows = ''.join(f'<tr><td><a href="{rel(P, f"signals/{s}.html")}">{esc(m.get("title", s))}</a></td>'
                       f'<td>{esc(m.get("from_site", ""))} → {esc(m.get("to_site", ""))}</td><td>{esc(m.get("desk", ""))}</td>'
                       f'<td><span class="tag">{esc(m.get("status", ""))}</span></td></tr>' for s, m, _, _ in self.signals)
        body = (f'<h1>Signals</h1><p class="lede">Cross-pollination: site A has X; site B is doing Y and does not seem to know about X. '
                f'{len(self.signals)} signals. Each cites both sides.</p>'
                f'<div class="table"><table><thead><tr><th>Signal</th><th>From → to</th><th>Desk</th><th>Status</th></tr></thead>'
                f'<tbody>{rows or "<tr><td colspan=4>No signals yet.</td></tr>"}</tbody></table></div>')
        md = '# Signals\n\n' + '\n'.join(f'- {m.get("title", s)} ({m.get("from_site")} -> {m.get("to_site")}, {m.get("status")})'
                                          for s, m, _, _ in self.signals) + '\n'
        self.page(P, 'Signals', body, self.prov_desk(P, 'Guest desks (Architect, Developer, Cartographer)', sources=None),
                  md=md, eyebrow='Guest desks')

    def build_loose_ends(self):
        P = 'loose-ends/index.html'
        link, _, _ = self.resolver(P)
        order = {'open': 0, 'unclear': 1, 'closed': 2}
        parts = []
        for status in ('open', 'unclear', 'closed'):
            xs = [x for x in self.loose if x.get('status') == status]
            if not xs:
                continue
            rows = []
            for x in sorted(xs, key=lambda x: (x.get('said_on', ''), x.get('id', '')), reverse=True):
                said = ', '.join(link(u, 'source') for u in x.get('said_at', []))
                closed = ', '.join(link(u, 'closed by') for u in x.get('closed_by', []) or [])
                rows.append(f'<tr id="{esc(x.get("id", ""))}"><td><strong>{esc(x.get("what", ""))}</strong>'
                            f'<br><span class="small">{esc(x.get("status_note", ""))}</span></td>'
                            f'<td class="nowrap">{esc(x.get("said_on", ""))}</td><td>{esc(x.get("waiting_on", ""))}</td>'
                            f'<td class="small">{said}{"<br>" + closed if closed else ""}</td><td class="small">{esc(x.get("desk", ""))}</td></tr>')
            parts.append(f'<h2>{status.capitalize()} ({len(xs)})</h2><div class="table"><table><thead><tr><th>What</th><th>Said on</th>'
                         f'<th>Waiting on</th><th>Where</th><th>Desk</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div>')
        body = (f'<h1>Loose ends</h1><p class="lede">What was said and not done: {len(self.loose)} recorded, '
                f'{sum(1 for x in self.loose if x.get("status") == "open")} open. Every desk adds to this list.</p>' + ''.join(parts))
        md = '# Loose ends\n\n' + '\n'.join(f'- [{x.get("status")}] {x.get("what")} (waiting on {x.get("waiting_on")})'
                                             for x in sorted(self.loose, key=lambda x: order.get(x.get('status'), 3))) + '\n'
        srcs = sorted({u for x in self.loose for u in x.get('said_at', []) + (x.get('closed_by') or [])})
        self.page(P, 'Loose ends', body, self.prov_desk(P, 'All desks', SNAPSHOT_TAKEN, sources=srcs,
                                                        extra=[('Data', f'<a href="{rel(P, "data/loose-ends.json")}">data/loose-ends.json</a>')]),
                  md=md, eyebrow='All desks')
        self.write('data/loose-ends.json', json.dumps(self.loose, indent=1, ensure_ascii=False))

    # ------------------------------------------------------------------ the newsroom, about, search
    def build_agents(self):
        """One page per agent (its ROLE.md and MANDATE.md as rendered from the register), and the run records."""
        reg = load_json('data/agents.json', {'agents': []})
        self.agents = reg['agents']
        self.runs = []
        if os.path.isdir(rp('runs')):
            for name in sorted(os.listdir(rp('runs'))):
                if name.endswith('.json'):
                    self.runs.append(json.load(open(rp('runs/' + name), encoding='utf-8')) | {'_file': name})
        self.runs.sort(key=lambda r: (r.get('when', ''), r.get('agent', '')), reverse=True)
        for a in self.agents:
            P = f'newsroom/agents/{a["id"]}.html'
            role = read(rp(f'agents/{a["id"]}/ROLE.md')) if os.path.exists(rp(f'agents/{a["id"]}/ROLE.md')) else ''
            mandate = read(rp(f'agents/{a["id"]}/MANDATE.md')) if os.path.exists(rp(f'agents/{a["id"]}/MANDATE.md')) else ''
            self_link = lambda t: re.sub(r'\]\((?:ROLE|MANDATE)\.md\)', f'](nr:newsroom/agents/{a["id"]})', t)
            r_html, heads = self.md(self_link(role), P)
            m_html, _ = self.md(self_link(mandate), P)
            mine = [r for r in self.runs if r.get('agent') == a['id']]
            runs = ''.join(f'<li><strong>{esc(r.get("when", ""))}</strong> · {esc(r.get("kind", ""))} · {esc(r.get("task", ""))}'
                           f'<ul>{"".join(f"<li>{esc(d)}</li>" for d in r.get("did", []))}</ul></li>' for r in mine)
            body = (f'<p class="crumbs"><a href="{rel(P, "newsroom/index.html")}">The newsroom</a> / agents / {esc(a["name"])}</p>'
                    f'<article class="source">{r_html}</article><article class="source">{m_html}</article>'
                    f'<h2>Runs ({len(mine)})</h2><ul class="list">{runs or "<li>None yet.</li>"}</ul>')
            self.page(P, f'{a["name"]}: role and mandate', body,
                      self.prov_desk(P, 'Editor (the register of agents)', sources=None,
                                     extra=[('Register', f'<a href="{rel(P, "data/agents.json")}">data/agents.json</a>'),
                                            ('Files', f'agents/{esc(a["id"])}/ROLE.md, MANDATE.md (rendered by tools/agents.py)')]),
                      md=role + '\n' + mandate, eyebrow=f'The newsroom · {esc(a["alias"])}', toc=heads)
        self.write('data/agents.json', json.dumps(reg, indent=1, ensure_ascii=False))
        P = 'newsroom/runs.html'
        names = {a['id']: a['name'] for a in self.agents}
        rows = ''.join(f'<tr><td class="nowrap">{esc(r.get("when", ""))}</td>'
                       f'<td><a href="{rel(P, "newsroom/agents/" + r.get("agent", "") + ".html")}">{esc(names.get(r.get("agent"), r.get("agent", "")))}</a>'
                       f'<br><span class="small muted">{esc(r.get("kind", ""))}</span></td>'
                       f'<td>{esc(r.get("task", ""))}<ul class="small">{"".join(f"<li>{esc(d)}</li>" for d in r.get("did", []))}</ul>'
                       f'{f"<p class=small muted>{esc(r.get(chr(110) + chr(111) + chr(116) + chr(101)))}</p>" if r.get("note") else ""}</td>'
                       f'<td class="small">{"<br>".join(esc(f) for f in r.get("folders_changed", []))}</td></tr>' for r in self.runs)
        body = (f'<h1>Runs</h1><p class="lede">Every run of every desk, newest first: {len(self.runs)} records from <code>runs/</code>. '
                f'The validator fails a record whose agent is not in the register or that changed a folder outside its mandate.</p>'
                f'<div class="table"><table><thead><tr><th>When</th><th>Agent</th><th>Task and what it did</th><th>Folders changed</th></tr></thead>'
                f'<tbody>{rows}</tbody></table></div>')
        self.page(P, 'Runs', body, self.prov_desk(P, 'Build, from runs/', sources=None), eyebrow='The newsroom',
                  md='# Runs\n\n' + '\n'.join(f'- {r.get("when")} {r.get("agent")}: {r.get("task")}' for r in self.runs) + '\n')
        for r in self.runs:
            self.write('runs/' + r['_file'], json.dumps({k: v for k, v in r.items() if k != '_file'}, indent=2, ensure_ascii=False))

    def build_newsroom(self):
        P = 'newsroom/index.html'
        latest = max(self.changes) if self.changes else None
        n_changes = len(self.changes.get(latest, {}).get('changes', [])) if latest else 0
        eds = [e for e in self.editions if e[0] == latest]
        sts = [s for s in self.stories if s[1].get('date') == latest]
        sig = [s for s in self.signals if s[1].get('date') == latest]
        hist = [h for h in self.history if h[1].get('date') == latest]
        sites_read = len(self.cat.sites())
        files = sum(1 for s in self.cat.sources.values() if s.site)
        desks = [
            ('fetch', 'Fetch', f'{files} files from {sites_read} sites, hashed into the manifest', 'src/sites/manifest.json.html'),
            ('lib', 'Librarian', f'read {n_changes} changes; wrote the changes file, the index ({len(self.index)} pages) and {len(self.concepts)} concepts',
             f'library/changes-{latest}.html' if latest else 'library/index.html'),
            ('jou', 'Journalist', f'wrote {len(eds)} edition and {len(sts)} {"story" if len(sts) == 1 else "stories"}',
             f'editions/{latest}.html' if eds else 'editions/index.html'),
            ('his', 'Historian', f'wrote {len(hist)} {"piece" if len(hist) == 1 else "pieces"} (the week, lessons, decisions)', 'history/index.html'),
            ('gst', 'Guest desks', f'wrote {len(sig)} signals', 'signals/index.html'),
            ('all', 'All desks', f'{len(self.loose)} loose ends, {sum(1 for x in self.loose if x.get("status") == "open")} open', 'loose-ends/index.html'),
            ('ed', 'Editor of record', f'reviewed {sum(1 for e in self.editions if e[1].get("reviewed_by"))} of {len(self.editions)} editions', 'about/index.html'),
            ('bld', 'Build and validate', f'{VERSION}: this site, offline', 'about/index.html'),
        ]
        pos = {'fetch': (20, 30), 'lib': (230, 30), 'jou': (460, 10), 'his': (460, 110), 'gst': (460, 210), 'all': (460, 310),
               'ed': (690, 160), 'bld': (690, 300)}
        W, H = 180, 76
        edges = [('fetch', 'lib'), ('lib', 'jou'), ('lib', 'his'), ('lib', 'gst'), ('lib', 'all'), ('jou', 'ed'), ('his', 'ed'),
                 ('gst', 'ed'), ('all', 'ed'), ('ed', 'bld')]
        svg = [f'<svg class="flow" viewBox="0 0 890 400" role="img" aria-label="The desks and the flow between them">'
               '<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
               '<path d="M0,0 L10,5 L0,10 z" class="arrowhead"/></marker></defs>']
        for a, b in edges:
            (x1, y1), (x2, y2) = pos[a], pos[b]
            if x2 > x1:
                sx, sy, ex, ey = x1 + W, y1 + H / 2, x2, y2 + H / 2
            else:
                sx, sy, ex, ey = x1 + W / 2, y1 + H, x2 + W / 2, y2
            svg.append(f'<path class="edge" d="M{sx},{sy} C{(sx + ex) / 2},{sy} {(sx + ex) / 2},{ey} {ex},{ey}" marker-end="url(#arr)"/>')
        for key, name, what, href in desks:
            x, y = pos[key]
            words, lines, cur = what.split(), [], ''
            for w in words:
                if len(cur) + len(w) + 1 > 30:
                    lines.append(cur); cur = w
                else:
                    cur = (cur + ' ' + w).strip()
            lines.append(cur)
            tsp = ''.join(f'<tspan x="{x + 10}" dy="{15 if i else 0}">{esc(t)}</tspan>' for i, t in enumerate(lines[:3]))
            svg.append(f'<a href="{rel(P, href)}"><rect class="desk" x="{x}" y="{y}" width="{W}" height="{H}" rx="8"/>'
                       f'<text class="dname" x="{x + 10}" y="{y + 20}">{esc(name)}</text>'
                       f'<text class="dwhat" x="{x + 10}" y="{y + 38}">{tsp}</text></a>')
        svg.append('</svg>')
        table = ''.join(f'<tr><td><a href="{rel(P, href)}"><strong>{esc(name)}</strong></a></td><td>{esc(what)}</td></tr>'
                        for _, name, what, href in desks)
        kinds = {'desk': 'Desks', 'guest desk': 'Guest desks', 'construction': 'Construction', 'human': 'People'}
        last = {}
        for r in self.runs:
            last.setdefault(r.get('agent'), r.get('when', ''))
        agent_rows = ''.join(f'<tr><td><a href="{rel(P, "newsroom/agents/" + a["id"] + ".html")}"><strong>{esc(a["name"])}</strong></a>'
                             f'<br><code class="small">{esc(a["id"])}</code></td><td>{esc(kinds.get(a["kind"], a["kind"]))}</td>'
                             f'<td>{esc(a["mission"])}</td><td class="small">{esc(", ".join(a["writes"]))}</td>'
                             f'<td class="nowrap small">{esc(last.get(a["id"], "no run yet"))}</td></tr>' for a in self.agents)
        agents_html = (f'<h2 id="agents">The agents</h2><p>Each desk is a role with a mandate: what it does, when it is failing, what it '
                       f'refuses, and the folders it may write in. A session works as a desk by reading its role first (the '
                       f'<code>/desk</code> and <code>/newsroom-run</code> skills do this) and leaves a run record. '
                       f'<a href="{rel(P, "newsroom/runs.html")}">All {len(self.runs)} runs</a>.</p>'
                       f'<div class="table"><table><thead><tr><th>Agent</th><th>Kind</th><th>Mission</th><th>Writes</th><th>Last run</th></tr></thead>'
                       f'<tbody>{agent_rows}</tbody></table></div>')
        body = (f'<h1>The newsroom</h1><p class="lede">The desks, and the flow between them, filled from the data of '
                f'{esc(latest or SNAPSHOT_TAKEN)}. Every box links to what that desk wrote.</p>'
                f'<div class="flowwrap">{"".join(svg)}</div>'
                f'<div class="table"><table><thead><tr><th>Desk</th><th>On {esc(latest or "")}: read and wrote</th></tr></thead><tbody>{table}</tbody></table></div>'
                f'<h2>How the desks run together</h2><pre>fetch sources  ->  Librarian (changes, index)  ->  Journalist (edition, stories)\n'
                f'                                                  ->  Historian (moment, lessons, decisions)\n'
                f'                                                  ->  guest desks (signals), all desks (loose ends)\n'
                f'                                                  ->  Editor of record (review)  ->  build  ->  publish</pre>'
                + agents_html)
        md = '# The newsroom\n\n' + '\n'.join(f'- **{n}**: {w}' for _, n, w, _ in desks) + '\n'
        self.page(P, 'The newsroom', body, self.prov_desk(P, 'Build, from the data', latest, sources=None), md=md, eyebrow='The newsroom')

    def build_about(self):
        P = 'about/index.html'
        reviewed = sum(1 for e in self.editions if e[1].get('reviewed_by'))
        honest = (f'In {esc(VERSION)} the desks were run once, by one session, on a snapshot taken on {SNAPSHOT_TAKEN}; nothing runs on a '
                  f'schedule yet; {"nothing has" if not reviewed else f"{reviewed} editions have"} been reviewed by the editor of record.')
        brief = ''.join(f'<li><a href="{rel(P, "brief/" + n + ".html")}">{esc(t)}</a></li>' for n, t in self.brief_pages)
        body = (f'<h1>About and method</h1><p class="honest"><strong>The honest sentence.</strong> {honest}</p>'
                f'<h2>What runs</h2><ul><li>A <a href="{rel(P, "src/sites/manifest.json.html")}">snapshot</a> of {len(self.cat.sites())} sites, '
                f'{sum(1 for s in self.cat.sources.values() if s.site)} files, each with its sha256, taken by <code>tools/fetch_sources.py</code>.</li>'
                f'<li>A build (<code>tools/build.py</code>, Python standard library only) that turns the snapshot and the desks\' files into this site, '
                f'deterministically.</li><li>A validator (<code>tools/validate.py</code>) that fails on a broken relative link, an external script or '
                f'stylesheet, a <code>fetch(</code> in a page, a credential-shaped string, or a page without a provenance block.</li>'
                f'<li>CI on every push to <code>dev</code>: build, check the committed site matches the build, validate, tag the release, publish to GitHub Pages.</li></ul>'
                f'<h2>What is design</h2><ul><li>The daily run (fetch, diff, desks, build) is documented and run by hand. It is not scheduled.</li>'
                f'<li>Signals are written, not sent: no brief has been delivered to another project\'s repository yet.</li>'
                f'<li>The editor of record\'s review is a field on each page, empty until someone reviews it.</li></ul>'
                f'<h2>Who reviews</h2><p>The editor of record is a human: the founder, for now. Every edition, story, history piece and signal shows '
                f'"not yet reviewed" until its <code>reviewed_by</code> field is filled.</p>'
                f'<h2>How sources are frozen</h2><p>Every file is fetched as text and recorded in the manifest with its URL, fetch time, size and '
                f'sha256. The reading room renders each file as fetched; the raw file is beside it. Every page that says anything about a source carries a '
                f'provenance block, so a reader can walk from any claim to the frozen copy it came from. The newsroom does the same thing for the '
                f'network that <a href="{rel(P, self.cat.find_url("https://pt.newsroom.sgit.ai/llms.txt").link) if self.cat.find_url("https://pt.newsroom.sgit.ai/llms.txt") else "#"}">pt.newsroom.sgit.ai</a> '
                f'does for Portuguese sources, and that newsroom.sgit.ai argues for.</p>'
                f'<h2>Reading it offline</h2><p>Clone the repository and open <code>site/index.html</code>, or run '
                f'<code>./run-local.sh</code>: online, it first brings home the .md twin of every linked network page not yet on disk '
                f'(<code>tools/fetch_missing.py</code>), then rebuilds, validates and serves on <code>http://localhost:8000/</code>; '
                f'with <code>--offline</code> it only rebuilds and serves. Search, filters and every page work with the network off.</p>'
                f'<h2>The brief</h2><ul>{brief}</ul>')
        md = f'# About and method\n\n{re.sub("<[^>]+>", "", honest)}\n'
        self.page(P, 'About and method', body, self.prov_desk(P, 'Editor', sources=None), md=md, eyebrow='Editor')

    def build_brief(self):
        self.brief_pages = []
        for name in sorted(os.listdir(rp('brief'))):
            if not name.endswith('.md'):
                continue
            text = read(rp(f'brief/{name}'))
            P = f'brief/{name[:-3]}.html'
            html_body, heads = self.md(text, P)
            t = title_of(text, name)
            self.brief_pages.append((name[:-3], t))
            self.page(P, t, '<article>' + html_body + '</article>',
                      self.prov_desk(P, 'Editor (the seed brief)', SNAPSHOT_TAKEN, sources=None), md=text, eyebrow='The brief',
                      toc=heads)

    def build_feedback_pages(self):
        P = 'feedback/read.html'
        body = ('<h1>What you have read</h1><p class="lede">Every piece and page you marked read, on this device, newest first. '
                'In your view these are hidden from the front page and the sections; here you can find them, and unmark them.</p>'
                '<div class="filters"><button type="button" class="btn-s" data-view-go="mine">Switch to my view</button></div>'
                '<ol class="list big" data-read-list><li class="muted">Nothing marked read yet, or feedback.js has not run.</li></ol>')
        self.page(P, 'What you have read', body, self.prov_desk(P, 'The reader (this device)', sources=None), eyebrow='Your feedback',
                  md='# What you have read\n\nA page filled from this browser\'s local storage.\n', search_text='')
        P = 'feedback/history.html'
        body = ('<h1>Your history</h1><p class="lede">Every action you took on this device, newest first: read, unread, star, vote, note, memo. '
                'Undo appends the opposite action, so the history stays complete; redo puts it back.</p>'
                '<div class="filters"><button type="button" class="btn-s" data-undo>Undo last</button><button type="button" class="btn-s" data-redo>Redo</button>'
                '<span class="muted" data-hist-count></span></div>'
                '<div class="table"><table class="hist"><thead><tr><th>When</th><th>Action</th><th>Piece</th><th></th></tr></thead><tbody data-history></tbody></table></div>')
        self.page(P, 'Your history', body, self.prov_desk(P, 'The reader (this device)', sources=None), eyebrow='Your feedback',
                  md='# Your history\n\nA page filled from this browser\'s local storage.\n', search_text='')

    def build_search(self):
        P = 'search/index.html'
        data = [[t, p, s, k, x] for t, p, s, k, x in sorted(self.search, key=lambda r: (r[3] != 'newsroom', r[1]))]
        js = 'window.SEARCH=' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';\n'
        self.write('search/data.js', js)
        body = (f'<h1>Search</h1><p class="lede">Search {len(data)} pages, offline: titles, headings and the opening of every page.</p>'
                f'<form class="filters" onsubmit="return false"><input id="sq" type="search" placeholder="Search the newsroom and the snapshot" autofocus>'
                f'<span id="sn" class="muted"></span></form><ol id="sr" class="results"></ol>'
                f'<script src="data.js"></script>' + SEARCH_JS)
        self.page(P, 'Search', body, self.prov_desk(P, 'Build', sources=None), md='# Search\n\nThe search runs in the browser.\n',
                  eyebrow='Search', search_text='')

    def build_llms(self):
        lines = ['# sgit newsroom', '',
                 '> A newsroom whose beat is the sgit network: an index of what exists, daily editions of what changed, a historian\'s '
                 'perspective, cross-pollination signals and loose ends. Built from a frozen, hashed snapshot; works offline.', '',
                 f'Version {VERSION}. Snapshot {SNAPSHOT_TAKEN}. Every page has a .md twin beside it.', '', '## Newsroom', '']
        for p, t in self.nav:
            lines.append(f'- [{t}](https://{DOMAIN}/{p[:-5] + ".md" if p.endswith(".html") else p})')
        lines += ['', '## Editions', '']
        for s, m, _, _ in sorted(self.editions, reverse=True):
            lines.append(f'- [{s}: {m.get("title", "")}](https://{DOMAIN}/editions/{s}.md)')
        if self.stories:
            lines += ['', '## Stories', '']
            lines += [f'- [{m.get("title", s)}](https://{DOMAIN}/stories/{s}.md)' for s, m, _, _ in self.stories]
        if self.history:
            lines += ['', '## History', '']
            lines += [f'- [{m.get("title", s)}](https://{DOMAIN}/history/{s}.md)' for s, m, _, _ in self.history]
        if self.signals:
            lines += ['', '## Signals', '']
            lines += [f'- [{m.get("title", s)}](https://{DOMAIN}/signals/{s}.md)' for s, m, _, _ in self.signals]
        self.write('llms.txt', '\n'.join(lines) + '\n')

    def build_assets(self):
        self.write('assets/style.css', read(os.path.join(ROOT, 'tools', 'style.css')))
        self.write('assets/feedback.js', read(os.path.join(ROOT, 'tools', 'feedback.js')))
        self.write('assets/panel.js', read(os.path.join(ROOT, 'tools', 'panel.js')))
        shots = rp('assets/shots')
        if os.path.isdir(shots):
            for dirpath, _, files in os.walk(shots):
                for name in sorted(files):
                    if name.endswith('.webp'):
                        full = os.path.join(dirpath, name)
                        self.write(os.path.relpath(full, ROOT).replace(os.sep, '/'), open(full, 'rb').read(), binary=True)
        self.write('assets/mermaid.min.js', open(os.path.join(ROOT, 'tools', 'vendor', 'mermaid.min.js'), 'rb').read(), binary=True)
        self.write('assets/diagrams.js', DIAGRAMS_JS)
        self.write('CNAME', DOMAIN + '\n')
        self.write('.nojekyll', '')

    def run(self):
        if os.path.exists(OUT):
            shutil.rmtree(OUT)
        os.makedirs(OUT)
        self.load_desks()
        self.build_assets()
        self.build_sources()
        self.build_reading_room()
        self.build_brief()
        self.build_library()
        self.build_editions()
        self.build_history()
        self.build_signals()
        self.build_loose_ends()
        self.build_agents()
        self.build_issues()
        self.build_versions()
        self.build_briefings()
        self.build_maps()
        self.build_news()
        self.build_admin()
        self.build_newsroom()
        self.build_about()
        self.build_front()
        self.build_llms()
        self.build_feedback_pages()
        self.build_search()
        pages = sum(1 for p in self.written if p.endswith('.html'))
        print(f'built site/ {VERSION}: {len(self.written)} files, {pages} html pages, {len(self.cat.sources)} sources, '
              f'{len(self.editions)} editions, {len(self.stories)} stories, {len(self.history)} history, {len(self.signals)} signals, '
              f'{len(self.loose)} loose ends, {len(self.maps)} maps, {len(self.concepts)} concepts, {len(self.index)} indexed pages')
        if self.unresolved:
            print(f'{len(self.unresolved)} links in the desks\' files could not be resolved:')
            for page, href in self.unresolved:
                print(f'  {page}: {href}')
            sys.exit(1)


ISSUES_JS = '''<script>
(function(){var fe=document.getElementById('fe'),fo=document.getElementById('fo'),fp=document.getElementById('fp'),n=document.getElementById('fn'),
cards=[].slice.call(document.querySelectorAll('.ik-card'));
function go(){var c=0;cards.forEach(function(r){var d=r.dataset,ok=(!fe.value||d.epic===fe.value||r.querySelector('a').getAttribute('href').indexOf(fe.value)>=0)
&&(!fo.value||d.owner===fo.value)&&(!fp.value||d.pri===fp.value);r.hidden=!ok;if(ok)c++;});n.textContent=c+' of '+cards.length;}
[fe,fo,fp].forEach(function(e){e.addEventListener('input',go);});go();})();
</script>'''

DIAGRAMS_JS = '''/* Renders the Cartographer's maps with the bundled Mermaid: no network, strict security (no HTML or
   scripts from diagram text), and a theme that follows the reader's light or dark setting. */
(function () {
  if (!window.mermaid) return;
  var dark = window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches;
  mermaid.initialize({ startOnLoad: true, securityLevel: 'antiscript', theme: dark ? 'dark' : 'neutral',
                       fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif' });
})();
'''

FILTER_JS = '''<script>
(function(){var q=document.getElementById('q'),fs=document.getElementById('fs'),ft=document.getElementById('ft'),
fc=document.getElementById('fc'),fd=document.getElementById('fd'),n=document.getElementById('n'),
rows=[].slice.call(document.querySelectorAll('#ix tbody tr'));
try{var h=decodeURIComponent(location.hash.slice(1));if(h){var kv=h.split('=');if(kv[0]==='concept')fc.value=kv[1];if(kv[0]==='site')fs.value=kv[1];if(kv[0]==='type')ft.value=kv[1];}}catch(e){}
function go(){var t=q.value.toLowerCase(),c=0;rows.forEach(function(r){var d=r.dataset,ok=(!t||r.textContent.toLowerCase().indexOf(t)>=0)
&&(!fs.value||d.site===fs.value)&&(!ft.value||d.type===ft.value)&&(!fc.value||(' '+d.concepts+' ').indexOf(' '+fc.value+' ')>=0)
&&(!fd.value||(fd.value==='dated'?d.date:d.date===fd.value));r.hidden=!ok;if(ok)c++;});n.textContent=c+' of '+rows.length;}
[q,fs,ft,fc,fd].forEach(function(e){e.addEventListener('input',go);});go();})();
</script>'''

SEARCH_JS = '''<script>
(function(){var D=window.SEARCH||[],q=document.getElementById('sq'),out=document.getElementById('sr'),n=document.getElementById('sn');
var root='../';function esc(s){return s.replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
function go(){var t=q.value.toLowerCase().trim();out.innerHTML='';if(t.length<2){n.textContent=D.length+' pages';return;}
var ws=t.split(/\\s+/),hits=[];D.forEach(function(r){var ti=r[0].toLowerCase(),tx=(r[2]+' '+r[4]).toLowerCase(),s=0;
for(var i=0;i<ws.length;i++){var w=ws[i];if(ti.indexOf(w)>=0)s+=10;else if(tx.indexOf(w)>=0)s+=1;else{s=0;break;}}
if(s)hits.push([s+(r[3]==='newsroom'?5:0),r]);});hits.sort(function(a,b){return b[0]-a[0];});
n.textContent=hits.length+' results';hits.slice(0,200).forEach(function(h){var r=h[1],i=r[4].toLowerCase().indexOf(ws[0]),
sn=i>=0?r[4].slice(Math.max(0,i-60),i+140):r[4].slice(0,160);var li=document.createElement('li'),a=document.createElement('a');
a.setAttribute('href',root+r[1]);a.textContent=r[0];li.appendChild(a);
li.insertAdjacentHTML('beforeend',' <span class="muted small">'+esc(r[2])+'</span><br><span class="small">'+esc(sn)+'</span>');
out.appendChild(li);});try{history.replaceState(null,'','#'+encodeURIComponent(q.value));}catch(e){}}
try{var h=decodeURIComponent(location.hash.slice(1));if(h)q.value=h;}catch(e){}
q.addEventListener('input',go);go();})();
</script>'''


if __name__ == '__main__':
    Site().run()

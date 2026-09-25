"""A small markdown renderer, standard library only.

Headings, paragraphs, nested lists, tables, fenced code, blockquotes, rules, links, images,
emphasis, inline code and autolinks: what the sources use, and nothing more exotic. Raw HTML in
the source is escaped, never passed through. Links go through a resolver the caller supplies, so
the same renderer serves the reading room (links into the snapshot) and the desks' own pages.
"""
import html
import re

_FENCE = re.compile(r'^(\s{0,3})(`{3,}|~{3,})\s*([\w+-]*)')
_HEADING = re.compile(r'^\s{0,3}(#{1,6})\s+(.*?)\s*#*\s*$')
_HR = re.compile(r'^\s{0,3}(?:(?:-\s*){3,}|(?:\*\s*){3,}|(?:_\s*){3,}|={3,})\s*$')
_ITEM = re.compile(r'^(\s*)([-*+]|\d{1,9}[.)])\s+(.*)$')
_TABLE_SEP = re.compile(r'^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$')


def slugify(text):
    text = re.sub(r'<[^>]+>', '', text)
    text = html.unescape(text).lower()
    text = re.sub(r'[^\w\s-]', '', text, flags=re.UNICODE)
    return re.sub(r'[\s_-]+', '-', text).strip('-')[:80] or 'section'


class Renderer:
    """render(text) -> html. `link(href, inner_html)` returns the <a>; `image(src, alt)` the <img>."""

    def __init__(self, link, image=None):
        self.link = link
        self.image = image or (lambda src, alt: None)
        self.ids = {}
        self.headings = []
        self._stash = []

    # ---------------------------------------------------------------- inline
    def inline(self, text):
        stash = self._stash

        def keep(fragment):
            stash.append(fragment)
            return f'\x00{len(stash) - 1}\x00'

        # code spans first: nothing inside them is markdown
        text = re.sub(r'(`+)(.+?)\1', lambda m: keep(f'<code>{html.escape(m.group(2).strip())}</code>'), text)
        # images, then links (text may hold one level of brackets); urls may hold one level of parens
        url = r'((?:[^()\s]|\([^()\s]*\))+)(?:\s+"[^"]*")?'
        text = re.sub(r'!\[([^\]]*)\]\(' + url + r'\)', lambda m: keep(self._image(m.group(2), m.group(1))), text)
        text = re.sub(r'\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\(' + url + r'\)',
                      lambda m: keep(self.link(m.group(2), self.inline(m.group(1)))), text)
        text = re.sub(r'<(https?://[^>\s]+)>', lambda m: keep(self.link(m.group(1), html.escape(m.group(1)))), text)
        text = re.sub(r'(?<![\w/="\'])(https?://[^\s<>()\[\]`"]*[^\s<>()\[\]`".,;:!?\'*_])',
                      lambda m: keep(self.link(m.group(1), html.escape(m.group(1)))), text)
        text = html.escape(text)
        text = re.sub(r'\*\*\*(\S(?:.*?\S)?)\*\*\*', r'<strong><em>\1</em></strong>', text)
        text = re.sub(r'\*\*(\S(?:.*?\S)?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'(?<![\w*])__(\S(?:.*?\S)?)__(?![\w*])', r'<strong>\1</strong>', text)
        text = re.sub(r'(?<![\w*])\*(\S(?:.*?\S)?)\*(?![\w*])', r'<em>\1</em>', text)
        text = re.sub(r'(?<![\w_])_(\S(?:.*?\S)?)_(?![\w_])', r'<em>\1</em>', text)
        text = re.sub(r'~~(\S(?:.*?\S)?)~~', r'<del>\1</del>', text)
        text = re.sub(r'  +\n|\\\n', '<br>\n', text)
        while '\x00' in text:
            text = re.sub(r'\x00(\d+)\x00', lambda m: stash[int(m.group(1))], text)
        return text

    def _image(self, src, alt):
        got = self.image(src, alt)
        if got:
            return got
        # remote images are never loaded: the site makes no request anywhere
        return self.link(src, f'[image: {html.escape(alt or src)}]')

    # ---------------------------------------------------------------- blocks
    def render(self, text):
        text = text.replace('\r\n', '\n').replace('\t', '    ')
        text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
        return self.blocks(text.split('\n'))

    def heading_id(self, text):
        base = slugify(text)
        n = self.ids.get(base, 0)
        self.ids[base] = n + 1
        return base if n == 0 else f'{base}-{n}'

    def blocks(self, lines):
        out, i, para = [], 0, []

        def flush():
            if para:
                out.append('<p>' + self.inline('\n'.join(s.strip() for s in para)) + '</p>')
                para.clear()

        while i < len(lines):
            line = lines[i]
            if not line.strip():
                flush(); i += 1; continue
            m = _FENCE.match(line)
            if m:
                flush()
                fence, lang, body = m.group(2), m.group(3), []
                i += 1
                while i < len(lines) and not lines[i].strip().startswith(fence):
                    body.append(lines[i]); i += 1
                i += 1
                cls = f' class="lang-{html.escape(lang)}"' if lang else ''
                out.append(f'<pre><code{cls}>' + html.escape('\n'.join(body)) + '</code></pre>')
                continue
            m = _HEADING.match(line)
            if m:
                flush()
                level, content = len(m.group(1)), m.group(2)
                inner = self.inline(content)
                # a heading that links to its own anchor ("### [Title](#slug)") keeps that anchor,
                # so deep links into the source page (sgit.ai's updates, for one) still land
                own = re.match(r'^\[[^\]]*\]\(#([\w-]+)\)', content)
                hid = self.heading_id(own.group(1) if own else inner)
                self.headings.append((level, re.sub(r'<[^>]+>', '', inner), hid))
                out.append(f'<h{level} id="{hid}">{inner}</h{level}>')
                i += 1; continue
            if _HR.match(line) and not (para and set(line.strip()) == {'-'}):
                flush(); out.append('<hr>'); i += 1; continue
            if para and set(line.strip()) == {'-'} and len(line.strip()) >= 3:
                para.append(''); flush(); out.append('<hr>'); i += 1; continue
            if line.lstrip().startswith('>'):
                flush()
                quoted = []
                while i < len(lines) and lines[i].strip() and lines[i].lstrip().startswith('>'):
                    quoted.append(re.sub(r'^\s*>\s?', '', lines[i])); i += 1
                out.append('<blockquote>' + self.blocks(quoted) + '</blockquote>')
                continue
            if '|' in line and i + 1 < len(lines) and _TABLE_SEP.match(lines[i + 1]) and '|' in lines[i + 1]:
                flush()
                rows = [line]
                i += 2
                while i < len(lines) and '|' in lines[i] and lines[i].strip():
                    rows.append(lines[i]); i += 1
                out.append(self.table(rows))
                continue
            if _ITEM.match(line) and (not para or not re.match(r'^\s*\d', line)):
                flush()
                i = self.listing(lines, i, out)
                continue
            para.append(line); i += 1
        flush()
        return '\n'.join(out)

    @staticmethod
    def cells(row):
        row = row.strip()
        if row.startswith('|'):
            row = row[1:]
        if row.endswith('|') and not row.endswith('\\|'):
            row = row[:-1]
        return [c.strip().replace('\\|', '|') for c in re.split(r'(?<!\\)\|', row)]

    def table(self, rows):
        head = self.cells(rows[0])
        h = ''.join(f'<th>{self.inline(c)}</th>' for c in head)
        body = []
        for r in rows[1:]:
            cs = self.cells(r)
            body.append('<tr>' + ''.join(f'<td>{self.inline(c)}</td>' for c in cs) + '</tr>')
        return f'<div class="table"><table><thead><tr>{h}</tr></thead><tbody>' + '\n'.join(body) + '</tbody></table></div>'

    def listing(self, lines, i, out):
        m = _ITEM.match(lines[i])
        indent = len(m.group(1))
        ordered = m.group(2)[0].isdigit()
        items, loose = [], False
        while i < len(lines):
            m = _ITEM.match(lines[i])
            if not m or len(m.group(1)) != indent or m.group(2)[0].isdigit() != ordered:
                break
            content_indent = len(m.group(1)) + len(m.group(2)) + 1
            body = [m.group(3)]
            i += 1
            while i < len(lines):
                ln = lines[i]
                if not ln.strip():
                    # a blank line: the item continues only if the next line is indented under it
                    j = i + 1
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j < len(lines) and len(lines[j]) - len(lines[j].lstrip()) > indent and not (
                            _ITEM.match(lines[j]) and len(_ITEM.match(lines[j]).group(1)) <= indent):
                        body.append(''); i += 1; loose = True; continue
                    break
                lead = len(ln) - len(ln.lstrip())
                im = _ITEM.match(ln)
                if im and lead <= indent:
                    break
                if lead == 0 and (_HEADING.match(ln) or _FENCE.match(ln) or ln.startswith('|')):
                    break
                body.append(ln[min(lead, content_indent):] if lead > indent else ln.strip())
                i += 1
            items.append(body)
            # blank lines between items of the same list
            j = i
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j > i and j < len(lines):
                m2 = _ITEM.match(lines[j])
                if m2 and len(m2.group(1)) == indent and m2.group(2)[0].isdigit() == ordered:
                    i = j; loose = True; continue
            if j > i:
                break
        tag = 'ol' if ordered else 'ul'
        html_items = []
        for body in items:
            inner = self.blocks(body)
            if not loose and inner.startswith('<p>') and inner.count('<p>') == 1:
                inner = inner[3:].replace('</p>', '', 1)
            html_items.append(f'<li>{inner}</li>')
        out.append(f'<{tag}>' + ''.join(html_items) + f'</{tag}>')
        return i


def front_matter(text):
    """Split `---` front matter (a small YAML subset) from a desk file. Returns (meta, body)."""
    if not text.startswith('---\n'):
        return {}, text
    end = text.find('\n---', 4)
    if end < 0:
        return {}, text
    meta, key = {}, None
    for raw in text[4:end].split('\n'):
        if not raw.strip():
            continue
        m = re.match(r'^\s+-\s+(.*)$', raw)
        if m and key:
            if not isinstance(meta.get(key), list):
                meta[key] = []
            meta[key].append(m.group(1).strip().strip('"\''))
            continue
        m = re.match(r'^([\w-]+):\s*(.*)$', raw)
        if m:
            key, val = m.group(1), m.group(2).strip()
            meta[key] = val.strip('"\'') if val else ''
    body = text[end + 4:]
    return meta, body.lstrip('\n')

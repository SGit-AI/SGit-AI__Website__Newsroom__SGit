/* sgit newsroom: the reading list's filters, and feedback that stays on this device.
 *
 * Feedback is an append-only event log in this browser's localStorage ({t, dev, src, sha, op, val}),
 * keyed by each source's path and sha256, so a note written today says so when tomorrow's snapshot
 * changes the page. Nothing is sent anywhere. "Copy for Claude" puts the events since the last copy
 * on the clipboard as markdown plus a JSON block; "Paste to merge" reads that JSON back in on another
 * device (events are deduplicated, then sorted, so merging never overwrites). Voice memos are kept in
 * IndexedDB and only their existence is exported. No network: this file makes no request at all.
 */
(function () {
  'use strict';
  var KEY = 'sgit-newsroom.feedback.v1';
  var DEVKEY = 'sgit-newsroom.device';
  var ICON = {
    star: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true"><path d="M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8L3.5 9.7l5.9-.9z"/></svg>',
    up: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 15l6-6 6 6"/></svg>',
    down: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>',
    note: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20h4L19 9l-4-4L4 16v4z"/></svg>',
    check: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg>',
    mic: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg>'
  };

  // ------------------------------------------------------------------ storage
  var mem = null;
  function load() {
    if (mem) return mem;
    var d = null;
    try { d = JSON.parse(localStorage.getItem(KEY) || 'null'); } catch (e) { d = null; }
    mem = d && d.events ? d : { v: 1, events: [], items: {}, cursor: '' };
    mem.items = mem.items || {};
    return mem;
  }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(mem)); } catch (e) { /* private mode: memory only */ } }
  function device() {
    var id = null;
    try { id = localStorage.getItem(DEVKEY); } catch (e) { id = null; }
    if (!id) {
      var kind = (window.matchMedia && matchMedia('(pointer: coarse)').matches && screen.width < 900) ? 'phone' : 'laptop';
      id = kind + '-' + Math.random().toString(16).slice(2, 6);
      try { localStorage.setItem(DEVKEY, id); } catch (e) { /* ignore */ }
    }
    return id;
  }
  var DEV = device();
  function now() { return new Date().toISOString().replace(/\.\d+Z$/, 'Z'); }
  function meta(el) {
    return { title: el.getAttribute('data-title') || '', site: el.getAttribute('data-site') || '',
             section: el.getAttribute('data-section') || '', date: el.getAttribute('data-date') || '',
             page: el.getAttribute('data-page') || '' };
  }
  function log(el, op, val) {
    var d = load(), src = el.getAttribute('data-id');
    d.items[src] = meta(el);
    d.events.push({ t: now(), dev: DEV, src: src, sha: el.getAttribute('data-sha') || '', op: op, val: val === undefined ? null : val });
    save();
    refresh();
  }
  function fold() {
    var st = {};
    load().events.forEach(function (e) {
      var s = st[e.src] || (st[e.src] = { memos: 0 });
      if (e.op === 'read') s.read = true;
      else if (e.op === 'unread') s.read = false;
      else if (e.op === 'star') s.star = !!e.val;
      else if (e.op === 'vote') s.vote = e.val || null;
      else if (e.op === 'note') { s.note = e.val || ''; s.noteSha = e.sha; }
      else if (e.op === 'memo') s.memos += 1;
      s.last = e.t;
    });
    return st;
  }

  // ------------------------------------------------------------------ export and merge
  function describe(s) {
    var bits = [];
    if (s.read) bits.push('read');
    if (s.star) bits.push('starred');
    if (s.vote) bits.push('vote: ' + s.vote);
    return bits.join(' · ') || 'no status';
  }
  function exportText(all) {
    var d = load(), st = fold();
    var evs = all ? d.events : d.events.filter(function (e) { return e.t > (d.cursor || ''); });
    var srcs = [];
    evs.forEach(function (e) { if (srcs.indexOf(e.src) < 0) srcs.push(e.src); });
    var out = ['<!-- sgit-newsroom feedback v1 · device ' + DEV + ' · ' + (document.documentElement.getAttribute('data-version') || '') +
               ' · ' + (all ? 'all ' + evs.length + ' events' : evs.length + ' events since ' + (d.cursor || 'the start')) + ' · ' + now() + ' -->', '',
               '# Reading-room feedback, ' + srcs.length + (srcs.length === 1 ? ' item' : ' items'), ''];
    srcs.forEach(function (src) {
      var m = d.items[src] || {}, s = st[src] || {};
      out.push('## ' + [m.date, m.site, m.section].filter(Boolean).join(' · '));
      out.push(m.title || src);
      out.push('- ' + describe(s));
      if (s.note) out.push('- note: ' + s.note.replace(/\n/g, '\n  '));
      if (s.memos) out.push('- voice memos: ' + s.memos + ', kept on ' + DEV + ' (not included)');
      out.push('- source: ' + src);
      var cur = currentSha(src);
      if (s.note && s.noteSha && cur && s.noteSha !== cur) out.push('- the source changed after this note (sha ' + s.noteSha.slice(0, 6) + ' > ' + cur.slice(0, 6) + ')');
      out.push('');
    });
    out.push('```json');
    out.push(JSON.stringify({ v: 1, device: DEV, items: srcs.reduce(function (o, s) { o[s] = d.items[s]; return o; }, {}), events: evs }));
    out.push('```');
    return out.join('\n');
  }
  function currentSha(src) {
    var el = document.querySelector('[data-id="' + (window.CSS && CSS.escape ? CSS.escape(src) : src) + '"]');
    return el ? el.getAttribute('data-sha') : '';
  }
  function copyText(text, done) {
    function fallback() {
      var ta = document.createElement('textarea');
      ta.value = text; ta.setAttribute('readonly', ''); ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      var ok = false;
      try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
      document.body.removeChild(ta);
      done(ok);
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () { done(true); }, fallback);
    } else { fallback(); }
  }
  function merge(text) {
    var m = /```json\s*([\s\S]*?)```/.exec(text), raw = m ? m[1] : text, data;
    try { data = JSON.parse(raw); } catch (e) { return -1; }
    if (!data || !data.events) return -1;
    var d = load(), seen = {}, added = 0;
    function k(e) { return [e.t, e.dev, e.src, e.op, JSON.stringify(e.val)].join('|'); }
    d.events.forEach(function (e) { seen[k(e)] = 1; });
    data.events.forEach(function (e) { if (e && e.src && !seen[k(e)]) { d.events.push(e); seen[k(e)] = 1; added++; } });
    Object.keys(data.items || {}).forEach(function (s) { if (!d.items[s] && data.items[s]) d.items[s] = data.items[s]; });
    d.events.sort(function (a, b) { return a.t < b.t ? -1 : a.t > b.t ? 1 : 0; });
    save(); refresh();
    return added;
  }

  // ------------------------------------------------------------------ voice memos (IndexedDB, this device only)
  function idb(cb) {
    if (!window.indexedDB) return cb(null);
    var r;
    try { r = indexedDB.open('sgit-newsroom', 1); } catch (e) { return cb(null); }
    r.onupgradeneeded = function () { r.result.createObjectStore('memos', { keyPath: 'id' }); };
    r.onsuccess = function () { cb(r.result); };
    r.onerror = function () { cb(null); };
  }
  function memoList(src, cb) {
    idb(function (db) {
      if (!db) return cb([]);
      var out = [], tx = db.transaction('memos', 'readonly');
      tx.objectStore('memos').openCursor().onsuccess = function (ev) {
        var c = ev.target.result;
        if (c) { if (c.value.src === src) out.push(c.value); c.continue(); } else cb(out);
      };
    });
  }
  function memoSave(rec, cb) {
    idb(function (db) {
      if (!db) return cb(false);
      var tx = db.transaction('memos', 'readwrite');
      tx.objectStore('memos').put(rec);
      tx.oncomplete = function () { cb(true); };
      tx.onerror = function () { cb(false); };
    });
  }
  function fmtDur(ms) { var s = Math.round(ms / 1000); return Math.floor(s / 60) + ':' + ('0' + (s % 60)).slice(-2); }

  // ------------------------------------------------------------------ the reading list
  var root = document.querySelector('[data-rl]');
  var bars = [].slice.call(document.querySelectorAll('[data-fb]'));
  var f = { q: '', status: 'all', site: 'all', section: 'all' };
  var selected = null;
  var narrow = window.matchMedia ? matchMedia('(max-width: 899px)') : { matches: false };

  function rows() { return root ? [].slice.call(root.querySelectorAll('.rl-row')) : []; }
  function setPressed(btn, on) { if (btn) { btn.setAttribute('aria-pressed', on ? 'true' : 'false'); btn.classList.toggle('on', !!on); } }

  function applyFilters() {
    if (!root) return;
    var st = fold(), q = f.q.toLowerCase(), shown = 0;
    rows().forEach(function (r) {
      var s = st[r.getAttribute('data-id')] || {};
      var ok = (f.status === 'all' || (f.status === 'unread' && !s.read) || (f.status === 'starred' && s.star) ||
                (f.status === 'noted' && s.note) || (f.status === 'voted' && s.vote)) &&
               (f.site === 'all' || r.getAttribute('data-site') === f.site) &&
               (f.section === 'all' || r.getAttribute('data-section') === f.section) &&
               (!q || r.getAttribute('data-title').toLowerCase().indexOf(q) >= 0);
      r.hidden = !ok;
      if (ok) shown++;
    });
    [].slice.call(root.querySelectorAll('.rl-day')).forEach(function (d) {
      var n = d.querySelectorAll('.rl-row:not([hidden])').length;
      d.hidden = n === 0;
      d.querySelector('.rl-n').textContent = n + (n === 1 ? ' item' : ' items');
    });
    root.querySelector('[data-shown]').textContent = shown;
    root.querySelector('.rl-empty').hidden = shown !== 0;
    [].slice.call(root.querySelectorAll('[data-status]')).forEach(function (b) { setPressed(b, b.getAttribute('data-status') === f.status); });
    [].slice.call(root.querySelectorAll('[data-site-f]')).forEach(function (b) { setPressed(b, b.getAttribute('data-site-f') === f.site); });
    [].slice.call(root.querySelectorAll('[data-section-f]')).forEach(function (b) { setPressed(b, b.getAttribute('data-section-f') === f.section); });
    try { history.replaceState(null, '', '#' + ['status=' + f.status, 'site=' + f.site, 'section=' + f.section, 'q=' + encodeURIComponent(f.q)].join('&')); } catch (e) { /* file:// may refuse */ }
  }

  function paintRow(r, s) {
    r.classList.toggle('read', !!s.read);
    r.classList.toggle('sel', selected === r);
    setPressed(r.querySelector('[data-act=star]'), s.star);
    setPressed(r.querySelector('[data-act=up]'), s.vote === 'up');
    setPressed(r.querySelector('[data-act=down]'), s.vote === 'down');
    var flags = r.querySelector('.rl-flags'), html = '';
    if (s.note) html += '<span class="rl-flag note">' + ICON.note + 'note</span>';
    if (s.memos) html += '<span class="rl-flag note">' + ICON.mic + s.memos + '</span>';
    if (s.note && s.noteSha && s.noteSha !== r.getAttribute('data-sha')) html += '<span class="rl-flag changed">changed since your note</span>';
    flags.innerHTML = html;
  }

  function paintCounts(st) {
    if (!root) return;
    var all = rows(), c = { all: all.length, unread: 0, starred: 0, noted: 0, voted: 0 };
    all.forEach(function (r) {
      var s = st[r.getAttribute('data-id')] || {};
      if (!s.read) c.unread++;
      if (s.star) c.starred++;
      if (s.note) c.noted++;
      if (s.vote) c.voted++;
    });
    Object.keys(c).forEach(function (k) { var el = root.querySelector('[data-count=' + k + ']'); if (el) el.textContent = c[k]; });
  }

  function paintDevice(st) {
    var box = document.querySelector('[data-dev]');
    if (!box) return;
    var d = load(), n = { read: 0, starred: 0, votes: 0, notes: 0 };
    Object.keys(st).forEach(function (k) { var s = st[k]; if (s.read) n.read++; if (s.star) n.starred++; if (s.vote) n.votes++; if (s.note) n.notes++; });
    Object.keys(n).forEach(function (k) { [].slice.call(document.querySelectorAll('[data-stat=' + k + ']')).forEach(function (el) { el.textContent = n[k]; }); });
    var pending = d.events.filter(function (e) { return e.t > (d.cursor || ''); }).length;
    var lastE = d.events[d.events.length - 1], ls = box.querySelector('[data-f=dev-status]');
    if (lastE && ls && !ls.textContent) ls.innerHTML = 'Last: ' + esc(lastE.op) + ' \u00b7 <a href="#" data-undo>undo</a>';
    [].slice.call(document.querySelectorAll('[data-stat=pending]')).forEach(function (el) { el.textContent = pending; });
    [].slice.call(document.querySelectorAll('[data-stat=device]')).forEach(function (el) { el.textContent = DEV; });
    var pre = box.querySelector('[data-preview]');
    if (pre) pre.textContent = pending ? exportText(false) : 'Nothing new since your last copy. "Download .md" has everything.';
  }

  function paintSel(st) {
    var p = document.querySelector('[data-sel]');
    if (!p) return;
    p.classList.toggle('empty', !selected);
    document.documentElement.classList.toggle('rl-sheet-open', !!selected && narrow.matches);
    if (!selected) return;
    var s = st[selected.getAttribute('data-id')] || {}, m = meta(selected);
    p.querySelector('[data-f=title]').textContent = m.title;
    p.querySelector('[data-f=meta]').textContent = [m.date, selected.getAttribute('data-time'), m.site, m.section].filter(Boolean).join(' · ');
    p.querySelector('[data-f=local]').setAttribute('href', selected.querySelector('.rl-title').getAttribute('href'));
    var live = selected.getAttribute('data-live');
    var lv = p.querySelector('[data-f=live]');
    lv.hidden = !live; if (live) lv.setAttribute('href', live);
    var rd = p.querySelector('[data-a=read]');
    rd.textContent = s.read ? 'Mark unread' : 'Mark read';
    setPressed(p.querySelector('[data-a=star]'), s.star);
    setPressed(p.querySelector('[data-a=up]'), s.vote === 'up');
    setPressed(p.querySelector('[data-a=down]'), s.vote === 'down');
    var ta = p.querySelector('textarea');
    if (document.activeElement !== ta) ta.value = s.note || '';
    var ml = p.querySelector('[data-memos]');
    memoList(selected.getAttribute('data-id'), function (list) {
      ml.innerHTML = '';
      list.forEach(function (rec) {
        var li = document.createElement('li'), a = document.createElement('audio');
        a.controls = true; a.preload = 'none'; a.src = URL.createObjectURL(rec.blob);
        li.appendChild(document.createTextNode(rec.t.slice(0, 16).replace('T', ' ') + ' · ' + fmtDur(rec.dur) + ' '));
        li.appendChild(a); ml.appendChild(li);
      });
    });
  }

  function paintBars(st) {
    bars.forEach(function (b) {
      var s = st[b.getAttribute('data-id')] || {};
      var rd = b.querySelector('[data-a=read]');
      if (rd) { rd.lastChild.textContent = s.read ? ' Read \u2713 \u00b7 mark unread' : ' Mark as read'; setPressed(rd, s.read); }
      setPressed(b.querySelector('[data-a=star]'), s.star);
      setPressed(b.querySelector('[data-a=up]'), s.vote === 'up');
      setPressed(b.querySelector('[data-a=down]'), s.vote === 'down');
      var ta = b.querySelector('textarea');
      if (ta && document.activeElement !== ta) ta.value = s.note || '';
      var nb = b.querySelector('[data-a=note]');
      if (nb) setPressed(nb, !!s.note);
      var ch = b.querySelector('[data-f=changed]');
      if (ch) ch.hidden = !(s.note && s.noteSha && s.noteSha !== b.getAttribute('data-sha'));
    });
  }

  function refresh() {
    var st = fold();
    rows().forEach(function (r) { paintRow(r, st[r.getAttribute('data-id')] || {}); });
    paintCounts(st); applyFilters(); paintDevice(st); paintSel(st); paintBars(st);
    paintView(st); paintCards(st); paintReadList(st); paintHistory(st);
  }

  // ------------------------------------------------------------------ the reader's view: read pieces hidden
  var VIEWKEY = 'sgit-newsroom.view';
  function view() { try { return localStorage.getItem(VIEWKEY) === 'mine' ? 'mine' : 'editor'; } catch (e) { return 'editor'; } }
  function setView(v) { try { localStorage.setItem(VIEWKEY, v); } catch (e) { /* ignore */ } refresh(); }
  function paintView(st) {
    var v = view();
    document.documentElement.classList.toggle('view-mine', v === 'mine');
    var box = document.querySelector('[data-views]');
    if (!box) return;
    box.hidden = false;
    [].slice.call(box.querySelectorAll('[data-view]')).forEach(function (b) { b.classList.toggle('on', b.getAttribute('data-view') === v); });
    var n = Object.keys(st).filter(function (k) { return st[k].read; }).length;
    var a = box.querySelector('[data-read-count]');
    if (a) a.textContent = n ? n + ' read' : '';
  }
  function paintCards(st) {
    var cards = [].slice.call(document.querySelectorAll('.rd[data-id]'));
    if (!cards.length) return;
    var mine = view() === 'mine', boxes = {};
    cards.forEach(function (c) {
      var s = st[c.getAttribute('data-id')] || {};
      c.classList.toggle('is-read', !!s.read);
      var box = c.parentElement;
      if (!boxes[box.__k]) { box.__k = box.__k || ('b' + Math.random().toString(16).slice(2, 7)); boxes[box.__k] = { el: box, hidden: 0, all: 0 }; }
      boxes[box.__k].all++;
      if (s.read) boxes[box.__k].hidden++;
    });
    var readHref = (document.querySelector('[data-views] [data-read-count]') || {}).getAttribute ? document.querySelector('[data-views] [data-read-count]').getAttribute('href') : 'feedback/read.html';
    Object.keys(boxes).forEach(function (k) {
      var b = boxes[k], clue = b.el.nextElementSibling && b.el.nextElementSibling.classList.contains('hidden-clue') ? b.el.nextElementSibling : null;
      if (!clue) { clue = document.createElement('p'); clue.className = 'hidden-clue'; b.el.insertAdjacentElement('afterend', clue); }
      if (mine && b.hidden) {
        clue.hidden = false;
        clue.innerHTML = b.hidden + (b.hidden === 1 ? ' read piece hidden' : ' read pieces hidden') + (b.hidden === b.all ? ' (all of them)' : '') +
          ' \u00b7 <a href="' + readHref + '">what you have read</a> \u00b7 <a href="#" data-view-go="editor">show</a>';
      } else { clue.hidden = true; }
    });
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-view], [data-view-go]');
    if (!b) return;
    if (b.hasAttribute('data-view-go')) e.preventDefault();
    setView(b.getAttribute('data-view') || b.getAttribute('data-view-go'));
  });

  // ------------------------------------------------------------------ what you have read, and the history
  function pieceLink(src, m) {
    var page = (m && m.page) || '';
    var root = document.documentElement.getAttribute('data-root') || '../';
    return page ? root + page : '';
  }
  function paintReadList(st) {
    var ol = document.querySelector('[data-read-list]');
    if (!ol) return;
    var d = load(), items = Object.keys(st).filter(function (k) { return st[k].read; })
      .sort(function (a, b) { return (st[b].last || '') < (st[a].last || '') ? -1 : 1; });
    ol.innerHTML = '';
    if (!items.length) { ol.innerHTML = '<li class="muted">Nothing marked read yet.</li>'; return; }
    items.forEach(function (src) {
      var m = d.items[src] || {}, s = st[src], li = document.createElement('li'), a = document.createElement('a');
      a.textContent = m.title || src; var href = pieceLink(src, m); if (href) a.setAttribute('href', href);
      li.appendChild(a);
      li.insertAdjacentHTML('beforeend', ' <span class="muted small">' + esc([m.site, m.section, m.date].filter(Boolean).join(' \u00b7 ')) +
        ' \u00b7 read ' + esc((s.last || '').slice(0, 16).replace('T', ' ')) + '</span> <button type="button" class="linkbtn" data-unread="' + esc(src) + '">mark unread</button>');
      ol.appendChild(li);
    });
  }
  function esc(t) { return String(t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-unread]');
    if (!b) return;
    var src = b.getAttribute('data-unread'), d = load(), m = d.items[src] || {};
    d.events.push({ t: now(), dev: DEV, src: src, sha: '', op: 'unread', val: null }); save(); refresh();
  });
  function stateBefore(idx) {
    var d = load(), st = {};
    d.events.slice(0, idx).forEach(function (e) {
      var s = st[e.src] || (st[e.src] = {});
      if (e.op === 'read') s.read = true; else if (e.op === 'unread') s.read = false;
      else if (e.op === 'star') s.star = !!e.val; else if (e.op === 'vote') s.vote = e.val || null;
      else if (e.op === 'note') s.note = e.val || '';
    });
    return st;
  }
  function inverse(e, idx) {
    var before = stateBefore(idx)[e.src] || {};
    if (e.op === 'read') return { op: 'unread', val: null };
    if (e.op === 'unread') return { op: 'read', val: null };
    if (e.op === 'star') return { op: 'star', val: !!before.star };
    if (e.op === 'vote') return { op: 'vote', val: before.vote || null };
    if (e.op === 'note') return { op: 'note', val: before.note || '' };
    return null;                                                    // a memo stays: undo does not delete audio
  }
  function undo() {
    var d = load();
    for (var i = d.events.length - 1; i >= 0; i--) {
      var e = d.events[i];
      if (e.undone || e.undo_of !== undefined) continue;
      var inv = inverse(e, i);
      if (!inv) continue;
      e.undone = true;
      d.events.push({ t: now(), dev: DEV, src: e.src, sha: e.sha, op: inv.op, val: inv.val, undo_of: i });
      d.redo = d.redo || []; d.redo.push(i);
      save(); refresh(); return;
    }
  }
  function redo() {
    var d = load();
    if (!d.redo || !d.redo.length) return;
    var i = d.redo.pop(), e = d.events[i];
    if (!e) return;
    delete e.undone;
    d.events.push({ t: now(), dev: DEV, src: e.src, sha: e.sha, op: e.op, val: e.val, redo_of: i });
    save(); refresh();
  }
  function paintHistory(st) {
    var tb = document.querySelector('[data-history]');
    if (!tb) return;
    var d = load(), rows = d.events.map(function (e, i) { return [i, e]; }).reverse();
    tb.innerHTML = '';
    rows.forEach(function (pair) {
      var i = pair[0], e = pair[1], m = d.items[e.src] || {}, tr = document.createElement('tr');
      var what = e.op + (e.val === null || e.val === undefined || e.val === true ? '' : ': ' + String(e.val).slice(0, 80));
      var flag = e.undone ? ' <span class="tag">undone</span>' : e.undo_of !== undefined ? ' <span class="tag">undo</span>' : e.redo_of !== undefined ? ' <span class="tag">redo</span>' : '';
      var href = pieceLink(e.src, m);
      tr.innerHTML = '<td class="nowrap small">' + esc(e.t.slice(0, 16).replace('T', ' ')) + '<br><span class="muted">' + esc(e.dev) + '</span></td>' +
        '<td>' + esc(what) + flag + '</td><td>' + (href ? '<a href="' + esc(href) + '">' : '') + esc(m.title || e.src) + (href ? '</a>' : '') +
        '<br><span class="muted small">' + esc([m.site, m.section].filter(Boolean).join(' \u00b7 ')) + '</span></td><td class="small"></td>';
      tb.appendChild(tr);
    });
    var c = document.querySelector('[data-hist-count]');
    if (c) c.textContent = d.events.length + ' actions \u00b7 ' + ((d.redo || []).length) + ' to redo';
  }
  document.addEventListener('click', function (e) {
    if (e.target.closest('[data-undo]')) undo();
    if (e.target.closest('[data-redo]')) redo();
  });

  function select(r) { selected = r; refresh(); }

  // ------------------------------------------------------------------ the shared controls (list panel and page bars)
  function act(el, a) {
    var st = fold(), s = st[el.getAttribute('data-id')] || {};
    if (a === 'read') log(el, s.read ? 'unread' : 'read');
    else if (a === 'star') log(el, 'star', !s.star);
    else if (a === 'up') log(el, 'vote', s.vote === 'up' ? null : 'up');
    else if (a === 'down') log(el, 'vote', s.vote === 'down' ? null : 'down');
  }
  var noteTimers = {};
  function noteInput(el, ta) {
    var id = el.getAttribute('data-id');
    clearTimeout(noteTimers[id]);
    noteTimers[id] = setTimeout(function () {
      var s = fold()[id] || {};
      if ((s.note || '') !== ta.value) log(el, 'note', ta.value);
    }, 700);
  }
  var rec = null;
  function recordToggle(el, btn, status) {
    if (rec) { rec.stop(); return; }
    if (!navigator.mediaDevices || !window.MediaRecorder) { status.textContent = 'This browser cannot record here.'; return; }
    navigator.mediaDevices.getUserMedia({ audio: true }).then(function (stream) {
      var chunks = [], t0 = Date.now(), timer;
      rec = new MediaRecorder(stream);
      rec.ondataavailable = function (e) { if (e.data.size) chunks.push(e.data); };
      rec.onstop = function () {
        clearInterval(timer);
        stream.getTracks().forEach(function (t) { t.stop(); });
        var dur = Date.now() - t0, id = el.getAttribute('data-id');
        var blob = new Blob(chunks, { type: rec.mimeType || 'audio/webm' });
        rec = null;
        btn.classList.remove('rec');
        btn.lastChild.textContent = ' Record a voice memo';
        memoSave({ id: DEV + '-' + Date.now(), src: id, t: now(), dur: dur, blob: blob }, function (ok) {
          status.textContent = ok ? 'Memo kept on this device (' + fmtDur(dur) + ').' : 'Could not keep the memo: storage refused.';
          if (ok) log(el, 'memo', fmtDur(dur));
        });
      };
      rec.start();
      btn.classList.add('rec');
      timer = setInterval(function () { btn.lastChild.textContent = ' Recording ' + fmtDur(Date.now() - t0) + ': tap to stop'; }, 250);
      status.textContent = '';
    }, function () { status.textContent = 'No microphone permission: nothing was recorded.'; });
  }

  // ------------------------------------------------------------------ wiring
  if (root) {
    try {
      location.hash.slice(1).split('&').forEach(function (kv) {
        var p = kv.split('='); if (p[0] in f && p[1] !== undefined) f[p[0]] = decodeURIComponent(p[1]);
      });
    } catch (e) { /* ignore */ }
    var q = root.querySelector('[data-q]');
    q.value = f.q;
    q.addEventListener('input', function () { f.q = q.value; applyFilters(); });
    root.addEventListener('click', function (e) {
      var b = e.target.closest('button, a');
      if (b && b.hasAttribute('data-status')) { f.status = b.getAttribute('data-status'); return applyFilters(); }
      if (b && b.hasAttribute('data-site-f')) { f.site = b.getAttribute('data-site-f'); return applyFilters(); }
      if (b && b.hasAttribute('data-section-f')) { f.section = b.getAttribute('data-section-f'); return applyFilters(); }
      if (b && b.hasAttribute('data-reset')) { f = { q: '', status: 'all', site: 'all', section: 'all' }; q.value = ''; return applyFilters(); }
      var r = e.target.closest('.rl-row');
      if (!r) return;
      if (b && b.hasAttribute('data-act')) {
        var a = b.getAttribute('data-act');
        if (a === 'open') return select(r);
        return act(r, a);
      }
      if (b && b.classList.contains('rl-title')) {
        if (narrow.matches) { e.preventDefault(); return select(r); }
        var s = fold()[r.getAttribute('data-id')] || {};
        if (!s.read) log(r, 'read');
        return;
      }
      select(r);
    });
    var sel = document.querySelector('[data-sel]');
    sel.addEventListener('click', function (e) {
      var b = e.target.closest('[data-a]');
      if (!b || !selected) return;
      var a = b.getAttribute('data-a');
      if (a === 'close') { selected = null; return refresh(); }
      if (a === 'next') {
        var st = fold(), list = rows().filter(function (r) { return !r.hidden && !(st[r.getAttribute('data-id')] || {}).read; });
        var i = list.indexOf(selected);
        return select(list[i + 1] || list[0] || null);
      }
      if (a === 'memo') return recordToggle(selected, b, sel.querySelector('[data-f=memo-status]'));
      act(selected, a);
    });
    sel.querySelector('textarea').addEventListener('input', function (e) { if (selected) noteInput(selected, e.target); });
  }

  bars.forEach(function (b) {
    b.hidden = false;
    var s = fold()[b.getAttribute('data-id')] || {};
    if (!s.read) log(b, 'read');                     // opening the local copy is reading it
    b.addEventListener('click', function (e) {
      var x = e.target.closest('[data-a]');
      if (!x) return;
      var a = x.getAttribute('data-a');
      if (a === 'note') { var n = b.querySelector('.fb-note'); n.hidden = !n.hidden; if (!n.hidden) n.querySelector('textarea').focus(); return; }
      if (a === 'memo') return recordToggle(b, x, b.querySelector('[data-f=memo-status]'));
      act(b, a);
    });
    var ta = b.querySelector('textarea');
    if (ta) ta.addEventListener('input', function () { noteInput(b, ta); });
  });

  var dev = document.querySelector('[data-dev]');
  if (dev) {
    dev.addEventListener('click', function (e) {
      var b = e.target.closest('[data-d]');
      if (!b) return;
      var a = b.getAttribute('data-d'), msg = dev.querySelector('[data-f=dev-status]');
      if (a === 'copy' || a === 'copy-all') {
        var d = load(), text = exportText(a === 'copy-all'), last = d.events.length ? d.events[d.events.length - 1].t : '';
        copyText(text, function (ok) {
          if (ok) { d.cursor = last; save(); refresh(); }
          msg.textContent = ok ? 'Copied: paste it to Claude.' : 'The browser refused the clipboard: select the preview and copy it.';
        });
      } else if (a === 'download') {
        var blob = new Blob([exportText(true)], { type: 'text/markdown' }), url = URL.createObjectURL(blob), l = document.createElement('a');
        l.href = url; l.download = 'sgit-newsroom-feedback-' + DEV + '-' + now().slice(0, 10) + '.md';
        document.body.appendChild(l); l.click(); document.body.removeChild(l);
        setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
      } else if (a === 'paste') {
        var box = dev.querySelector('.rl-merge'); box.hidden = !box.hidden;
      } else if (a === 'merge') {
        var n = merge(dev.querySelector('.rl-merge textarea').value);
        msg.textContent = n < 0 ? 'No feedback JSON found in what was pasted.' : 'Merged ' + n + ' new events.';
      } else if (a === 'more') {
        dev.classList.toggle('open');
      }
    });
  }
  if (narrow.addEventListener) narrow.addEventListener('change', refresh);
  refresh();
})();

/* sgit newsroom: the side panel. Three tabs on the right edge of every page:
 *   Peek: a local link opened beside the page (an iframe of the local copy, so it works offline), with
 *         "open as the page"; links in a piece carry the reader's state (read, noted) as a small mark.
 *   Notes: the page's feedback bar, moved into the pane on wide screens.
 *   Chat: tier 0, a local matcher over the site's own search index (no key, works offline);
 *         tier 1, the reader's own OpenRouter key kept in this browser, a model with tools over the site
 *         (search, open a page, the reader's feedback, file feedback, what to read next). The key goes to
 *         openrouter.ai and nowhere else; when the call fails, tier 0 answers and says so.
 * The pane's width is dragged and remembered. No network request happens without the reader's action.
 */
(function () {
  'use strict';
  var ROOT = document.documentElement.getAttribute('data-root') || './';
  var KEYS = { open: 'sgit-newsroom.panel.open', tab: 'sgit-newsroom.panel.tab', w: 'sgit-newsroom.panel.w',
               key: 'sgit-newsroom.openrouter.key', model: 'sgit-newsroom.openrouter.model', chat: 'sgit-newsroom.chat.v1' };
  function get(k, d) { try { return localStorage.getItem(k) || d; } catch (e) { return d; } }
  function set(k, v) { try { localStorage.setItem(k, v); } catch (e) { /* ignore */ } }
  function esc(t) { return String(t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  var narrow = window.matchMedia && matchMedia('(max-width: 899px)').matches;
  if (narrow || !document.querySelector('main')) return;

  // ---------------------------------------------------------------- the pane
  var pane = document.createElement('aside');
  pane.className = 'pane';
  pane.innerHTML =
    '<div class="pane-handle" title="Drag to resize"></div>' +
    '<div class="pane-head"><div class="pane-tabs" role="tablist">' +
    '<button type="button" data-tab="peek" role="tab">Peek</button><button type="button" data-tab="notes" role="tab">Notes</button>' +
    '<button type="button" data-tab="chat" role="tab">Chat</button></div>' +
    '<button type="button" class="pane-close" aria-label="Close the panel">×</button></div>' +
    '<section class="pane-body" data-pane="peek"><p class="pane-hint">Click the ⧉ beside a local link in a piece to open it here, beside what you are reading. ' +
    'Marks on links: ✓ read, ✎ noted.</p><div class="peek-bar" hidden><a class="peek-open" href="#">Open as the page →</a><span class="peek-title"></span></div>' +
    '<iframe class="peek" title="The linked page" hidden sandbox="allow-scripts allow-same-origin allow-popups"></iframe></section>' +
    '<section class="pane-body" data-pane="notes" hidden><div class="pane-notes-slot"><p class="pane-hint">This page has no feedback bar.</p></div></section>' +
    '<section class="pane-body" data-pane="chat" hidden>' +
    '<div class="chat-log" aria-live="polite"></div>' +
    '<form class="chat-form"><textarea rows="2" placeholder="Ask about the network, or type feedback (start with “For the RiskMandate agent:” to relay it)"></textarea>' +
    '<div class="chat-row"><button type="submit" class="btn-p">Send</button><span class="chat-tier"></span></div></form>' +
    '<details class="chat-key"><summary>Your OpenRouter key (optional)</summary><p class="small">Tier 0 answers from the site’s own index, offline, with no key. ' +
    'With a key, a model answers with tools over the site. The key stays in this browser and is sent only to openrouter.ai; this page has no server. ' +
    'It is a trust decision, and it is yours.</p><label class="small">Key<input type="password" class="chat-keyin" autocomplete="off" placeholder="sk-or-..."></label>' +
    '<label class="small">Model<input type="text" class="chat-modelin" placeholder="openrouter/auto"></label>' +
    '<button type="button" class="btn-s chat-keysave">Save</button> <button type="button" class="btn-s chat-keyclear">Forget</button></details>' +
    '<p class="chat-cost small muted"></p></section>';
  var rail = document.createElement('div');
  rail.className = 'pane-rail';
  rail.innerHTML = '<button type="button" data-tab="peek" title="Peek a link beside the page">Peek</button>' +
    '<button type="button" data-tab="notes" title="Your notes on this page">Notes</button>' +
    '<button type="button" data-tab="chat" title="Ask the site">Chat</button>';
  document.body.appendChild(pane); document.body.appendChild(rail);
  document.documentElement.classList.add('has-pane');

  function openPane(tab) {
    document.documentElement.classList.add('pane-open');
    set(KEYS.open, '1');
    if (tab) { set(KEYS.tab, tab); }
    tab = get(KEYS.tab, 'peek');
    [].slice.call(pane.querySelectorAll('[data-pane]')).forEach(function (s) { s.hidden = s.getAttribute('data-pane') !== tab; });
    [].slice.call(document.querySelectorAll('[data-tab]')).forEach(function (b) { b.classList.toggle('on', b.getAttribute('data-tab') === tab); });
    if (tab === 'notes') moveNotes();
    if (tab === 'chat') initChat();
  }
  function closePane() { document.documentElement.classList.remove('pane-open'); set(KEYS.open, '0'); moveNotesBack(); }
  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-tab]'); if (t) { openPane(t.getAttribute('data-tab')); return; }
    if (e.target.closest('.pane-close')) closePane();
  });
  var w = parseInt(get(KEYS.w, '420'), 10); if (w >= 280 && w <= 900) document.documentElement.style.setProperty('--pane-w', w + 'px');
  (function drag() {
    var h = pane.querySelector('.pane-handle'), on = false;
    h.addEventListener('mousedown', function (e) { on = true; e.preventDefault(); document.body.classList.add('dragging'); });
    document.addEventListener('mousemove', function (e) { if (!on) return; var nw = Math.max(280, Math.min(900, window.innerWidth - e.clientX)); document.documentElement.style.setProperty('--pane-w', nw + 'px'); });
    document.addEventListener('mouseup', function (e) { if (!on) return; on = false; document.body.classList.remove('dragging'); set(KEYS.w, String(Math.max(280, Math.min(900, window.innerWidth - e.clientX)))); });
  })();

  // ---------------------------------------------------------------- peek: local links opened beside the page
  function idOf(href) {
    // the feedback log keys: a source page is sites/...md; a piece is <folder>/<slug>.md
    var p = href.split('#')[0].split('?')[0];
    p = p.replace(/^(\.\.\/)+/, '').replace(/^\.\//, '');
    if (p.indexOf('src/') === 0) { p = p.slice(4); return /\.html$/.test(p) ? p.replace(/\.html$/, '.md') : p; }
    if (/^(stories|editions|history|maps|signals)\/[^/]+\.html$/.test(p)) return p.replace(/\.html$/, '.md');
    return '';
  }
  function localHref(a) {
    var h = a.getAttribute('href') || '';
    return h && !/^([a-z]+:|#|\/\/)/i.test(h) && /\.html(#|$)/.test(h) ? h : '';
  }
  var article = document.querySelector('article.piece, article.source, .rl');
  if (article) {
    var st = {};
    try { var d = JSON.parse(localStorage.getItem('sgit-newsroom.feedback.v1') || 'null'); if (d && d.events) d.events.forEach(function (e) {
      var s = st[e.src] || (st[e.src] = {}); if (e.op === 'read') s.read = true; else if (e.op === 'unread') s.read = false; else if (e.op === 'note') s.note = !!e.val; }); } catch (e) { /* ignore */ }
    [].slice.call(article.querySelectorAll('a[href]')).forEach(function (a) {
      var h = localHref(a); if (!h || a.classList.contains('ext') || a.closest('.fb-bar')) return;
      var s = st[idOf(h)] || {};
      var mark = (s.read ? '✓' : '') + (s.note ? '✎' : '');
      var b = document.createElement('button'); b.type = 'button'; b.className = 'peek-btn'; b.title = 'Open beside this page';
      b.setAttribute('data-peek', h); b.textContent = '⧉' + mark;
      a.insertAdjacentElement('afterend', b);
    });
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-peek]'); if (!b) return;
    e.preventDefault(); openPane('peek');
    var fr = pane.querySelector('iframe.peek'), bar = pane.querySelector('.peek-bar');
    fr.hidden = false; bar.hidden = false; fr.src = b.getAttribute('data-peek');
    bar.querySelector('.peek-open').setAttribute('href', b.getAttribute('data-peek'));
    bar.querySelector('.peek-title').textContent = (b.previousElementSibling && b.previousElementSibling.textContent) || '';
  });

  // ---------------------------------------------------------------- notes: the page's feedback bar, in the pane
  var notesHome = null;
  function moveNotes() {
    var bar = document.querySelector('.fb-bar'); if (!bar || bar.closest('.pane')) return;
    notesHome = document.createComment('fb-bar home'); bar.parentNode.insertBefore(notesHome, bar);
    var slot = pane.querySelector('.pane-notes-slot'); slot.innerHTML = ''; slot.appendChild(bar); bar.classList.add('in-pane');
    var n = bar.querySelector('.fb-note'); if (n) n.hidden = false;
  }
  function moveNotesBack() {
    var bar = pane.querySelector('.fb-bar'); if (!bar || !notesHome) return;
    notesHome.parentNode.insertBefore(bar, notesHome); notesHome.parentNode.removeChild(notesHome); notesHome = null; bar.classList.remove('in-pane');
  }

  // ---------------------------------------------------------------- chat
  var chatReady = false, index = null, log = [];
  function initChat() {
    if (chatReady) return; chatReady = true;
    var form = pane.querySelector('.chat-form'), ta = form.querySelector('textarea');
    pane.querySelector('.chat-keyin').value = get(KEYS.key, '');
    pane.querySelector('.chat-modelin').value = get(KEYS.model, 'openrouter/auto');
    pane.querySelector('.chat-keysave').addEventListener('click', function () { set(KEYS.key, pane.querySelector('.chat-keyin').value.trim()); set(KEYS.model, pane.querySelector('.chat-modelin').value.trim() || 'openrouter/auto'); tier(); say('sys', 'Key saved in this browser.'); });
    pane.querySelector('.chat-keyclear').addEventListener('click', function () { try { localStorage.removeItem(KEYS.key); } catch (e) { } pane.querySelector('.chat-keyin').value = ''; tier(); say('sys', 'Key forgotten.'); });
    try { log = JSON.parse(localStorage.getItem(KEYS.chat) || '[]'); } catch (e) { log = []; }
    log.slice(-20).forEach(function (m) { say(m.role, m.text, true); });
    if (!log.length) say('sys', 'Ask about the network: "what changed on riskmandate.ai this week", "which pieces mention append lanes", "what should I read next". Or type feedback.');
    tier();
    ta.addEventListener('keydown', function (e) { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); form.requestSubmit(); } });
    form.addEventListener('submit', function (e) { e.preventDefault(); var q = ta.value.trim(); if (!q) return; ta.value = ''; ask(q); });
    loadIndex();
  }
  function tier() { pane.querySelector('.chat-tier').textContent = get(KEYS.key, '') ? 'tier 1 · ' + get(KEYS.model, 'openrouter/auto') : 'tier 0 · local matcher, offline'; }
  function say(role, text, silent) {
    var el = document.createElement('div'); el.className = 'chat-msg ' + role;
    el.innerHTML = renderText(text);
    var box = pane.querySelector('.chat-log'); box.appendChild(el); box.scrollTop = box.scrollHeight;
    if (!silent && role !== 'sys') { log.push({ role: role, text: text, t: new Date().toISOString() }); set(KEYS.chat, JSON.stringify(log.slice(-60))); }
    return el;
  }
  function renderText(t) {
    // links [title](path) become links relative to the site root; everything else is escaped text
    return esc(t).replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, function (m, a, b) { var h = /^https?:/.test(b) ? b : ROOT + b.replace(/^\//, ''); return '<a href="' + esc(h) + '">' + a + '</a>'; }).replace(/\n/g, '<br>');
  }
  function loadIndex(cb) {
    if (index) return cb && cb(index);
    if (window.SEARCH) { index = window.SEARCH; return cb && cb(index); }
    var s = document.createElement('script'); s.src = ROOT + 'search/data.js';
    s.onload = function () { index = window.SEARCH || []; if (cb) cb(index); };
    s.onerror = function () { index = []; if (cb) cb(index); };
    document.head.appendChild(s);
  }
  // ---- tools (tier 0 and tier 1 share them)
  function feedbackLog() { try { return JSON.parse(localStorage.getItem('sgit-newsroom.feedback.v1') || 'null') || { events: [], items: {} }; } catch (e) { return { events: [], items: {} }; } }
  var tools = {
    search: { description: 'Search the newsroom and the snapshot by words. Returns up to 10 pages: title, path, site and an excerpt.',
      parameters: { type: 'object', properties: { query: { type: 'string' } }, required: ['query'] },
      run: function (a, cb) { loadIndex(function (ix) { cb(match(ix, a.query, 10).map(function (r) { return { title: r[0], path: r[1], site: r[2], kind: r[3], excerpt: r[4].slice(0, 240) }; })); }); } },
    open_page: { description: 'Read a page of the site as markdown (its .md twin). Path as returned by search. Works when the site is served over http(s), not from file://.',
      parameters: { type: 'object', properties: { path: { type: 'string' } }, required: ['path'] },
      run: function (a, cb) {
        if (location.protocol === 'file:') return cb({ error: 'The site is open from file://: pages cannot be read by the chat here. Open the path in the Peek tab instead.', path: a.path });
        var p = String(a.path).replace(/^\//, '').replace(/\.html$/, '.md');
        fetch(ROOT + p).then(function (r) { return r.ok ? r.text() : Promise.reject(r.status); }).then(function (t) { cb({ path: p, markdown: t.slice(0, 12000) }); })
          .catch(function (err) { cb({ error: 'could not read ' + p + ' (' + err + ')' }); });
      } },
    my_feedback: { description: 'The reader’s own feedback on this device: what they marked read, starred, voted, noted; the last 40 events.',
      parameters: { type: 'object', properties: {} },
      run: function (a, cb) { var d = feedbackLog(); cb({ events: d.events.slice(-40), items: d.items }); } },
    file_feedback: { description: 'File feedback from the reader on a page: a note (kept on the device, keyed by the page path), or a relayed message when addressed to another site’s agent (starts with "For the <site> agent:").',
      parameters: { type: 'object', properties: { path: { type: 'string', description: 'the page path (search result path) or "chat" when about no page' }, text: { type: 'string' } }, required: ['text'] },
      run: function (a, cb) {
        var d = feedbackLog(), src = idOf(a.path || '') || (a.path || 'chat'), now = new Date().toISOString().replace(/\.\d+Z$/, 'Z');
        var relay = /^for (the )?([a-z0-9.\- ]+?) agent:/i.exec(a.text || '');
        d.items[src] = d.items[src] || { title: a.path || 'chat', site: '', section: 'chat', date: now.slice(0, 10), page: '' };
        d.events.push({ t: now, dev: get('sgit-newsroom.device', 'chat'), src: src, sha: '', op: relay ? 'relay' : 'note', val: a.text, to: relay ? relay[2].trim() : undefined });
        try { localStorage.setItem('sgit-newsroom.feedback.v1', JSON.stringify(d)); } catch (e) { }
        cb({ filed: true, kind: relay ? 'relay to ' + relay[2].trim() : 'note', hint: 'It is in the device log; "Copy for Claude" on the reading room carries it out.' + (relay ? ' A relayed message lands on the target site’s briefing page when the log is filed.' : '') });
      } },
    read_next: { description: 'Pieces of the newsroom the reader has not marked read, newest first (up to 8).',
      parameters: { type: 'object', properties: {} },
      run: function (a, cb) { loadIndex(function (ix) { var d = feedbackLog(), read = {}; d.events.forEach(function (e) { if (e.op === 'read') read[e.src] = true; if (e.op === 'unread') read[e.src] = false; });
        var out = ix.filter(function (r) { return r[3] === 'newsroom' && /^(stories|editions|history|maps|signals)\//.test(r[1]) && !read[r[1].replace(/\.html$/, '.md')]; })
          .sort(function (a, b) { return b[1].localeCompare(a[1]); }).slice(0, 8).map(function (r) { return { title: r[0], path: r[1] }; }); cb(out); }); } }
  };
  function match(ix, q, n) {
    var ws = String(q).toLowerCase().split(/\s+/).filter(function (w) { return w.length > 2; }), hits = [];
    ix.forEach(function (r) { var ti = r[0].toLowerCase(), tx = (r[2] + ' ' + r[4]).toLowerCase(), s = 0;
      ws.forEach(function (w) { if (ti.indexOf(w) >= 0) s += 10; else if (tx.indexOf(w) >= 0) s += 1; });
      if (s) hits.push([s + (r[3] === 'newsroom' ? 3 : 0), r]); });
    hits.sort(function (a, b) { return b[0] - a[0]; });
    return hits.slice(0, n).map(function (h) { return h[1]; });
  }
  function ask(q) {
    say('user', q);
    var relay = /^for (the )?([a-z0-9.\- ]+?) agent:/i.exec(q);
    if (relay || /^(feedback|note):/i.test(q)) {
      tools.file_feedback.run({ path: document.querySelector('.fb-bar') ? document.querySelector('.fb-bar').getAttribute('data-page') : 'chat', text: q.replace(/^(feedback|note):\s*/i, '') },
        function (r) { say('bot', 'Filed as a ' + r.kind + '. ' + r.hint); });
      return;
    }
    if (get(KEYS.key, '')) return askModel(q);
    tier0(q);
  }
  function tier0(q, prefix) {
    loadIndex(function (ix) {
      if (/read next|what next|what should i read/i.test(q)) {
        return tools.read_next.run({}, function (out) { say('bot', (prefix || '') + (out.length ? 'Not yet read, newest first:\n' + out.map(function (r) { return '- [' + r.title + '](' + r.path + ')'; }).join('\n') : 'You have read every piece.')); });
      }
      var hits = match(ix, q, 6);
      say('bot', (prefix || '') + (hits.length ? 'From the site’s index (tier 0, matched on words in the title and the opening):\n' + hits.map(function (r) { return '- [' + r[0] + '](' + r[1] + ') · ' + r[2]; }).join('\n') : 'Nothing in the index matches those words. Try fewer, or different, words.'));
    });
  }
  function askModel(q) {
    var key = get(KEYS.key, ''), model = get(KEYS.model, 'openrouter/auto');
    var sys = 'You are the sgit newsroom’s assistant, on a static site that reads the sgit network. Answer from the site: use the tools ' +
      '(search first, then open_page for detail) and cite pages as markdown links [title](path). British English, plain, short. If the reader gives feedback or a message for another site’s agent, call file_feedback. ' +
      'Current page: ' + (document.title || '') + '.';
    var msgs = [{ role: 'system', content: sys }].concat(log.slice(-8).map(function (m) { return { role: m.role === 'bot' ? 'assistant' : 'user', content: m.text }; }));
    var defs = Object.keys(tools).map(function (n) { return { type: 'function', function: { name: n, description: tools[n].description, parameters: tools[n].parameters } }; });
    var el = say('bot', '…'), usage = null, rounds = 0;
    function step() {
      fetch('https://openrouter.ai/api/v1/chat/completions', { method: 'POST', headers: { 'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json', 'HTTP-Referer': 'https://sgit.newsroom.sgit.ai', 'X-Title': 'sgit newsroom' },
        body: JSON.stringify({ model: model, messages: msgs, tools: defs, tool_choice: 'auto' }) })
        .then(function (r) { return r.ok ? r.json() : r.text().then(function (t) { throw new Error(r.status + ' ' + t.slice(0, 200)); }); })
        .then(function (j) {
          usage = j.usage || usage; var m = j.choices && j.choices[0] && j.choices[0].message; if (!m) throw new Error('empty reply');
          if (m.tool_calls && m.tool_calls.length && rounds < 4) {
            rounds++; msgs.push(m); var left = m.tool_calls.length;
            m.tool_calls.forEach(function (tc) {
              var name = tc.function.name, args = {}; try { args = JSON.parse(tc.function.arguments || '{}'); } catch (e) { }
              el.innerHTML = renderText('… ' + name + '(' + (args.query || args.path || '') + ')');
              (tools[name] ? tools[name].run : function (a, cb) { cb({ error: 'no such tool' }); })(args, function (out) {
                msgs.push({ role: 'tool', tool_call_id: tc.id, name: name, content: JSON.stringify(out).slice(0, 16000) });
                if (--left === 0) step();
              });
            });
            return;
          }
          var text = m.content || '(no text)'; el.innerHTML = renderText(text);
          log.push({ role: 'bot', text: text, t: new Date().toISOString() }); set(KEYS.chat, JSON.stringify(log.slice(-60)));
          if (usage) pane.querySelector('.chat-cost').textContent = model + ' · ' + (usage.prompt_tokens || 0) + ' in, ' + (usage.completion_tokens || 0) + ' out tokens this reply';
        })
        .catch(function (err) { el.remove(); tier0(q, 'The model call failed (' + err.message.slice(0, 120) + '); falling back to tier 0.\n'); });
    }
    step();
  }

  if (get(KEYS.open, '0') === '1') openPane();
})();

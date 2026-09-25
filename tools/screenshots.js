// Screenshots of the live pages the desks cite, so a piece can show the page it talks about (principle 9).
//   node tools/screenshots.js            # every live URL in the sources: front matter of stories, editions, signals, history, maps
//   node tools/screenshots.js --all      # also every page in data/index.json (slow)
// Needs the network and Playwright; not part of the standard-library build. Writes assets/shots/<host>/<path>.jpg
// (1200x750, jpeg, top of the page) and assets/shots/manifest.json with the capture time; the build shows a thumbnail
// in a piece's byline for each of its sources that has one. Re-run to refresh; a URL that fails is recorded and skipped.
const fs = require('fs'), path = require('path');
let pw; try { pw = require('playwright'); } catch (e) { pw = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright'); }
const ROOT = path.join(__dirname, '..'), OUT = path.join(ROOT, 'assets', 'shots'), MAN = path.join(OUT, 'manifest.json');
const urls = new Set();
for (const d of ['stories', 'editions', 'signals', 'history', 'maps', 'briefings']) {
  const base = path.join(ROOT, d); if (!fs.existsSync(base)) continue;
  for (const n of fs.readdirSync(base)) {
    if (!n.endsWith('.md')) continue;
    const t = fs.readFileSync(path.join(base, n), 'utf8'), fm = t.startsWith('---\n') ? t.split('\n---')[0] : '';
    for (const m of fm.matchAll(/^\s+-\s+(https?:\/\/\S+)/gm)) urls.add(m[1].replace(/\.md$/, '.html'));
  }
}
if (process.argv.includes('--all')) for (const e of JSON.parse(fs.readFileSync(path.join(ROOT, 'data', 'index.json'), 'utf8'))) urls.add(e.live);
const manifest = fs.existsSync(MAN) ? JSON.parse(fs.readFileSync(MAN, 'utf8')) : {};
const fileFor = (u) => { const x = new URL(u); let p = x.pathname.replace(/\/$/, '/index.html').replace(/^\//, '') || 'index.html'; return path.join(x.host, p.replace(/\.(html|md)$/, '') + '.jpg'); };
(async () => {
  // One long-lived browser wears the network out (tunnels close mid-exchange after a few dozen pages), so the context is
  // recycled every 10 pages, third-party requests are blocked, and a failed URL gets one retry on a fresh context.
  const b = await pw.chromium.launch(); let ctx, p, n = 0, ok = 0, bad = 0;
  const fresh = async () => {
    if (ctx) await ctx.close().catch(() => {});
    ctx = await b.newContext({ viewport: { width: 1200, height: 750 }, deviceScaleFactor: 1, ignoreHTTPSErrors: true });
    await ctx.route('**/*', (route, req) => {
      const h = new URL(req.url()).host, own = new URL(req.frame().url() || 'about:blank').host;
      (req.resourceType() === 'document' || h === own || /(^|\.)sgit\.ai$|(^|\.)riskmandate\.ai$/.test(h)) ? route.continue() : route.abort();
    });
    p = await ctx.newPage();
  };
  const shoot = async (u, file) => {
    const r = await p.goto(u, { waitUntil: 'commit', timeout: 15000 });
    if (!r || r.status() >= 400) throw new Error('HTTP ' + (r && r.status()));
    await p.waitForLoadState('domcontentloaded', { timeout: 8000 }).catch(() => {});
    await p.waitForTimeout(500);
    fs.mkdirSync(path.dirname(file), { recursive: true });
    await p.screenshot({ path: file, type: 'jpeg', quality: 60, clip: { x: 0, y: 0, width: 1200, height: 750 } });
  };
  await fresh();
  for (const u of [...urls].sort()) {
    const rel = fileFor(u), file = path.join(OUT, rel);
    if (manifest[u] && manifest[u].ok && fs.existsSync(file) && !process.argv.includes('--refresh')) continue;
    if (++n % 10 === 0) await fresh();
    try {
      try { await shoot(u, file); } catch (e) { await fresh(); await shoot(u, file); }
      manifest[u] = { ok: true, file: 'assets/shots/' + rel.split(path.sep).join('/'), taken: new Date().toISOString().slice(0, 16) + 'Z' }; ok++;
    } catch (e) { manifest[u] = { ok: false, error: String(e.message).split('\n')[0].slice(0, 80), taken: new Date().toISOString().slice(0, 16) + 'Z' }; bad++; }
    fs.mkdirSync(OUT, { recursive: true }); fs.writeFileSync(MAN, JSON.stringify(manifest, null, 1));   // saved after every page
    console.log(`${ok} taken, ${bad} failed of ${urls.size}: ${u}`);
  }
  console.log(`\nscreenshots: ${ok} taken, ${bad} failed, ${Object.keys(manifest).length} in the manifest`); await b.close();
})();

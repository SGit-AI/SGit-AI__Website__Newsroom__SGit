// Open every page with a diagram in a real browser, offline, and report any Mermaid diagram that did not render.
//   node tools/check_diagrams.js [site-dir]        (needs Playwright; not part of the standard-library build)
const path = require('path'), fs = require('fs');
let pw; try { pw = require('playwright'); } catch (e) { pw = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright'); }
const site = path.resolve(process.argv[2] || process.env.NEWSROOM_SITE_OUT || path.join(__dirname, '..', 'site'));
const pages = [];
(function walk(d) { for (const n of fs.readdirSync(d)) { const f = path.join(d, n);
  if (fs.statSync(f).isDirectory()) { if (n !== 'src') walk(f); } else if (n.endsWith('.html') && fs.readFileSync(f, 'utf8').includes('class="mermaid"')) pages.push(f); } })(site);
(async () => {
  const b = await pw.chromium.launch(); const p = await (await b.newContext({ offline: true })).newPage();
  let bad = 0;
  for (const f of pages) {
    await p.goto('file://' + f); await p.waitForTimeout(1500);
    const r = await p.evaluate(() => [...document.querySelectorAll('pre.mermaid')].map((e, i) =>
      e.textContent.includes('Syntax error') ? 'diagram ' + (i + 1) + ': syntax error' : (e.querySelector('svg') ? '' : 'diagram ' + (i + 1) + ': not rendered')).filter(Boolean));
    if (r.length) { bad += r.length; console.log('FAIL', path.relative(site, f), r.join('; ')); } else console.log('ok  ', path.relative(site, f));
  }
  await b.close(); console.log(`diagrams: ${pages.length} pages checked, ${bad} failures`); process.exit(bad ? 1 : 0);
})();

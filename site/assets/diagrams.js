/* Renders the Cartographer's maps with the bundled Mermaid: no network, strict security (no HTML or
   scripts from diagram text), and a theme that follows the reader's light or dark setting. */
(function () {
  if (!window.mermaid) return;
  var dark = window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches;
  mermaid.initialize({ startOnLoad: true, securityLevel: 'strict', theme: dark ? 'dark' : 'neutral',
                       fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif' });
})();

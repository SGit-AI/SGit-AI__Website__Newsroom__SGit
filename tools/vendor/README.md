# Vendored: Mermaid

`mermaid.min.js` is Mermaid 12.0.0 (MIT licence, `mermaid.LICENSE`), the UMD build from the npm package's
`dist/`, copied unchanged so the Cartographer's maps render with the network off. The build copies it to
`site/assets/mermaid.min.js` and loads it only on pages that have a diagram. It is the one file in the site
that is not built from this repository's sources; it makes no network request when rendering.

sha256: `28fca7ae6ebc7ed7bb63bde63136a74bfef14f296a57e403657eeb8b32836073`

To upgrade: `npm pack mermaid@<version>`, copy `package/dist/mermaid.min.js` and `package/LICENSE` here,
update this file and the sha256, rebuild, and open every page under `site/maps/` to check each map still renders.

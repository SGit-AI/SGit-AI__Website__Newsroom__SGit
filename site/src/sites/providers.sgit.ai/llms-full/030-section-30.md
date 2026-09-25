## What adding a provider actually takes

The ElevenLabs site proved this by carrying a stub of the next one: **a provider page is one Markdown file with front-matter**, and the comparison follows from it. At the hub level, adding a site to this family is:

1. **A repository**, from the same template — the build system, the gate and the release pipeline are the same files.
2. **A `patterns:` block** in its report's front-matter, per product. That is what this hub syncs.
3. **A row in `data/providers.yml`**, added by running `bin/sync-providers.py` rather than typed.

**No template surgery, and no edit to the comparison page.** If adding the second provider requires either, the contract is wrong and the fix belongs in the contract rather than in the page.

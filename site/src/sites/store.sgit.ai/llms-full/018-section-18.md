## The structure it will open into

The shape is already specified and the build already follows half of it: one index,
one folder per pack, a `pack.json` manifest with hashes, and **compiled files
rather than one file per record** — because the published performance cliffs
punish thousands of small objects, and a cold open of 2,375 objects was measured at
over three minutes.

```
  /dev-packs/
    index.html          this page — the list of packs, with date, count and state
    pack.json           the manifest, machine-readable      ← published today
    llms.txt            per the estate convention
    llms-full.txt       the quotation set, the gaps, the open questions
    /store/             this pack — held
```

**Two things are already decided and neither is a formatting question.** A
published pack is **frozen, not maintained**: a dated document with hashes is a
promise about a moment, and a pack that gets quietly updated breaks that promise —
so new versions are added beside, never over. And whether packs from other days
and other subjects follow this one is **a separate decision with a much larger
surface**, not an extension of this instruction.

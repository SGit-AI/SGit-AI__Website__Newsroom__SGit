## The second axis: what the tool keeps

The four patterns are a property of **the provider**. There is a second axis and it is a property of **your tool**: what state it keeps. It decides whether the tool works for somebody with no key at all, and whether it survives being downloaded and run somewhere else.

| Tier | What it keeps | Works with no key? | Survives being downloaded? |
|---|---|---|---|
| **1** | Nothing. A pure function in a page | **Yes** | Yes, completely |
| **2** | This browser's `localStorage`, on this device | No | Yes, and it carries no key with it |
| **3** | A vault, which holds the key the page never sees | Yes — the *vault* holds it | **No.** A vault app's calls fail on a static host, because the key is sealed to its owner |

**The intersection is one sentence:** a tier-two tool holding a key in `localStorage` is **pattern 0 with a ceiling**, and a tier-three tool is **pattern 3**. Said once, the two axes stop competing to explain the same thing.

**And the honest finding is the empty corner.** Across this family, tier three has no working tool: the pattern the argument recommends is the one it has not yet demonstrated. That is a state the ledger has a word for, and the pages use it rather than avoiding the subject.

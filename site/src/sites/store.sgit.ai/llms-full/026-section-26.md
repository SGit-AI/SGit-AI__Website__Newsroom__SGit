## Why the catalogue is not inside the payment provider

**Sixty-two product codes maintained in two places is sixty-two codes that will one
day disagree.** The catalogue lives here, in one file, checked on every build. The
provider takes an amount and a reference. Neither side has to know about the
other, and there is no synchronisation to get wrong.

It also means **adding a product is a build**, not a build plus a console.

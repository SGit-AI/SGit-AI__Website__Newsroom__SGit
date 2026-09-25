## A discount code, and why there is nowhere to type one

**A code arrives in the address, not in a field.** There is no text input anywhere
in this site's output and the gate refuses one, so a code is handed over the way a
printed card or a QR at a stand hands it over anyway: `store.sgit.ai/policies/?code=…`.
The store recognises it, shows it as a chip that can be removed, and **takes it back
out of the address bar**, because a screenshot of a checkout should not carry one.

**What ships is the hash of the code and never the code.** A page that recognised a
code by carrying it would publish it the moment it was built, so the browser hashes
what it was handed and compares — and a build check reads every byte of the built
site against every code and fails the release if one is found, which is the same
rule, with the same test behind it, as *no vault key on any page*.

**That is worth what it is worth and no more.** A nine-character code can be ground
out of a hash. What actually stops a stranger paying nothing is that **a browser does
not take money**: a recognised code changes the amount a payment link is issued
*for*, and the rail decides what is charged. No rail exists yet.
{{claim:discount-code-is-in-the-browser}}

**It comes off the price, and the deposit is taken on what is left.** Half off the
£500 level is £250, of which £50 is taken now and £200 on delivery; a code never
moves the split, which belongs to the offer. **A code at a hundred per cent still
places an order** and still lands on the page that says what happens next — which is
the whole use of one, and how this flow gets walked end to end before a single real
payment link exists.

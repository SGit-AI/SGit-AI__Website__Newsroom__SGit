## The argument, in one paragraph

Vendor documentation tells you what an API does. It does not tell you **what it cost on a named workload on a named date**, **what broke**, or **which credential patterns the product can actually support** — and the third one is the question that decides your architecture. A site in this family exists to answer those three, per provider, with every claim carrying the state that says how far it can be trusted.

The strongest form of the answer is a pattern rather than a rule: *a browser application can use a paid API without ever holding the key, because a host holds it and enforces the terms.* That is [pattern three](/patterns/), it is [specified and not shipped](/contract/) {{claim:sg-tts-spec}}, and saying so is the point.

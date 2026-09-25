## How this table is made

Each provider site publishes two things for its own purposes: **the markdown twin of its report**, which carries a `patterns:` block in its front-matter, and **the claim index** its own search pane matches against. `bin/sync-providers.py` reads both and writes `data/providers.yml`; the build reads that file and never touches the network.

That is deliberate in three ways:

- **A sync is a dated act.** The date is printed under the table, and CI does not silently refresh it. If the data is stale, the staleness is visible rather than guessed at.
- **The build is reproducible and offline.** A site whose build depends on the network is a site that breaks when somebody else deploys.
- **There is one source of truth per fact, and it is not here.** A hub that maintains its own table of other people's properties will drift from them, and it will be the hub that is wrong.

`bin/sync-providers.py --check` reports drift without changing anything, which is the form CI could take if this ever needs to be automatic.

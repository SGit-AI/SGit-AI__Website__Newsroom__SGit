## The sync is not part of the build

`bin/sync-providers.py` refreshes `data/providers.yml` from the provider sites. **It is never run by CI**, because a build that reaches the network is a build that breaks when somebody else deploys, and because a sync should be a dated act rather than a silent one. `--check` reports drift without changing anything.

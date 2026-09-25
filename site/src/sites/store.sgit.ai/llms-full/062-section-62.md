## Why the groups are a view and not a range

**Because the alternative is how an offer list grows without anybody deciding to
grow it.** Three audiences, three pages, and within a month each page has a thing
of its own on it that nobody priced, nobody specified, and nobody can say the
state of.

So the grouping is mechanical. `data/buyers.yml` names offer ids and nothing else;
the build joins them to `data/offers.yml`; and the gate fails the release if a
group names an offer that does not exist, if an offer belongs to no group, or if
the set of groups changes. **A buyer page cannot contain a product**, in the same
way [the eight further offers](/catalogue/) cannot quietly widen the four that are
for sale.

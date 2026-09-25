# `identity`

credentials and who the agent can act as

> **A node carries no inherent meaning.** What `identity` means here emerges from the edges traceable from it, and confidence in that meaning is proportional to how richly it is connected. It is connected to **3 of 23 primitives** here. That, and not the sentence above, is what it means. [The discipline this follows](https://graphs.sgit.ai/).



## The 3 primitives with this family

| Primitive | Published gloss | Spelled out | Undo | In how many shapes |
|---|---|---|---|---|
| [`authenticate-as.credential.tenant`](../../../../model/capabilities/authenticate-as.credential.tenant/index.md) | Act in accounts with the credentials it holds | [`authenticate-as`](../../../../model/lexicon/verbs/authenticate-as/index.md)`.`[`credential`](../../../../model/lexicon/objects/credential/index.md)`.`[`tenant`](../../../../model/lexicon/reaches/tenant/index.md) | no | 15 of 17 |
| [`grant.credential.self`](../../../../model/capabilities/grant.credential.self/index.md) | Change its own permission settings | [`grant`](../../../../model/lexicon/verbs/grant/index.md)`.`[`credential`](../../../../model/lexicon/objects/credential/index.md)`.`[`self`](../../../../model/lexicon/reaches/self/index.md) | yes | 3 of 17 |
| [`read.credential.host`](../../../../model/capabilities/read.credential.host/index.md) | Read credentials stored where it runs | [`read`](../../../../model/lexicon/verbs/read/index.md)`.`[`credential`](../../../../model/lexicon/objects/credential/index.md)`.`[`host`](../../../../model/lexicon/reaches/host/index.md) | no | 11 of 17 |

## How this node connects

| Edge | Reads as | To |
|---|---|---|
| `family_of` | `identity` is the family of these 3 primitives | 3 capabilities |
| `in_family` | the inverse, walked the other way, with different fan out | one capability at a time |

[This node as JSON](../../../../data/lexicon/families/identity.json) · [The lexicon](../../../../model/lexicon/index.md) · [The edge vocabulary](../../../../model/graph/edges/index.md)

---

*[Site index for agents](../../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/lexicon/families/identity/index.html)*


------------------------------------------------------------------------

<!-- https://abp.sgit.ai/model/lexicon/families/money/index.html -->

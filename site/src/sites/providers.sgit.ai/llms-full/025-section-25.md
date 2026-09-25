## The four

{{claim:patterns-canonical}}

| # | Pattern | Where the credential lives | What bounds it | Verdict |
|---|---|---|---|---|
| **0** | **Key in the page** | In the delivered application | **Nothing** | **Never.** Anybody who opens the page has the key and the account. A plan quota is a ceiling, not a bound: it belongs to the whole account |
| **1** | **Bounded key** in the page | In the page, provisioned per user with a spending limit and a reset | **Money, and a reset window** | Acceptable where the platform can mint one. The limit *is* the blast radius, so choosing the number is a risk decision rather than a default |
| **2** | **Short-lived token** | Not in the page. A server exchanges the real key for a token with a short life | **Time, and the server's policy** | The standard answer — and it needs a server: the vendor's, if it offers one for that product, otherwise yours |
| **3** | **Host holds the key** | Never in the application. The application asks a host, which holds the key and enforces the terms | **The host, which the application cannot reach** | The strongest, and this estate's own: the only pattern where the bounded thing cannot reach the bounding thing |

**The ladder is not a maturity model.** Pattern 1 with a $5 limit can be a better answer than pattern 2 with a badly-scoped minter. The question is always *what is the blast radius, and who chose it.*

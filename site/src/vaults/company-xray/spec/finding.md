# A finding

A finding is one statement a customer can act on, with the evidence under it. It is the unit the business sells, the reviewer checks, and the customer keeps asking about in Claude.

```json
{
 "id": "F05",
 "area": "Customers",
 "label": "inferred",
 "title": "One sentence, the finding itself.",
 "detail": "A short paragraph: the figures, the dates, the documents, and what is not known.",
 "evidence": [{"file": "inbox/customers.csv", "where": "row 'Calder Retail Group'", "text": "the value or quote"}],
 "so_what": "Why it matters to this company, in one or two sentences.",
 "action": "What to do, specific enough to be done.",
 "owner": "A role, never a named individual chosen by us.",
 "checks": {"figure_name": "value"}
}
```

## The three labels

| Label | Means | The reader should |
|---|---|---|
| **read** | Stated in a document the customer sent. Quoted, with where. | Trust it as much as they trust their own document. |
| **computed** | Arithmetic on the customer's data. Every figure in `checks` is re-run by a script and must match. | Trust the arithmetic, and question the data. |
| **inferred** | A reading of two or more documents together. | Check it before acting. Most of the value is here, and so are most of the mistakes. |

## Rules

- **The title is the finding.** A reader who reads only titles should get the X-ray.
- **Say what is not known**, inside the finding, not in a disclaimer at the end.
- **No finding without evidence.** A finding whose evidence is "general experience" is advice, and advice goes in the handover call, not in the X-ray.
- **Invented, public and customer facts are never mixed without saying which is which.** A public source is cited by URL.
- **Personal data stays out of findings.** Roles, not people, unless the customer's own document names them and the name is needed.

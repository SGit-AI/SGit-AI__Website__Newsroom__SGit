# A vault per material risk

A material risk earns a vault of its own. The vault is the evidence pack of governance: the facts and their sources, the controls, the decisions, and the history, versioned, hash-chained and encrypted, readable by each audience with its own key.

## Layout

```
risk/
  risk.json            the statement, the chain of holders, facts, controls
  record.jsonl         the acceptance record, one decision per line, hash-chained
  facts/               one file per fact: what it says, where it came from, when observed
  evidence/            the source material: exported configs, log extracts, screenshots, hashes
  controls/            one file per control: what it does, its state, what enforces it
  decisions/           the signed acceptance for each interval, and any funding decision
  incidents/           incident timelines that became facts
  index.html           a viewer, like the one in this vault
```

## Keys

- **The holder and the risk engineer** hold write access.
- **The holder's chain up to the board** receives a read key. They see the risk arrive with its evidence.
- **The auditor and the insurer** receive their own read keys when they need them, and nothing else.
- **The GRC platform** stores a link to the vault on the register row, and the read key where the platform can hold secrets. It never receives the vault key.

## Why a vault and not an attachment

An attachment in a GRC platform is a copy with no history. A vault keeps every version of every fact and decision, proves the record was not altered after the fact, travels as one read key, and stays readable if the client changes GRC platform. It is also fractal: a corporate risk's vault can link to the vaults of the business, operational and technical risks beneath it.

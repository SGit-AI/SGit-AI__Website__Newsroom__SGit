## What makes it possible

**CORS is on, and it was verified rather than assumed.** On 16 September 2026,
`https://riskmandate.ai/abp-vaults.html` answered `access-control-allow-origin: *`.
So a page on this domain can read a file on that one, in the reader's browser,
with no server on either side.

**That is not yet used, and the reason is a rule rather than an oversight.** Every
page on this site that sells anything opens no network connection at all, and a
build check fails the release if one does. Reading a catalogue over CORS is opening
a connection on a selling page. That rule has been narrowed twice and loosened
never — the absolute half stayed absolute, the exception was named in the check,
and a deliberate break was run against the new check before anything shipped. The
same discipline applies here, and the narrowing comes **before** the first fetch.

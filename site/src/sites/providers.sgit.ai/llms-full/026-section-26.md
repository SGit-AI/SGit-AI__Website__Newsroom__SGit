## Why pattern three is different in kind

Patterns 0 to 2 all end with a credential in the hands of the code that spends it — for a moment in pattern 2, for good in pattern 0. Pattern 3 does not: the application asks for a **result**, and the host holds the credential, applies the terms, and returns only the output.

In this estate the vault host already does that for a model call: the app frame never sees the key and cannot read the sealed config under any grant it can be given, and the terms — allowed models, spend cap per session, per-app overrides — live in the vault with the content they govern. **The terms travel with the data**, so a vault shared read-only carries neither the key nor the ability to spend against it.

Whether that generalises past a model call is the open question this family exists to answer. For a voice API the answer is written down and not yet built {{claim:sg-tts-spec}}.

# Installation

Pure Python, two runtime dependencies. Python 3.11 or newer.

```
$ pip install sgit-ai
# or, on externally-managed systems:
$ pipx install sgit-ai
```

This installs two entry points: `sgit` and `sgit-ai` (they are identical, use whichever you like).

## Verify

```
$ sgit version
sgit-ai v0.14.x
$ sgit doctor
✓ remote reachable   ✓ TLS ok   ✓ config valid
```

`sgit doctor` checks connectivity and configuration and prints per-OS fix instructions for the common problems (including SSL certificate issues). Add `--json` if a script or an agent is doing the checking.

## Upgrade

```
$ sgit update   # wraps pip install --upgrade sgit-ai
```

[← What is sgit](what-is-sgit.md)[Quickstart →](quickstart.md)



==============================================================================
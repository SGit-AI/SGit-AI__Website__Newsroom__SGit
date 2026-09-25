# 04 — Bash, and the generated-shell pattern

**There are five `.sh` files in a 217,000-line repository.** That is the finding. Shell is not written here — it is **generated from typed Python**, and the pattern is original enough to be the site's most interesting infrastructure page.

---

## 1. Where shell actually lives

| Location | What |
|---|---|
| **`sg_compute/platforms/ec2/user_data/`** | **15 `Section__*` classes** that render shell fragments. This is where nearly all shell in the estate lives |
| `docker/` | Dockerfiles (`host-control`, `local-claude`) and their `RUN` lines |
| `.github/workflows/` | inline `run:` blocks |
| `scripts/` | a handful of `.sh` and Python CLI shims |

---

## 2. The `Section__*` pattern

`sg_compute/platforms/ec2/user_data/Section__Shutdown.py`, verbatim and entire:

```python
# ═══════════════════════════════════════════════════════════════════════════════
# Ephemeral EC2 — Section__Shutdown
# Schedules auto-termination via systemd-run. Paired with
# InstanceInitiatedShutdownBehavior=terminate in EC2__Launch__Helper so that
# halt causes termination, not stop.
# max_hours=0 emits a no-op comment (caller omits this section instead).
# ═══════════════════════════════════════════════════════════════════════════════

from osbot_utils.type_safe.Type_Safe import Type_Safe

TEMPLATE = '''
# ── Auto-terminate after {max_hours}h ({seconds}s) ───────────────────────────
systemd-run --on-active={seconds}s /sbin/shutdown -h now
echo "[ephemeral-ec2] auto-terminate timer set: {max_hours}h ({seconds}s) from now"
'''


class Section__Shutdown(Type_Safe):

    def render(self, max_hours: float = 1.0) -> str:
        seconds = max(1, int(round(max_hours * 3600)))
        return TEMPLATE.format(max_hours=max_hours, seconds=seconds)
```

**The anatomy, and every part of it is a convention:**

1. **A `═══` banner** carrying not just the purpose but **the coupling** — *"Paired with `InstanceInitiatedShutdownBehavior=terminate` in `EC2__Launch__Helper`."* The shell and the API call that makes it correct are documented together, in the place where forgetting one would break the other.
2. **A module-level `TEMPLATE`** — a triple-quoted string, so the shell is readable as shell.
3. **The generated shell gets its own banner**, using the JS box-drawing character `──` rather than Python's `═══`. **Shell inside Python is marked as a different language by its comment style.**
4. **`Section__X(Type_Safe)` with a single `render()` method** returning `str`.
5. **Computation in Python, not in shell.** `seconds = max(1, int(round(max_hours * 3600)))` — the arithmetic, the clamping and the rounding all happen where they can be tested. The emitted shell contains a literal.
6. **An `echo` breadcrumb** with a bracketed prefix (`[ephemeral-ec2]`) so the boot log is greppable.
7. **The edge case documented in the banner** — `max_hours=0` — with the caller's correct behaviour named.

---

## 3. The fifteen sections

`Base` · `Docker` · `Sidecar` · `Nginx` · `Env__File` · `GPU_Verify` · `NVIDIA_Container_Toolkit` · `Ollama` · `VLLM` · `SGit_Venv` · `Claude_Code__Firstboot` · `Claude_Launch` · `Agent_Tools` · `Node` · `Shutdown`

A node's user-data is composed by rendering the sections it needs and concatenating them. **Composition is a list, not a template with conditionals** — which is why there is no `{% if gpu %}` anywhere, and why a spec that does not need CUDA simply omits `NVIDIA_Container_Toolkit`.

---

## 4. Why this is better than `.sh` files, and what it costs

Worth arguing on the site, because it is a real trade.

**What it buys:**

- **The parameters are typed and tested.** `Section__Shutdown` has unit tests; a bash script interpolated with `sed` does not.
- **No quoting hell.** Values are substituted by `str.format` in Python, not by shell expansion inside a heredoc inside a YAML string.
- **Composition without conditionals.** Include a section or do not.
- **The shell is diffable as a unit.** A change to the shutdown behaviour is a change to one small file, not a hunk inside a 400-line boot script.
- **The coupling is documented next to the code**, as the banner shows.

**What it costs:**

- **You cannot run it directly.** There is no `bash -n` on a template, no `shellcheck`, and no way to execute a section in isolation without rendering it first.
- **Two languages in one file**, with `{}` meaning `str.format` in a language where `{}` also means shell brace expansion. A literal `{` in the shell must be escaped as `{{`.
- **The rendered output is not committed**, so a reviewer reads the template and not the script.

**Both mitigations are cheap and neither exists yet:** render every section in a test and pipe it through `shellcheck`; and commit a rendered golden file per section so diffs show the actual shell. `08__` §1.

---

## 5. Hand-written shell — where it survives

Five `.sh` files, and **`set -e` discipline is inconsistent**: 2 of 5 have it, in three different forms — `set -euo pipefail`, `set -eu`, `set -u`.

That is a small enough surface to fix in an hour, and the site should publish the rule it settles on. **The recommendation is `set -euo pipefail` everywhere**, since it is already the strictest form in use and the other two are strictly weaker.

For `RUN` lines in Dockerfiles and `run:` blocks in workflows, the conventions visible in the repo are: one logical step per `RUN`, `&&` chaining with `\` continuations, cleanup in the same layer, and — from the Playwright Dockerfile — **build-time assertions rather than trust**, with a comment naming the production incident that motivated each.

---

## 6. What a linter would encode

- **`shellcheck` on rendered sections** — the highest-value change in this document. Render each `Section__*` in a test and shellcheck the output.
- **`set -euo pipefail` required** in every `.sh` file.
- **Every generated section starts with a `# ── … ──` banner.**
- **Every section emits at least one bracketed `echo` breadcrumb**, so boot logs stay greppable.
- **No `{` in a `TEMPLATE` that is not a format placeholder or escaped as `{{`** — a small custom check that prevents a real and confusing class of bug.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
source: /briefs/05__cross-cutting.md

==============================================================================


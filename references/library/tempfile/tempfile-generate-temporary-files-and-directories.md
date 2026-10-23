# tempfile: Temporary file and directory lifecycle overview

## tempfile - Generate temporary files and directories

### `tempfile` - Generate temporary files and directories

**Source code:** [Lib/tempfile.py](https://github.com/python/cpython/tree/3.14/Lib/tempfile.py)

---

Producing temporary files and directories is what this module is for, and it does so on every supported platform. The high-level entry points — `TemporaryFile`, `NamedTemporaryFile`, `TemporaryDirectory`, and `SpooledTemporaryFile` — clean up after themselves automatically and work as [context managers](https://docs.python.org/3.14/glossary.html#term-context-manager). At a lower level sit `mkstemp()` and `mkdtemp()`, which leave cleanup to you.

Every user-callable function and constructor here accepts further arguments that let you steer exactly where temporary files and directories go and what they are named. The names this module assigns embed a run of random characters, which is what makes it safe to create such files inside shared temporary directories. The argument ordering is a little quirky for the sake of staying backward-compatible; for clarity, passing keyword arguments is advised.

These are the user-callable items the module provides:

[Subject index](INDEX.md) · [Continue](tempfile-temporaryfile.md)

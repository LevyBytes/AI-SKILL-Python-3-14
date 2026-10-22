# Python 3.14.0 beta 1 / core and builtins / call len split into several uops jit can drop them

[gh-131798](https://github.com/python/cpython/issues/131798): `CALL_LEN` is split into several uops so that the JIT can drop them during optimization. Diego Russo wrote this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

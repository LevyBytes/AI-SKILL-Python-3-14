# Python 3.14.0 beta 1 / core and builtins / call str 1 split into several uops jit can drop some

[gh-131798](https://github.com/python/cpython/issues/131798): `CALL_STR_1` is split into several uops so the JIT can drop some of them. Tomas Roun wrote this patch

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

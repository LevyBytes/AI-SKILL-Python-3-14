# Python 3.12.0 alpha 1 / c api / functions and types

[gh-85858](https://github.com/python/cpython/issues/85858): Take out the `PyUnicode_InternImmortal()` function together with the `SSTATE_INTERNED_IMMORTAL` macro. Victor Stinner supplied the patch.

[gh-95756](https://github.com/python/cpython/issues/95756): To speed up the code getters, the `co_` attributes are now built lazily and cached.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

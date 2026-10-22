# Python 3.14.0 alpha 6 / core and builtins / functions and types

[gh-128974](https://github.com/python/cpython/issues/128974): A crash in [`UnicodeError.__str__`](https://docs.python.org/3.14/reference/datamodel.html#object.__str__), triggered when custom attributes define a `__str__()` that has side-effects, has been fixed. Bénédikt Tran supplied the patch.

[gh-122029](https://github.com/python/cpython/issues/122029): `INSTRUMENTED_CALL_KW` now expands the method ahead of monitoring so that the real behavior is captured more accurately.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

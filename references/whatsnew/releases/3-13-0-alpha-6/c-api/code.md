# Python 3.13.0 alpha 6 / c api / code

[gh-115756](https://github.com/python/cpython/issues/115756): `PyCode_GetFirstFree()` counts as an ustable API these days and has been given the new name [`PyUnstable_Code_GetFirstFree()`](https://docs.python.org/3.14/c-api/code.html#c.PyUnstable_Code_GetFirstFree). (Bogdan Romanyuk landed this — see [gh-115781](https://github.com/python/cpython/issues/115781))

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.12.0 alpha 1 / core and builtins / code

[gh-93382](https://github.com/python/cpython/issues/93382): Caches what [`PyCode_GetCode()`](https://docs.python.org/3.14/c-api/code.html#c.PyCode_GetCode) returns to bring back the *O*(1) lookup of the `co_code` attribute.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

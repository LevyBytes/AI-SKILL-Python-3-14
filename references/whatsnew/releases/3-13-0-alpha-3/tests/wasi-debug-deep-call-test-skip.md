# Python 3.13.0 alpha 3 / tests / turn off test super deep within test call pydebug builds running wasi

[gh-111798](https://github.com/python/cpython/issues/111798): Turn off `test_super_deep()` within `test_call` for pydebug builds running on WASI; with such a shallow stack the check yields nothing useful.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

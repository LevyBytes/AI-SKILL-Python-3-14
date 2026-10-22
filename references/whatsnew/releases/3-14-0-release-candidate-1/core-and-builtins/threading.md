# Python 3.14.0 release candidate 1 / core and builtins / threading

[gh-133136](https://github.com/python/cpython/issues/133136): Cap the surplus memory consumed under the [free threading](https://docs.python.org/3.14/glossary.html#term-free-threading) build whenever a sizeable dictionary or list gets resized and is touched by several threads.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

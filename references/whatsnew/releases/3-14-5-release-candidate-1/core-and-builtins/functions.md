# Python 3.14.5 release candidate 1 / core and builtins / functions

[gh-149122](https://github.com/python/cpython/issues/149122): Resolve a crash affecting optimized invocations of [`all()`](https://docs.python.org/3.14/library/functions.html#all), [`any()`](https://docs.python.org/3.14/library/functions.html#any), [`tuple()`](https://docs.python.org/3.14/library/stdtypes.html#tuple), [`list()`](https://docs.python.org/3.14/library/stdtypes.html#list), and [`set()`](https://docs.python.org/3.14/library/stdtypes.html#set) given an async generator expression (such as `tuple(await x for x in y)`). Such invocations now properly raise `TypeError` rather than crashing.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

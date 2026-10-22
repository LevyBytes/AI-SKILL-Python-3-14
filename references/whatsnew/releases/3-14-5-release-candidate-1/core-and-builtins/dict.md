# Python 3.14.5 release candidate 1 / core and builtins / dict

[gh-148393](https://github.com/python/cpython/issues/148393): Resolve data races pitting [`PyDict_Watch()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_Watch) / [`PyDict_Unwatch()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_Unwatch) against simultaneous dict mutation on the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.14.1 final / c api / import

[gh-137422](https://github.com/python/cpython/issues/137422): Resolve a [free threading](https://docs.python.org/3.14/glossary.html#term-free-threading) race condition within [`PyImport_AddModuleRef()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_AddModuleRef). Previously a pair of calls to the function could yield two distinct objects, of which only one had been stored within [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

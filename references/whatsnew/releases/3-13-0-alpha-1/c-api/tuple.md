# Python 3.13.0 alpha 1 / c api / tuple

[gh-106168](https://github.com/python/cpython/issues/106168): Where Python is compiled in [debug mode](https://docs.python.org/3.14/using/configure.html#debug-build) or [`with assertions`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-assertions), [`PyTuple_SET_ITEM()`](https://docs.python.org/3.14/c-api/tuple.html#c.PyTuple_SET_ITEM) and [`PyList_SET_ITEM()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_SET_ITEM) now validate the index argument through an assertion. Should that assertion trip, confirm the size was set beforehand. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

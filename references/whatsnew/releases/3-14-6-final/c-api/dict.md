# Python 3.14.6 final / c api / dict

[gh-145235](https://github.com/python/cpython/issues/145235): Made [`PyDict_AddWatcher()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_AddWatcher), [`PyDict_ClearWatcher()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_ClearWatcher), [`PyDict_Watch()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_Watch), and [`PyDict_Unwatch()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_Unwatch) safe to call across threads on the [free threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) build.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

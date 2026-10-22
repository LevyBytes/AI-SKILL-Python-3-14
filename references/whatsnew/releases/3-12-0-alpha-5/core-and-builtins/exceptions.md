# Python 3.12.0 alpha 5 / core and builtins / exceptions

[gh-101046](https://github.com/python/cpython/issues/101046): Close a possible parser memory leak raised while throwing [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError). Pablo Galindo wrote the patch

[gh-91351](https://github.com/python/cpython/issues/91351): Address a scenario where re-entrant imports might corrupt the import deadlock detection logic and let a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) escape from `importlib/_bootstrap`. Beyond the obvious cases, this could equally arise when garbage collection causes a warning to surface – which it does upon collecting an open socket or file)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.14.0 alpha 2 / core and builtins / functions

[gh-125017](https://github.com/python/cpython/issues/125017): Resolve a crash arising from particular accesses to the `__annotations__` belonging to [`staticmethod`](https://docs.python.org/3.14/library/functions.html#staticmethod) and [`classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod) objects.

[gh-119793](https://github.com/python/cpython/issues/119793): The [`map()`](https://docs.python.org/3.14/library/functions.html#map) built-in gains an optional keyword-only *strict* flag, mirroring [`zip()`](https://docs.python.org/3.14/library/functions.html#zip), to verify that every iterable shares the same length. Patch by Wannes Boeykens.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

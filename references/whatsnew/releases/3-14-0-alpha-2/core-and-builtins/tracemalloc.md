# Python 3.14.0 alpha 2 / core and builtins / tracemalloc

[gh-126076](https://github.com/python/cpython/issues/126076): Objects that get relocated, for instance `tuple`, `bytes` and `str` instances, are now correctly followed by [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc) together with the hooks that accompany it. Patch by Pablo Galindo.

[gh-125703](https://github.com/python/cpython/issues/125703): Make the specialized `Py_DECREF` paths correctly respect [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc) hooks. Patch by Pablo Galindo

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

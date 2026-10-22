# Python 3.14.0 release candidate 1 / c api / synchronization

[gh-133296](https://github.com/python/cpython/issues/133296): Fresh variants of the critical section API, taking one or two [`PyMutex`](https://docs.python.org/3.14/c-api/synchronization.html#c.PyMutex) pointers in place of [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) instances, are now exposed in the non-limited C API.

[gh-134009](https://github.com/python/cpython/issues/134009): Make [`PyMutex_IsLocked()`](https://docs.python.org/3.14/c-api/synchronization.html#c.PyMutex_IsLocked) available within the public C API.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

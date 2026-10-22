# Python 3.13.0 alpha 2 / c api / threads

[gh-112026](https://github.com/python/cpython/issues/112026): Reinstate the private `_PyThreadState_UncheckedGet()` function, this time as an alias of the new public [`PyThreadState_GetUnchecked()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_GetUnchecked) function. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

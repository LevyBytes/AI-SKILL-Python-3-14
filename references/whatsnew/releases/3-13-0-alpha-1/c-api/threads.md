# Python 3.13.0 alpha 1 / c api / threads

[gh-108867](https://github.com/python/cpython/issues/108867): A new [`PyThreadState_GetUnchecked()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_GetUnchecked) function behaves like [`PyThreadState_Get()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_Get) yet avoids killing the process with a fatal error when the value is NULL. Checking for a NULL result is left to the caller. This used to be the private `_PyThreadState_UncheckedGet()`. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

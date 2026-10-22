# Python 3.14.0 beta 3 / windows / synchronization

[gh-135099](https://github.com/python/cpython/issues/135099): A crash that could happen on Windows was fixed; it occurred when a background thread waits on a [`PyMutex`](https://docs.python.org/3.14/c-api/synchronization.html#c.PyMutex) while the main thread tears down the interpreter.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

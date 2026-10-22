# Python 3.14.4 final / core and builtins / importlib

[gh-143650](https://github.com/python/cpython/issues/143650): Corrects a race condition within [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) where one thread might pick up a stale module reference once another thread's import fails.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

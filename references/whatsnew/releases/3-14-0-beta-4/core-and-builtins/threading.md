# Python 3.14.0 beta 4 / core and builtins / threading

[gh-135871](https://github.com/python/cpython/issues/135871): On the [free threading](https://docs.python.org/3.14/glossary.html#term-free-threading) build, a non-blocking attempt to acquire a mutex lock now returns at once when the lock is busy, rather than spinning briefly.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

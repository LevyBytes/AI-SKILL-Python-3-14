# Python 3.12.0 alpha 1 / library / faulthandler

[gh-96652](https://github.com/python/cpython/issues/96652): Within faulthandler's `faulthandler.register(signal, chain=True)` handling, when the `sigaction()` function is missing, a NULL prior signal handler is no longer invoked. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

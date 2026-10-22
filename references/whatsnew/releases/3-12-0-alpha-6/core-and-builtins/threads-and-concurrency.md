# Python 3.12.0 alpha 6 / core and builtins / threads and concurrency

[gh-102126](https://github.com/python/cpython/issues/102126): Resolve a shutdown deadlock encountered while clearing thread states whenever some finalizer attempts to take the runtime head lock. Kumar Aditya supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

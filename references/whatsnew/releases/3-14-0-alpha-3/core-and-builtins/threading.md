# Python 3.14.0 alpha 3 / core and builtins / threading

[gh-127582](https://github.com/python/cpython/issues/127582): On the free threading build, repair the unsafe object resurrection that occurred while finalizers and watcher callbacks ran.

[gh-127536](https://github.com/python/cpython/issues/127536): Several list assignment operations on the free threading build gained the locks they were missing.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

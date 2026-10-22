# Python 3.14.4 final / library / functions

[gh-144475](https://github.com/python/cpython/issues/144475): Invoking [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) upon [`functools.partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) is now safer should the partial object's internal attributes get swapped out while the string representation is under construction.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

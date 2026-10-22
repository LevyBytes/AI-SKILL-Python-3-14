# Python 3.14.0 alpha 3 / library / operator

[gh-127065](https://github.com/python/cpython/issues/127065): Render [`operator.methodcaller()`](https://docs.python.org/3.14/library/operator.html#operator.methodcaller) safe for threads and safe under re-entrancy.

[gh-127065](https://github.com/python/cpython/issues/127065): Eliminate the crash that arose from calling a [`operator.methodcaller()`](https://docs.python.org/3.14/library/operator.html#operator.methodcaller) instance across several threads under the free threading build.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.14.0 alpha 7 / library / annotationlib

[gh-129463](https://github.com/python/cpython/issues/129463): Equality and hashing for [`annotationlib.ForwardRef`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.ForwardRef) now draw on every attribute carried by the object. A pair of `ForwardRef` objects count as equal only when all of their attributes match.

[gh-128593](https://github.com/python/cpython/issues/128593): Once they evaluate successfully, [`annotationlib.ForwardRef`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.ForwardRef) objects no longer cache the result. Repeated calls to [`annotationlib.ForwardRef.evaluate()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.ForwardRef.evaluate) can therefore yield differing values.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.14.0 alpha 6 / library / functools

[gh-127750](https://github.com/python/cpython/issues/127750): Strips out the broken [`functools.singledispatchmethod()`](https://docs.python.org/3.14/library/functools.html#functools.singledispatchmethod) caching that arrived via [gh-85160](https://github.com/python/cpython/issues/85160). The same performance is reached through a different optimization.

[gh-127750](https://github.com/python/cpython/issues/127750): Polishes the repr of [`functools.singledispatchmethod`](https://docs.python.org/3.14/library/functools.html#functools.singledispatchmethod) methods plus descriptors.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

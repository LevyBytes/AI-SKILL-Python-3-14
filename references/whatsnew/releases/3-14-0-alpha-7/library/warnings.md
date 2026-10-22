# Python 3.14.0 alpha 7 / library / warnings

[gh-129843](https://github.com/python/cpython/issues/129843): Corrected the way arguments are passed inside [`warnings.warn_explicit()`](https://docs.python.org/3.14/library/warnings.html#warnings.warn_explicit).

[gh-132159](https://github.com/python/cpython/issues/132159): The decorator [`warnings.deprecated`](https://docs.python.org/3.14/library/warnings.html#warnings.deprecated) no longer shadows user arguments inside the generated `__new__()`. Xuehai Pan authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

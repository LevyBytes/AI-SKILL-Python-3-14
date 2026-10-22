# Python 3.14.0 beta 1 / core and builtins / functions

[gh-130104](https://github.com/python/cpython/issues/130104): The three-argument form of [`pow()`](https://docs.python.org/3.14/library/functions.html#pow) now falls back to [`__rpow__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__rpow__) when needed. Earlier that call happened only for the two-argument `pow()` and for the binary power operator.

[gh-130070](https://github.com/python/cpython/issues/130070): An assertion error is fixed for [`exec()`](https://docs.python.org/3.14/library/functions.html#exec) when given a string `source` together with a non-`None` `closure`. Bartosz Sławecki wrote this patch.

[gh-132457](https://github.com/python/cpython/issues/132457): Both [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod) and [`classmethod()`](https://docs.python.org/3.14/library/functions.html#classmethod) are now generic.

[gh-132386](https://github.com/python/cpython/issues/132386): A crash is fixed that happened when a dict subclass was handed in as the `globals` parameter of [`exec()`](https://docs.python.org/3.14/library/functions.html#exec).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

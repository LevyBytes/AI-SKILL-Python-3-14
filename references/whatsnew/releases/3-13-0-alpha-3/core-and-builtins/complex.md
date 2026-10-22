# Python 3.13.0 alpha 3 / core and builtins / complex

[gh-109598](https://github.com/python/cpython/issues/109598): [`PyComplex_RealAsDouble()`](https://docs.python.org/3.14/c-api/complex.html#c.PyComplex_RealAsDouble)/[`PyComplex_ImagAsDouble()`](https://docs.python.org/3.14/c-api/complex.html#c.PyComplex_ImagAsDouble) will now attempt converting an object into a [`complex`](https://docs.python.org/3.14/library/functions.html#complex) instance via its `__complex__()` method ahead of falling back on the `__float__()` method. Sergey B Kirpichev supplied this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

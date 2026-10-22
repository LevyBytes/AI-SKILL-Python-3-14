# Python 3.14.0 alpha 1 / c api / refcounting

[gh-124127](https://github.com/python/cpython/issues/124127): Throughout the limited C API for 3.14 onward, [`Py_REFCNT()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_REFCNT) becomes an opaque function call so the implementation stays hidden. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

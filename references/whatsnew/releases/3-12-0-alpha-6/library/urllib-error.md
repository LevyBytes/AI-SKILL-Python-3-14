# Python 3.12.0 alpha 6 / library / urllib error

[gh-101936](https://github.com/python/cpython/issues/101936): When an [`HTTPError`](https://docs.python.org/3.14/library/urllib.error.html#urllib.error.HTTPError) is created without a `fp` parameter being designated, the default value of `fp` becomes [`io.BytesIO`](https://docs.python.org/3.14/library/io.html#io.BytesIO). Long Vo supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.14.0 beta 2 / core and builtins / exceptions

[gh-133999](https://github.com/python/cpython/issues/133999): Repair the [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) regression in [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) parsing introduced after [gh-123440](https://github.com/python/cpython/issues/123440).

[gh-133516](https://github.com/python/cpython/issues/133516): Raise [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) whenever the constants `True`, `False` or `None` serve as an identifier following NFKC normalization.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

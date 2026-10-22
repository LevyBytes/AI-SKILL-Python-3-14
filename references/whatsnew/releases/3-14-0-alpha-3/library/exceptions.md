# Python 3.14.0 alpha 3 / library / exceptions

[gh-126947](https://github.com/python/cpython/issues/126947): Have `_pydatetime.timedelta.__new__()` raise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) when its supplied arguments are neither [`int`](https://docs.python.org/3.14/library/functions.html#int) nor [`float`](https://docs.python.org/3.14/library/functions.html#float), bringing the Python implementation into agreement with the C one.

[gh-122431](https://github.com/python/cpython/issues/122431): A negative argument now triggers a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) from [`readline.append_history_file()`](https://docs.python.org/3.14/library/readline.html#readline.append_history_file).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

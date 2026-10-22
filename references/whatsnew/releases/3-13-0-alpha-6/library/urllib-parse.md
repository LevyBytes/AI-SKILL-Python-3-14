# Python 3.13.0 alpha 6 / library / urllib parse

[gh-116764](https://github.com/python/cpython/issues/116764): Bring back acceptance of `None` plus other false values across the [`urllib.parse`](https://docs.python.org/3.14/library/urllib.parse.html#module-urllib.parse) functions [`parse_qs()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.parse_qs) and [`parse_qsl()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.parse_qsl). They additionally raise a TypeError now for non-zero integers as well as non-empty sequences.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.14.0 alpha 2 / library / urllib parse

[gh-125926](https://github.com/python/cpython/issues/125926): Correct [`urllib.parse.urljoin()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urljoin) for a base URI lacking a defined authority. Even though [**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html) describes reference resolution solely for an absolute base URI, `urljoin()` ought to keep yielding a reasonable outcome with a relative base URI.

[gh-116897](https://github.com/python/cpython/issues/116897): Within the [`urllib.parse`](https://docs.python.org/3.14/library/urllib.parse.html#module-urllib.parse) functions [`parse_qsl()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.parse_qsl) and [`parse_qs()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.parse_qs), accepting objects holding false values (such as `0` and `[]`), apart from empty strings, byte-like objects and `None`, is now deprecated.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

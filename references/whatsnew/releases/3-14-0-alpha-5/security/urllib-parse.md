# Python 3.14.0 alpha 5 / security / urllib parse

[gh-105704](https://github.com/python/cpython/issues/105704): With [`urllib.parse.urlsplit()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urlsplit) and [`urllib.parse.urlparse()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urlparse), host parsing previously let through domain names that contained square brackets (`[` and `]`). Per [RFC 3986 Section 3.2.2](https://www.rfc-editor.org/rfc/rfc3986#section-3.2.2), square brackets belong only to IPv6 and IPvFuture hosts.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

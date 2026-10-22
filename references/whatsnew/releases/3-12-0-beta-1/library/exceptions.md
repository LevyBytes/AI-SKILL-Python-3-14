# Python 3.12.0 beta 1 / library / exceptions

[gh-100370](https://github.com/python/cpython/issues/100370): Address a possible [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) within [`sqlite3.Connection.blobopen()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.blobopen) on 32-bit builds. Erlend E. Aasland authored the patch.

[gh-103472](https://github.com/python/cpython/issues/103472): Head off a possible [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning) inside [`http.client.HTTPConnection`](https://docs.python.org/3.14/library/http.client.html#http.client.HTTPConnection) by explicitly closing the proxy / tunnel's CONNECT response.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

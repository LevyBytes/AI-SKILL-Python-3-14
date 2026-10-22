# Python 3.12.0 beta 1 / library / http server

[gh-103204](https://github.com/python/cpython/issues/103204): Corrects [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server) tolerating HTTP requests whose HTTP version numbers carry a leading "+", or "-", or contain digit-separating "_" characters. A bound is also placed on the length of the version numbers.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

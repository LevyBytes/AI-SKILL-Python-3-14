# Python 3.12.0 alpha 1 / security / http server

[gh-87389](https://github.com/python/cpython/issues/87389): [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server): Closes an open redirection hole in the HTTP server triggered whenever a URI path begins with `//`. Hamza Avvan both reported the flaw and offered the first fix.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

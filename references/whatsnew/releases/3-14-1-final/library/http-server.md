# Python 3.14.1 final / library / http server

[gh-70765](https://github.com/python/cpython/issues/70765): [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server): corrects how [`BaseHTTPRequestHandler`](https://docs.python.org/3.14/library/http.server.html#http.server.BaseHTTPRequestHandler) deals with HTTP/0.9 requests by default. Formerly, `BaseHTTPRequestHandler.parse_request()` wrongly held out for headers on the request, despite HTTP/0.9 not supporting them. Bénédikt Tran authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.11.0 alpha 1 / library / http server

[bpo-43972](https://bugs.python.org/issue?@action=redirect&bpo=43972): Whenever [`http.server.SimpleHTTPRequestHandler`](https://docs.python.org/3.14/library/http.server.html#http.server.SimpleHTTPRequestHandler) returns a `301 (Moved Permanently)` for a directory path that lacks a trailing `/`, it now appends a `Content-Length: 0` header. Certain clients behave better as a result.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# What's New In Python 3.3 / http — http.client, http.server, io

### http

Calling [`end_headers()`](https://docs.python.org/3.14/library/http.server.html#http.server.BaseHTTPRequestHandler.end_headers) now flushes them in one write because [`http.server.BaseHTTPRequestHandler`](https://docs.python.org/3.14/library/http.server.html#http.server.BaseHTTPRequestHandler) buffers the headers first. To steer exactly when those collected headers go out, call the new [`flush_headers()`](https://docs.python.org/3.14/library/http.server.html#http.server.BaseHTTPRequestHandler.flush_headers) method. Andrew Schaaf landed this ([bpo-3709](https://bugs.python.org/issue?@action=redirect&bpo=3709)).

Output from [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server) is now valid `HTML 4.01 strict`. Ezio Melotti landed this ([bpo-13295](https://bugs.python.org/issue?@action=redirect&bpo=13295)).

A [`readinto()`](https://docs.python.org/3.14/library/http.client.html#http.client.HTTPResponse.readinto) method now lives on [`http.client.HTTPResponse`](https://docs.python.org/3.14/library/http.client.html#http.client.HTTPResponse), letting it stand in as an [`io.RawIOBase`](https://docs.python.org/3.14/library/io.html#io.RawIOBase) class. John Kuhn landed this ([bpo-13464](https://bugs.python.org/issue?@action=redirect&bpo=13464)).

[Subject index](INDEX.md) · [Previous source section](hmac.md) · [Next source section](html.md) · [Release/subject declaration](summary-release-highlights.md)

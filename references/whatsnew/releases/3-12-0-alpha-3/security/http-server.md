# Python 3.12.0 alpha 3 / security / http server

[gh-100001](https://github.com/python/cpython/issues/100001): A garbage request handed to `python -m http.server` can no longer push terminal control characters into the stderr server log.

The fix changes the [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server) `BaseHTTPRequestHandler` `.log_message` method so that control characters become a `\x*HH*` hex escape before anything is printed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

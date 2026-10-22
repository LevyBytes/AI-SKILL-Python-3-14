# Python 3.6.0 beta 1 / library / python

[bpo-12319](https://bugs.python.org/issue?@action=redirect&bpo=12319): http.client.HTTPConnection requests gained chunked transfer encoding support. The urllib.request.AbstractHTTPHandler class no longer insists on a Content-Length header. When an HTTP request carries a file or iterable body yet lacks a Content-Length header, the library now resorts to chunked transfer-encoding.

- > A new version of typing.py from [https://github.com/python/typing](https://github.com/python/typing): - Collection (only for 3.6) ([bpo-27598](https://bugs.python.org/issue?@action=redirect&bpo=27598)) - Add FrozenSet to __all__ (upstream #261) - fix crash in _get_type_vars() (upstream #259) - Remove the dict constraint in ForwardRef._eval_type (upstream #252)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

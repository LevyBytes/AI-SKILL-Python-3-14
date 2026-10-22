# Python 3.12.0 beta 1 / library / http client

[gh-99353](https://github.com/python/cpython/issues/99353): Honour the [`http.client.HTTPConnection`](https://docs.python.org/3.14/library/http.client.html#http.client.HTTPConnection) `.debuglevel` flag from inside `urllib.request.AbstractHTTPHandler` when its constructor parameter `debuglevel` goes unset. Apply the same treatment to `*HTTPS*`.

[bpo-24964](https://bugs.python.org/issue?@action=redirect&bpo=24964): New method [`http.client.HTTPConnection.get_proxy_response_headers()`](https://docs.python.org/3.14/library/http.client.html#http.client.HTTPConnection.get_proxy_response_headers) exposes the HTTP headers returned by a proxy server in answer to the `CONNECT` request.

[bpo-22708](https://bugs.python.org/issue?@action=redirect&bpo=22708): Several refinements to the http.client CONNECT tunnel: switch to the HTTP 1.1 protocol; emit a Host: header alongside CONNECT whenever the caller omits one; translate IDN domain names into Punycode. Michael Handler authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

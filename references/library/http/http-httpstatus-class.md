# http — `http` — HTTP modules

## http — HTTP modules

### `http` — HTTP modules

**Source code:** [Lib/http/__init__.py](https://github.com/python/cpython/tree/3.14/Lib/http/__init__.py)

---

As a package, `http` bundles together a number of modules aimed at the HyperText Transfer Protocol:

- [`http.client`](https://docs.python.org/3.14/library/http.client.html#module-http.client) offers a low-level client for the HTTP protocol; when you need high-level URL opening instead, reach for [`urllib.request`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.request)

- [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server) supplies elementary HTTP server classes built on top of [`socketserver`](https://docs.python.org/3.14/library/socketserver.html#module-socketserver)

- [`http.cookies`](https://docs.python.org/3.14/library/http.cookies.html#module-http.cookies) carries helpers for doing cookie-based state management

- [`http.cookiejar`](https://docs.python.org/3.14/library/http.cookiejar.html#module-http.cookiejar) handles keeping cookies around persistently

Alongside those, the `http` module declares the enums below to ease work with http-related code:

 *class *http.HTTPStatus

Added in version 3.5.

An [`enum.IntEnum`](https://docs.python.org/3.14/library/enum.html#enum.IntEnum) subclass laying out a collection of HTTP status codes together with their reason phrases and lengthy English-language descriptions.

Usage:

```python
>>> from http import HTTPStatus
>>> HTTPStatus.OK
HTTPStatus.OK
>>> HTTPStatus.OK == 200
True
>>> HTTPStatus.OK.value
200
>>> HTTPStatus.OK.phrase
'OK'
>>> HTTPStatus.OK.description
'Request fulfilled, document follows'
>>> list(HTTPStatus)
[HTTPStatus.CONTINUE, HTTPStatus.SWITCHING_PROTOCOLS, ...]

```

[Subject index](INDEX.md) · [Continue](http-status-codes.md)

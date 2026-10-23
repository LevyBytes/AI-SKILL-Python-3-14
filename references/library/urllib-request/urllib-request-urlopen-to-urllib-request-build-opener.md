# urllib.request`urllib.request` - Extensible library for opening URLs

### `urllib.request` - Extensible library for opening URLs

**Source code:** [Lib/urllib/request.py](https://github.com/python/cpython/tree/3.14/Lib/urllib/request.py)

---

Functions and classes that assist with opening URLs — predominantly HTTP — across a tangled landscape of basic and digest authentication, redirects, cookies, and similar concerns are supplied by the `urllib.request` module.

See also

For a higher-level HTTP client interface, consider the [Requests package](https://requests.readthedocs.io/en/master/).

Warning

Calling this module from programs that invoke [`os.fork()`](https://docs.python.org/3.14/library/os.html#os.fork) is unsafe on macOS, since the macOS `getproxies()` implementation relies on a higher-level system API. Sidestep the issue by setting the `no_proxy` environment variable to `*` (for instance, `os.environ["no_proxy"] = "*"`).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

On WebAssembly this module is either unavailable or non-functional. Consult [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for further details.

These functions are defined by the `urllib.request` module:

 urllib.request.urlopen(*url*, *data=None*, [*timeout*, ]***, *context=None*)

Open *url*, supplied either as a string holding a valid, correctly encoded URL or as a `Request` object.

*data* is required to be an object that carries extra data destined for the server, or `None` when no such data applies. Consult `Request` for the specifics.

The urllib.request module operates over HTTP/1.1 and attaches a `Connection:close` header to the HTTP requests it issues.

When supplied, the optional *timeout* parameter sets, in seconds, a limit on blocking operations such as the connection attempt (when omitted, the global default timeout setting applies). This is actually honored only for HTTP, HTTPS, and FTP connections.

When *context* is given, it has to be a [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) instance laying out the assorted SSL options. Refer to [`HTTPSConnection`](https://docs.python.org/3.14/library/http.client.html#http.client.HTTPSConnection) for additional detail.

The object this function always hands back can serve as a [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) and exposes the *url*, *headers*, and *status* properties. For more on these properties, see `urllib.response.addinfourl`.

With HTTP and HTTPS URLs, the returned value is a slightly altered [`http.client.HTTPResponse`](https://docs.python.org/3.14/library/http.client.html#http.client.HTTPResponse) object. Beyond the three new methods noted above, its msg attribute holds the same content as the [`reason`](https://docs.python.org/3.14/library/http.client.html#http.client.HTTPResponse.reason) attribute — the server's reason phrase — rather than the response headers that the `HTTPResponse` documentation describes.

With FTP, file, and data URLs, the value returned is a `urllib.response.addinfourl` object.

Protocol errors trigger a [`URLError`](https://docs.python.org/3.14/library/urllib.error.html#urllib.error.URLError).

Bear in mind that `None` can come back when no handler services the request (although the default installed global `OpenerDirector` relies on `UnknownHandler` so that this never occurs).

Furthermore, when proxy settings are picked up (such as a `*_proxy` environment variable like `http_proxy` being set), `ProxyHandler` is installed by default and ensures the requests flow through the proxy.

The old `urllib.urlopen` function present in Python 2.6 and earlier no longer exists; `urllib.request.urlopen()` maps to the former `urllib2.urlopen`. The proxy handling once achieved by handing a dictionary parameter to `urllib.urlopen` is now available through `ProxyHandler` objects.

An [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) named `urllib.Request` is raised by the default opener, carrying the arguments `fullurl`, `data`, `headers`, `method` drawn from the request object.

Changed in version 3.2: *cafile* and *capath* were added.

HTTPS virtual hosts are now supported if possible (that is, if [`ssl.HAS_SNI`](https://docs.python.org/3.14/library/ssl.html#ssl.HAS_SNI) is true).

*data* can be an iterable object.

Changed in version 3.3: *cadefault* was added.

Changed in version 3.4.3: *context* was added.

Changed in version 3.10: When no *context* is given, an HTTPS connection now sends an ALPN extension whose protocol indicator is `http/1.1`. A custom *context* ought to configure its ALPN protocols using [`set_alpn_protocols()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.set_alpn_protocols).

Changed in version 3.13: The *cafile*, *capath* and *cadefault* parameters were removed; rely on the *context* parameter in their place.

 urllib.request.install_opener(*opener*)

Register an `OpenerDirector` instance to act as the default global opener. You only need to install an opener when you want urlopen to make use of it; otherwise, just invoke `OpenerDirector.open()` rather than `urlopen()`. No check is made for a genuine `OpenerDirector`, so any class exposing the right interface is acceptable.

 urllib.request.build_opener([*handler*, *...*])

Hand back an `OpenerDirector` instance that links the handlers in the sequence supplied. Each *handler* may be an instance of `BaseHandler` or a subclass of `BaseHandler` (in the latter case the constructor must be callable with no parameters). Instances of the classes below precede the *handler*s, except when those *handler*s already contain them — whether the classes themselves, their instances, or their subclasses: `ProxyHandler` (when proxy settings are detected), `UnknownHandler`, `HTTPHandler`, `HTTPDefaultErrorHandler`, `HTTPRedirectHandler`, `FTPHandler`, `FileHandler`, `HTTPErrorProcessor`.

When the Python installation provides SSL support (that is, when the [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) module is importable), `HTTPSHandler` is added as well.

To shift its place within the handlers list, a `BaseHandler` subclass may also alter its `handler_order` attribute.

[Subject index](INDEX.md) · [Continue](urllib-request-pathname2url-to-urllib-request-getproxies.md)

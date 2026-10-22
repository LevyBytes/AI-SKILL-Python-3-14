# http.client: `HTTPConnection.request()`, `HTTPConnection.getresponse()`, `HTTPConnection.set_debuglevel()`, `HTTPConnection.set_tunnel()`

### HTTPConnection Objects

The methods available on `HTTPConnection` instances are:

 HTTPConnection.request(*method*, *url*, *body=None*, *headers={}*, ***, *encode_chunked=False*)

This dispatches a request to the server, using HTTP request method *method* together with the request URI *url*. For compliance with [**RFC 26165.1.2**](https://datatracker.ietf.org/doc/html/rfc2616.html#section-5.1.2), the supplied *url* has to be an absolute path (except when connecting through an HTTP proxy server or when using the `OPTIONS` or `CONNECT` methods).

When *body* is given, that data follows once the headers have been completed. It can be a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object), an open [file object](https://docs.python.org/3.14/glossary.html#term-file-object), or an iterable of [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes). A string *body* is encoded as ISO-8859-1, HTTP's default. A bytes-like object is transmitted unchanged. A file object causes its contents to be sent; such a file object needs to support at minimum the `read()` method. Where the file object is an instance of [`io.TextIOBase`](https://docs.python.org/3.14/library/io.html#io.TextIOBase), whatever `read()` returns is encoded as ISO-8859-1; otherwise the output of `read()` is sent unchanged. An iterable *body* has its elements emitted as is until the iterable runs out.

Pass the *headers* argument as a mapping of additional HTTP headers to accompany the request. For compliance with [**RFC 26165.1.2**](https://datatracker.ietf.org/doc/html/rfc2616.html#section-5.1.2), a [**Host header**](https://datatracker.ietf.org/doc/html/rfc2616.html#section-14.23) has to be present (except when connecting through an HTTP proxy server or when using the `OPTIONS` or `CONNECT` methods).

Should *headers* include neither Content-Length nor Transfer-Encoding while a request body exists, one of those header fields gets added for you. When *body* is `None`, the Content-Length header becomes `0` for methods that anticipate a body (`PUT`, `POST`, and `PATCH`). When *body* is a string or a bytes-like object that is not simultaneously a [file](https://docs.python.org/3.14/glossary.html#term-file-object), the Content-Length header takes its length. Any *body* of another sort (files and iterables broadly) is chunk-encoded, and the Transfer-Encoding header is set automatically rather than Content-Length.

The *encode_chunked* argument matters only when Transfer-Encoding appears in *headers*. With *encode_chunked* set to `False`, the HTTPConnection object presumes the calling code manages all encoding. With it set to `True`, the body undergoes chunk-encoding.

For instance, to issue a `GET` request to `https://docs.python.org/3/`:

```python
>>> import http.client
>>> host = "docs.python.org"
>>> conn = http.client.HTTPSConnection(host)
>>> conn.request("GET", "/3/", headers={"Host": host})
>>> response = conn.getresponse()
>>> print(response.status, response.reason)
200 OK

```

Note

Chunked transfer encoding arrived with version 1.1 of the HTTP protocol. Unless it is certain the HTTP server speaks HTTP 1.1, the caller has to either state the Content-Length or supply, as the body, a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or bytes-like object that is not also a file.

Note

Be aware that you must have consumed the entire response, or invoked `close()`, whenever `getresponse()` raised a non-[`ConnectionError`](https://docs.python.org/3.14/library/exceptions.html#ConnectionError) exception, before another request can go out to the server.

Changed in version 3.2: *body* can now be an iterable.

Changed in version 3.6: When *headers* sets neither Content-Length nor Transfer-Encoding, file and iterable *body* objects now get chunk-encoded. The *encode_chunked* argument arrived. For file objects, no effort is made to work out the Content-Length.

 HTTPConnection.getresponse()

Invoke this once a request has gone out, to obtain the server's response. It hands back an `HTTPResponse` instance.

Changed in version 3.5: Should a [`ConnectionError`](https://docs.python.org/3.14/library/exceptions.html#ConnectionError) or one of its subclasses be raised, the `HTTPConnection` object stands ready to reconnect once a fresh request goes out.

Be aware this does not cover [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError)s coming from the underlying socket. There it falls to the caller to invoke `close()` on the present connection.

 HTTPConnection.set_debuglevel(*level*)

Adjust the debugging level. The debug level defaults to `0`, which prints no debugging output. Any value above `0` makes every currently defined debug output print to stdout. The `debuglevel` propagates to each new `HTTPResponse` object that gets created.

Added in version 3.1.

 HTTPConnection.set_tunnel(*host*, *port=None*, *headers=None*)

Establish the host and the port for HTTP Connect Tunnelling. This lets the connection route through a proxy server.

The *host* and *port* arguments designate the endpoint of the tunneled connection (that is, the address placed in the CONNECT request, *not* the proxy server's own address).

Supply the *headers* argument as a mapping of additional HTTP headers to send along with the CONNECT request.

Because HTTP/1.1 carries the HTTP CONNECT tunnelling request, [as per the RFC](https://datatracker.ietf.org/doc/html/rfc7231#section-4.3.6), an HTTP `Host:` header has to be present, matching the authority-form of the request target named as the destination of the CONNECT request. Should no HTTP `Host:` header come through the headers argument, one gets generated and sent for you.

For instance, to tunnel by way of an HTTPS proxy server running locally on port 8080, we hand the proxy's address to the `HTTPSConnection` constructor and the address of the host we ultimately want to reach to the `set_tunnel()` method:

```python
>>> import http.client
>>> conn = http.client.HTTPSConnection("localhost", 8080)
>>> conn.set_tunnel("www.python.org")
>>> conn.request("HEAD","/index.html")

```

Added in version 3.2.

Changed in version 3.12: HTTP CONNECT tunnelling requests now run over protocol HTTP/1.1, raised from protocol HTTP/1.0. Since HTTP/1.1 requires `Host:` HTTP headers, one is generated and sent for you whenever the headers argument omits it.

[Subject index](INDEX.md) · [Previous](http-client-responses.md) · [Continue](http-proxy-response-and-connection-output.md) · [Owning module, declaration or section: http.client](http-client-httpconnection-class.md)

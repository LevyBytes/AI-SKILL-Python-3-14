# http.server: `http.server.ThreadingHTTPServer`

*class *http.server.ThreadingHTTPServer(*server_address*, *RequestHandlerClass*)

Behaving the same as HTTPServer, this class relies on threads for request handling through the [`ThreadingMixIn`](https://docs.python.org/3.14/library/socketserver.html#socketserver.ThreadingMixIn). It helps with web browsers that pre-open sockets, where `HTTPServer` would otherwise block forever.

Added in version 3.7.

```text
class http.server.HTTPSServer(server_address, RequestHandlerClass, bind_and_activate=True, *, certfile, keyfile=None, password=None, alpn_protocols=None)
```

A `HTTPServer` subclass whose socket is wrapped via the [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) module. When the `ssl` module is absent, creating a `HTTPSServer` object raises a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

The *certfile* argument gives the path to the SSL certificate chain file, while *keyfile* points to the file holding the private key.

You may supply a *password* for files protected and wrapped using PKCS#8, though be aware this risks exposing hardcoded passwords in plaintext.

See also

Refer to [`ssl.SSLContext.load_cert_chain()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.load_cert_chain) for more on the values permitted for *certfile*, *keyfile* and *password*.

If given, the *alpn_protocols* argument has to be a sequence of strings naming the "Application-Layer Protocol Negotiation" (ALPN) protocols the server supports. ALPN lets the server and client agree on the application protocol while the TLS handshake takes place.

The default value is `["http/1.1"]`, indicating that the server speaks HTTP/1.1.

Added in version 3.14.

```text
class http.server.ThreadingHTTPSServer(server_address, RequestHandlerClass, bind_and_activate=True, *, certfile, keyfile=None, password=None, alpn_protocols=None)
```

Functioning the same as `HTTPSServer`, this class handles requests with threads by deriving from [`ThreadingMixIn`](https://docs.python.org/3.14/library/socketserver.html#socketserver.ThreadingMixIn). The relationship mirrors `ThreadingHTTPServer`, except built on `HTTPSServer`.

Added in version 3.14.

When instantiated, `HTTPServer`, `ThreadingHTTPServer`, `HTTPSServer` and `ThreadingHTTPSServer` each require a *RequestHandlerClass*; this module supplies three distinct options:

[Subject index](INDEX.md) · [Previous](http-server-httpserver-class.md) · [Continue](http-server-basehttprequesthandler-class.md) · [Owning module, declaration or section: http.server](http-server-httpserver-class.md)

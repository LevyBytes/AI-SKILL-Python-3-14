# http.client: `http.client.HTTPConnection`

# Http.Client

### `http.client` - HTTP protocol client

**Source code:** [Lib/http/client.py](https://github.com/python/cpython/tree/3.14/Lib/http/client.py)

---

The classes here implement the client end of the HTTP and HTTPS protocols. Direct use is uncommon — the [`urllib.request`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.request) module relies on it when resolving URLs whose scheme is HTTP or HTTPS.

See also

For a more convenient, higher-level HTTP client API, the [Requests package](https://requests.readthedocs.io/en/latest/) is the recommended choice.

Note

HTTPS works only when Python's build included SSL support (supplied via the [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) module).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

On WebAssembly this module is either absent or non-functional. Consult [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for additional details.

These are the classes exposed by the module:

 *class *http.client.HTTPConnection(*host*, *port=None*, [*timeout*, ]*source_address=None*, *blocksize=8192*)

A single transaction against an HTTP server is modeled by an `HTTPConnection` instance. Construct one by supplying a host plus, optionally, a port number. When the port is omitted, it is read from the host string should that string look like `host:port`; otherwise the standard HTTP port (80) applies. Supplying the optional *timeout* argument causes blocking operations (such as attempting to connect) to give up after the stated number of seconds (when omitted, the global default timeout setting takes effect). The optional *source_address* argument can be a (host, port) tuple naming the local address from which the HTTP connection originates. The optional *blocksize* argument fixes the buffer size, in bytes, used when transmitting a file-like message body.

As an illustration, every one of these calls builds an instance pointed at the same host and port on the server:

```python
>>> h1 = http.client.HTTPConnection('www.python.org')
>>> h2 = http.client.HTTPConnection('www.python.org:80')
>>> h3 = http.client.HTTPConnection('www.python.org', 80)
>>> h4 = http.client.HTTPConnection('www.python.org', 80, timeout=10)

```

Changed in version 3.2: *source_address* gained support.

Changed in version 3.4: Dropped the *strict* parameter. Support for HTTP 0.9-style “Simple Responses” ended.

Changed in version 3.7: The *blocksize* parameter became available.

[Subject index](INDEX.md) · [Continue](http-client-httpsconnection-class.md)

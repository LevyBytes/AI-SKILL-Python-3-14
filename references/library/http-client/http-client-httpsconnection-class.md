# http.client: `http.client.HTTPSConnection`

*class *http.client.HTTPSConnection(*host*, *port=None*, ***, [*timeout*, ]*source_address=None*, *context=None*, *blocksize=8192*)

A `HTTPConnection` subclass that secures communication with servers through SSL. The default port is `443`. When *context* is provided, it has to be a [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) instance laying out the assorted SSL options.

For guidance on recommended practice, consult [Security considerations](https://docs.python.org/3.14/library/ssl.html#ssl-security).

Changed in version 3.2: *source_address*, *context* and *check_hostname* gained support.

Changed in version 3.2: Where feasible, this class now handles HTTPS virtual hosts (specifically, when [`ssl.HAS_SNI`](https://docs.python.org/3.14/library/ssl.html#ssl.HAS_SNI) holds true).

Changed in version 3.4: Dropped the *strict* parameter. Support for HTTP 0.9-style “Simple Responses” ended.

Changed in version 3.4.3: By default, this class now runs every required certificate and hostname check. Passing `ssl._create_unverified_context()` to the *context* parameter restores the earlier, unverified behavior.

Changed in version 3.8: For the default *context*, or whenever *cert_file* accompanies a custom *context*, this class now turns on TLS 1.3 [`ssl.SSLContext.post_handshake_auth`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.post_handshake_auth).

Changed in version 3.10: When no *context* is supplied, this class now emits an ALPN extension carrying the protocol indicator `http/1.1`. A custom *context* ought to register ALPN protocols via [`set_alpn_protocols()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.set_alpn_protocols).

Changed in version 3.12: The deprecated *key_file*, *cert_file* and *check_hostname* parameters are now gone.

[Subject index](INDEX.md) · [Previous](http-client-httpconnection-class.md) · [Continue](http-client-httpresponse-class.md) · [Owning module, declaration or section: http.client](http-client-httpconnection-class.md)

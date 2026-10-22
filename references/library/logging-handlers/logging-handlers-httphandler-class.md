# logging.handlers: `logging.handlers.HTTPHandler`

### HTTPHandler

Living in the `logging.handlers` module, the `HTTPHandler` class lets you deliver logging messages to a web server under either `GET` or `POST` semantics.

 *class *logging.handlers.HTTPHandler(*host*, *url*, *method='GET'*, *secure=False*, *credentials=None*, *context=None*)

Hands back a fresh instance of the `HTTPHandler` class. You may write *host* as `host:port` whenever a particular port number is needed. Leave *method* unspecified and `GET` applies. When *secure* is true, an HTTPS connection is used. You can point the *context* parameter at an [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) instance to tune the SSL settings of that HTTPS connection. When *credentials* is given, make it a 2-tuple of userid and password, which lands in an HTTP ‘Authorization’ header via Basic authentication. If you do give credentials, also set secure=True so your userid and password never cross the wire in cleartext.

Changed in version 3.5: The *context* parameter was added.

[Subject index](INDEX.md) · [Previous](memory-handler-class-and-flush-policy.md) · [Continue](http-handler-record-mapping-and-emission.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md)

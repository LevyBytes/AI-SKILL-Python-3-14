# What's New In Python 3.2 / http.client — http.client, http.server

### http.client

Several modest API tweaks reached the [`http.client`](https://docs.python.org/3.14/library/http.client.html#module-http.client) module. Simple HTTP 0.9 responses of the old style are dropped, and across every class the *strict* parameter is now deprecated.

A *source_address* parameter — a (host, port) tuple naming where the HTTP connection originates — now appears on both the [`HTTPConnection`](https://docs.python.org/3.14/library/http.client.html#http.client.HTTPConnection) and [`HTTPSConnection`](https://docs.python.org/3.14/library/http.client.html#http.client.HTTPSConnection) classes.

[`HTTPSConnection`](https://docs.python.org/3.14/library/http.client.html#http.client.HTTPSConnection) gained both certificate checking and HTTPS virtual host support.

On connection objects the [`request()`](https://docs.python.org/3.14/library/http.client.html#http.client.HTTPConnection.request) method had long taken an optional *body* argument, letting a [file object](https://docs.python.org/3.14/glossary.html#term-file-object) furnish the request content. Handily, *body* now also takes an [iterable](https://docs.python.org/3.14/glossary.html#term-iterable) object provided it carries an explicit `Content-Length` header. That widened interface offers far more flexibility than the earlier one.

For routing an HTTPS connection via a proxy server, a new [`set_tunnel()`](https://docs.python.org/3.14/library/http.client.html#http.client.HTTPConnection.set_tunnel) method records the host and port used for HTTP Connect tunneling.

So that it lines up with [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server), the HTTP client library now encodes outgoing headers with ISO-8859-1 (Latin-1) too. Since incoming headers already used it, both directions of traffic now behave alike. (See work by Armin Ronacher in [bpo-10980](https://bugs.python.org/issue?@action=redirect&bpo=10980).)

[Subject index](INDEX.md) · [Previous source section](imaplib.md) · [Next source section](unittest.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)

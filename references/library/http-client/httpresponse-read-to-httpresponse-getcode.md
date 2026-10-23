# http.client - HTTPResponse Objects

### HTTPResponse Objects

An `HTTPResponse` instance enwraps the server's HTTP response. Through it you reach the request headers along with the entity body. Being an iterable object, the response also works within a with statement.

Changed in version 3.5: The [`io.BufferedIOBase`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase) interface now has an implementation, with every one of its reader operations available.

 HTTPResponse.read([*amt*])

Reads the response body and returns it, or at most the next *amt* bytes.

 HTTPResponse.readinto(*b*)

Reads as many as the next len(b) bytes from the response body into buffer *b*, then returns how many bytes were read.

Added in version 3.3.

 HTTPResponse.getheader(*name*, *default=None*)

Give back the value of the header *name*, or *default* when no header matches *name*. When more than one header carries the name *name*, return all the values joined by ‘, ‘. If *default* is any iterable beyond a single string, its elements come back joined by commas in the same way.

 HTTPResponse.getheaders()

Return a list of (header, value) tuples.

 HTTPResponse.fileno()

Return the `fileno` of the underlying socket.

 HTTPResponse.msg

A `http.client.HTTPMessage` instance containing the response headers. `http.client.HTTPMessage` is a subclass of [`email.message.Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message).

 HTTPResponse.version

HTTP protocol version used by server. 10 for HTTP/1.0, 11 for HTTP/1.1.

 HTTPResponse.url

URL of the fetched resource, often checked to tell whether a redirect occurred.

 HTTPResponse.headers

Headers of the response in the form of an [`email.message.EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) instance.

 HTTPResponse.status

Status code returned by server.

 HTTPResponse.reason

Reason phrase returned by server.

 HTTPResponse.debuglevel

A debugging hook. When `debuglevel` exceeds zero, the reading and parsing of the response prints messages to stdout.

 HTTPResponse.closed

Is `True` if the stream is closed.

 HTTPResponse.geturl()

Deprecated since version 3.9: Deprecated in favor of `url`.

 HTTPResponse.info()

Deprecated since version 3.9: Deprecated in favor of `headers`.

 HTTPResponse.getcode()

Deprecated since version 3.9: Deprecated in favor of `status`.

[Subject index](INDEX.md) · [Previous](http-proxy-response-and-connection-output.md) · [Continue](examples.md) · [Owning module, declaration or section: http.client](http-client-httpconnection-class.md)

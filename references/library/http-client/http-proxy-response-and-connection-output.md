# http.client: Proxy response inspection and low-level request output

HTTPConnection.get_proxy_response_headers()

Hands back a dictionary holding the headers from the response the proxy server returned to the CONNECT request.

When no CONNECT request was sent, the method gives back `None`.

Added in version 3.12.

 HTTPConnection.connect()

Open a connection to the server named at the time the object was created. Ordinarily this fires automatically when a request is made if the client lacks a connection already.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `http.client.connect` with arguments `self`, `host`, `port`.

 HTTPConnection.close()

Shut down the connection to the server.

 HTTPConnection.blocksize

Buffer size in bytes for sending a file-like message body.

Added in version 3.7.

Rather than relying on the `request()` method covered above, you may instead transmit your request piece by piece using the four functions that follow.

 HTTPConnection.putrequest(*method*, *url*, *skip_host=False*, *skip_accept_encoding=False*)

Make this the very first call once the connection to the server is established. It writes a line to the server made up of the *method* string, the *url* string, and the HTTP version (`HTTP/1.1`). To suppress automatic emission of `Host:` or `Accept-Encoding:` headers (say, to permit extra content encodings), give *skip_host* or *skip_accept_encoding* non-False values.

 HTTPConnection.putheader(*header*, *argument*[, *...*])

Transmit an [**RFC 822**](https://datatracker.ietf.org/doc/html/rfc822.html)-style header to the server. It writes the server a line composed of the header, a colon and a space, and the first argument. When extra arguments appear, continuation lines follow, each made of a tab and an argument.

 HTTPConnection.endheaders(*message_body=None*, ***, *encode_chunked=False*)

Write a blank line to the server to mark the end of the headers. The optional *message_body* argument serves to carry a message body tied to the request.

When *encode_chunked* is `True`, each iteration of *message_body* yields a result that is chunk-encoded in the manner laid out by [**RFC 7230**](https://datatracker.ietf.org/doc/html/rfc7230.html), Section 3.3.1. The encoding approach hinges on the type of *message_body*. Where *message_body* implements the [buffer interface](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects), the encoding produces a single chunk. Where *message_body* is a [`collections.abc.Iterable`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Iterable), each iteration of *message_body* yields a chunk. Where *message_body* is a [file object](https://docs.python.org/3.14/glossary.html#term-file-object), every call to `.read()` yields a chunk. Right after *message_body*, the method emits the marker that ends the chunk-encoded data on its own.

Note

Owing to the chunked encoding specification, the chunk-encoder discards empty chunks produced by an iterator body. This guards against the target server cutting short its read of the request because of malformed encoding.

Changed in version 3.6: Added chunked encoding support and the *encode_chunked* parameter.

 HTTPConnection.send(*data*)

Transmit data to the server. Use this directly only in the window after `endheaders()` has been called and before `getresponse()` is called.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `http.client.send` with arguments `self`, `data`.

[Subject index](INDEX.md) · [Previous](httpconnection-request-to-httpconnection-set-tunnel.md) · [Continue](httpresponse-read-to-httpresponse-getcode.md) · [Owning module, declaration or section: http.client](http-client-httpconnection-class.md) · [Owning module, declaration or section: HTTPConnection Objects](httpconnection-request-to-httpconnection-set-tunnel.md)

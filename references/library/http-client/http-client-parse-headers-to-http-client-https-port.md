# http.client: HTTP header parsing, exception types and port constants

http.client.parse_headers(*fp*)

Read the headers out of a file pointer *fp* that stands for an HTTP request or response. That file must be a [`BufferedIOBase`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase) reader (in other words, not text) and has to deliver a valid [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html) style header.

The return value is an `http.client.HTTPMessage` instance carrying the header fields but no payload (matching `HTTPResponse.msg` and [`http.server.BaseHTTPRequestHandler.headers`](https://docs.python.org/3.14/library/http.server.html#http.server.BaseHTTPRequestHandler.headers)). Once it returns, the file pointer *fp* sits ready to read the HTTP body.

Note

`parse_headers()` leaves the start-line of an HTTP message untouched; only the `Name: value` lines get parsed. Because the file must be positioned to read those field lines, the first line should have been consumed already before the call.

The exceptions below are raised when circumstances warrant:

 *exception *http.client.HTTPException

The parent class for the rest of this module's exceptions. It derives from [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception).

 *exception *http.client.NotConnected

A subclass of `HTTPException`.

 *exception *http.client.InvalidURL

A subclass of `HTTPException`, raised whenever a supplied port is empty or not numeric.

 *exception *http.client.UnknownProtocol

A subclass of `HTTPException`.

 *exception *http.client.UnknownTransferEncoding

A subclass of `HTTPException`.

 *exception *http.client.UnimplementedFileMode

A subclass of `HTTPException`.

 *exception *http.client.IncompleteRead

A subclass of `HTTPException`.

 *exception *http.client.ImproperConnectionState

A subclass of `HTTPException`.

 *exception *http.client.CannotSendRequest

A subclass of `ImproperConnectionState`.

 *exception *http.client.CannotSendHeader

A subclass of `ImproperConnectionState`.

 *exception *http.client.ResponseNotReady

A subclass of `ImproperConnectionState`.

 *exception *http.client.BadStatusLine

A subclass of `HTTPException`. Raised when a server's reply carries an HTTP status code that we cannot interpret.

 *exception *http.client.LineTooLong

A subclass of `HTTPException`. Raised when a line of excessive length arrives over the HTTP protocol from the server.

 *exception *http.client.RemoteDisconnected

A subclass of [`ConnectionResetError`](https://docs.python.org/3.14/library/exceptions.html#ConnectionResetError) and `BadStatusLine`. Raised by `HTTPConnection.getresponse()` when reading the response yields no data from the connection, signaling that the far end has shut the connection down.

Added in version 3.5: Previously, `BadStatusLine``('')` was raised.

These are the constants the module defines:

 http.client.HTTP_PORT

The default port for the HTTP protocol (always `80`).

 http.client.HTTPS_PORT

The default port for the HTTPS protocol (always `443`).

[Subject index](INDEX.md) · [Previous](http-client-httpresponse-class.md) · [Continue](http-client-responses.md) · [Owning module, declaration or section: http.client](http-client-httpconnection-class.md)

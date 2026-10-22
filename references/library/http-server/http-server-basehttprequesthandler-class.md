# http.server: `http.server.BaseHTTPRequestHandler`

*class *http.server.BaseHTTPRequestHandler(*request*, *client_address*, *server*)

Handling the HTTP requests reaching the server is the job of this class. On its own it cannot answer any real HTTP requests; you must subclass it to support each request method (such as `'GET'` or `'POST'`). `BaseHTTPRequestHandler` exposes several class and instance variables, plus methods that subclasses can use.

After parsing the request and the headers, the handler invokes a method tied to the request type. The method name comes from the request itself. As an example, given the request method `SPAM`, the `do_SPAM()` method gets invoked with no arguments. Every piece of pertinent data lives in the handler's instance variables. There is normally no need for subclasses to replace or extend `__init__()`.

These instance variables belong to `BaseHTTPRequestHandler`:

 client_address

Holds a tuple shaped like `(host, port)` that points to the client's address.

 server

Holds the server instance.

 close_connection

A Boolean to be set prior to the return of `handle_one_request()`, signalling whether a further request might arrive or whether the connection ought to be closed.

 requestline

Holds the string form of the HTTP request line, with the trailing CRLF removed. `handle_one_request()` is responsible for setting this attribute. When no valid request line was handled, it should become the empty string.

 command

Holds the command (request type) — for instance, `'GET'`.

 path

Holds the request path. When the URL carries a query component, `path` also covers the query. In the vocabulary of [**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html), `path` here spans `hier-part` together with the `query`.

 request_version

Holds the version string taken from the request — for instance, `'HTTP/1.0'`.

 headers

Stores an instance of whatever class the `MessageClass` class variable names. That instance reads and handles the headers within the HTTP request. The [`parse_headers()`](https://docs.python.org/3.14/library/http.client.html#http.client.parse_headers) function out of [`http.client`](https://docs.python.org/3.14/library/http.client.html#module-http.client) does the header parsing, and it expects the HTTP request to supply a valid [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html) style header.

 rfile

A [`io.BufferedIOBase`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase) input stream positioned to read from the beginning of any optional input data.

 wfile

Holds the output stream used to send a response back to the client. To interoperate successfully with HTTP clients, you must follow the HTTP protocol correctly when writing into this stream.

Changed in version 3.6: This is an [`io.BufferedIOBase`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase) stream.

These attributes belong to `BaseHTTPRequestHandler`:

 server_version

Declares the version of the server software. Overriding it is often desirable. Its format is several whitespace-separated strings, each in the shape name[/version]. As an example, `'BaseHTTP/0.2'`.

 sys_version

Holds the Python system version in a form the `version_string` method and the `server_version` class variable can use. As an example, `'Python/1.4'`.

 error_message_format

Declares a format string for the `send_error()` method to use when assembling an error response for the client. By default the string is populated with variables from `responses`, chosen according to the status code handed to `send_error()`.

 error_content_type

Declares the Content-Type HTTP header of error responses returned to the client. Its default is `'text/html'`.

 protocol_version

Declares the HTTP version the server conforms to. The server sends it in responses so the client learns the server's communication capabilities for later requests. When set to `'HTTP/1.1'`, the server allows HTTP persistent connections; your server *must* then supply an accurate `Content-Length` header (via `send_header()`) on every response it returns to clients. To preserve backwards compatibility, the default is `'HTTP/1.0'`.

 MessageClass

Declares a [`email.message.Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message)-like class for parsing HTTP headers. Overriding this is uncommon; its default is [`http.client.HTTPMessage`](https://docs.python.org/3.14/library/http.client.html#http.client.HTTPMessage).

 responses

This attribute holds a mapping from error code integers to two-element tuples carrying a short and a long message — for example, `{code: (shortmessage, longmessage)}`. The *shortmessage* normally serves as the *message* key inside an error response, and *longmessage* as the *explain* key. The `send_response_only()` and `send_error()` methods make use of it.

The methods below belong to a `BaseHTTPRequestHandler` instance:

[Subject index](INDEX.md) · [Previous](http-server-threadinghttpserver-class.md) · [Continue](http-request-handling-response-and-logging.md) · [Owning module, declaration or section: http.server](http-server-httpserver-class.md)

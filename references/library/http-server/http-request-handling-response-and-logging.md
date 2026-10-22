# http.server.BaseHTTPRequestHandler: HTTP request lifecycle, response headers and logging

handle()

Invokes `handle_one_request()` a single time (or repeatedly when persistent connections are turned on) to service incoming HTTP requests. Overriding it should never be necessary; instead, supply suitable `do_*()` methods.

 handle_one_request()

This method parses the request and dispatches it to the matching `do_*()` method. Overriding it should never be necessary.

 handle_expect_100()

Upon getting an `Expect: 100-continue` request header, an HTTP/1.1 conformant server answers with a `100 Continue` and then `200 OK` headers. You can override this method to raise an error when the server prefers the client not to proceed. For instance, the server may opt to return `417 Expectation Failed` as a response header and `return False`.

Added in version 3.2.

 send_error(*code*, *message=None*, *explain=None*)

Dispatches and records a full error reply to the client. The numeric *code* gives the HTTP error code, and *message* supplies an optional, short, human readable account of the error. Use the *explain* argument to add fuller information about the error; it gets formatted with the `error_message_format` attribute and sent, following a complete set of headers, as the response body. The `responses` attribute supplies the default values for *message* and *explain* used when none is given; for unknown codes both default to the string `???`. The body is empty when the method is HEAD or the response code is any of these: `1*xx*`, `204 No Content`, `205 Reset Content`, `304 Not Modified`.

Changed in version 3.4: A Content-Length header is now part of the error response. The *explain* argument was added.

 send_response(*code*, *message=None*)

Appends a response header to the headers buffer and records the accepted request. The HTTP response line goes into the internal buffer, then the *Server* and *Date* headers. Those two header values come from the `version_string()` and `date_time_string()` methods, respectively. When the server plans to send no additional headers through the `send_header()` method, an `end_headers()` call should follow `send_response()`.

Changed in version 3.3: Headers go to an internal buffer, and `end_headers()` must be invoked explicitly.

 send_header(*keyword*, *value*)

Appends the HTTP header to an internal buffer that gets flushed to the output stream once either `end_headers()` or `flush_headers()` runs. *keyword* gives the header keyword and *value* gives its value. Be aware that once the send_header calls finish, `end_headers()` MUST BE called to finish the operation.

This method does not reject input containing CRLF sequences.

Changed in version 3.2: Headers are stored in an internal buffer.

 send_response_only(*code*, *message=None*)

Dispatches only the response header, intended for cases where the server sends a `100 Continue` response to the client. The headers are not buffered and go straight to the output stream. When *message* is omitted, the HTTP message matching the response *code* is sent.

This method does not reject *message* containing CRLF sequences.

Added in version 3.2.

 end_headers()

Appends a blank line (marking the end of the HTTP headers in the response) to the headers buffer and invokes `flush_headers()`.

Changed in version 3.2: The output stream receives the buffered headers.

 flush_headers()

Sends the headers to the output stream at last and clears the internal headers buffer.

Added in version 3.3.

 log_request(*code='-'*, *size='-'*)

Records an accepted (successful) request. *code* gives the numeric HTTP code tied to the response. When the response size is known, pass it through the *size* parameter.

 log_error(*...*)

Records an error whenever a request cannot be satisfied. By default it hands the message off to `log_message()`, so it accepts the same arguments (*format* plus extra values).

 log_message(*format*, *...*)

Records any message to `sys.stderr`. This is usually overridden to build custom error logging schemes. The *format* argument is a regular printf-style format string, and the extra arguments to `log_message()` feed into the formatting. Each logged message is prefixed with the client ip address and the current date and time.

 version_string()

Yields the version string of the server software. It combines the `server_version` and `sys_version` attributes.

 date_time_string(*timestamp=None*)

Yields the date and time supplied by *timestamp* (which must be `None` or in the format that [`time.time()`](https://docs.python.org/3.14/library/time.html#time.time) returns), formatted for a message header. When *timestamp* is left out, the current date and time are used.

The outcome resembles `'Sun, 06 Nov 1994 08:49:37 GMT'`.

 log_date_time_string()

Yields the current date and time, formatted for logging.

[Subject index](INDEX.md) · [Previous](http-server-basehttprequesthandler-class.md) · [Continue](http-server-basehttprequesthandler-address-string.md) · [Owning module, declaration or section: http.server](http-server-httpserver-class.md) · [Owning module, declaration or section: http.server.BaseHTTPRequestHandler](http-server-basehttprequesthandler-class.md)

# http.server — Security considerations

### Security considerations

`SimpleHTTPRequestHandler` follows symbolic links while servicing requests, which means files outside the chosen directory can end up being served.

The `BaseHTTPRequestHandler.send_header()` and `BaseHTTPRequestHandler.send_response_only()` methods presume sanitized input and skip input validation such as testing for CRLF sequences. Untrusted input can therefore lead to HTTP Header injection attacks.

Older Python releases did not strip control characters out of the log messages written to stderr by `python -m http.server` or by the default `BaseHTTPRequestHandler` `.log_message` implementation. That could let remote clients connecting to your server deliver malicious control codes to your terminal.

Changed in version 3.12: Control characters are scrubbed in stderr logs.

[Subject index](INDEX.md) · [Previous](command-line-interface-port.md) · [Owning module, declaration or section: http.server](http-server-httpserver-class.md)

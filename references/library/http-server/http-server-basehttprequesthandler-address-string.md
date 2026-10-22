# http.server.BaseHTTPRequestHandler: `address_string()`

address_string()

Yields the client address.

Changed in version 3.3: A name lookup used to happen here. So that name resolution does not slow things down, the IP address is now always what gets returned.

[Subject index](INDEX.md) · [Previous](http-request-handling-response-and-logging.md) · [Continue](simple-http-file-request-handler.md) · [Owning module, declaration or section: http.server](http-server-httpserver-class.md) · [Owning module, declaration or section: http.server.BaseHTTPRequestHandler](http-server-basehttprequesthandler-class.md)

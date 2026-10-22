# wsgiref.simple_server: `wsgiref.simple_server.WSGIServer`, `set_app()`, `get_app()`

*class *wsgiref.simple_server.WSGIServer(*server_address*, *RequestHandlerClass*)

Construct a `WSGIServer` instance. *server_address* ought to be a `(host,port)` tuple, and *RequestHandlerClass* ought to be the subclass of [`http.server.BaseHTTPRequestHandler`](https://docs.python.org/3.14/library/http.server.html#http.server.BaseHTTPRequestHandler) that will be tasked with servicing requests.

Calling this constructor is not usually necessary, since the `make_server()` function takes care of every detail on your behalf.

Being a subclass of [`http.server.HTTPServer`](https://docs.python.org/3.14/library/http.server.html#http.server.HTTPServer), `WSGIServer` makes all of that class’s methods (`serve_forever()` and `handle_request()` among them) available. `WSGIServer` further supplies these WSGI-specific methods:

 set_app(*application*)

Designate the callable *application* as the WSGI application that requests will be routed to.

 get_app()

Return whichever application callable is currently set.

You typically won’t need these extra methods, since `make_server()` normally calls `set_app()`, and `get_app()` is there chiefly for the sake of request handler instances.

[Subject index](INDEX.md) · [Previous](wsgi-server-factory-and-demo-application.md) · [Continue](wsgi-request-handler-contract.md) · [Owning module, declaration or section: wsgiref.simple_server](wsgi-server-factory-and-demo-application.md)

# wsgiref.simple_server: `wsgiref.simple_server.WSGIRequestHandler`, `get_environ()`, `get_stderr()`, `handle()`

*class *wsgiref.simple_server.WSGIRequestHandler(*request*, *client_address*, *server*)

Build an HTTP handler for the supplied *request* (that is, a socket), *client_address* (a `(host,port)` tuple), and *server* (a `WSGIServer` instance).

There’s no need to instantiate this class yourself; `WSGIServer` objects spin them up automatically whenever they’re needed. You may, though, subclass it and pass your subclass as a *handler_class* to the `make_server()` function. A few methods that subclasses might find worth overriding:

 get_environ()

Produce a `WSGIEnvironment` dictionary for a request. By default the implementation duplicates the contents of the `WSGIServer` object’s `base_environ` dictionary attribute and then layers in assorted headers drawn from the HTTP request. Every call to this method ought to yield a brand-new dictionary holding all the pertinent CGI environment variables that [**PEP 3333**](https://peps.python.org/pep-3333/) specifies.

 get_stderr()

Return whatever object is to act as the `wsgi.errors` stream. By default the implementation merely returns `sys.stderr`.

 handle()

Service the HTTP request. By default the implementation builds a handler instance from a `wsgiref.handlers` class to carry out the actual WSGI application interface.

[Subject index](INDEX.md) · [Previous](wsgi-server-application-access.md) · [Continue](../wsgiref-validate/wsgiref-validate-validator.md) · [Owning module, declaration or section: wsgiref.simple_server](wsgi-server-factory-and-demo-application.md)

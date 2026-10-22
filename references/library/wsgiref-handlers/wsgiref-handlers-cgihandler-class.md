# wsgiref.handlers: `wsgiref.handlers.CGIHandler`

### `wsgiref.handlers` – server/gateway base classes

Base handler classes for constructing WSGI servers and gateways are what this module provides. Provided they’re handed a CGI-like environment together with input, output, and error streams, these base classes take care of most of the labor involved in talking to a WSGI application.

 *class *wsgiref.handlers.CGIHandler

CGI-style invocation through `sys.stdin`, `sys.stdout`, `sys.stderr` and `os.environ`. This proves useful when you hold a WSGI application and wish to run it as a CGI script. Just call `CGIHandler().run(app)`, in which `app` is the WSGI application object you mean to invoke.

This class subclasses `BaseCGIHandler`, setting `wsgi.run_once` to true, `wsgi.multithread` to false, and `wsgi.multiprocess` to true, and it always turns to [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) and [`os`](https://docs.python.org/3.14/library/os.html#module-os) to acquire the CGI streams and environment it needs.

[Subject index](INDEX.md) · [Previous](../wsgiref-validate/wsgiref-validate-validator.md) · [Continue](wsgiref-handlers-iiscgihandler-class.md)

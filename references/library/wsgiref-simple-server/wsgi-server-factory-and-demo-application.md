# wsgiref.simple_server: `wsgiref.simple_server.make_server()`, `wsgiref.simple_server.demo_app()`

### `wsgiref.simple_server` – a simple WSGI HTTP server

A basic HTTP server (built atop [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server)) that hosts WSGI applications is what this module delivers. A single WSGI application is served by each server instance on a particular host and port. To host several applications on one host and port, build a WSGI application that reads `PATH_INFO` to decide which application each request should reach. (For example, with the `shift_path_info()` function from `wsgiref.util`.)

 wsgiref.simple_server.make_server(*host*, *port*, *app*, *server_class=WSGIServer*, *handler_class=WSGIRequestHandler*)

Spin up a new WSGI server bound to *host* and *port* that accepts connections on behalf of *app*. What comes back is an instance of the given *server_class*, which will service requests by way of the named *handler_class*. As specified by [**PEP 3333**](https://peps.python.org/pep-3333/), *app* must be a WSGI application object.

Example usage:

```python
from wsgiref.simple_server import make_server, demo_app

with make_server('', 8000, demo_app) as httpd:
    print("Serving HTTP on port 8000...")

    # Respond to requests until process is killed
    httpd.serve_forever()

    # Alternative: serve one request, then exit
    httpd.handle_request()

```

 wsgiref.simple_server.demo_app(*environ*, *start_response*)

A compact yet complete WSGI application, this function returns a text page bearing the message “Hello world!” together with a listing of the key/value pairs carried in the *environ* argument. It comes in handy for confirming that a WSGI server (for instance `wsgiref.simple_server`) can run a straightforward WSGI application properly.

The *start_response* callable is expected to conform to the `StartResponse` protocol.

[Subject index](INDEX.md) · [Previous](../wsgiref-headers/wsgi-response-header-access-and-addition.md) · [Continue](wsgi-server-application-access.md)

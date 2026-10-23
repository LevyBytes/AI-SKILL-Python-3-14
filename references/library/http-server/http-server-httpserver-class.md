# http.server: `http.server.HTTPServer`

# Http.Server

### `http.server` - HTTP servers

**Source code:** [Lib/http/server.py](https://github.com/python/cpython/tree/3.14/Lib/http/server.py)

---

The classes for building HTTP servers are provided by this module.

Warning

`http.server` is not advised for production deployments. Only rudimentary security checks are implemented.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

On WebAssembly, this module is either unavailable or non-functional. Consult [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for further details.

A single class, `HTTPServer`, derives from [`socketserver.TCPServer`](https://docs.python.org/3.14/library/socketserver.html#socketserver.TCPServer). It opens and listens on the HTTP socket, then routes incoming requests to a handler. The following code shows how to set up and start the server:

```python
def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

```

 *class *http.server.HTTPServer(*server_address*, *RequestHandlerClass*)

Extending the [`TCPServer`](https://docs.python.org/3.14/library/socketserver.html#socketserver.TCPServer) class, this class keeps the server address in instance variables called `server_name` and `server_port`. The handler can reach the server, usually via its own `server` instance variable.

[Subject index](INDEX.md) · [Continue](http-server-threadinghttpserver-class.md)

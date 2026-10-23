# xmlrpc.server: `xmlrpc.server.SimpleXMLRPCServer`

# Xmlrpc.Server

### `xmlrpc.server` - Basic XML-RPC servers

**Source code:** [Lib/xmlrpc/server.py](https://github.com/python/cpython/tree/3.14/Lib/xmlrpc/server.py)

---

A rudimentary server framework for XML-RPC servers coded in Python is what the `xmlrpc.server` module offers. Such servers may run on their own through `SimpleXMLRPCServer`, or sit inside a CGI environment by way of `CGIXMLRPCRequestHandler`.

Warning

Against maliciously built data the `xmlrpc.server` module offers no protection. Should you have to parse untrusted or unauthenticated data, consult [XML security](https://docs.python.org/3.14/library/xml.html#xml-security).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

On WebAssembly this module is unavailable or non-functional. Consult [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for further detail.

`*class *xmlrpc.server.SimpleXMLRPCServer(*addr*, *requestHandler=SimpleXMLRPCRequestHandler*, *logRequests=True*, *allow_none=False*, *encoding=None*, *bind_and_activate=True*, *use_builtin_types=False*)`

Spin up a fresh server instance. The class hands you methods for registering functions that the XML-RPC protocol can then call. Supply the *requestHandler* parameter as a factory producing request handler instances; left alone it defaults to `SimpleXMLRPCRequestHandler`. Both the *addr* and *requestHandler* parameters flow through to the [`socketserver.TCPServer`](https://docs.python.org/3.14/library/socketserver.html#socketserver.TCPServer) constructor. While *logRequests* stays true (its default), requests are logged; flip it to false and logging stops. The *allow_none* and *encoding* parameters pass along to [`xmlrpc.client`](https://docs.python.org/3.14/library/xmlrpc.client.html#module-xmlrpc.client), where they govern the XML-RPC responses the server sends back. The *bind_and_activate* parameter decides whether the constructor calls `server_bind()` and `server_activate()` straight away; it defaults to true, and setting it false lets code adjust the *allow_reuse_address* class variable before the address gets bound. The *use_builtin_types* parameter feeds into the [`loads()`](https://docs.python.org/3.14/library/xmlrpc.client.html#xmlrpc.client.loads) function and decides which types are handled when date/time values or binary data arrive; it too defaults to false.

Changed in version 3.3: The *use_builtin_types* flag was added.

[Subject index](INDEX.md) · [Continue](xmlrpc-server-cgixmlrpcrequesthandler-class.md)

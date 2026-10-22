# socketserver: `socketserver.StreamRequestHandler`, `socketserver.DatagramRequestHandler`

*class *socketserver.StreamRequestHandler

 *class *socketserver.DatagramRequestHandler

These subclasses of `BaseRequestHandler` override the `setup()` and `finish()` methods and supply `rfile` and `wfile` attributes.

 rfile

A file object from which the received request is read. Supports the [`io.BufferedIOBase`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase) readable interface.

 wfile

A file object the reply is written to. Supports the [`io.BufferedIOBase`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase) writable interface

Changed in version 3.6: `wfile` also supports the [`io.BufferedIOBase`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase) writable interface.

[Subject index](INDEX.md) · [Previous](request-handler-setup-handle-and-finish.md) · [Continue](tcp-server-example-overview.md) · [Owning module, declaration or section: socketserver](socketserver-tcpserver-class.md) · [Owning module, declaration or section: Request Handler Objects](socketserver-baserequesthandler-class.md)

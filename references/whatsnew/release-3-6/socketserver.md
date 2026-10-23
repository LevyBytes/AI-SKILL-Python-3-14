# What's New In Python 3.6 / socketserver - http.server, io, socketserver, wsgiref, xmlrpc.server

### socketserver

The [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) protocol is now honored by servers built on the [`socketserver`](https://docs.python.org/3.14/library/socketserver.html#module-socketserver) module, among them those declared in [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server), [`xmlrpc.server`](https://docs.python.org/3.14/library/xmlrpc.server.html#module-xmlrpc.server) and [`wsgiref.simple_server`](https://docs.python.org/3.14/library/wsgiref.html#module-wsgiref.simple_server). (Contributed by Aviv Palivoda in [bpo-26404](https://bugs.python.org/issue?@action=redirect&bpo=26404).)

On [`StreamRequestHandler`](https://docs.python.org/3.14/library/socketserver.html#socketserver.StreamRequestHandler) classes, the [`wfile`](https://docs.python.org/3.14/library/socketserver.html#socketserver.DatagramRequestHandler.wfile) attribute now provides the [`io.BufferedIOBase`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase) writable interface. Notably, a [`write()`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.write) call is now assured to transmit every byte. (Contributed by Martin Panter in [bpo-26721](https://bugs.python.org/issue?@action=redirect&bpo=26721).)

[Subject index](INDEX.md) · [Previous source section](socket.md) · [Next source section](ssl.md) · [Release/subject declaration](summary-release-highlights.md)

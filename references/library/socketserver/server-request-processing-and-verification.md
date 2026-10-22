# socketserver.BaseServer: `process_request()`, `server_activate()`, `server_bind()`, `verify_request()`

process_request(*request*, *client_address*)

Invokes `finish_request()` to build an instance of the `RequestHandlerClass`. When wanted, this function may launch a fresh process or thread to handle the request; the `ForkingMixIn` and `ThreadingMixIn` classes do exactly that.

 server_activate()

Invoked by the server's constructor to bring the server online. A TCP server's default behaviour merely calls [`listen()`](https://docs.python.org/3.14/library/socket.html#socket.socket.listen) on the server's socket. Can be overridden.

 server_bind()

Invoked by the server's constructor to bind the socket to the intended address. Can be overridden.

 verify_request(*request*, *client_address*)

Has to return a Boolean; if the result is [`True`](https://docs.python.org/3.14/library/constants.html#True), the request goes ahead and is processed, whereas if it is [`False`](https://docs.python.org/3.14/library/constants.html#False), the request is rejected. Override this function to enforce access controls on a server. The default implementation always returns `True`.

Changed in version 3.6: The [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) protocol gained support here. Leaving the context manager amounts to a `server_close()` call.

[Subject index](INDEX.md) · [Previous](server-lifecycle-and-timeout-handling.md) · [Continue](socketserver-baserequesthandler-class.md) · [Owning module, declaration or section: socketserver](socketserver-tcpserver-class.md) · [Owning module, declaration or section: socketserver.BaseServer](socketserver-baseserver-class.md) · [Owning module, declaration or section: Server Objects](socketserver-baseserver-class.md)

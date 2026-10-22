# socketserver.BaseRequestHandler: `setup()`, `handle()`, `finish()`

setup()

Runs ahead of the `handle()` method to carry out whatever initialization is needed. By default it does nothing.

 handle()

This function has to perform everything needed to service a request. The default implementation does nothing. A number of instance attributes are at its disposal: the request is reachable through `request`; the client address through `client_address`; and the server instance through `server`, should it require per-server information.

What type `request` holds differs between datagram and stream services. In stream services `request` is a socket object, while in datagram services `request` is a pair consisting of a string and a socket.

 finish()

Runs after the `handle()` method to carry out any needed cleanup. By default it does nothing. Should `setup()` throw an exception, this function will not run.

 request

The *new* [`socket.socket`](https://docs.python.org/3.14/library/socket.html#socket.socket) object that will be used for communicating with the client.

 client_address

Client address handed back by `BaseServer.get_request()`.

 server

`BaseServer` object employed for handling the request.

[Subject index](INDEX.md) · [Previous](socketserver-baserequesthandler-class.md) · [Continue](stream-and-datagram-request-handlers.md) · [Owning module, declaration or section: socketserver](socketserver-tcpserver-class.md) · [Owning module, declaration or section: socketserver.BaseRequestHandler](socketserver-baserequesthandler-class.md) · [Owning module, declaration or section: Request Handler Objects](socketserver-baserequesthandler-class.md)

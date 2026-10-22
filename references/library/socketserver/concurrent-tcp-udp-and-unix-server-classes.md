# socketserver: Forking and threading TCP, UDP and Unix server classes

*class *socketserver.ForkingTCPServer

 *class *socketserver.ForkingUDPServer

 *class *socketserver.ThreadingTCPServer

 *class *socketserver.ThreadingUDPServer

 *class *socketserver.ForkingUnixStreamServer

 *class *socketserver.ForkingUnixDatagramServer

 *class *socketserver.ThreadingUnixStreamServer

 *class *socketserver.ThreadingUnixDatagramServer

The mix-in classes are used to define these classes ahead of time.

Added in version 3.12: The `ForkingUnixStreamServer` and `ForkingUnixDatagramServer` classes were added.

Implementing a service means deriving a class from `BaseRequestHandler` and overriding its `handle()` method. You may then operate different flavours of the service by pairing one of the server classes with your request handler class. Stream services and datagram services need a different request handler class. Using the handler subclasses `StreamRequestHandler` or `DatagramRequestHandler` can conceal that detail.

Naturally, judgment is still required! As an example, a forking server is pointless when the service keeps in-memory state that varying requests can alter, because changes made in a child process never propagate back to the original state held in the parent and handed to each child. Under such circumstances a threading server is an option, though you will likely need locks to safeguard the consistency of the shared data.

Conversely, when constructing an HTTP server whose data all lives elsewhere (in the file system, say), a synchronous class essentially leaves the service "deaf" for the duration of one request — possibly a very long stretch if the client is slow to take in everything it asked for. In that situation a threading or forking server fits.

There are occasions where it makes sense to handle one portion of a request synchronously and then complete the rest inside a forked child, depending on the request's contents. You can achieve this with a synchronous server plus an explicit fork carried out in the request handler class's `handle()` method.

A further technique for coping with several concurrent requests where neither threads nor [`fork()`](https://docs.python.org/3.14/library/os.html#os.fork) is supported (or where they prove too costly or unsuitable for the service) is to keep an explicit table of partially completed requests and lean on [`selectors`](https://docs.python.org/3.14/library/selectors.html#module-selectors) to choose which request to advance next (or whether instead to accept a fresh incoming request). This matters most for stream services, since any client there might stay connected for an extended period (when threads or subprocesses are off the table).

[Subject index](INDEX.md) · [Previous](server-creation-notes.md) · [Continue](socketserver-baseserver-class.md) · [Owning module, declaration or section: socketserver](socketserver-tcpserver-class.md) · [Owning module, declaration or section: Server Creation Notes](forking-and-threading-server-mixins.md)

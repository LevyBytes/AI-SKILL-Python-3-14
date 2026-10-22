# socketserver: `socketserver.UnixStreamServer`, `socketserver.UnixDatagramServer`

*class *socketserver.UnixStreamServer(*server_address*, *RequestHandlerClass*, *bind_and_activate=True*)

 *class *socketserver.UnixDatagramServer(*server_address*, *RequestHandlerClass*, *bind_and_activate=True*)

Seen far less often, these classes resemble the TCP and UDP ones but rely on Unix domain sockets; they are absent on platforms other than Unix. Their parameters match those of `TCPServer`.

All four of these classes deal with requests *synchronously*: every request has to finish before the following one may begin. Such an approach falls short when a single request takes a while — perhaps it demands heavy computation, or it sends back a large volume of data that a slow client struggles to consume. The remedy is to spin off an individual process or thread per request; the `ForkingMixIn` and `ThreadingMixIn` mix-in classes exist to enable asynchronous behaviour.

Building a server involves a handful of steps. To begin, write a request handler class that subclasses `BaseRequestHandler` and overrides its `handle()` method; that method handles incoming requests. Next, create an instance of one of the server classes, handing it both the server's address and the request handler class. The advised practice is to employ the server within a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement. After that, invoke the server object's `handle_request()` or `serve_forever()` method to service one request or many. Lastly, call `server_close()` to shut the socket (unless a `with` statement was used).

If you subclass `ThreadingMixIn` to get threaded connection handling, be explicit about how the threads should act during a sudden shutdown. `ThreadingMixIn` provides a *daemon_threads* attribute that controls whether the server waits for threads to finish. Set the flag deliberately when you want the threads to operate independently; the default value is [`False`](https://docs.python.org/3.14/library/constants.html#False), so Python holds off exiting until every thread spawned by `ThreadingMixIn` has finished.

Regardless of which network protocol a server class uses, they all share the same outward-facing methods and attributes.

[Subject index](INDEX.md) · [Previous](socketserver-udpserver-class.md) · [Continue](forking-and-threading-server-mixins.md) · [Owning module, declaration or section: socketserver](socketserver-tcpserver-class.md)

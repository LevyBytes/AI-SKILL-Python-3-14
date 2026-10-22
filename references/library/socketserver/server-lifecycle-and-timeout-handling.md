# socketserver.BaseServer: `fileno()`, `handle_request()`, `serve_forever()`, `service_actions()`, `shutdown()`, `server_close()`, `finish_request()`, `get_request()`, `handle_error()`, `handle_timeout()`

fileno()

Returns an integer file descriptor for the socket the server listens on. This function is typically handed to [`selectors`](https://docs.python.org/3.14/library/selectors.html#module-selectors) so that several servers can be watched within one process.

 handle_request()

Services one request. The function invokes these methods one after another: `get_request()`, `verify_request()`, and `process_request()`. Should the handler class's user-supplied `handle()` method throw an exception, the server's `handle_error()` method is invoked. When no request comes in during `timeout` seconds, `handle_timeout()` runs and `handle_request()` returns.

 serve_forever(*poll_interval=0.5*)

Keeps servicing requests until an explicit `shutdown()` request arrives. Checks for shutdown at intervals of *poll_interval* seconds. Disregards the `timeout` attribute. It additionally calls `service_actions()`, which a subclass or mixin may employ to supply actions tied to a specific service. To illustrate, the `ForkingMixIn` class relies on `service_actions()` to reap zombie child processes.

Changed in version 3.3: Added `service_actions` call to the `serve_forever` method.

 service_actions()

Invoked within the `serve_forever()` loop. Subclasses or mixin classes may override this method to carry out service-specific actions such as cleanup work.

Added in version 3.3.

 shutdown()

Instructs the `serve_forever()` loop to halt and blocks until it has. `shutdown()` has to be called while `serve_forever()` runs in a separate thread, or a deadlock results.

 server_close()

Tidies up the server. Can be overridden.

 address_family

The protocol family that the server's socket belongs to. Frequent examples include [`socket.AF_INET`](https://docs.python.org/3.14/library/socket.html#socket.AF_INET), [`socket.AF_INET6`](https://docs.python.org/3.14/library/socket.html#socket.AF_INET6), and [`socket.AF_UNIX`](https://docs.python.org/3.14/library/socket.html#socket.AF_UNIX). To obtain IPv6 server classes, subclass this module's TCP or UDP server classes and set the class attribute `address_family = AF_INET6`.

 RequestHandlerClass

The request handler class provided by the user; one instance of it gets built per request.

 server_address

The address the server listens on. How addresses are formatted depends on the protocol family; refer to the [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module's documentation for specifics. With internet protocols this is a tuple holding a string for the address plus an integer port number — for instance, `('127.0.0.1', 80)`.

 socket

The socket object the server uses to listen for arriving requests.

These class variables are supported by the server classes:

 allow_reuse_address

Indicates whether the server permits reusing an address. The default is [`False`](https://docs.python.org/3.14/library/constants.html#False); subclasses can set it to alter that policy.

 request_queue_size

How big the request queue is. When processing a single request drags on, any requests showing up while the server is occupied get queued, up to `request_queue_size` of them. After the queue fills, additional client requests receive a "Connection denied" error. The usual default is 5, but subclasses may override it.

 socket_type

The kind of socket the server uses; [`socket.SOCK_STREAM`](https://docs.python.org/3.14/library/socket.html#socket.SOCK_STREAM) and [`socket.SOCK_DGRAM`](https://docs.python.org/3.14/library/socket.html#socket.SOCK_DGRAM) are two frequent choices.

 timeout

How long the timeout lasts, expressed in seconds, or [`None`](https://docs.python.org/3.14/library/constants.html#None) when no timeout should apply. Should `handle_request()` see no arriving requests before the timeout elapses, the `handle_timeout()` method runs.

Subclasses of base server classes such as `TCPServer` can override a range of server methods; these methods hold no value for outside users of the server object.

 finish_request(*request*, *client_address*)

Carries out the actual request processing by building a `RequestHandlerClass` instance and calling its `handle()` method.

 get_request()

Has to take a request off the socket and hand back a 2-tuple holding the *new* socket object that will be used for talking with the client, along with the client's address.

 handle_error(*request*, *client_address*)

This function runs whenever a `RequestHandlerClass` instance's `handle()` method throws an exception. By default it writes the traceback to standard error and keeps handling subsequent requests.

Changed in version 3.6: Invoked solely for exceptions that derive from the [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception) class from now on.

 handle_timeout()

This function runs once the `timeout` attribute is given a value besides [`None`](https://docs.python.org/3.14/library/constants.html#None) and the timeout interval elapses without any requests arriving. For forking servers the default behaviour is to gather the status of any child processes that have terminated, whereas in threading servers this method does nothing at all.

[Subject index](INDEX.md) · [Previous](socketserver-baseserver-class.md) · [Continue](server-request-processing-and-verification.md) · [Owning module, declaration or section: socketserver](socketserver-tcpserver-class.md) · [Owning module, declaration or section: socketserver.BaseServer](socketserver-baseserver-class.md) · [Owning module, declaration or section: Server Objects](socketserver-baseserver-class.md)

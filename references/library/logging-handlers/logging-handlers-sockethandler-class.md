# logging.handlers: `logging.handlers.SocketHandler`

### SocketHandler

Found in the `logging.handlers` module, the `SocketHandler` class routes logging output to a network socket. A TCP socket is what the base class uses.

 *class *logging.handlers.SocketHandler(*host*, *port*)

Hands back a fresh instance of the `SocketHandler` class meant to talk to a remote machine whose address is given by *host* and *port*.

Changed in version 3.4: When `port` is given as `None`, a Unix domain socket is built from the value in `host` — otherwise, a TCP socket is built.

[Subject index](INDEX.md) · [Previous](timed-rotation-rollover-methods.md) · [Continue](socket-handler-lifecycle-and-connection.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md)

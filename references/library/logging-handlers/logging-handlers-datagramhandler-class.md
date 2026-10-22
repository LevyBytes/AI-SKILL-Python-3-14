# logging.handlers: `logging.handlers.DatagramHandler`

### DatagramHandler

Found in the `logging.handlers` module, the `DatagramHandler` class derives from `SocketHandler` to support sending logging messages over UDP sockets.

 *class *logging.handlers.DatagramHandler(*host*, *port*)

Hands back a fresh instance of the `DatagramHandler` class meant to talk to a remote machine whose address is given by *host* and *port*.

Note

Because UDP isn't a streaming protocol, no persistent connection exists between an instance of this handler and *host*. For that reason, when a network socket is in use, a DNS lookup might be needed each time an event is logged, which can add some latency to the system. Should this affect you, you can perform a lookup yourself and initialize this handler with the looked-up IP address in place of the hostname.

Changed in version 3.4: When `port` is given as `None`, a Unix domain socket is built from the value in `host` — otherwise, a UDP socket is built.

[Subject index](INDEX.md) · [Previous](socket-handler-lifecycle-and-connection.md) · [Continue](datagram-handler-emission-and-send.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md)

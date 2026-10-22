# logging.handlers.DatagramHandler: `emit()`, `makeSocket()`, `send()`

emit()

Pickles the record's attribute dictionary and writes it onto the socket in binary form. Should the socket hit an error, the packet is silently dropped. To unpickle the record back into a [`LogRecord`](https://docs.python.org/3.14/library/logging.html#logging.LogRecord) at the receiving end, use the [`makeLogRecord()`](https://docs.python.org/3.14/library/logging.html#logging.makeLogRecord) function.

 makeSocket()

Here the factory method of `SocketHandler` is overridden to build a UDP socket ([`socket.SOCK_DGRAM`](https://docs.python.org/3.14/library/socket.html#socket.SOCK_DGRAM)).

 send(*s*)

Send a pickled byte-string to a socket. The format of the byte-string sent matches what's described in the documentation for `SocketHandler.makePickle()`.

[Subject index](INDEX.md) · [Previous](logging-handlers-datagramhandler-class.md) · [Continue](logging-handlers-sysloghandler-class.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md) · [Owning module, declaration or section: logging.handlers.DatagramHandler](logging-handlers-datagramhandler-class.md) · [Owning module, declaration or section: DatagramHandler](logging-handlers-datagramhandler-class.md)

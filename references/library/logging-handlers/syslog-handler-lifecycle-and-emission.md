# logging.handlers.SysLogHandler: `close()`, `createSocket()`, `emit()`

close()

Closes the socket to the remote host.

 createSocket()

Attempts to create a socket and, when it isn't a datagram socket, connect it to the far end. This method is invoked during handler initialization, but it isn't treated as an error if the far end isn't listening at that moment — the method gets invoked again while emitting an event, should there be no socket at that point.

Added in version 3.11.

 emit(*record*)

The record is formatted, and afterwards sent to the syslog server. Where exception information exists, it is *not* sent to the server.

[Subject index](INDEX.md) · [Previous](logging-handlers-sysloghandler-class.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md) · [Owning module, declaration or section: logging.handlers.SysLogHandler](logging-handlers-sysloghandler-class.md) · [Owning module, declaration or section: SysLogHandler](logging-handlers-sysloghandler-class.md) · [Required continuation of the source contract](syslog-priority-encoding-and-mapping.md)

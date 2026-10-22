# socketserver: `socketserver.BaseServer`

### Server Objects

 *class *socketserver.BaseServer(*server_address*, *RequestHandlerClass*)

This serves as the parent class for every Server object in the module. It lays out the interface shown below yet leaves most methods unimplemented, deferring that to subclasses. Both supplied parameters end up saved in the matching `server_address` and `RequestHandlerClass` attributes.

[Subject index](INDEX.md) · [Previous](concurrent-tcp-udp-and-unix-server-classes.md) · [Continue](server-lifecycle-and-timeout-handling.md) · [Owning module, declaration or section: socketserver](socketserver-tcpserver-class.md)

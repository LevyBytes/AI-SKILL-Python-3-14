# socketserver: `socketserver.BaseRequestHandler`

### Request Handler Objects

 *class *socketserver.BaseRequestHandler

This acts as the parent class for all request handler objects. It establishes the interface presented below. A concrete request handler subclass is required to supply a fresh `handle()` method and may override any of the remaining methods. Each request gets a brand-new instance of the subclass.

[Subject index](INDEX.md) · [Previous](server-request-processing-and-verification.md) · [Continue](request-handler-setup-handle-and-finish.md) · [Owning module, declaration or section: socketserver](socketserver-tcpserver-class.md)

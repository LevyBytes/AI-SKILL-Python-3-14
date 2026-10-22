# xmlrpc.server: `xmlrpc.server.DocXMLRPCServer`

### Documenting XMLRPC server

These classes build on the ones above to serve HTML documentation when HTTP GET requests come in. Such servers may run on their own through `DocXMLRPCServer`, or sit inside a CGI environment by way of `DocCGIXMLRPCRequestHandler`.

`*class *xmlrpc.server.DocXMLRPCServer(*addr*, *requestHandler=DocXMLRPCRequestHandler*, *logRequests=True*, *allow_none=False*, *encoding=None*, *bind_and_activate=True*, *use_builtin_types=True*)`

Spin up a fresh server instance. Every parameter carries the same meaning it has for `SimpleXMLRPCServer`, except that *requestHandler* defaults to `DocXMLRPCRequestHandler`.

Changed in version 3.3: The *use_builtin_types* flag was added.

[Subject index](INDEX.md) · [Previous](cgi-xmlrpc-registration-and-request-handling.md) · [Continue](xmlrpc-server-doccgixmlrpcrequesthandler-class.md) · [Owning module, declaration or section: xmlrpc.server](xmlrpc-server-simplexmlrpcserver-class.md)

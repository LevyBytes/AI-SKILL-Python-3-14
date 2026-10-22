# xmlrpc.server: `xmlrpc.server.CGIXMLRPCRequestHandler`

`*class *xmlrpc.server.CGIXMLRPCRequestHandler(*allow_none=False*, *encoding=None*, *use_builtin_types=False*)`

Spin up a fresh instance to service XML-RPC requests within a CGI environment. The *allow_none* and *encoding* parameters pass along to [`xmlrpc.client`](https://docs.python.org/3.14/library/xmlrpc.client.html#module-xmlrpc.client), where they govern the XML-RPC responses the server sends back. The *use_builtin_types* parameter feeds into the [`loads()`](https://docs.python.org/3.14/library/xmlrpc.client.html#xmlrpc.client.loads) function and decides which types are handled when date/time values or binary data arrive; it defaults to false.

Changed in version 3.3: The *use_builtin_types* flag was added.

[Subject index](INDEX.md) · [Previous](xmlrpc-server-simplexmlrpcserver-class.md) · [Continue](xmlrpc-server-simplexmlrpcrequesthandler-class.md) · [Owning module, declaration or section: xmlrpc.server](xmlrpc-server-simplexmlrpcserver-class.md)

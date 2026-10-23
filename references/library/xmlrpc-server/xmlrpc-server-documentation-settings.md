# xmlrpc.server - DocXMLRPCServer objects

### DocXMLRPCServer objects

Derived from `SimpleXMLRPCServer`, the `DocXMLRPCServer` class gives you a way to assemble self-documenting, self-contained XML-RPC servers. HTTP POST requests are treated as XML-RPC method calls, while HTTP GET requests are answered by producing pydoc-style HTML documentation. That lets a server publish its own web-based documentation.

`DocXMLRPCServer.set_server_title(*server_title*)`

Set the title that the generated HTML documentation uses. This title goes inside the HTML “title” element.

`DocXMLRPCServer.set_server_name(*server_name*)`

Set the name that the generated HTML documentation uses. This name shows up at the top of the generated documentation within an “h1” element.

`DocXMLRPCServer.set_server_documentation(*server_documentation*)`

Set the description that the generated HTML documentation uses. This description shows up as a paragraph, sitting below the server name, in the documentation.

[Subject index](INDEX.md) · [Previous](xmlrpc-server-docxmlrpcrequesthandler-class.md) · [Continue](cgi-xmlrpc-documentation-settings.md) · [Owning module, declaration or section: xmlrpc.server](xmlrpc-server-simplexmlrpcserver-class.md)

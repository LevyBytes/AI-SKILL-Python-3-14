# xmlrpc.server - CGIXMLRPCRequestHandler

### CGIXMLRPCRequestHandler

You can put the `CGIXMLRPCRequestHandler` class to work servicing XML-RPC requests directed at Python CGI scripts.

`CGIXMLRPCRequestHandler.register_function(*function=None*, *name=None*)`

Register a function able to answer XML-RPC requests. Provide *name* and it becomes the method name tied to *function*; leave it out and [`function.__name__`](https://docs.python.org/3.14/reference/datamodel.html#function.__name__) is used instead. *name* is a string and may carry characters that aren't valid in Python identifiers, the period among them.

You can also apply this method as a decorator. In that role, *name* may only be passed as a keyword argument to register *function* beneath *name*. Without a *name*, [`function.__name__`](https://docs.python.org/3.14/reference/datamodel.html#function.__name__) is used.

Changed in version 3.7: `register_function()` can be used as a decorator.

`CGIXMLRPCRequestHandler.register_instance(*instance*)`

Register an object that surfaces method names which were never registered through `register_function()`. Where instance carries a `_dispatch()` method, that method is invoked with the requested method name and the request's parameters, and its return value goes back to the client as the result. Where instance lacks a `_dispatch()` method, it is scanned for an attribute whose name matches the requested method; and if the requested method name holds periods, each of its components is looked up one by one, amounting to a simple hierarchical search. The value turned up by that search is then invoked with the request's parameters, and the return value travels back to the client.

`CGIXMLRPCRequestHandler.register_introspection_functions()`

Register the XML-RPC introspection functions `system.listMethods`, `system.methodHelp`, and `system.methodSignature`.

`CGIXMLRPCRequestHandler.register_multicall_functions()`

Register the XML-RPC multicall function `system.multicall`.

`CGIXMLRPCRequestHandler.handle_request(*request_text=None*)`

Service an XML-RPC request. When *request_text* is supplied, it ought to be the POST data delivered by the HTTP server; otherwise stdin's contents are read instead.

Example:

```python
class MyFuncs:
    def mul(self, x, y):
        return x * y

handler = CGIXMLRPCRequestHandler()
handler.register_function(pow)
handler.register_function(lambda x,y: x+y, 'add')
handler.register_introspection_functions()
handler.register_instance(MyFuncs())
handler.handle_request()

```

[Subject index](INDEX.md) · [Previous](xmlrpc-client-server-proxy-example.md) · [Continue](xmlrpc-server-docxmlrpcserver-class.md) · [Owning module, declaration or section: xmlrpc.server](xmlrpc-server-simplexmlrpcserver-class.md)

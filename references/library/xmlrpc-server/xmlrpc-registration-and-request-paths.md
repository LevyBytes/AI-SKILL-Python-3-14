# xmlrpc.server — SimpleXMLRPCServer objects

### SimpleXMLRPCServer objects

Built on [`socketserver.TCPServer`](https://docs.python.org/3.14/library/socketserver.html#socketserver.TCPServer), the `SimpleXMLRPCServer` class gives you a way to put together simple, self-contained XML-RPC servers.

`SimpleXMLRPCServer.register_function(*function=None*, *name=None*)`

Register a function able to answer XML-RPC requests. Provide *name* and it becomes the method name tied to *function*; leave it out and [`function.__name__`](https://docs.python.org/3.14/reference/datamodel.html#function.__name__) is used instead. *name* is a string and may carry characters that aren't valid in Python identifiers, the period among them.

You can also apply this method as a decorator. In that role, *name* may only be passed as a keyword argument to register *function* beneath *name*. Without a *name*, [`function.__name__`](https://docs.python.org/3.14/reference/datamodel.html#function.__name__) is used.

Changed in version 3.7: `register_function()` can be used as a decorator.

`SimpleXMLRPCServer.register_instance(*instance*, *allow_dotted_names=False*)`

Register an object that surfaces method names which were never registered through `register_function()`. Where *instance* carries a `_dispatch()` method, that method gets invoked with the requested method name and the request's parameters. Its API reads `def _dispatch(self, method, params)` (mind that *params* is not a variable argument list). Should it delegate to an underlying function for the work, that function is invoked as `func(*params)`, which spreads out the parameter list. Whatever `_dispatch()` returns goes back to the client as the result. Where *instance* lacks a `_dispatch()` method, it is scanned for an attribute whose name matches the requested method.

When the optional *allow_dotted_names* argument is true and the instance has no `_dispatch()` method, then a requested method name containing periods has each of its components looked up one by one, which amounts to a simple hierarchical search. The value turned up by that search is then invoked with the request's parameters, and the return value travels back to the client.

Warning

Turning on the *allow_dotted_names* option opens the door for intruders to reach your module's global variables and possibly to run arbitrary code on your machine. Reserve this option for a secure, closed network.

`SimpleXMLRPCServer.register_introspection_functions()`

Registers the XML-RPC introspection functions `system.listMethods`, `system.methodHelp`, and `system.methodSignature`.

`SimpleXMLRPCServer.register_multicall_functions()`

Registers the XML-RPC multicall function system.multicall.

`SimpleXMLRPCRequestHandler.rpc_paths`

An attribute whose value has to be a tuple naming the valid path segments of the URL on which XML-RPC requests are accepted. A request posted to any other path draws a 404 “no such page” HTTP error. Should the tuple be empty, every path counts as valid. Its default value is `('/', '/RPC2')`.

[Subject index](INDEX.md) · [Previous](xmlrpc-server-simplexmlrpcrequesthandler-class.md) · [Continue](xmlrpc-server-example-overview.md) · [Owning module, declaration or section: xmlrpc.server](xmlrpc-server-simplexmlrpcserver-class.md)

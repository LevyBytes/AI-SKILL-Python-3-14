# xmlrpc.client — ServerProxy Objects

### ServerProxy Objects

For every remote procedure call the XML-RPC server accepts, a `ServerProxy` instance exposes a matching method. Invoking that method fires off an RPC, routed by both its name and its argument signature (so one method name can be overloaded across several argument signatures). The RPC wraps up by handing back a value — either data in a conformant type, or a `Fault` or `ProtocolError` object that flags an error.

Servers offering the XML introspection API expose a handful of shared methods gathered beneath the reserved `system` attribute:

 ServerProxy.system.listMethods()

It hands back a list of strings — one entry per (non-system) method the XML-RPC server provides.

 ServerProxy.system.methodSignature(*name*)

You give this method a single parameter: the name of some method the XML-RPC server implements. Back comes an array of the candidate signatures for it. Each signature is itself an array of types, where the leading type is the method's return type and the remainder are its parameters.

Since overloading (that is, multiple signatures) is allowed, the call yields a list of signatures instead of just one.

A signature itself only spans the top-level parameters a method expects. To illustrate: a method that takes a single array of structs and returns a string has the plain signature “string, array”, while one taking three integers and returning a string has “string, int, int, int”.

When the method carries no defined signature, you get back a non-array value — in Python, that means the returned value's type is something other than list.

 ServerProxy.system.methodHelp(*name*)

This one also takes a lone parameter: the name of a method the XML-RPC server implements. It returns a documentation string explaining how to use that method, or an empty string when none exists. That documentation string is allowed to carry HTML markup.

Changed in version 3.5: `ServerProxy` instances now honor the [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) protocol so the transport beneath can be closed.

Below is a working example. First the server code:

```python
from xmlrpc.server import SimpleXMLRPCServer

def is_even(n):
    return n % 2 == 0

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(is_even, "is_even")
server.serve_forever()

```

And the matching client code for that server:

```python
import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    print("3 is even: %s" % str(proxy.is_even(3)))
    print("100 is even: %s" % str(proxy.is_even(100)))

```

[Subject index](INDEX.md) · [Previous](xmlrpc-client-xml-rpc-client-access.md) · [Continue](xmlrpc-client-datetime-class.md) · [Owning module, declaration or section: xmlrpc.client](xmlrpc-client-xml-rpc-client-access.md)

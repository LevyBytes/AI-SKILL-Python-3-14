# xmlrpc.client — MultiCall Objects

### MultiCall Objects

By means of the `MultiCall` object you can bundle several calls bound for a remote server into one request [1].

 *class *xmlrpc.client.MultiCall(*server*)

Build an object for boxcaring method calls. *server* names where the call will ultimately land. You may invoke calls on the result object, yet they return `None` right away, merely recording each call's name and parameters inside the `MultiCall` object. Calling the object itself ships every stored call off as a single `system.multicall` request. That call's result is a [generator](https://docs.python.org/3.14/glossary.html#term-generator), and stepping through it surfaces the individual results.

An example of using this class follows. The server code:

```python
from xmlrpc.server import SimpleXMLRPCServer

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x // y

# A simple server with simple arithmetic functions
server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_multicall_functions()
server.register_function(add, 'add')
server.register_function(subtract, 'subtract')
server.register_function(multiply, 'multiply')
server.register_function(divide, 'divide')
server.serve_forever()

```

The corresponding client code for the server above:

```python
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
multicall = xmlrpc.client.MultiCall(proxy)
multicall.add(7, 3)
multicall.subtract(7, 3)
multicall.multiply(7, 3)
multicall.divide(7, 3)
result = multicall()

print("7+3=%d, 7-3=%d, 7*3=%d, 7//3=%d" % tuple(result))

```

[Subject index](INDEX.md) · [Previous](protocolerror-objects.md) · [Continue](xmlrpc-client-dumps-to-xmlrpc-client-loads.md) · [Owning module, declaration or section: xmlrpc.client](xmlrpc-client-xml-rpc-client-access.md)

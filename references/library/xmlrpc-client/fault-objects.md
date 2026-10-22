# xmlrpc.client: XML-RPC fault codes and messages

faultCode

An int that signals which kind of fault occurred.

 faultString

A string carrying a diagnostic message tied to the fault.

The example that follows deliberately triggers a `Fault` by handing back a complex-type object. The server code:

```python
from xmlrpc.server import SimpleXMLRPCServer

# A marshalling error is going to occur because we're returning a
# complex number
def add(x, y):
    return x+y+0j

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(add, 'add')

server.serve_forever()

```

The client half that pairs with that server:

```python
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
try:
    proxy.add(2, 5)
except xmlrpc.client.Fault as err:
    print("A fault occurred")
    print("Fault code: %d" % err.faultCode)
    print("Fault string: %s" % err.faultString)

```

[Subject index](INDEX.md) · [Previous](xmlrpc-client-fault-class.md) · [Continue](xmlrpc-client-protocolerror-class.md) · [Owning module, declaration or section: xmlrpc.client](xmlrpc-client-xml-rpc-client-access.md) · [Owning module, declaration or section: xmlrpc.client.Fault](xmlrpc-client-fault-class.md) · [Owning module, declaration or section: Fault Objects](xmlrpc-client-fault-class.md)

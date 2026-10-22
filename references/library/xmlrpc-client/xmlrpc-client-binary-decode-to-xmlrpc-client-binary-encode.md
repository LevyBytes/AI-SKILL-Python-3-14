# xmlrpc.client.Binary: Binary XML-RPC value encoding and decoding

data

The binary payload held within the `Binary` instance, handed to you as a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object.

The methods on `Binary` objects, given below, are there primarily so the marshalling/unmarshalling code can use them internally:

 decode(*bytes*)

Take a base64 [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object, decode it, and store the result as the instance's fresh data.

 encode(*out*)

Emit the XML-RPC base 64 encoding of this binary item into the *out* stream object.

Per [**RFC 2045 section 6.8**](https://datatracker.ietf.org/doc/html/rfc2045.html#section-6.8) — the base64 specification that was the de facto standard back when the XML-RPC spec was authored — the encoded output inserts a newline at each 76-character boundary.

By way of [`__eq__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__eq__) and [`__ne__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__ne__) methods it too backs some of Python's built-in operators.

A sample showing the binary objects in action. Here we'll move an image across XMLRPC:

```python
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

def python_logo():
    with open("python_logo.jpg", "rb") as handle:
        return xmlrpc.client.Binary(handle.read())

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(python_logo, 'python_logo')

server.serve_forever()

```

On the client end the image is fetched and written out to a file:

```python
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
with open("fetched_python_logo.jpg", "wb") as handle:
    handle.write(proxy.python_logo().data)

```

[Subject index](INDEX.md) · [Previous](xmlrpc-client-binary-class.md) · [Continue](xmlrpc-client-fault-class.md) · [Owning module, declaration or section: xmlrpc.client](xmlrpc-client-xml-rpc-client-access.md) · [Owning module, declaration or section: xmlrpc.client.Binary](xmlrpc-client-binary-class.md) · [Owning module, declaration or section: Binary Objects](xmlrpc-client-binary-class.md)

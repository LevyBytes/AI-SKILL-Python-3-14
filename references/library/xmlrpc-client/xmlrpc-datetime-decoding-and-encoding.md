# xmlrpc.client.DateTime: DateTime XML-RPC value encoding and decoding

decode(*string*)

Take a string and adopt it as the instance's fresh time value.

 encode(*out*)

Emit the XML-RPC encoding of this `DateTime` item into the *out* stream object.

Through [`rich comparison`](https://docs.python.org/3.14/reference/datamodel.html#object.__lt__) and [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__) methods it likewise backs some of Python's built-in operators.

Below is a working example. First the server code:

```python
import datetime as dt
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

def today():
    today = dt.datetime.today()
    return xmlrpc.client.DateTime(today)

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(today, "today")
server.serve_forever()

```

The client side that talks to the server above:

```python
import xmlrpc.client
import datetime as dt

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

today = proxy.today()
# convert the ISO 8601 string to a datetime object
converted = dt.datetime.strptime(today.value, "%Y%m%dT%H:%M:%S")
print(f"Today: {converted.strftime('%d.%m.%Y, %H:%M')}")

```

[Subject index](INDEX.md) · [Previous](xmlrpc-client-datetime-class.md) · [Continue](xmlrpc-client-binary-class.md) · [Owning module, declaration or section: xmlrpc.client](xmlrpc-client-xml-rpc-client-access.md) · [Owning module, declaration or section: xmlrpc.client.DateTime](xmlrpc-client-datetime-class.md) · [Owning module, declaration or section: DateTime Objects](xmlrpc-client-datetime-class.md)

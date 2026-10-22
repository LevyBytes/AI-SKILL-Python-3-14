# xmlrpc.server — SimpleXMLRPCServer example — Code example: server = ServerProxy("http://localhost:8000")

```python
server = ServerProxy("http://localhost:8000")

try:
    print(server.currentTime.getCurrentTime())
except Error as v:
    print("ERROR", v)

multi = MultiCall(server)
multi.getData()
multi.pow(2,9)
multi.add(1,2)
try:
    for response in multi():
        print(response)
except Error as v:
    print("ERROR", v)

```

You can launch this client, which talks to the demo XMLRPC server, like so:

```python
python -m xmlrpc.client

```

[Subject index](INDEX.md) · [Previous](xmlrpc-server-construction-example.md) · [Continue](cgi-xmlrpc-registration-and-request-handling.md) · [Owning module, declaration or section: xmlrpc.server](xmlrpc-server-simplexmlrpcserver-class.md) · [Owning module, declaration or section: SimpleXMLRPCServer example](xmlrpc-server-example-overview.md)

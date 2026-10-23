# xmlrpc.server - SimpleXMLRPCServer example - Code example: from xmlrpc.server import SimpleXMLRPCServer

```python
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register pow() function; this will use the value of
    # pow.__name__ as the name, which is just 'pow'.
    server.register_function(pow)

    # Register a function under a different name, using
    # register_function as a decorator. *name* can only be given
    # as a keyword argument.
    @server.register_function(name='add')
    def adder_function(x, y):
        return x + y

    # Register a function under function.__name__.
    @server.register_function
    def mul(x, y):
        return x * y

    server.serve_forever()

```

The example below, shipped inside the `Lib/xmlrpc/server.py` module, demonstrates a server that permits dotted names and registers a multicall function.

Warning

Turning on the *allow_dotted_names* option opens the door for intruders to reach your module's global variables and possibly to run arbitrary code on your machine. Confine this example to a secure, closed network.

```python
import datetime as dt

class ExampleService:
    def getData(self):
        return '42'

    class currentTime:
        @staticmethod
        def getCurrentTime():
            return dt.datetime.now()

with SimpleXMLRPCServer(("localhost", 8000)) as server:
    server.register_function(pow)
    server.register_function(lambda x,y: x+y, 'add')
    server.register_instance(ExampleService(), allow_dotted_names=True)
    server.register_multicall_functions()
    print('Serving XML-RPC on localhost port 8000')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
        sys.exit(0)

```

You can launch this ExampleService demo straight from the command line:

```python
python -m xmlrpc.server

```

A client built to talk to the server above ships within `Lib/xmlrpc/client.py`:

[Subject index](INDEX.md) · [Previous](xmlrpc-server-example-overview.md) · [Continue](xmlrpc-client-server-proxy-example.md) · [Owning module, declaration or section: xmlrpc.server](xmlrpc-server-simplexmlrpcserver-class.md) · [Owning module, declaration or section: SimpleXMLRPCServer example](xmlrpc-server-example-overview.md)

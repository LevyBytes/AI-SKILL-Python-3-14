# xmlrpc.client - Example of Client Usage

### Example of Client Usage

```python
# simple test program (from the XML-RPC specification)
from xmlrpc.client import ServerProxy, Error

# server = ServerProxy("http://localhost:8000") # local server
with ServerProxy("http://betty.userland.com") as proxy:

    print(proxy)

    try:
        print(proxy.examples.getStateName(41))
    except Error as v:
        print("ERROR", v)

```

Reaching an XML-RPC server by way of an HTTP proxy calls for a custom transport of your own. Here is how to set one up:

```python
import http.client
import xmlrpc.client

class ProxiedTransport(xmlrpc.client.Transport):

    def set_proxy(self, host, port=None, headers=None):
        self.proxy = host, port
        self.proxy_headers = headers

    def make_connection(self, host):
        connection = http.client.HTTPConnection(*self.proxy)
        connection.set_tunnel(host, headers=self.proxy_headers)
        self._connection = host, connection
        return connection

transport = ProxiedTransport()
transport.set_proxy('proxy-server', 8080)
server = xmlrpc.client.ServerProxy('http://betty.userland.com', transport=transport)
print(server.examples.getStateName(41))

```

[Subject index](INDEX.md) · [Previous](xmlrpc-client-dumps-to-xmlrpc-client-loads.md) · [Continue](example-of-client-and-server-usage.md) · [Owning module, declaration or section: xmlrpc.client](xmlrpc-client-xml-rpc-client-access.md)

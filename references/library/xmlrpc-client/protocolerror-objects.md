# xmlrpc.client: HTTP protocol-error URL, code, message and headers

url

Whichever URI or URL set off the error.

 errcode

The error code.

 errmsg

The diagnostic string or error message.

 headers

A dict holding the headers from the HTTP/HTTPS request that set off the error.

The example below intentionally provokes a `ProtocolError` by handing over an invalid URI:

```python
import xmlrpc.client

# create a ServerProxy with a URI that doesn't respond to XMLRPC requests
proxy = xmlrpc.client.ServerProxy("http://google.com/")

try:
    proxy.some_method()
except xmlrpc.client.ProtocolError as err:
    print("A protocol error occurred")
    print("URL: %s" % err.url)
    print("HTTP/HTTPS headers: %s" % err.headers)
    print("Error code: %d" % err.errcode)
    print("Error message: %s" % err.errmsg)

```

[Subject index](INDEX.md) · [Previous](xmlrpc-client-protocolerror-class.md) · [Continue](xmlrpc-client-multicall-class.md) · [Owning module, declaration or section: xmlrpc.client](xmlrpc-client-xml-rpc-client-access.md) · [Owning module, declaration or section: xmlrpc.client.ProtocolError](xmlrpc-client-protocolerror-class.md) · [Owning module, declaration or section: ProtocolError Objects](xmlrpc-client-protocolerror-class.md)

# Sockets and Layers

### Sockets and Layers

Python's machinery for pulling resources off the web is built in layers. urllib draws on the [`http.client`](https://docs.python.org/3.14/library/http.client.html#module-http.client) library, and that one in turn draws on the socket library.

Beginning with Python 2.3 you're able to dictate how long a socket waits for a response before it gives up. That's handy in applications whose job involves fetching web pages. Left alone, the socket module applies *no timeout* and may stall indefinitely. At the moment neither http.client nor urllib.request surfaces the socket timeout directly, but you can establish the default timeout for every socket at once like so

```python
import socket
import urllib.request

# timeout in seconds
timeout = 10
socket.setdefaulttimeout(timeout)

# this call to urllib.request.urlopen now uses the default timeout
# we have set in the socket module
req = urllib.request.Request('http://www.voidspace.org.uk')
response = urllib.request.urlopen(req)

```

---

[Subject index](INDEX.md) · [Previous source context](proxies.md) · [Following source context](footnotes.md)

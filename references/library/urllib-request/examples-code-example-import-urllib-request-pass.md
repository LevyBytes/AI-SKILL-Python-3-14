# urllib.request - Examples - Code example: import urllib.request

```python
import urllib.request
DATA = b'some data'
req = urllib.request.Request(url='http://localhost:8080', data=DATA, method='PUT')
with urllib.request.urlopen(req) as f:
    pass
print(f.status)
print(f.reason)

```

Use of Basic HTTP Authentication:

```python
import urllib.request
# Create an OpenerDirector with support for Basic HTTP Authentication...
auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm='PDQ Application',
                          uri='https://mahler:8092/site-updates.py',
                          user='klem',
                          passwd='kadidd!ehopper')
opener = urllib.request.build_opener(auth_handler)
# ...and install it globally so it can be used with urlopen.
urllib.request.install_opener(opener)
with urllib.request.urlopen('http://www.example.com/login.html') as f:
    print(f.read().decode('utf-8'))

```

Out of the box, `build_opener()` supplies a great many handlers, the `ProxyHandler` among them. Out of the box, `ProxyHandler` draws on the environment variables named `<scheme>_proxy`, where `<scheme>` is the URL scheme in play. As an example, the `http_proxy` environment variable is consulted to get the URL of the HTTP proxy.

The example here swaps the default `ProxyHandler` for one that draws on proxy URLs supplied programmatically, and brings in proxy authorization support by way of `ProxyBasicAuthHandler`.

```python
proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')

opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
# This time, rather than install the OpenerDirector, we use it directly:
with opener.open('http://www.example.com/login.html') as f:
   print(f.read().decode('utf-8'))

```

Adding HTTP headers:

Use the *headers* argument to the `Request` constructor, or:

```python
import urllib.request
req = urllib.request.Request('http://www.example.com/')
req.add_header('Referer', 'https://www.python.org/')
# Customize the default User-Agent header value:
req.add_header('User-Agent', 'urllib-example/0.1 (Contact: . . .)')
with urllib.request.urlopen(req) as f:
    print(f.read().decode('utf-8'))

```

To each `Request`, `OpenerDirector` adds a *User-Agent* header on its own. To override this:

```python
import urllib.request
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
with opener.open('http://www.example.com/') as f:
   print(f.read().decode('utf-8'))

```

Keep in mind, too, that a handful of standard headers (*Content-Length*, *Content-Type* and *Host*) get added once the `Request` reaches `urlopen()` (or `OpenerDirector.open()`).

The example session below applies the `GET` method to fetch a URL that carries parameters:

[Subject index](INDEX.md) · [Previous](examples-section-introduction-and-initial-examples.md) · [Continue](url-request-post-example.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md) · [Owning module, declaration or section: Examples](examples-section-introduction-and-initial-examples.md)

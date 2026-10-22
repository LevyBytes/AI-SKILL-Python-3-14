# Proxies

### Proxies

**urllib** detects your proxy configuration on its own and applies it, courtesy of the `ProxyHandler` that joins the ordinary handler chain once a proxy setting turns up. That's usually welcome, though now and then it works against you [5]. One remedy is to stand up a `ProxyHandler` of our own with no proxies declared at all, following much the same steps used to set up a Basic Authentication handler:

```python
>>> proxy_support = urllib.request.ProxyHandler({})
>>> opener = urllib.request.build_opener(proxy_support)
>>> urllib.request.install_opener(opener)

```

Note

As things stand, `urllib.request` offers *no* support for retrieving `https` locations by way of a proxy. You can switch that capability on, however, by extending urllib.request along the lines of the recipe [6].

Note

Whenever a `REQUEST_METHOD` variable is present, `HTTP_PROXY` gets disregarded; consult the documentation for [`getproxies()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.getproxies).

[Subject index](INDEX.md) · [Previous source context](basic-authentication.md) · [Following source context](sockets-and-layers.md)

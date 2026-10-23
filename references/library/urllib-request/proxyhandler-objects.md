# urllib.request - ProxyHandler Objects

### ProxyHandler Objects

 ProxyHandler.&lt;protocol&gt;_open(request)

For each *protocol* that has a proxy listed in the *proxies* dictionary passed to the constructor, the `ProxyHandler` carries a matching `<protocol>_open()` method. That method rewrites requests so they pass through the proxy, by invoking `request.set_proxy()`, and then hands off to the next handler in the chain to actually carry out the protocol.

[Subject index](INDEX.md) · [Previous](httpcookieprocessor-cookiejar.md) · [Continue](http-password-registration-and-lookup.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md)

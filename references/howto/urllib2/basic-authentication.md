# Basic Authentication

### Basic Authentication

As a demonstration of building and installing a handler, we'll turn to the `HTTPBasicAuthHandler`. If you'd like a fuller treatment of the topic — including how Basic Authentication actually operates — have a look at the [Basic Authentication Tutorial](https://web.archive.org/web/20201215133350/http://www.voidspace.org.uk/python/articles/authentication.shtml).

Whenever credentials are needed, the server returns a header (alongside the 401 error code) asking for authentication. That header names both the authentication scheme and a ‘realm’, and takes the shape: `WWW-Authenticate: SCHEME realm="REALM"`.

e.g.

```none
WWW-Authenticate: Basic realm="cPanel Users"

```

At that point the client ought to send the request again, this time embedding the matching name and password for the realm as a header. That exchange is ‘basic authentication’. To make the whole thing easier, we can spin up an `HTTPBasicAuthHandler` instance plus an opener that uses it.

Behind the scenes `HTTPBasicAuthHandler` leans on something called a password manager to map URLs and realms onto usernames and passwords. When you already know the realm (taken from the authentication header the server sent), a `HTTPPasswordMgr` will do. More often than not the realm isn't something you care about, and for that case `HTTPPasswordMgrWithDefaultRealm` is the convenient pick: it lets you register a default username and password against a URL, to be used whenever you haven't supplied a different pairing for some specific realm. You signal this by passing `None` as the realm argument to the `add_password` method.

By the top-level URL we mean the very first URL along the path that demands authentication. Any URL sitting “deeper” than the one you hand to .add_password() will match as well.

```python
# create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password.
# If we knew the realm, we could use it instead of None.
top_level_url = "http://example.com/foo/"
password_mgr.add_password(None, top_level_url, username, password)

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)

# use the opener to fetch a URL
opener.open(a_url)

# Install the opener.
# Now all calls to urllib.request.urlopen use our opener.
urllib.request.install_opener(opener)

```

Note

The example just above handed only our `HTTPBasicAuthHandler` to `build_opener`. Openers come pre-loaded with the handlers meant for ordinary cases – `ProxyHandler` (provided a proxy setting like an `http_proxy` environment variable exists), `UnknownHandler`, `HTTPHandler`, `HTTPDefaultErrorHandler`, `HTTPRedirectHandler`, `FTPHandler`, `FileHandler`, `DataHandler`, `HTTPErrorProcessor`.

What `top_level_url` actually accepts is *either* a complete URL (carrying the ‘http:’ scheme part, the hostname, and possibly the port number) such as `"http://example.com/"`, *or* an “authority” (that is, the hostname, optionally with the port number) such as `"example.com"` or `"example.com:8080"` (this last one shows a port number). When an authority is given, it must NOT carry the “userinfo” piece — `"joe:password@example.com"`, for instance, is wrong.

[Subject index](INDEX.md) · [Previous source context](openers-and-handlers.md) · [Following source context](proxies.md)

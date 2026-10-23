# http.cookiejar - CookiePolicy Objects

### CookiePolicy Objects

Objects that implement the `CookiePolicy` interface provide these methods:

 CookiePolicy.set_ok(*cookie*, *request*)

Return a boolean signalling whether the cookie ought to be accepted from the server.

*cookie* is a `Cookie` instance. *request* is an object that implements the interface laid out by the documentation for `CookieJar.extract_cookies()`.

 CookiePolicy.return_ok(*cookie*, *request*)

Return a boolean signalling whether the cookie ought to be sent back to the server.

*cookie* is a `Cookie` instance. *request* is an object that implements the interface laid out by the documentation for `CookieJar.add_cookie_header()`.

 CookiePolicy.domain_return_ok(*domain*, *request*)

Given the cookie domain, return `False` when the cookies ought not to be sent back.

This method exists as an optimization. It does away with the need to inspect every cookie under a given domain (something that could mean reading numerous files). When `domain_return_ok()` and `path_return_ok()` both return true, all the remaining work falls to `return_ok()`.

When `domain_return_ok()` returns true for the cookie domain, `path_return_ok()` runs next for the cookie path. If it doesn't, then `path_return_ok()` and `return_ok()` are never invoked for that cookie domain. When `path_return_ok()` returns true, `return_ok()` runs with the `Cookie` object itself for a complete check. If it doesn't, `return_ok()` is never invoked for that cookie path.

Be aware that `domain_return_ok()` runs for every *cookie* domain, not solely for the *request* domain. For instance, the function could be invoked with both `".example.com"` and `"www.example.com"` when the request domain is `"www.example.com"`. The same is true of `path_return_ok()`.

The *request* argument is as documented for `return_ok()`.

 CookiePolicy.path_return_ok(*path*, *request*)

Given the cookie path, return `False` when the cookies ought not to be sent back.

Refer to the documentation covering `domain_return_ok()`.

On top of providing the methods above, anything implementing the `CookiePolicy` interface must also expose the following attributes, which signal which protocols are to be used and in what way. Every one of these attributes may be assigned to.

 CookiePolicy.netscape

Implement Netscape protocol.

 CookiePolicy.rfc2965

Implement [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) protocol.

 CookiePolicy.hide_cookie2

Refrain from adding a *Cookie2* header to requests (that header, when present, tells the server we understand [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) cookies).

The handiest approach for defining a `CookiePolicy` class is to subclass `DefaultCookiePolicy` and override some or every one of the methods above. On its own, `CookiePolicy` can serve as a "null policy" that permits setting and receiving any and every cookie (which is unlikely to be of much use).

[Subject index](INDEX.md) · [Previous](http-cookiejar-lwpcookiejar-class.md) · [Continue](cookie-domain-blocklists-and-name-restrictions.md) · [Owning module, declaration or section: http.cookiejar](http-cookiejar-loaderror.md)

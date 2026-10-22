# http.cookiejar: Cookie attributes, scope and expiration inspection

`Cookie.version`

Either an integer or [`None`](https://docs.python.org/3.14/library/constants.html#None). For Netscape cookies `version` is 0. Cookies of the [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) and [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) kind carry a `version` cookie-attribute equal to 1. Be aware, though, that `http.cookiejar` is allowed to 'downgrade' RFC 2109 cookies into Netscape cookies, and then `version` becomes 0.

`Cookie.name`

The cookie's name (a string).

`Cookie.value`

The cookie's value (a string), or else [`None`](https://docs.python.org/3.14/library/constants.html#None).

`Cookie.port`

A string giving a single port or several ports (for example '80', or '80,8080'), or [`None`](https://docs.python.org/3.14/library/constants.html#None).

`Cookie.domain`

The cookie's domain (a string).

`Cookie.path`

The cookie's path (a string, for example `'/acme/rocket_launchers'`).

`Cookie.secure`

`True` when the cookie ought to travel only across a secure connection.

`Cookie.expires`

The expiry date as an integer number of seconds since the epoch, or [`None`](https://docs.python.org/3.14/library/constants.html#None). Refer as well to the `is_expired()` method.

`Cookie.discard`

`True` when this happens to be a session cookie.

`Cookie.comment`

A string comment provided by the server that describes what this cookie is for, or [`None`](https://docs.python.org/3.14/library/constants.html#None).

`Cookie.comment_url`

A URL pointing to a server-side comment that describes what this cookie is for, or [`None`](https://docs.python.org/3.14/library/constants.html#None).

`Cookie.rfc2109`

`True` when this cookie came in as an [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) cookie (that is, it showed up in a *Set-Cookie* header whose Version cookie-attribute held the value 1). The attribute exists because `http.cookiejar` is allowed to 'downgrade' RFC 2109 cookies into Netscape cookies, after which `version` is 0.

`Cookie.port_specified`

`True` when the server named a port, or a collection of ports, outright (within the *Set-Cookie* / *Set-Cookie2* header).

`Cookie.domain_specified`

`True` when the server named a domain outright.

`Cookie.domain_initial_dot`

`True` when the domain the server gave explicitly opened with a dot (`'.'`).

Cookies can also carry extra non-standard cookie-attributes, reachable through the methods below:

`Cookie.has_nonstandard_attr(*name*)`

Yield `True` when the cookie carries the named cookie-attribute.

`Cookie.get_nonstandard_attr(*name*, *default=None*)`

When the cookie carries the named cookie-attribute, give back its value; failing that, give back *default*.

`Cookie.set_nonstandard_attr(*name*, *value*)`

Assign the value of the named cookie-attribute.

One further method is defined on the `Cookie` class:

`Cookie.is_expired(*now=None*)`

`True` when the cookie is now past the expiry moment the server asked for. Should *now* be supplied (as seconds since the epoch), the result tells you whether the cookie had already expired at that given time.

[Subject index](INDEX.md) · [Continue](examples.md) · [Owning module, declaration or section: http.cookiejar](http-cookiejar-loaderror.md) · [Owning module, declaration or section: Cookie Objects](cookie-objects.md)

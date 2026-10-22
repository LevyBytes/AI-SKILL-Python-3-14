# http.cookiejar: `http.cookiejar.Cookie`

*class *http.cookiejar.Cookie

Netscape, [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) and [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) cookies are all represented by this class. Users of `http.cookiejar` aren't expected to build their own `Cookie` instances. Instead, when you need them, invoke `make_cookies()` on a `CookieJar` instance.

See also

Module [`urllib.request`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.request)

Opening URLs while cookies are handled for you automatically.

Module [`http.cookies`](https://docs.python.org/3.14/library/http.cookies.html#module-http.cookies)

Classes for HTTP cookies, mostly handy on the server side. There is no dependency between the `http.cookiejar` and [`http.cookies`](https://docs.python.org/3.14/library/http.cookies.html#module-http.cookies) modules in either direction.

[https://curl.se/rfc/cookie_spec.html](https://curl.se/rfc/cookie_spec.html)

The specification for the original Netscape cookie protocol. Even though it remains the prevailing protocol, the "Netscape cookie protocol" that every major browser (and `http.cookiejar`) implements has only a faint resemblance to the one outlined in `cookie_spec.html`.

[**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) - HTTP State Management Mechanism

Made obsolete by [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html). Relies on *Set-Cookie* carrying version=1.

[**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) - HTTP State Management Mechanism

Essentially the Netscape protocol once its bugs were corrected. Swaps in *Set-Cookie2* for *Set-Cookie*. Sees little use.

[https://kristol.org/cookie/errata.html](https://kristol.org/cookie/errata.html)

Unfinished errata to [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html).

[**RFC 2964**](https://datatracker.ietf.org/doc/html/rfc2964.html) - Use of HTTP State Management

[Subject index](INDEX.md) · [Previous](http-cookiejar-defaultcookiepolicy-class.md) · [Continue](cookiejar-add-cookie-header-to-filecookiejar-save.md) · [Owning module, declaration or section: http.cookiejar](http-cookiejar-loaderror.md)

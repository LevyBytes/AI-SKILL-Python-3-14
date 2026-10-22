# http.cookies: `http.cookies.SimpleCookie`

*class *http.cookies.SimpleCookie([*input*])

Extending `BaseCookie`, this class replaces `value_decode()` and `value_encode()` with its own versions. `SimpleCookie` treats cookie values as strings. While assigning a value, `SimpleCookie` invokes the builtin [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) so that the value becomes a string. Anything arriving over HTTP stays as a string.

See also

Module [`http.cookiejar`](https://docs.python.org/3.14/library/http.cookiejar.html#module-http.cookiejar)

Manages HTTP cookies for web *clients*. Neither the [`http.cookiejar`](https://docs.python.org/3.14/library/http.cookiejar.html#module-http.cookiejar) module nor `http.cookies` relies on the other.

[**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) - HTTP State Management Mechanism

That document is the state-management spec that this module realizes.

[Subject index](INDEX.md) · [Previous](http-cookies-basecookie-class.md) · [Continue](basecookie-value-decode-to-basecookie-load.md) · [Owning module, declaration or section: http.cookies](http-cookies-cookieerror.md)

# Python 3.14.5 release candidate 1 / security / http cookies

[gh-90309](https://github.com/python/cpython/issues/90309): When cookies are written into JavaScript via the [`http.cookies.BaseCookie.js_output()`](https://docs.python.org/3.14/library/http.cookies.html#http.cookies.BaseCookie.js_output) method, Base64-encode the values so injection and escaping problems are avoided.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

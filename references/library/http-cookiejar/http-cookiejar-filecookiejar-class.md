# http.cookiejar: `http.cookiejar.FileCookieJar`

*class *http.cookiejar.FileCookieJar(*filename=None*, *delayload=None*, *policy=None*)

*policy* is an object implementing the `CookiePolicy` interface. Regarding the remaining arguments, consult the documentation covering the matching attributes.

A `CookieJar` capable of loading cookies from, and possibly writing cookies to, a file stored on disk. Cookies are **NOT** read from the named file until you call either the `load()` or `revert()` method. The subclasses of this class are described in section FileCookieJar subclasses and co-operation with web browsers.

Rather than instantiating this directly, reach for one of its subclasses listed below.

Changed in version 3.8: The filename parameter supports a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

[Subject index](INDEX.md) · [Previous](http-cookiejar-cookiejar-class.md) · [Continue](http-cookiejar-cookiepolicy-class.md) · [Owning module, declaration or section: http.cookiejar](http-cookiejar-loaderror.md)

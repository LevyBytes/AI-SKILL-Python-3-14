# http.cookiejar: `http.cookiejar.CookieJar`

*class *http.cookiejar.CookieJar(*policy=None*)

*policy* is an object implementing the `CookiePolicy` interface.

Cookies for HTTP are held by the `CookieJar` class. It pulls cookies out of HTTP requests and hands them back in HTTP responses. Contained cookies are expired automatically by `CookieJar` instances whenever that is required. Storing and fetching cookies from a file or database is left to subclasses.

[Subject index](INDEX.md) · [Previous](http-cookiejar-loaderror.md) · [Continue](http-cookiejar-filecookiejar-class.md) · [Owning module, declaration or section: http.cookiejar](http-cookiejar-loaderror.md)

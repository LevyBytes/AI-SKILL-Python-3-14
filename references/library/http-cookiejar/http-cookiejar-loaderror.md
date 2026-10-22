# http.cookiejar: `http.cookiejar.LoadError`

### `http.cookiejar` — Cookie handling for HTTP clients

**Source code:** [Lib/http/cookiejar.py](https://github.com/python/cpython/tree/3.14/Lib/http/cookiejar.py)

---

Classes for managing HTTP cookies automatically are defined by the `http.cookiejar` module. It comes in handy when you reach websites that expect tiny chunks of data — *cookies* — to be deposited on the client machine by an HTTP response coming from a web server, and afterward sent back to that server during subsequent HTTP requests.

Two protocols are supported: the standard Netscape cookie protocol along with the protocol laid out in [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html). Handling for RFC 2965 is disabled by default. Cookies following [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) are parsed in the Netscape style and then treated afterward as either Netscape or RFC 2965 cookies depending on whichever "policy" is currently in force. Keep in mind that almost all cookies found across the internet are Netscape cookies. The `http.cookiejar` module aims to mirror the de-facto Netscape cookie protocol (which is quite different from what the original Netscape specification described), and this includes honoring the `max-age` and `port` cookie-attributes that RFC 2965 brought in.

Note

The assorted named parameters that appear within *Set-Cookie* and *Set-Cookie2* headers (eg. `domain` and `expires`) are by convention called *attributes*. So that they aren't confused with Python attributes, this module's documentation adopts the term *cookie-attribute* in their place.

This exception is defined by the module:

 *exception *http.cookiejar.LoadError

When `FileCookieJar` instances cannot load cookies out of a file, they raise this exception. `LoadError` is a subclass of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

Changed in version 3.3: in earlier releases `LoadError` was a subtype of [`IOError`](https://docs.python.org/3.14/library/exceptions.html#IOError); that name now serves as an alias of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

These classes are made available:

[Subject index](INDEX.md) · [Continue](http-cookiejar-cookiejar-class.md)

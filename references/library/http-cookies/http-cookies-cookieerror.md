# http.cookies: `http.cookies.CookieError`

# Http.Cookies, Http

## Overview

Covers: http.cookies — HTTP state management; http — HTTP modules.

## http.cookies — HTTP state management

### `http.cookies` — HTTP state management

**Source code:** [Lib/http/cookies.py](https://github.com/python/cpython/tree/3.14/Lib/http/cookies.py)

---

Within `http.cookies` you'll find classes that model cookies at an abstract level — cookies being the HTTP state management mechanism. Beyond plain string-only cookies, the module also lets any serializable data-type stand in as a cookie's value.

Earlier releases of this code enforced, to the letter, the parsing rules laid out in the [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) and [**RFC 2068**](https://datatracker.ietf.org/doc/html/rfc2068.html) specifications. Over time, though, people realized that MSIE 3.0x ignored the character conventions those documents prescribed; plenty of modern browsers and servers have likewise loosened their treatment of cookies during parsing. Consequently, the parsing performed here today is somewhat more lenient than its original behavior.

Across [`string.ascii_letters`](https://docs.python.org/3.14/library/string.html#string.ascii_letters), [`string.digits`](https://docs.python.org/3.14/library/string.html#string.digits) and `!#$%&'*+-.^_`|~:` denote the set of valid characters allowed by this module in a cookie name (as `key`).

Changed in version 3.3: Allowed ‘:’ as a valid cookie name character.

Note

Whenever an invalid cookie turns up, the code raises `CookieError`; because cookies arriving from a browser may be malformed, always be ready to handle bad input and trap `CookieError` while parsing.

 *exception *http.cookies.CookieError

The exception signaling a violation of [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) — for instance a bad attribute, a malformed *Set-Cookie* header, and so on.

[Subject index](INDEX.md) · [Continue](http-cookies-basecookie-class.md)

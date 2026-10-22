# What's New In Python 3.10 / urllib.parse — urllib.parse

### urllib.parse

Releases of Python before Python 3.10 permitted both `;` and `&` to act as query parameter separators inside [`urllib.parse.parse_qs()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.parse_qs) and [`urllib.parse.parse_qsl()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.parse_qsl). For security reasons, and to align with the newer W3C recommendations, only one separator key is now permitted, defaulting to `&`. Because they call the affected functions under the hood, `cgi.parse()` and `cgi.parse_multipart()` are affected by this change as well. Their respective documentation covers the finer points. (Contributed by Adam Goldschmidt, Senthil Kumaran and Ken Jin in [bpo-42967](https://bugs.python.org/issue?@action=redirect&bpo=42967).)

Some attack forms become possible when newline or tab characters appear within parts of a URL. In keeping with the WHATWG specification that revises [**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html), the parser in [`urllib.parse`](https://docs.python.org/3.14/library/urllib.parse.html#module-urllib.parse) now strips ASCII newline `\n`, `\r` and tab `\t` characters out of the URL, heading off such attacks. Which characters get removed is governed by a fresh module level variable `urllib.parse._UNSAFE_URL_BYTES_TO_REMOVE`. (See [gh-88048](https://github.com/python/cpython/issues/88048))

[Subject index](INDEX.md) · [Previous source section](unittest.md) · [Next source section](xml.md) · [Release/subject declaration](summary-release-highlights.md)

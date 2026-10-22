# What's New In Python 3.9 / urllib.parse — urllib.parse

### urllib.parse

In older Python releases you could use either `;` or `&` to separate query parameters within [`urllib.parse.parse_qs()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.parse_qs) and [`urllib.parse.parse_qsl()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.parse_qsl). On security grounds, and to fall in line with newer W3C recommendations, that has been narrowed to a lone separator key, with `&` serving as the default. The shift touches `cgi.parse()` and `cgi.parse_multipart()` too, since they lean on the affected functions under the hood. Their respective documentation has the finer points. (Contributed by Adam Goldschmidt, Senthil Kumaran and Ken Jin in [bpo-42967](https://bugs.python.org/issue?@action=redirect&bpo=42967).)

### Notable changes in Python 3.9.5

### urllib.parse

When newline or tab characters show up inside portions of a URL, they open the door to certain attacks. In keeping with the WHATWG specification that revises [**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html), the parser in [`urllib.parse`](https://docs.python.org/3.14/library/urllib.parse.html#module-urllib.parse) now strips the ASCII newline `\n`, `\r` and tab `\t` characters out of the URL, shutting such attacks down. A new module-level variable, `urllib.parse._UNSAFE_URL_BYTES_TO_REMOVE`, governs which characters get removed. (See [gh-88048](https://github.com/python/cpython/issues/88048))

[Subject index](INDEX.md) · [Previous source section](collections-abc.md) · [Next source section](notable-changes-in-python-3-9-3.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](notable-changes-in-python-3-9-3.md) · [Next source section](notable-security-feature-in-3-9-14.md)

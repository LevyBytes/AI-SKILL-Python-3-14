# What's New In Python 3.6 / Notable changes in Python 3.6.13 — urllib.parse

### Notable changes in Python 3.6.13

In bygone Python releases you could employ either `;` or `&` to separate query parameters within [`urllib.parse.parse_qs()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.parse_qs) and [`urllib.parse.parse_qsl()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.parse_qsl). For security reasons, and to fall in line with the latest W3C guidance, that has been narrowed so only one separator key is permitted, defaulting to `&`. The shift carries over to `cgi.parse()` and `cgi.parse_multipart()` too, since they call the impacted functions behind the scenes. Further specifics live in each one's own documentation. (Contributed by Adam Goldschmidt, Senthil Kumaran and Ken Jin in [bpo-42967](https://bugs.python.org/issue?@action=redirect&bpo=42967).)

[Subject index](INDEX.md) · [Previous source section](notable-changes-in-python-3-6-10.md) · [Next source section](notable-changes-in-python-3-6-14.md) · [Release/subject declaration](summary-release-highlights.md)

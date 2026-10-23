# What’s New In Python 3.8 / Notable changes in Python 3.8.8 - urllib.parse

### Notable changes in Python 3.8.8

In releases before this, both `;` and `&` were accepted as separators for query parameters within [`urllib.parse.parse_qs()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.parse_qs) along with [`urllib.parse.parse_qsl()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.parse_qsl). For the sake of security and to line up with the latest W3C guidance, the behavior was tightened to permit just one separator key, defaulting to `&`. Because `cgi.parse()` and `cgi.parse_multipart()` lean on those functions under the hood, they feel this shift as well. Consult each one's own documentation for the finer points. (The work here came from Adam Goldschmidt, Senthil Kumaran and Ken Jin under [bpo-42967](https://bugs.python.org/issue?@action=redirect&bpo=42967).)

[Subject index](INDEX.md) · [Previous source section](notable-changes-in-python-3-8-3.md) · [Next source section](notable-changes-in-python-3-8-9.md) · [Release/subject declaration](assignment-expressions.md)

# What's New In Python 3.7 / Notable changes in Python 3.7.10 — urllib.parse

### Notable changes in Python 3.7.10

Earlier Python releases let you use either `;` or `&` as a separator between query parameters inside [`urllib.parse.parse_qs()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.parse_qs) and [`urllib.parse.parse_qsl()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.parse_qsl). Owing to security worries, and to line up with newer W3C recommendations, this was narrowed to permit only a single separator key, defaulting to `&`. This shift further touches `cgi.parse()` and `cgi.parse_multipart()` since those call the affected functions under the hood. For fuller detail, please consult their individual documentation. Adam Goldschmidt, Senthil Kumaran and Ken Jin delivered this — see [bpo-42967](https://bugs.python.org/issue?@action=redirect&bpo=42967).

[Subject index](INDEX.md) · [Previous source section](notable-changes-in-python-3-7-6.md) · [Next source section](notable-changes-in-python-3-7-11.md) · [Release/subject declaration](summary-release-highlights.md)

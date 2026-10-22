# Python 3.10.0 alpha 1 / library / html parser

[bpo-31844](https://bugs.python.org/issue?@action=redirect&bpo=31844): Drop the `ParserBase.error()` method out of the private, undocumented `_markupbase` module. The single subclass of `ParserBase` is [`html.parser.HTMLParser`](https://docs.python.org/3.14/library/html.parser.html#html.parser.HTMLParser), and that class's `error()` implementation was deprecated in Python 3.4 before being removed in Python 3.5.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

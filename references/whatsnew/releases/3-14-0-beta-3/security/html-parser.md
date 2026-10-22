# Python 3.14.0 beta 3 / security / html parser

[gh-135462](https://github.com/python/cpython/issues/135462): Quadratic complexity when handling specially crafted input within [`html.parser.HTMLParser`](https://docs.python.org/3.14/library/html.parser.html#html.parser.HTMLParser) was fixed. End-of-file errors now follow the HTML5 specs – comments and declarations close automatically, while tags are ignored.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.14.0 release candidate 1 / security / html parser

[gh-135661](https://github.com/python/cpython/issues/135661): Correct, per the HTML5 standard, how [`html.parser.HTMLParser`](https://docs.python.org/3.14/library/html.parser.html#html.parser.HTMLParser) parses attributes that have whitespace surrounding the `=` separator.

[gh-118350](https://github.com/python/cpython/issues/118350): Add proper handling for escapable raw text mode (the elements “textarea” and “title”) within [`html.parser.HTMLParser`](https://docs.python.org/3.14/library/html.parser.html#html.parser.HTMLParser).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

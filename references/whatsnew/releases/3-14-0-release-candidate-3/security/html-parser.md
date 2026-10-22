# Python 3.14.0 release candidate 3 / security / html parser

[gh-135661](https://github.com/python/cpython/issues/135661): Correct CDATA section parsing within [`html.parser.HTMLParser`](https://docs.python.org/3.14/library/html.parser.html#html.parser.HTMLParser) to follow the HTML5 standard: the sequences `] ]>` and `]] >` will no longer terminate a CDATA section. A private `_set_support_cdata()` method is introduced for choosing how `<[CDATA[` is interpreted — either as a CDATA section inside foreign content (SVG or MathML) or as a bogus comment within the HTML namespace.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

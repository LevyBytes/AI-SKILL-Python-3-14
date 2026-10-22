# Python 3.14.0 beta 2 / library / html parser

[gh-77057](https://github.com/python/cpython/issues/77057): Repair the treatment of invalid markup declarations inside [`html.parser.HTMLParser`](https://docs.python.org/3.14/library/html.parser.html#html.parser.HTMLParser).

[gh-86155](https://github.com/python/cpython/issues/86155): [`html.parser.HTMLParser.close()`](https://docs.python.org/3.14/library/html.parser.html#html.parser.HTMLParser.close) no longer drops data when the `<script>` tag stays unclosed. Patch by Waylan Limberg.

[gh-69426](https://github.com/python/cpython/issues/69426): Repair [`html.parser.HTMLParser`](https://docs.python.org/3.14/library/html.parser.html#html.parser.HTMLParser) so character entities in attribute values stay escaped when an ASCII alphanumeric or an equals sign comes right after them.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

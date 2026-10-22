# Python 3.14.4 final / library / pyexpat

[gh-144984](https://github.com/python/cpython/issues/144984): Corrects a crash within [`xml.parsers.expat.xmlparser.ExternalEntityParserCreate()`](https://docs.python.org/3.14/library/pyexpat.html#xml.parsers.expat.xmlparser.ExternalEntityParserCreate) when an allocation fails. Those error paths might dereference NULL `handlers` along with double-decrementing the parent parser's reference count.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

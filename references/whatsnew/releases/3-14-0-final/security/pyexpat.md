# Python 3.14.0 final / security / pyexpat

[gh-139400](https://github.com/python/cpython/issues/139400): [`xml.parsers.expat`](https://docs.python.org/3.14/library/pyexpat.html#module-xml.parsers.expat): Guarantee that a parent Expat parser becomes eligible for garbage collection only after no subparser produced via [`ExternalEntityParserCreate()`](https://docs.python.org/3.14/library/pyexpat.html#xml.parsers.expat.xmlparser.ExternalEntityParserCreate) still holds a reference to it. Sebastian Pipping authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

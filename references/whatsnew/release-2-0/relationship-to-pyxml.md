# What’s New in Python 2.0 / Relationship to PyXML - xml

### Relationship to PyXML

For some time now, the XML Special Interest Group has been developing Python code dealing with XML. You can grab its code release, named PyXML, from the SIG’s web pages at [https://www.python.org/community/sigs/current/xml-sig](https://www.python.org/community/sigs/current/xml-sig). That PyXML release likewise adopted the package name `xml`. Anyone who has built programs on top of PyXML is likely curious about how it lines up with the 2.0 [`xml`](https://docs.python.org/3.14/library/xml.html#module-xml) package.

In short, the [`xml`](https://docs.python.org/3.14/library/xml.html#module-xml) package bundled with Python 2.0 does not line up with PyXML on its own, yet installing a current PyXML release brings the two into alignment. Plenty of programs do fine with the XML facilities that ship inside Python 2.0, but the more involved ones will need the complete PyXML package set up. Once present, PyXML at version 0.6.0 or newer swaps out the `xml` package that comes with Python, acting as a strict superset of the standard one and tacking on a range of extra capabilities. A few of those extras in PyXML are:

- 4DOM: a complete DOM implementation contributed by FourThought, Inc.

- The validating xmlproc parser, authored by Lars Marius Garshol.

- The `sgmlop` module that speeds up parsing, authored by Fredrik Lundh.

[Subject index](INDEX.md) · [Previous source section](dom-support.md) · [Next source section](module-changes.md) · [Release/subject declaration](introduction.md)

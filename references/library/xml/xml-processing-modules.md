# XML Processing Modules

# Xml, Xml.Sax.Handler

## Overview

Covers: XML Processing Modules??; xml.sax.handler — Base classes for SAX handlers??.

## XML Processing Modules??

### XML Processing Modules

**Source code:** [Lib/xml/](https://github.com/python/cpython/tree/3.14/Lib/xml/)

---

The XML-processing interfaces that Python exposes are collected under the `xml` package.

Note

When the data you intend to parse is untrusted or unauthenticated, consult XML security.

Keep in mind that the modules inside the `xml` package depend on having at least one SAX-compliant XML parser present. Because the Expat parser ships with Python, the [`xml.parsers.expat`](https://docs.python.org/3.14/library/pyexpat.html#module-xml.parsers.expat) module is guaranteed to be present.

The reference for the [`xml.dom`](https://docs.python.org/3.14/library/xml.dom.html#module-xml.dom) and [`xml.sax`](https://docs.python.org/3.14/library/xml.sax.html#module-xml.sax) packages constitutes the definition of Python's bindings for the DOM and SAX interfaces.

These are the XML handling submodules:

- [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree): the ElementTree API, a simple and lightweight XML processor

- [`xml.dom`](https://docs.python.org/3.14/library/xml.dom.html#module-xml.dom): the DOM API definition

- [`xml.dom.minidom`](https://docs.python.org/3.14/library/xml.dom.minidom.html#module-xml.dom.minidom): a minimal DOM implementation

- [`xml.dom.pulldom`](https://docs.python.org/3.14/library/xml.dom.pulldom.html#module-xml.dom.pulldom): support for building partial DOM trees

- [`xml.sax`](https://docs.python.org/3.14/library/xml.sax.html#module-xml.sax): SAX2 base classes and convenience functions

- [`xml.parsers.expat`](https://docs.python.org/3.14/library/pyexpat.html#module-xml.parsers.expat): the Expat parser binding

[Subject index](INDEX.md) · [Continue](xml-security.md)

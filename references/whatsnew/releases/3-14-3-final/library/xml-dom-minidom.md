# Python 3.14.3 final / library / xml dom minidom

[gh-142754](https://github.com/python/cpython/issues/142754): The *ownerDocument* attribute is now present on [`xml.dom.minidom`](https://docs.python.org/3.14/library/xml.dom.minidom.html#module-xml.dom.minidom) elements and attributes built by directly instantiating the `Element` or `Attr` class. Bear in mind this method of node creation is unsupported; creator functions such as [`xml.dom.Document.documentElement()`](https://docs.python.org/3.14/library/xml.dom.html#xml.dom.Document.documentElement) ought to be used instead.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.14.0 alpha 1 / library / xml etree elementtree

[gh-123213](https://github.com/python/cpython/issues/123213): When a faulty generator is supplied, [`xml.etree.ElementTree.Element.extend()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.extend) plus [`Element`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element) assignment will no longer swallow the underlying exception. Patch by Bar Harel.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

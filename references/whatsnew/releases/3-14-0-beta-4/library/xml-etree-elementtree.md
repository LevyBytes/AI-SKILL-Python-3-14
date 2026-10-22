# Python 3.14.0 beta 4 / library / xml etree elementtree

[gh-135640](https://github.com/python/cpython/issues/135640): A bug was addressed wherein [`xml.etree.ElementTree.ElementTree.write()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree.write) could be invoked on an ElementTree object whose root element was invalid. That behavior would blank out the file handed to `write` if it already existed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

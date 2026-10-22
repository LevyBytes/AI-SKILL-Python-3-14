# Python 3.12.0 alpha 1 / library / xml etree elementtree

[gh-91810](https://github.com/python/cpython/issues/91810): The [`ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree) [`write()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree.write) method and the [`tostring()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.tostring) function will now draw the XML declaration's encoding from the text file (defaulting to “UTF-8” where none is available) instead of from the locale encoding, whenever `encoding="unicode"` is requested.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

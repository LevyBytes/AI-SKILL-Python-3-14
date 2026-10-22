# Python 3.14.6 final / library / xml etree elementtree

[gh-149571](https://github.com/python/cpython/issues/149571): Repair the C implementation of [`xml.etree.ElementTree.Element.itertext()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.itertext): it no longer yields text covering comments and processing instructions.

[gh-149489](https://github.com/python/cpython/issues/149489): Repair [`ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree) serialization into HTML. The contents of the “xmp”, “iframe”, “noembed”, “noframes”, and “plaintext” elements are no longer escaped. The “plaintext” element now lacks its closing tag.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

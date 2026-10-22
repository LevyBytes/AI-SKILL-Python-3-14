# Python 3.11.0 alpha 6 / library / xml etree elementtree

[bpo-45948](https://bugs.python.org/issue?@action=redirect&bpo=45948): Settled an inconsistency in the C build of the [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree) module. From now on, building an [`xml.etree.ElementTree.XMLParser`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser) with a `target=None` keyword supplies a default [`xml.etree.ElementTree.TreeBuilder`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.TreeBuilder) target, just as the Python build already does.

[bpo-25707](https://bugs.python.org/issue?@action=redirect&bpo=25707): Closed a file leak in [`xml.etree.ElementTree.iterparse()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.iterparse) arising when the iterator is left partly consumed. Jacob Walls wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

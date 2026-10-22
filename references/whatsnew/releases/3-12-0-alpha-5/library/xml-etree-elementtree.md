# Python 3.12.0 alpha 5 / library / xml etree elementtree

[bpo-38941](https://bugs.python.org/issue?@action=redirect&bpo=38941): Testing the truth value of an [`xml.etree.ElementTree.Element`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element) now makes the [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree) module raise [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). Previously the Python implementation produced [`FutureWarning`](https://docs.python.org/3.14/library/exceptions.html#FutureWarning) while the C implementation produced nothing.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

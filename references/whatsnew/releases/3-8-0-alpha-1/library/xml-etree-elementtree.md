# Python 3.8.0 alpha 1 / library / xml etree elementtree

[bpo-29209](https://bugs.python.org/issue?@action=redirect&bpo=29209): Dropped the `doctype()` method together with the *html* parameter from the constructor of [`XMLParser`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser). A `doctype()` method declared within a subclass is no longer invoked. The deprecated `getchildren()` and `getiterator()` methods in the [`ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree) module now raise a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) rather than a [`PendingDeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#PendingDeprecationWarning).

[bpo-35502](https://bugs.python.org/issue?@action=redirect&bpo=35502): Corrected reference leaks within [`xml.etree.ElementTree.TreeBuilder`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.TreeBuilder) when the tree is left half-built (notably whenever an error gets raised midway through parsing XML).

[bpo-35008](https://bugs.python.org/issue?@action=redirect&bpo=35008): Closed reference leaks that occurred when the `__setstate__()` method of [`xml.etree.ElementTree.Element`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element) was invoked in the C implementation against an element that had already been initialized.

[bpo-34941](https://bugs.python.org/issue?@action=redirect&bpo=34941): The `Element` class methods `find()`, `findtext()` and `findall()` in the [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree) module can now locate children that are instances of `Element` subclasses.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

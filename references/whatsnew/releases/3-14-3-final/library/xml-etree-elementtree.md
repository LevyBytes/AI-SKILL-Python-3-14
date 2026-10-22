# Python 3.14.3 final / library / xml etree elementtree

[gh-143200](https://github.com/python/cpython/issues/143200): [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree): use-after-free crashes in the [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) and [`__setitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__setitem__) methods of [`Element`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element), occurring when the element is mutated concurrently, are now fixed. Bénédikt Tran supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

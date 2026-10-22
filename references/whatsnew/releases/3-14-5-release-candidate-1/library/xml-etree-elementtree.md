# Python 3.14.5 release candidate 1 / library / xml etree elementtree

[gh-148801](https://github.com/python/cpython/issues/148801): [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree): Stop a crash inside [`Element.__deepcopy__`](https://docs.python.org/3.14/library/copy.html#object.__deepcopy__) when the tree is deeply nested.

[gh-148735](https://github.com/python/cpython/issues/148735): [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree): Close a use-after-free in [`Element.findtext`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.findtext) that arose when the tree was mutated by another path mid-search.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

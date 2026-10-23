# What's new in Python 3.14 / Pending removal in future versions - sys, wsgiref, xml.etree.elementtree

- `splituser()`

  - `splitvalue()`

  - `to_bytes()`

- [`wsgiref`](https://docs.python.org/3.14/library/wsgiref.html#module-wsgiref): partial writes from `SimpleHandler.stdout.write()` are to be avoided.

- [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree): Evaluating the truth value of an [`Element`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element) carries a deprecation. A later release will have it always yield `True`. Favor explicit `len(elem)` or `elem is not None` checks instead.

- [`sys._clear_type_cache()`](https://docs.python.org/3.14/library/sys.html#sys._clear_type_cache) carries a deprecation: lean on [`sys._clear_internal_caches()`](https://docs.python.org/3.14/library/sys.html#sys._clear_internal_caches) instead.

[Subject index](INDEX.md) · [Previous source section](pending-removal-in-future-versions-ssl-tlsversion-tlsv1.md) · [Next source section](cpython-bytecode-changes.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](undated-api-removals.md)

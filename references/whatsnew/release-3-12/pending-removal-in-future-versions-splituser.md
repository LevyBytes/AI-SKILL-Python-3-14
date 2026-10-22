# What’s New In Python 3.12 / Pending removal in future versions — sys, wsgiref, xml.etree.elementtree

- `splituser()`

  - `splitvalue()`

  - `to_bytes()`

- [`wsgiref`](https://docs.python.org/3.14/library/wsgiref.html#module-wsgiref): `SimpleHandler.stdout.write()` ought to avoid partial writes.

- [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree): Evaluating the truth value of an [`Element`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element) is deprecated. A later release will make it always return `True`. Favor explicit `len(elem)` or `elem is not None` tests instead.

- [`sys._clear_type_cache()`](https://docs.python.org/3.14/library/sys.html#sys._clear_type_cache) is deprecated: rely on [`sys._clear_internal_caches()`](https://docs.python.org/3.14/library/sys.html#sys._clear_internal_caches) in its place.

[Subject index](INDEX.md) · [Previous source section](pending-removal-in-future-versions-ssl-tlsversion-tlsv1.md) · [Next source section](asynchat-and-asyncore.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](undated-api-removals.md)

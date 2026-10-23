# What’s New In Python 3.12 / xml.etree.ElementTree - copy, xml.etree.elementtree

### xml.etree.ElementTree

- Drop the pure Python implementation's `ElementTree.Element.copy()` method (deprecated back in Python 3.10); reach for the [`copy.copy()`](https://docs.python.org/3.14/library/copy.html#copy.copy) function in its place. Note that the C build of [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree) never had a `copy()` method, exposing only `__copy__()`. (Contributed by Victor Stinner in [gh-94383](https://github.com/python/cpython/issues/94383).)

[Subject index](INDEX.md) · [Previous source section](webbrowser.md) · [Next source section](zipimport.md) · [Release/subject declaration](summary-release-highlights.md)

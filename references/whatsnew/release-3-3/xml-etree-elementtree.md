# What's New In Python 3.3 / xml.etree.ElementTree — xml.etree.elementtree

### xml.etree.ElementTree

By default, the [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree) module now pulls in its C accelerator, so importing `xml.etree.cElementTree` explicitly is no longer required (that module remains for backward compatibility but carries a deprecation now). On top of that, the `iter` group of [`Element`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element) methods was sped up (reimplemented in C). The module's docs were likewise expanded considerably, gaining examples and a fuller reference.

[Subject index](INDEX.md) · [Previous source section](webbrowser.md) · [Next source section](zlib.md) · [Release/subject declaration](summary-release-highlights.md)

# What's New In Python 3.9 / xml - xml.etree.elementtree

### xml

Whitespace characters inside attributes are now retained when [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree) is serialized to an XML file. EOLNs are no longer collapsed to ?n?. This follows from a discussion over the interpretation of section 2.11 of the XML spec. (Contributed by Mefistotelis in [bpo-39011](https://bugs.python.org/issue?@action=redirect&bpo=39011).)

[Subject index](INDEX.md) · [Previous source section](venv.md) · [Next source section](optimizations.md) · [Release/subject declaration](summary-release-highlights.md)

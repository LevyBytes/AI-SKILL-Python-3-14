# What's New In Python 3.13 / xml — pyexpat, xml.etree.elementtree

### xml

- Permit governing of Expat >=2.6.0 reparse deferral ([**CVE 2023-52425**](https://www.cve.org/CVERecord?id=CVE-2023-52425)) through five additional methods:

  - [`xml.etree.ElementTree.XMLParser.flush()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser.flush)

  - [`xml.etree.ElementTree.XMLPullParser.flush()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLPullParser.flush)

  - [`xml.parsers.expat.xmlparser.GetReparseDeferralEnabled()`](https://docs.python.org/3.14/library/pyexpat.html#xml.parsers.expat.xmlparser.GetReparseDeferralEnabled)

  - [`xml.parsers.expat.xmlparser.SetReparseDeferralEnabled()`](https://docs.python.org/3.14/library/pyexpat.html#xml.parsers.expat.xmlparser.SetReparseDeferralEnabled)

  - `xml.sax.expatreader.ExpatParser.flush()`

(Contributed by Sebastian Pipping in [gh-115623](https://github.com/python/cpython/issues/115623).)

- Introduce a `close()` method on the iterator that [`iterparse()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.iterparse) returns, allowing deliberate cleanup. (Contributed by Serhiy Storchaka in [gh-69893](https://github.com/python/cpython/issues/69893).)

[Subject index](INDEX.md) · [Previous source section](warnings.md) · [Next source section](zipimport.md) · [Release/subject declaration](summary-release-highlights.md)

# Python 3.13.0 alpha 5 / security / xml etree elementtree

[gh-115398](https://github.com/python/cpython/issues/115398): Permit control over Expat >=2.6.0 reparse deferral ([**CVE 2023-52425**](https://www.cve.org/CVERecord?id=CVE-2023-52425)) through five freshly added methods:

  - [`xml.etree.ElementTree.XMLParser.flush()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser.flush)

  - [`xml.etree.ElementTree.XMLPullParser.flush()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLPullParser.flush)

  - [`xml.parsers.expat.xmlparser.GetReparseDeferralEnabled()`](https://docs.python.org/3.14/library/pyexpat.html#xml.parsers.expat.xmlparser.GetReparseDeferralEnabled)

  - [`xml.parsers.expat.xmlparser.SetReparseDeferralEnabled()`](https://docs.python.org/3.14/library/pyexpat.html#xml.parsers.expat.xmlparser.SetReparseDeferralEnabled)

  - `xml.sax.expatreader.ExpatParser.flush()`

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

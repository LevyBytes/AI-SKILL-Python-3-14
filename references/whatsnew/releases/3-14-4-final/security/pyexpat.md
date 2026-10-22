# Python 3.14.4 final / security / pyexpat

[gh-145986](https://github.com/python/cpython/issues/145986): [`xml.parsers.expat`](https://docs.python.org/3.14/library/pyexpat.html#module-xml.parsers.expat): Repaired a crash brought on by unbounded C recursion while transforming deeply nested XML content models via [`ElementDeclHandler()`](https://docs.python.org/3.14/library/pyexpat.html#xml.parsers.expat.xmlparser.ElementDeclHandler). This covers [**CVE 2026-4224**](https://www.cve.org/CVERecord?id=CVE-2026-4224).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

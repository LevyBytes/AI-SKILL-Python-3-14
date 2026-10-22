# Python 3.14.4 final / security / io

[gh-145506](https://github.com/python/cpython/issues/145506): Clears [**CVE 2026-2297**](https://www.cve.org/CVERecord?id=CVE-2026-2297) by making `SourcelessFileLoader` route through [`io.open_code()`](https://docs.python.org/3.14/library/io.html#io.open_code) whenever it opens `.pyc` files.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

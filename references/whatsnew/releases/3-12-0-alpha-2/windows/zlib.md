# Python 3.12.0 alpha 2 / windows / zlib

[gh-98689](https://github.com/python/cpython/issues/98689): Move Windows builds up to zlib v1.2.13. Although v1.2.12 carries [**CVE 2022-37434**](https://www.cve.org/CVERecord?id=CVE-2022-37434), Python never calls the affected `inflateGetHeader` API.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

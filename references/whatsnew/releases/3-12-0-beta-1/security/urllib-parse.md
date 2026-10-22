# Python 3.12.0 beta 1 / security / urllib parse

[gh-102153](https://github.com/python/cpython/issues/102153): Following WHATWG's URL specification, [`urllib.parse.urlsplit()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urlsplit) now removes any leading C0 control characters and spaces, addressing [**CVE 2023-24329**](https://www.cve.org/CVERecord?id=CVE-2023-24329). Illia Volochii supplied this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

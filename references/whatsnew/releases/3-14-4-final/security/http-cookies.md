# Python 3.14.4 final / security / http cookies

[gh-145599](https://github.com/python/cpython/issues/145599): Refuse control characters within [`http.cookies.Morsel`](https://docs.python.org/3.14/library/http.cookies.html#http.cookies.Morsel) [`update()`](https://docs.python.org/3.14/library/http.cookies.html#http.cookies.Morsel.update) and [`js_output()`](https://docs.python.org/3.14/library/http.cookies.html#http.cookies.BaseCookie.js_output). This covers [**CVE 2026-3644**](https://www.cve.org/CVERecord?id=CVE-2026-3644).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

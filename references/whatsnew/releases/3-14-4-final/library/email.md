# Python 3.14.4 final / library / email

[gh-144156](https://github.com/python/cpython/issues/144156): Corrects the folding of headers performed by the [`email`](https://docs.python.org/3.14/library/email.html#module-email) library whenever [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html) encoded words appear. Whitespace is now preserved correctly and also added correctly between adjacent encoded words. That latter property had been broken through the fix for [gh-92081](https://github.com/python/cpython/issues/92081), which mostly repaired earlier failures to preserve whitespace.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

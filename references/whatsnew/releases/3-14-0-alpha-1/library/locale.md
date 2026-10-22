# Python 3.14.0 alpha 1 / library / locale

[gh-69998](https://github.com/python/cpython/issues/69998): Repairs [`locale.nl_langinfo()`](https://docs.python.org/3.14/library/locale.html#locale.nl_langinfo) for situations where the various categories carry differing locales. Under certain circumstances the routine momentarily assigns the `LC_CTYPE` locale. That brief switch will reach other threads too.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

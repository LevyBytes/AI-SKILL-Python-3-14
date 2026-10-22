# Python 3.14.0 alpha 5 / c api / unicode

[gh-89188](https://github.com/python/cpython/issues/89188): Provided [`PyUnicode_KIND()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_KIND) and [`PyUnicode_DATA()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_DATA) as functions as well, alongside the identically named macros. Those macros depend on C bit fields, whose layout varies by compiler. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

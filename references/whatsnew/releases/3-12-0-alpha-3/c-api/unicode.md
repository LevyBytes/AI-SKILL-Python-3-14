# Python 3.12.0 alpha 3 / c api / unicode

[gh-99612](https://github.com/python/cpython/issues/99612): Correct [`PyUnicode_DecodeUTF8Stateful()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_DecodeUTF8Stateful) on ASCII-only input, where `*consumed` had gone unset.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

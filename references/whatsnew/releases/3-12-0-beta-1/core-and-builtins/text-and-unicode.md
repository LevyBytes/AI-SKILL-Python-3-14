# Python 3.12.0 beta 1 / core and builtins / text and unicode

[gh-103895](https://github.com/python/cpython/issues/103895): Better handle the corner cases in how `Exception.__notes__` is displayed. The messages now always finish with a newline, and string/bytes values are no longer spread across multiple lines. Carey Metcalfe wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.14.6 final / core and builtins / unicodedata

[gh-149449](https://github.com/python/cpython/issues/149449): Repair a use-after-free segfault arising once the [`unicodedata`](https://docs.python.org/3.14/library/unicodedata.html#module-unicodedata) module had been dropped from [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules) and collected as garbage between calls decoding `\N{...}` escapes or invoking the `namereplace` codec error handler.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

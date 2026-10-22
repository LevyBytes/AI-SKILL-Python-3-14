# Python 3.14.4 final / core and builtins / unicode

[gh-146196](https://github.com/python/cpython/issues/146196): Eliminates possible Undefined Behavior within [`PyUnicodeWriter_WriteASCII()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteASCII) through the addition of a zero-length guard. Shamil Abdulaev supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

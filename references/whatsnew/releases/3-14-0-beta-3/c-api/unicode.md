# Python 3.14.0 beta 3 / c api / unicode

[gh-133968](https://github.com/python/cpython/issues/133968): Introduce a [`PyUnicodeWriter_WriteASCII()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteASCII) function for emitting an ASCII string into a [`PyUnicodeWriter`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter). It runs faster than [`PyUnicodeWriter_WriteUTF8()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteUTF8), though its behavior becomes undefined should the supplied string carry non-ASCII characters. Patch by Victor Stinner.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

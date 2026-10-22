# Python 3.12.0 alpha 1 / c api / unicode

[gh-98393](https://github.com/python/cpython/issues/98393): The [`PyUnicode_FSDecoder()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FSDecoder) routine will no longer take bytes-like paths such as the [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) and [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) types; for byte strings, only the precise [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) type works. Victor Stinner provided the patch.

[gh-95781](https://github.com/python/cpython/issues/95781): When a format character is not recognized, [`PyUnicode_FromFormat()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormat) and [`PyUnicode_FromFormatV()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormatV) now raise a [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError). Earlier releases instead copied the remainder of the format string verbatim into the output and threw away any leftover arguments.

[gh-95504](https://github.com/python/cpython/issues/95504): Correct where the sign lands when a width or precision is given to [`PyUnicode_FromFormat()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormat) and [`PyUnicode_FromFormatV()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormatV). Philip Georgi authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

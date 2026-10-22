# Locale Encoding

### Locale Encoding

Text coming from the operating system can be decoded with the current locale encoding.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_DecodeLocaleAndSize(const char *str, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) length, const char *errors)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

On Android and VxWorks decode a string from UTF-8; on every other platform decode from the current locale encoding. The error handlers that are honored are `"strict"` and `"surrogateescape"` ([**PEP 383**](https://peps.python.org/pep-0383/)). Whenever *errors* is `NULL`, the decoder defaults to the `"strict"` error handler. *str* has to be terminated by a null character yet must not hold any embedded null characters.

When you instead want to decode a string from the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler), turn to `PyUnicode_DecodeFSDefaultAndSize()`.

The [Python UTF-8 Mode](https://docs.python.org/3.14/library/os.html#utf8-mode) is disregarded by this routine.

See also

The [`Py_DecodeLocale()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_DecodeLocale) function.

Added in version 3.3.

Changed in version 3.7: Outside of Android, the routine now applies the current locale encoding for the `surrogateescape` error handler as well. Formerly [`Py_DecodeLocale()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_DecodeLocale) handled `surrogateescape`, while the current locale encoding handled `strict`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_DecodeLocale(const char *str, const char *errors)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Comparable to `PyUnicode_DecodeLocaleAndSize()`, except that it derives the string length by calling `strlen()`.

Added in version 3.3.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_EncodeLocale([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, const char *errors)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

On Android and VxWorks encode a Unicode object to UTF-8; on every other platform encode to the current locale encoding. The error handlers that are honored are `"strict"` and `"surrogateescape"` ([**PEP 383**](https://peps.python.org/pep-0383/)). Whenever *errors* is `NULL`, the encoder defaults to the `"strict"` error handler. A [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object comes back. *unicode* must not hold any embedded null characters.

When you instead want to encode a string to the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler), turn to `PyUnicode_EncodeFSDefault()`.

The [Python UTF-8 Mode](https://docs.python.org/3.14/library/os.html#utf8-mode) is disregarded by this routine.

See also

The [`Py_EncodeLocale()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_EncodeLocale) function.

Added in version 3.3.

Changed in version 3.7: Outside of Android, the routine now applies the current locale encoding for the `surrogateescape` error handler as well. Formerly [`Py_EncodeLocale()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_EncodeLocale) handled `surrogateescape`, while the current locale encoding handled `strict`.

[Subject index](INDEX.md) · [Previous source contract](pyunicode-fill-to-pyunicode-asucs4copy.md) · [Following source contract](pyunicode-fsconverter-to-pyunicode-encodefsdefault.md)

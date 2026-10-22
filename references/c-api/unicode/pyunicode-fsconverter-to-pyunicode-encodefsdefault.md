# File System Encoding

### File System Encoding

Routines that encode to and decode from the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler) ([**PEP 383**](https://peps.python.org/pep-0383/) and [**PEP 529**](https://peps.python.org/pep-0529/)).

When you want to turn file names into [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) while parsing arguments, reach for the `"O&"` converter and supply `PyUnicode_FSConverter()` as the conversion routine:

 int PyUnicode_FSConverter([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, void *result)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

[PyArg_Parse* converter](https://docs.python.org/3.14/c-api/arg.html#arg-parsing): take [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) objects – whether supplied directly or by way of the [`os.PathLike`](https://docs.python.org/3.14/library/os.html#os.PathLike) interface – and encode them to [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) by means of `PyUnicode_EncodeFSDefault()`; any `bytes` objects pass straight through unchanged. *result* has to be the address of a C variable whose type is [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)* (or [PyBytesObject](https://docs.python.org/3.14/c-api/bytes.html#c.PyBytesObject)*). When it succeeds, the variable is set to a new [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) pointing at a [bytes object](https://docs.python.org/3.14/c-api/bytes.html#bytesobjects) — which has to be released once it is done with — and a non-zero value is returned ([`Py_CLEANUP_SUPPORTED`](https://docs.python.org/3.14/c-api/arg.html#c.Py_CLEANUP_SUPPORTED)). The result may not contain any embedded null bytes. When it fails, `0` is returned with an exception raised.

Should *obj* be `NULL`, the routine drops a strong reference held in the variable that *result* points at and returns `1`.

Added in version 3.1.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

When you want to turn file names into [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) while parsing arguments, reach for the `"O&"` converter and supply `PyUnicode_FSDecoder()` as the conversion routine:

 int PyUnicode_FSDecoder([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, void *result)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

[PyArg_Parse* converter](https://docs.python.org/3.14/c-api/arg.html#arg-parsing): take [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) objects – whether supplied directly or indirectly by way of the [`os.PathLike`](https://docs.python.org/3.14/library/os.html#os.PathLike) interface – and decode them to [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) by means of `PyUnicode_DecodeFSDefaultAndSize()`; any `str` objects pass straight through unchanged. *result* has to be the address of a C variable whose type is [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)* (or PyUnicodeObject*). When it succeeds, the variable is set to a new [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) pointing at a Unicode object — which has to be released once it is done with — and a non-zero value is returned ([`Py_CLEANUP_SUPPORTED`](https://docs.python.org/3.14/c-api/arg.html#c.Py_CLEANUP_SUPPORTED)). The result may not contain any embedded null characters. When it fails, `0` is returned with an exception raised.

Should *obj* be `NULL`, drop the strong reference to the object that *result* points at and return `1`.

Added in version 3.2.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_DecodeFSDefaultAndSize(const char *str, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Decode a string by way of the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler).

Should you need instead to decode a string from the current locale encoding, use `PyUnicode_DecodeLocaleAndSize()`.

See also

The [`Py_DecodeLocale()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_DecodeLocale) function.

Changed in version 3.6: The [filesystem error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler) is now used.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_DecodeFSDefault(const char *str)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Decode a null-terminated string by way of the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler).

When the string length is already known, use `PyUnicode_DecodeFSDefaultAndSize()`.

Changed in version 3.6: The [filesystem error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler) is now used.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_EncodeFSDefault([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Encode a Unicode object by way of the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler), and return [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes). Be aware that the `bytes` object produced may hold null bytes.

Should you need instead to encode a string to the current locale encoding, use `PyUnicode_EncodeLocale()`.

See also

The [`Py_EncodeLocale()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_EncodeLocale) function.

Added in version 3.2.

Changed in version 3.6: The [filesystem error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler) is now used.

[Subject index](INDEX.md) · [Previous source contract](pyunicode-decodelocaleandsize-to-pyunicode-encodelocale.md) · [Following source contract](pyunicode-fromwidechar-to-pyunicode-aswidecharstring.md)

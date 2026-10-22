# Generic Codecs

### Generic Codecs

This macro is made available:

 Py_UNICODE_REPLACEMENT_CHARACTER

The Unicode code point `U+FFFD` (replacement character).

When the *errors* argument is set to “replace”, this Unicode character serves as the replacement character throughout decoding.

The generic codec APIs are these:

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_Decode(const char *str, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size, const char *encoding, const char *errors)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Construct a Unicode object out of *str*, decoding *size* bytes of that encoded string. *encoding* and *errors* carry the same meaning as the like-named parameters of the [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) built-in function. Which codec to apply is resolved through the Python codec registry. Should the codec raise an exception, `NULL` is returned.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_AsEncodedString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, const char *encoding, const char *errors)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Encode a Unicode object and return the outcome as a Python bytes object. *encoding* and *errors* carry the same meaning as the like-named parameters of the Unicode [`encode()`](https://docs.python.org/3.14/library/stdtypes.html#str.encode) method. Which codec to apply is resolved through the Python codec registry. Should the codec raise an exception, `NULL` is returned.

[Subject index](INDEX.md) · [Previous source contract](built-in-codecs.md) · [Following source contract](pyunicode-decodeutf8-to-pyunicode-asutf8string.md)

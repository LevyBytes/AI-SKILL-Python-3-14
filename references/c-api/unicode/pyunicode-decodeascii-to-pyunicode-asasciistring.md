# ASCII Codecs

### ASCII Codecs

The ASCII codec APIs are listed below. Only 7-bit ASCII data passes; every other code produces errors.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_DecodeASCII(const char *str, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size, const char *errors)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Build a Unicode object by decoding *size* bytes from the ASCII encoded string *str*. Return `NULL` if the codec raised an exception.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_AsASCIIString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Apply ASCII to encode a Unicode object and hand back the outcome as a Python bytes object. Error handling is “strict”. Return `NULL` if the codec raised an exception.

[Subject index](INDEX.md) · [Previous source contract](pyunicode-decodelatin1-to-pyunicode-aslatin1string.md) · [Following source contract](pyunicode-decodecharmap-to-pyunicode-translate.md)

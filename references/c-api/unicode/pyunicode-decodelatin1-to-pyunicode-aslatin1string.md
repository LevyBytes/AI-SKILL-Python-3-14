# Latin-1 Codecs

### Latin-1 Codecs

The Latin-1 codec APIs are listed below: Latin-1 maps to the first 256 Unicode ordinals, and during encoding the codecs accept only those.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_DecodeLatin1(const char *str, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size, const char *errors)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Build a Unicode object by decoding *size* bytes from the Latin-1 encoded string *str*. Return `NULL` if the codec raised an exception.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_AsLatin1String([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Apply Latin-1 to encode a Unicode object and hand back the outcome as a Python bytes object. Error handling is “strict”. Return `NULL` if the codec raised an exception.

[Subject index](INDEX.md) · [Previous source contract](raw-unicode-escape-codecs.md) · [Following source contract](pyunicode-decodeascii-to-pyunicode-asasciistring.md)

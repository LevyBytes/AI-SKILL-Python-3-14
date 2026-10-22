# Raw-Unicode-Escape Codecs

### Raw-Unicode-Escape Codecs

The “Raw Unicode Escape” codec APIs are listed below:

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_DecodeRawUnicodeEscape(const char *str, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size, const char *errors)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Build a Unicode object by decoding *size* bytes from the Raw-Unicode-Escape encoded string *str*. Return `NULL` if the codec raised an exception.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_AsRawUnicodeEscapeString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Apply Raw-Unicode-Escape to encode a Unicode object and hand back the outcome as a bytes object. Error handling is “strict”. Return `NULL` if the codec raised an exception.

[Subject index](INDEX.md) · [Previous source contract](unicode-escape-codecs.md) · [Following source contract](pyunicode-decodelatin1-to-pyunicode-aslatin1string.md)

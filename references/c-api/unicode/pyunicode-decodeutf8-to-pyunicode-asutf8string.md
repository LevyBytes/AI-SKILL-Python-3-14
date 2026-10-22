# UTF-8 Codecs

### UTF-8 Codecs

The UTF-8 codec APIs are these:

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_DecodeUTF8(const char *str, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size, const char *errors)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Construct a Unicode object out of *str*, decoding *size* bytes of that UTF-8 encoded string. Should the codec raise an exception, `NULL` is returned.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_DecodeUTF8Stateful(const char *str, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size, const char *errors, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *consumed)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

When *consumed* is `NULL`, this acts just like `PyUnicode_DecodeUTF8()`. When *consumed* isn't `NULL`, a trailing incomplete UTF-8 byte sequence is not flagged as an error. Such bytes go undecoded, and the tally of bytes that did get decoded is placed into *consumed*.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_AsUTF8String([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Encode a Unicode object with UTF-8 and return the outcome as a Python bytes object. The error handling is “strict”. Should the codec raise an exception, `NULL` is returned.

This routine fails whenever the string holds surrogate code points (`U+D800` - `U+DFFF`).

[Subject index](INDEX.md) · [Previous source contract](py-unicode-replacement-character-to-pyunicode-asencodedstring.md) · [Following source contract](pyunicode-asutf8andsize.md)

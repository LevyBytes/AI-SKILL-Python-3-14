# UTF-7 Codecs

### UTF-7 Codecs

The UTF-7 codec APIs are listed below:

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_DecodeUTF7(const char *str, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size, const char *errors)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Build a Unicode object by decoding *size* bytes from the UTF-7 encoded string *str*. Return `NULL` if the codec raised an exception.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_DecodeUTF7Stateful(const char *str, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size, const char *errors, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *consumed)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

When *consumed* is `NULL`, the behavior matches `PyUnicode_DecodeUTF7()`. When *consumed* is not `NULL`, an error is not raised for trailing incomplete UTF-7 base-64 portions. Such bytes go undecoded, and the count of bytes that were decoded gets recorded in *consumed*.

[Subject index](INDEX.md) · [Previous source contract](pyunicode-decodeutf16-to-pyunicode-asutf16string.md) · [Following source contract](unicode-escape-codecs.md)

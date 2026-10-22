# const char *PyUnicode_AsUTF8(PyObject *unicode)

const char *PyUnicode_AsUTF8([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode)

Behaves like `PyUnicode_AsUTF8AndSize()`, except the size is not recorded.

Warning

For [null characters](https://en.wikipedia.org/wiki/Null_character) sitting inside *unicode*, this function applies no special handling. Consequently, any null characters in a string stay within the value that is returned, and certain C routines may read such a byte as a string terminator, which causes truncation. When that truncation matters, prefer `PyUnicode_AsUTF8AndSize()` as the alternative.

Added in version 3.3.

Changed in version 3.7: The returned type became `const char *` in place of the former `char *`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyunicode-decodeutf8-to-pyunicode-asutf8string.md) · [Following source contract](pyunicode-asutf8andsize.md) · [Following source contract](pyunicode-decodeutf32-to-pyunicode-asutf32string.md)

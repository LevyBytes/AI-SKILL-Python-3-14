# Py_ssize_t PyUnicode_GetLength(PyObject *unicode)

[Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyUnicode_GetLength([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode)
* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Give back the length, measured in code points, of the Unicode object.

When something goes wrong, raise an exception and hand back `-1`.

Added in version 3.3.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyunicode-new-to-pyunicode-fromstring.md) · [Previous source contract](pyunicode-fromformatv-to-pyunicode-getdefaultencoding.md) · [Previous source contract](pyunicode-copycharacters.md)

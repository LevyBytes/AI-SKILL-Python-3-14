# Py_ssize_t PyUnicode_CopyCharacters(PyObject *to, Py_ssize_t to_start, PyObject *from, Py_ssize_t from_start, Py_ssize_t how_many)

[Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyUnicode_CopyCharacters([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *to, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) to_start, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *from, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) from_start, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) how_many)

Transfer characters out of one Unicode object and into another. Where required this routine converts characters, and where it can it drops back to `memcpy()`. On error it yields `-1` and raises an exception; otherwise it yields the count of characters that were copied.

The string is required not to have been “used” already. Consult `PyUnicode_New()` for the specifics.

Added in version 3.3.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyunicode-new-to-pyunicode-fromstring.md) · [Following source contract](pyunicode-getlength.md) · [Following source contract](pyunicode-fill-to-pyunicode-asucs4copy.md)

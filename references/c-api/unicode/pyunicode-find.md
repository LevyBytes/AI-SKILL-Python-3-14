# Py_ssize_t PyUnicode_Find(PyObject *unicode, PyObject *substr, Py_ssize_t start, Py_ssize_t end, int direction)

[Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyUnicode_Find([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *substr, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) start, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) end, int direction)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*
Yield the earliest spot where *substr* turns up within `unicode[start:end]`, scanning according to *direction* (with *direction* == `1` requesting a forward sweep and *direction* == `-1` a reverse one). What comes back is the index of that first hit; a `-1` here signals nothing matched, while `-2` signals a failure occurred and an exception is now set.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyunicode-concat-to-pyunicode-tailmatch.md) · [Previous source contract](pyunicode-findchar.md)

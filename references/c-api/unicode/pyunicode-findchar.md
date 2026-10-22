# Py_ssize_t PyUnicode_FindChar(PyObject *unicode, Py_UCS4 ch, Py_ssize_t start, Py_ssize_t end, int direction)

[Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyUnicode_FindChar([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, Py_UCS4 ch, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) start, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) end, int direction)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Yield the earliest spot where the character *ch* turns up within `unicode[start:end]`, scanning according to *direction* (with *direction* == `1` requesting a forward sweep and *direction* == `-1` a reverse one). What comes back is the index of that first hit; a `-1` here signals nothing matched, while `-2` signals a failure occurred and an exception is now set.

Added in version 3.3.

Changed in version 3.7: the *start* and *end* arguments are henceforth clamped so they act the way `unicode[start:end]` does.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyunicode-concat-to-pyunicode-tailmatch.md) · [Following source contract](pyunicode-find.md) · [Following source contract](pyunicode-count-to-pyunicode-comparewithasciistring.md)

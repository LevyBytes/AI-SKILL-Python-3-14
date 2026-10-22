# unicode C API: `PyUnicode_READ()`, `PyUnicode_READ_CHAR()`, `PyUnicode_MAX_CHAR_VALUE()`, `PyUnicode_IsIdentifier()`, `PyUnicode_IS_ASCII()`

Py_UCS4 PyUnicode_READ(int kind, void *data, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) index)

Fetches a code point out of a canonical representation *data* (such as you get from `PyUnicode_DATA()`). It runs no checks and no ready calls.

Added in version 3.3.

 Py_UCS4 PyUnicode_READ_CHAR([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) index)

Fetches a character from a Unicode object *unicode*, which has to be in the “canonical” representation. When you perform several reads back to back, this is slower than `PyUnicode_READ()`.

Added in version 3.3.

 Py_UCS4 PyUnicode_MAX_CHAR_VALUE([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode)

Gives the largest code point fit for building a fresh string out of *unicode*, which has to be in the “canonical” representation. The figure is always an estimate, though it beats looping across the string.

Added in version 3.3.

 int PyUnicode_IsIdentifier([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Gives `1` when the string is a legal identifier under the language definition, section [Names (identifiers and keywords)](https://docs.python.org/3.14/reference/lexical_analysis.html#identifiers). Otherwise it gives `0`.

Changed in version 3.9: When the string is not ready, the function no longer invokes [`Py_FatalError()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_FatalError).

 unsigned int PyUnicode_IS_ASCII([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode)

Returns true when the string holds nothing but ASCII characters. Equivalent to [`str.isascii()`](https://docs.python.org/3.14/library/stdtypes.html#str.isascii).

Added in version 3.2.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyunicode-type-to-pyunicodeiter-type.md) · [Owning structure and shared ABI conditions](pyasciiobject-to-pyunicode-write.md) · [Following source contract](py-unicode-isspace-to-py-unicode-is-high-surrogate.md)

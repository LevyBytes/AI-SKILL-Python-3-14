# const char *PyUnicode_AsUTF8AndSize(PyObject *unicode, Py_ssize_t *size)

const char *PyUnicode_AsUTF8AndSize([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *size)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Hand back a pointer to the UTF-8 encoding of the Unicode object, and record the size of that encoded representation (counted in bytes) in *size*. The *size* argument is allowed to be `NULL`, in which case no size gets recorded. Whether or not other null code points are present, the buffer handed back always carries one extra null byte at its end (which *size* does not count).

On error, raise an exception, set *size* to `-1` (provided it is not NULL) and hand back `NULL`.

This routine fails whenever the string holds surrogate code points (`U+D800` - `U+DFFF`).

The UTF-8 representation of the string is cached inside the Unicode object, so later calls hand back a pointer to that very same buffer. Freeing the buffer is not the caller's job. Once the Unicode object is garbage collected, the buffer is freed and any pointers into it stop being valid.

Added in version 3.3.
Changed in version 3.7: The returned type became `const char *` in place of the former `char *`.

Changed in version 3.10: This belongs to the [limited API](https://docs.python.org/3.14/c-api/stable.html#limited-c-api).

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyunicode-decodeutf8-to-pyunicode-asutf8string.md) · [Previous source contract](pyunicode-asutf8.md)

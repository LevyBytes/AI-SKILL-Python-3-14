# wchar_t Support

### wchar_t Support

`wchar_t` support on the platforms that provide it:

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_FromWideChar(const wchar_t *wstr, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Build a Unicode object out of the `wchar_t` buffer *wstr* of the supplied *size*. Handing in `-1` for *size* signals that the routine has to work out the length on its own, by calling `wcslen()`. On failure `NULL` is returned.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyUnicode_AsWideChar([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, wchar_t *wstr, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Move the contents of the Unicode object into the `wchar_t` buffer *wstr*. No more than *size* `wchar_t` characters get copied (a trailing null terminator, if any, excluded). The count of `wchar_t` characters copied is returned, or `-1` should an error occur.

If *wstr* is `NULL`, return instead the *size* that would be needed to hold the whole of *unicode* together with a terminating null.

Be aware that the wchar_t* string produced may or may not carry a null terminator. Making certain the wchar_t* string ends in null where the application demands it is left to the caller. Be aware too that the wchar_t* string can hold null characters, which would truncate the string when handed to most C functions.

 wchar_t *PyUnicode_AsWideCharString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *size)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Turn the Unicode object into a wide character string. A null character always terminates the output string. When *size* isn't `NULL`, the number of wide characters (with the trailing null terminator excluded) is written into **size*. Be aware that the `wchar_t` string produced can hold null characters, which would truncate the string when handed to most C functions. When *size* is `NULL` and the wchar_t* string holds null characters, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

On success a buffer allocated via [`PyMem_New`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_New) is returned (free it with [`PyMem_Free()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Free)). On error, `NULL` is returned and **size* holds no defined value. A [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) is raised whenever memory allocation does not succeed.

Added in version 3.2.

Changed in version 3.7: Now raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) whenever the wchar_t* string holds null characters while *size* is `NULL`.

[Subject index](INDEX.md) · [Previous source contract](pyunicode-fsconverter-to-pyunicode-encodefsdefault.md) · [Following source contract](built-in-codecs.md)

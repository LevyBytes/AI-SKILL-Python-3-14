# unicode C API: `PyUnicode_Resize()`, `PyUnicode_Fill()`, `PyUnicode_WriteChar()`, `PyUnicode_ReadChar()`, `PyUnicode_Substring()`, `PyUnicode_AsUCS4()`, `PyUnicode_AsUCS4Copy()`

int PyUnicode_Resize([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **unicode, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) length);

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Change the size of a Unicode object **unicode* so that it holds the new *length*, counted in code points.

Attempt to adjust the string's size in place — typically quicker than reserving fresh storage and moving characters over — or else build a brand-new string.

On success, **unicode* is updated to reference the freshly resized object and `0` comes back. If not, `-1` comes back, an exception is raised, and **unicode* stays as it was.

This routine performs no validation of the string's contents, so the outcome might not be a string in its canonical form.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyUnicode_Fill([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) start, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) length, Py_UCS4 fill_char)

Populate a string with one repeated character: store *fill_char* across `unicode[start:start+length]`.

This fails when *fill_char* exceeds the string's maximum character, or when the string carries more than a single reference.

The string is required not to have been “used” already. Consult `PyUnicode_New()` for the specifics.

Hand back how many characters were written, or hand back `-1` and raise an exception when something goes wrong.

Added in version 3.3.

 int PyUnicode_WriteChar([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) index, Py_UCS4 character)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Place a *character* into the string *unicode* at the zero-based *index*. Yield `0` when it works and `-1` when it fails with an exception raised.

This routine confirms that *unicode* really is a Unicode object, that the supplied index stays within bounds, and that the object holds a reference count of one. For a variant that omits these checks — leaving them up to you — see `PyUnicode_WRITE()`.

The string is required not to have been “used” already. Consult `PyUnicode_New()` for the specifics.

Added in version 3.3.

 Py_UCS4 PyUnicode_ReadChar([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) index)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Fetch a single character out of a string. Unlike `PyUnicode_READ_CHAR()`, which does no checking whatsoever, this routine confirms that *unicode* is a Unicode object and that the index sits within bounds.

Yield the character when it works, or `-1` when it fails with an exception raised.

Added in version 3.3.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_Substring([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) start, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) end)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Produce a portion of *unicode*, running from character index *start* (inclusive) up to character index *end* (exclusive). Negative index values aren't accepted. When something goes wrong, raise an exception and hand back `NULL`.

Added in version 3.3.

 Py_UCS4 *PyUnicode_AsUCS4([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, Py_UCS4 *buffer, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) buflen, int copy_null)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Move the string *unicode* into a UCS4 buffer, appending a null character when *copy_null* is set. It yields `NULL` and raises an exception on error (specifically, a [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) when *buflen* falls below the length of *unicode*). On success *buffer* is what comes back.

Added in version 3.3.

 Py_UCS4 *PyUnicode_AsUCS4Copy([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Move the string *unicode* into a freshly allocated UCS4 buffer obtained through [`PyMem_Malloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Malloc). Should that allocation fail, `NULL` comes back together with a [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError). The buffer handed back always carries one additional null code point at its end.

Added in version 3.3.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyunicode-new-to-pyunicode-fromstring.md) · [Previous source contract](pyunicode-copycharacters.md) · [Following source contract](pyunicode-decodelocaleandsize-to-pyunicode-encodelocale.md)

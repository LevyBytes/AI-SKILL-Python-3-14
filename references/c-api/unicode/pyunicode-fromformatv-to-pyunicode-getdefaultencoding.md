# unicode C API: Unicode construction, appending and encoding maps

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_FromFormatV(const char *format, va_list vargs)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Works the same as `PyUnicode_FromFormat()` apart from taking exactly two arguments.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_FromObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Copies an instance of a Unicode subtype into a fresh true Unicode object when that is needed. Should *obj* already be a true Unicode object (and not a subtype), a new [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to that object is returned.

Anything other than Unicode or one of its subtypes triggers a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_FromOrdinal(int ordinal)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Builds a Unicode Object from the supplied Unicode code point *ordinal*.

That ordinal has to lie within `range(0x110000)`. Should it not, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_FromEncodedObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, const char *encoding, const char *errors)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Decodes an encoded object *obj* into a Unicode object.

[`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) and other [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) are decoded following the supplied *encoding* and using the error handling spelled out by *errors*. Either one may be `NULL`, which makes the interface fall back on the default values (consult Built-in Codecs for details).

Every other object, Unicode objects included, makes a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) be set.

The API hands back `NULL` whenever an error occurred. Decref'ing the returned objects is the caller's job.

 void PyUnicode_Append([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **p_left, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *right)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Tacks the string *right* onto the end of *p_left*. The *p_left* argument has to point at a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to a Unicode object; `PyUnicode_Append()` gives up (“steals”) that reference.

On error, **p_left* is set to `NULL` and an exception is set.

On success, **p_left* is set to a new strong reference to the result.

 void PyUnicode_AppendAndDel([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **p_left, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *right)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This function resembles `PyUnicode_Append()`, the sole distinction being that it lowers the reference count of *right* by one.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_BuildEncodingMap([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *string)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hands back a mapping fit for decoding a custom single-byte encoding. Supplied a Unicode string *string* of as many as 256 characters that represents an encoding table, it returns either a compact internal mapping object or a dictionary that maps character ordinals onto byte values. Invalid input raises a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) and returns `NULL`.

Added in version 3.2.

 const char *PyUnicode_GetDefaultEncoding(void)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hands back the name of the default string encoding, `"utf-8"`. See [`sys.getdefaultencoding()`](https://docs.python.org/3.14/library/sys.html#sys.getdefaultencoding).

You need not free the returned string, and it stays valid right up to interpreter shutdown.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyunicode-new-to-pyunicode-fromstring.md) · [Previous source contract](pyunicode-fromformat.md) · [Following source contract](pyunicode-getlength.md)

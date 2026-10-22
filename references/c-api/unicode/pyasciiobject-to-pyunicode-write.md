# unicode C API: Unicode object layouts, storage kinds and data access

type PyASCIIObject

 type PyCompactUnicodeObject

 type PyUnicodeObject

Each of these subtypes of [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) embodies a Python Unicode object. You rarely touch them directly, because every API function operating on Unicode objects accepts and hands back `PyObject` pointers.

Added in version 3.3.

You can identify how a given object is laid out via the macros below. They never fail, yet feeding them anything other than a Python Unicode object leaves their behavior undefined.

 PyUnicode_IS_COMPACT(o)

True when *o* relies on the `PyCompactUnicodeObject` structure.

Added in version 3.3.

 PyUnicode_IS_COMPACT_ASCII(o)

True when *o* relies on the `PyASCIIObject` structure.

Added in version 3.3.

The APIs that follow are C macros plus static inline functions giving quick checks and access to a Unicode object's internal read-only data:

 int PyUnicode_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

Returns true when *obj* is a Unicode object or an instance of some Unicode subtype. The call never fails.

 int PyUnicode_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

Returns true when *obj* is a Unicode object yet not an instance of any subtype. The call never fails.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyUnicode_GET_LENGTH([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode)

Gives the Unicode string's length, counted in code points. Here *unicode* must be a Unicode object held in the “canonical” representation (this is not verified).

Added in version 3.3.

 Py_UCS1 *PyUnicode_1BYTE_DATA([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode)

 Py_UCS2 *PyUnicode_2BYTE_DATA([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode)

 Py_UCS4 *PyUnicode_4BYTE_DATA([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode)

Hands back a pointer to the canonical representation, cast to the UCS1, UCS2, or UCS4 integer type so you can reach characters directly. Nothing verifies that the canonical representation actually has the matching character size; lean on `PyUnicode_KIND()` to pick the appropriate function.

Added in version 3.3.

 PyUnicode_1BYTE_KIND

 PyUnicode_2BYTE_KIND

 PyUnicode_4BYTE_KIND

The values the `PyUnicode_KIND()` macro may return.

Added in version 3.3.

Changed in version 3.12: `PyUnicode_WCHAR_KIND` has been removed.

 int PyUnicode_KIND([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode)

Returns one of the PyUnicode kind constants listed above, telling you how many bytes per character the Unicode object spends storing its data. Here *unicode* must be a Unicode object in the “canonical” representation (this is not verified).

Added in version 3.3.

 void *PyUnicode_DATA([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode)

Hands back a void pointer aimed at the raw Unicode buffer. Here *unicode* must be a Unicode object in the “canonical” representation (this is not verified).

Added in version 3.3.

 void PyUnicode_WRITE(int kind, void *data, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) index, Py_UCS4 value)

Stores the code point *value* at the supplied zero-based *index* within a string.

Both the *kind* value and the *data* pointer have to come from a string by way of `PyUnicode_KIND()` and `PyUnicode_DATA()` respectively. Keep a reference to that string alive throughout your `PyUnicode_WRITE()` call. Everything `PyUnicode_WriteChar()` demands applies here too.

The routine validates none of its prerequisites and is meant to run inside loops.

Added in version 3.3.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyunicode-type-to-pyunicodeiter-type.md) · [Previous source contract](py-ucs4-to-py-ucs1.md) · [Following source contract](pyunicode-read-to-pyunicode-is-ascii.md)

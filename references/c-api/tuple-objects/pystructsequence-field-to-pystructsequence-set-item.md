# tuple objects C API: `PyStructSequence_Field`, `PyStructSequence_UnnamedField`, `PyStructSequence_New()`, `PyStructSequence_GetItem()`, `PyStructSequence_GET_ITEM()`, `PyStructSequence_SetItem()`, `PyStructSequence_SET_ITEM()`

type PyStructSequence_Field

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) (including all members).*

Describes one field of a struct sequence. Because a struct sequence is modeled as a tuple, every field carries the type [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*. A field's position within the `fields` array of the `PyStructSequence_Desc` selects which field of the struct sequence it describes.

 const char *name

The field's name; use `NULL` to terminate the named-field list, or `PyStructSequence_UnnamedField` to keep the field unnamed.

 const char *doc

Field docstring or `NULL` to omit.

 const char *const PyStructSequence_UnnamedField

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.11.*

Special value for a field name to leave it unnamed.

Changed in version 3.9: The type was changed from `char *`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyStructSequence_New([PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *type)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Produce an instance of *type*, which has to have been created via `PyStructSequence_NewType()`.

Return `NULL` with an exception set on failure.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyStructSequence_GetItem([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) pos)

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the object at index *pos* within the struct sequence that *p* points to.

Whenever Python is built in [debug mode](https://docs.python.org/3.14/using/configure.html#debug-build) or [`with assertions`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-assertions), an assertion enforces the bounds check.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyStructSequence_GET_ITEM([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) pos)

*Return value: Borrowed reference.*

Alias to `PyStructSequence_GetItem()`.

Changed in version 3.13: Now implemented as an alias to `PyStructSequence_GetItem()`.

 void PyStructSequence_SetItem([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) pos, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Assign value *o* to the field at index *pos* of the struct sequence *p*. As with `PyTuple_SET_ITEM()`, restrict this to populating brand new instances.

Should Python be built in [debug mode](https://docs.python.org/3.14/using/configure.html#debug-build) or [`with assertions`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-assertions), an assertion carries out the bounds check.

Note

This function “steals” a reference to *o*.

 void PyStructSequence_SET_ITEM([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *pos, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Alias to `PyStructSequence_SetItem()`.

Changed in version 3.13: Now implemented as an alias to `PyStructSequence_SetItem()`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytupleobject-to-pytuple-setitem.md) · [Owning C API section and shared conditions](pystructsequence-newtype-to-pystructsequence-inittype2.md) · [Previous source contract](pystructsequence-desc-to-n-in-sequence.md)

# object structures C API: `Py_TYPE()`, `Py_IS_TYPE()`, `Py_SET_TYPE()`, `Py_SIZE()`, `Py_SET_SIZE()`, `PyObject_HEAD_INIT()`, `PyVarObject_HEAD_INIT()`

[PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *Py_TYPE(PyObject *o)

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.14.*

Retrieve the type belonging to the Python object *o*.

What comes back is a reference [borrowed](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) from *o*. Don't free it via [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) or anything comparable.

Changed in version 3.11: `Py_TYPE()` now becomes a static inline function, and its parameter no longer has the const PyObject* type.

 int Py_IS_TYPE(PyObject *o, [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *type)

Yields a non-zero result when object *o* has the type *type*, and zero in every other case. Equivalent to: `Py_TYPE(o) == type`.

Added in version 3.9.

 void Py_SET_TYPE(PyObject *o, [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *type)

Assign *type* as the type of object *o*, performing no checks and no reference counting.

It is a deeply low-level operation. You'd usually be better off assigning the Python attribute [`__class__`](https://docs.python.org/3.14/reference/datamodel.html#object.__class__) through [`PyObject_SetAttrString()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_SetAttrString) or something similar.

Be aware that handing it a mismatched type may produce undefined behavior.

When *type* happens to be a [heap type](https://docs.python.org/3.14/c-api/typeobj.html#heap-types), the caller is responsible for creating a fresh reference to it. By the same token, if *o*'s previous type was a heap type, the caller has to drop a reference to that type.

Added in version 3.9.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) Py_SIZE(PyVarObject *o)

Retrieve the `ob_size` field belonging to *o*.

Changed in version 3.11: `Py_SIZE()` now becomes a static inline function, and its parameter no longer has the const PyVarObject* type.

 void Py_SET_SIZE(PyVarObject *o, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size)

Assign *size* to the `ob_size` field belonging to *o*.

Added in version 3.9.

 PyObject_HEAD_INIT(type)

This macro produces the initializer values needed for a fresh `PyObject` type. It expands to:

```c
_PyObject_EXTRA_INIT
1, type,

```

 PyVarObject_HEAD_INIT(type, size)

This macro produces the initializer values needed for a fresh `PyVarObject` type, the `ob_size` field included. It expands to:

```c
_PyObject_EXTRA_INIT
1, type, size,

```

[Subject index](INDEX.md) · [Owning C API section and shared conditions](base-object-types-and-macros.md) · [Owning structure and shared ABI conditions](pyvarobject-to-py-isfalse.md) · [Following source contract](pycfunction.md)

# object structures C API: `PyObject`

type PyObject

* Part of the [Limited API](https://docs.python.org/3.14/c-api/stable.html#stable). (Only some members are part of the stable ABI.)*

Every object type builds on top of this one. It bundles the data that lets Python view a pointer to an object as exactly that ? an object. Within an ordinary "release" build, all it holds is the reference count for the object plus a pointer back to its type object. No variable is ever literally declared as a `PyObject`, yet any pointer aimed at a Python object can be cast to a PyObject*.

Never reach for the members directly; rely on macros instead, such as [`Py_REFCNT`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_REFCNT) and `Py_TYPE`.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) ob_refcnt

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This holds the object's reference count, the same value [`Py_REFCNT`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_REFCNT) hands back. Rather than touching the field yourself, go through functions and macros like `Py_REFCNT`, [`Py_INCREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_INCREF) and [`Py_DecRef()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DecRef).

Depending on how the build is configured and which platform you target, this field's type can differ from `Py_ssize_t`.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *ob_type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This is the type of the object. Don't read the field directly; reach for `Py_TYPE` and `Py_SET_TYPE()` instead.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](base-object-types-and-macros.md) · [Following source contract](pyvarobject-to-py-isfalse.md)

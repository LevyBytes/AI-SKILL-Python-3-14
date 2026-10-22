# Built-in descriptors

### Built-in descriptors

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PySuper_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The type object behind super objects. On the Python side this is one and the same as [`super`](https://docs.python.org/3.14/library/functions.html#super).

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyClassMethod_Type

The type that class method objects have. Over in Python this is identical to [`classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod).

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyClassMethodDescr_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The type object behind class method descriptor objects at the C level. It is the type given to the descriptors built for [`classmethod()`](https://docs.python.org/3.14/library/functions.html#classmethod) declared inside C extension types, and in Python it is the very same object as [`classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyClassMethod_New([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *callable)

Build a fresh [`classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod) object that wraps *callable*. The *callable* you pass has to itself be callable and cannot be `NULL`.

When it succeeds, the call yields a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to a newly made class method descriptor. When it fails, the call yields `NULL` and leaves an exception set.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyStaticMethod_Type

The type that static method objects have. Over in Python this is identical to [`staticmethod`](https://docs.python.org/3.14/library/functions.html#staticmethod).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyStaticMethod_New([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *callable)

Build a fresh [`staticmethod`](https://docs.python.org/3.14/library/functions.html#staticmethod) object that wraps *callable*. The *callable* you pass has to itself be callable and cannot be `NULL`.

When it succeeds, the call yields a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to a newly made static method descriptor. When it fails, the call yields `NULL` and leaves an exception set.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyproperty-type-to-pywrapper-new.md)

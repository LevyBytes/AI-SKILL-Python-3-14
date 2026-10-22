# Range Objects

### Range Objects

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyRange_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The type object backing [`range`](https://docs.python.org/3.14/library/stdtypes.html#range) objects.

 int PyRange_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Yields true when the object *o* is a [`range`](https://docs.python.org/3.14/library/stdtypes.html#range) instance. This function always succeeds.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyseqiter-type-to-pycalliter-new.md) · [Following source contract](builtin-iterator-types.md)

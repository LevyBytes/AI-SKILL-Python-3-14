# Type check macros

### Type check macros

 int PyByteArray_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Yields true whenever *o* is either a bytearray itself or belongs to a class derived from the bytearray type; the call can never fail.

 int PyByteArray_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Gives true only when *o* is exactly a bytearray and not drawn from any subclass of that type; this check always returns without error.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pybytearrayobject-to-pybytearray-type.md) · [Following source contract](pybytearray-fromobject-to-pybytearray-resize.md)

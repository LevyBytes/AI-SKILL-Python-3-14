# Ellipsis Object

### Ellipsis Object

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyEllipsis_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The type of the Python [`Ellipsis`](https://docs.python.org/3.14/library/constants.html#Ellipsis) object. The same as [`types.EllipsisType`](https://docs.python.org/3.14/library/types.html#types.EllipsisType) at the Python layer.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *Py_Ellipsis

The Python `Ellipsis` object. There are no methods on this object. As with [`Py_None`](https://docs.python.org/3.14/c-api/none.html#c.Py_None), it is an [immortal](https://docs.python.org/3.14/glossary.html#term-immortal) singleton object.

Changed in version 3.12: `Py_Ellipsis` is immortal.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyslice-type-to-pyslice-unpack.md) · [Previous source contract](pyslice-adjustindices.md)

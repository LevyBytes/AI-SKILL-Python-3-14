# Byte Array Objects

## Byte Array Objects

### Byte Array Objects

 type PyByteArrayObject

A Python bytearray value is modeled in C by this [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) subtype.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyByteArray_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

At the C level this [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) stands in for the bytearray type, and it is identical to [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) as seen from Python code.

[Subject index](INDEX.md) · [Previous source contract](../orientation/overview.md) · [Following source contract](pybytearray-check-to-pybytearray-checkexact.md)

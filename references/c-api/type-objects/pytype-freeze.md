# int PyType_Freeze(PyTypeObject *type)

int PyType_Freeze(PyTypeObject *type)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.14.*
Render a type immutable by switching on the [`Py_TPFLAGS_IMMUTABLETYPE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE) flag.

Immutability is required of every base class belonging to *type*.

A `0` comes back when this works. Should it fail, raise an exception and hand back `-1`.

Do not touch the type until after it has become immutable. As an illustration, no instances of the type may be built ahead of the type turning immutable.

Added in version 3.14.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytype-frommetaclass-to-pytype-fromspec.md) · [Previous source contract](pytype-spec.md)

# type Py_UCS4 / type Py_UCS2 / type Py_UCS1

type Py_UCS4

 type Py_UCS2

 type Py_UCS1

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

These are typedefs naming unsigned integer types large enough to hold characters of 32, 16, and 8 bits, in that order. For a lone Unicode character, reach for `Py_UCS4`.

Added in version 3.3.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyunicode-type-to-pyunicodeiter-type.md) · [Following source contract](pyasciiobject-to-pyunicode-write.md)

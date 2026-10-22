# Macro definition utilities

#### Macro definition utilities

 Py_FORCE_EXPANSION(X)

Equivalent to `*X*`, handy for token-pasting within macros, since the preprocessor forcefully evaluates any macro expansions found in *X*.

 Py_STRINGIFY(x)

Turns `x` into a C string. For instance, `Py_STRINGIFY(123)` yields `"123"`.

Added in version 3.4.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-unused-to-py-gcc-attribute.md) · [Previous source contract](py-array-length-to-py-member-size.md) · [Following source contract](py-always-inline-to-pyapi-data.md)

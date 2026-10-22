# Python 3.12.0 alpha 1 / core and builtins / opaque interpreter frame fields

[gh-96237](https://github.com/python/cpython/issues/96237): The internal field `_PyInterpreterFrame.f_func` was renamed to `_PyInterpreterFrame.f_funcobj` and is permitted to hold any object. The `f_globals` and `f_builtin` fields are allowed to contain junk values.

The safest course is to regard the `_PyInterpreterFrame` struct as opaque.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

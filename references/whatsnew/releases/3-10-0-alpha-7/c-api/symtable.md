# Python 3.10.0 alpha 7 / c api / symtable

[bpo-43244](https://bugs.python.org/issue?@action=redirect&bpo=43244): Delete the `symtable.h` header file together with these undocumented functions:

  - `PyST_GetScope()`

  - `PySymtable_Build()`

  - `PySymtable_BuildObject()`

  - `PySymtable_Free()`

  - `Py_SymtableString()`

  - `Py_SymtableStringObject()`

By mistake the `Py_SymtableString()` function belonged to the stable ABI, yet it was unusable, since the `symtable.h` header file fell outside the limited C API.

The Python [`symtable`](https://docs.python.org/3.14/library/symtable.html#module-symtable) module stays available and is left unchanged.

Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

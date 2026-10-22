# object structures C API: Shared object headers and layout macros

### Base object types and macros

At the start of every Python object's in-memory layout sits a handful of fields shared by all of them. The `PyObject` and `PyVarObject` types carry these fields, and those two are themselves built from macro expansions that ? directly or by way of other macros ? appear in how every remaining Python object is declared. You can find more macros over at [reference counting](https://docs.python.org/3.14/c-api/refcounting.html#countingrefs).

[Subject index](INDEX.md) · [Previous source contract](common-object-structures.md) · [Following source contract](pyobject-to-ob-refcnt.md)

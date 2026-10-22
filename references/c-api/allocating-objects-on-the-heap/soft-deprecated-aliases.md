# Soft-deprecated aliases

### Soft-deprecated aliases

[Soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) since version 3.10.

The entries below are simply aliases pointing at functions and macros that already exist, kept around only to preserve backwards compatibility.

| Soft-deprecated alias | Function |
| --- | --- |
| PyObject_NEW(type, typeobj) | `PyObject_New` |
| PyObject_NEW_VAR(type, typeobj, n) | `PyObject_NewVar` |
| PyObject_INIT(op, typeobj) | `PyObject_Init()` |
| PyObject_INIT_VAR(op, typeobj, n) | `PyObject_InitVar()` |
| PyObject_MALLOC(n) | `PyObject_Malloc()` |
| PyObject_REALLOC(p, n) | `PyObject_Realloc()` |
| PyObject_FREE(p) | `PyObject_Free()` |
| PyObject_DEL(p) | `PyObject_Free()` |
| PyObject_Del(p) | `PyObject_Free()` |

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyobject-new-to-pytype-genericalloc.md) · [Previous source contract](pyobject-newvar-to-py-nonestruct.md) · [Following source contract](../api-and-abi-versioning/build-time-version-constants.md)

# Deprecated aliases

### Deprecated aliases

The following are [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) aliases pointing at functions and macros that already exist. Their only reason for being is backwards compatibility.

| Deprecated alias | Corresponding function or macro |
| --- | --- |
| PyMem_MALLOC(size)?? | `PyMem_Malloc()` |
| PyMem_NEW(type, size)?? | `PyMem_New` |
| PyMem_REALLOC(ptr, size)?? | `PyMem_Realloc()` |
| PyMem_RESIZE(ptr, type, size)?? | `PyMem_Resize` |
| PyMem_FREE(ptr)?? | `PyMem_Free()` |
| PyMem_DEL(ptr)?? | `PyMem_Free()` |

Changed in version 3.4: These macros have become aliases for their matching functions and macros. Earlier on, they acted identically, yet relying on them gave no guarantee of binary compatibility from one Python version to the next.

Deprecated since version 2.0.

[Subject index](INDEX.md) · [Previous source contract](pymem-malloc-to-pymem-del.md) · [Following source contract](pyobject-malloc-to-pyobject-newvar.md)

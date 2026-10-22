# What's New In Python 3.0 / Build and C API Changes

### Build and C API Changes

With time being short, what follows is a decidedly partial rundown of the C API revisions.

- A number of platforms lost their support, among them Mac OS 9, BeOS, RISCOS, Irix, and Tru64, to name only some.

- [**PEP 3118**](https://peps.python.org/pep-3118/): New Buffer API.

- [**PEP 3121**](https://peps.python.org/pep-3121/): Extension Module Initialization & Finalization.

- [**PEP 3123**](https://peps.python.org/pep-3123/): Making [`PyObject_HEAD`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject_HEAD) conform to standard C.

- No more C API support for restricted execution.

- `PyNumber_Coerce()`, `PyNumber_CoerceEx()`, `PyMember_Get()`, and `PyMember_Set()` C APIs are removed.

- A new C API entry, [`PyImport_ImportModuleNoBlock()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModuleNoBlock), behaves much like [`PyImport_ImportModule()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModule) except that it refuses to wait on the import lock, handing back an error in that situation.

- The C-level slot and method handling boolean conversion got a new name: `nb_nonzero` is these days called `nb_bool`.

- Removed `METH_OLDARGS` and `WITH_CYCLE_GC` from the C API.

[Subject index](INDEX.md) · [Previous source section](builtins.md) · [Next source section](performance.md) · [Release/subject declaration](common-stumbling-blocks.md)

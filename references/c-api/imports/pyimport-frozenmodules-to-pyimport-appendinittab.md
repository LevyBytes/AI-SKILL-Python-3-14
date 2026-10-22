# imports C API: `PyImport_AppendInittab()`

struct _frozen

This is the structure type definition describing frozen module descriptors, as produced by the **freeze** utility (refer to `Tools/freeze/` within the Python source distribution). You can find its definition inside `Include/import.h`:

```c
struct _frozen {
    const char *name;
    const unsigned char *code;
    int size;
    bool is_package;
};

```

Changed in version 3.11: a freshly added `is_package` field records whether or not the module counts as a package. Previously that distinction was conveyed by giving the `size` field a negative value.

 const struct _frozen *PyImport_FrozenModules

At startup this pointer is set to reference an array of `_frozen` records, the last of which has every member equal to `NULL` or zero. Importing a frozen module triggers a search through this table. Third-party code might exploit this mechanism to supply a collection of frozen modules built up at runtime.

 int PyImport_AppendInittab(const char *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *(*initfunc)(void))

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Append one module to the table of built-in modules already present. Acting as a convenience wrapper over `PyImport_ExtendInittab()`, it returns `-1` when the table couldn't be extended. The added module becomes importable under the name *name*, with the function *initfunc* serving as the initialization function fired on the first import attempt. Make this call before [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize).

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyimport-importmodule-to-pyimport-addmoduleref.md) · [Previous source contract](pyimport-getmodule-to-pyimport-importfrozenmodule.md) · [Following source contract](name-to-pyimport-importmoduleattrstring.md)

# imports C API: `PyImport_GetModule()`, `PyImport_GetImporter()`, `PyImport_ImportFrozenModuleObject()`, `PyImport_ImportFrozenModule()`

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyImport_GetModule([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *name)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.8.*

Yield the module bearing the supplied name that has already been imported. Should the module not yet be imported, this returns `NULL` without setting an error. It returns `NULL` and sets an error when the lookup itself fails.

Added in version 3.7.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyImport_GetImporter([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *path)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yield a finder object for a [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path)/`pkg.__path__` item *path*, perhaps by pulling it out of the [`sys.path_importer_cache`](https://docs.python.org/3.14/library/sys.html#sys.path_importer_cache) dict. When it isn't already cached, walk through [`sys.path_hooks`](https://docs.python.org/3.14/library/sys.html#sys.path_hooks) until some hook turns up that is capable of handling the path item. Should none be capable, return `None`; that signals to our caller that the [path based finder](https://docs.python.org/3.14/glossary.html#term-path-based-finder) was unable to locate a finder for this path item. Store the outcome in `sys.path_importer_cache`. Yield a new reference to the finder object.

 int PyImport_ImportFrozenModuleObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *name)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Load a frozen module called *name*. The return is `1` on success, `0` should the module go unfound, and `-1` (with an exception set) when initialization breaks down. After a load succeeds, call `PyImport_ImportModule()` to obtain the imported module. (The name misleads: this routine would re-load a module that was already imported.)

Added in version 3.3.

Changed in version 3.4: the module no longer has its `__file__` attribute assigned.

 int PyImport_ImportFrozenModule(const char *name)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Behaves like `PyImport_ImportFrozenModuleObject()`, except the name arrives as a UTF-8 encoded string rather than a Unicode object.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyimport-importmodule-to-pyimport-addmoduleref.md) · [Previous source contract](pyimport-addmoduleobject-to-pyimport-getmoduledict.md) · [Following source contract](pyimport-frozenmodules-to-pyimport-appendinittab.md)

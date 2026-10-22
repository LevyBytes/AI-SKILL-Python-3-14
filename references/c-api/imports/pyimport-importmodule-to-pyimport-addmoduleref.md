# imports C API: Importing modules and registering module objects

# Import

### Importing Modules

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyImport_ImportModule(const char *name)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A thin wrapper over `PyImport_Import()` whose argument is a const char* rather than a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyImport_ImportModuleNoBlock(const char *name)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Treat this as a deprecated alias that simply forwards to `PyImport_ImportModule()`.

Changed in version 3.3: Previously this routine would bail out at once whenever a different thread held the import lock. Starting with Python 3.3, however, locking moved to per-module locks for most situations, which removed the need for this function's special handling.

Deprecated since version 3.13, will be removed in version 3.15: switch over to `PyImport_ImportModule()`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyImport_ImportModuleEx(const char *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *globals, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *locals, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *fromlist)

*Return value: New reference.*

Import a module. The clearest explanation comes from comparing it with the built-in Python function [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__).

What you get back is a fresh reference to either the imported module or the top-level package, or else `NULL` accompanied by a set exception when the call fails. As with [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__), asking for a submodule of a package usually yields the top-level package, except when a non-empty *fromlist* is supplied.

When imports fail, partially built module objects are discarded, just as `PyImport_ImportModule()` does.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyImport_ImportModuleLevelObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *globals, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *locals, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *fromlist, int level)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Import a module. Again, the best reference point is the built-in Python function [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__), since the standard `__import__()` function delegates straight to this one.

What you get back is a fresh reference to either the imported module or the top-level package, or else `NULL` accompanied by a set exception when the call fails. As with [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__), asking for a submodule of a package usually yields the top-level package, except when a non-empty *fromlist* is supplied.

Added in version 3.3.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyImport_ImportModuleLevel(const char *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *globals, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *locals, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *fromlist, int level)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Behaves like `PyImport_ImportModuleLevelObject()`, except the name arrives as a UTF-8 encoded string rather than a Unicode object.

Changed in version 3.3: a *level* given as a negative value is now rejected.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyImport_Import([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *name)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A higher-level entry point that invokes the active "import hook function" (passing an explicit *level* of 0, which signals an absolute import). It reaches the [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__) function via the `__builtins__` belonging to the current globals. As a result, the import respects whichever import hooks are active in the present environment.

Imports done through this function are always absolute.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyImport_ReloadModule([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *m)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Reload a module. Hand back a fresh reference to the reloaded module, or `NULL` plus a set exception on failure (in which case the module remains in existence).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyImport_AddModuleRef(const char *name)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Hand back the module object tied to a given module name.

The *name* argument can take the form `package.module`. The routine first consults the modules dictionary for an existing entry, and when none is found it builds a fresh one and stores it in that dictionary.

On success, return a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to the module. On failure, return `NULL` with an exception set.

UTF-8 is the encoding from which the module name *name* is decoded.

Note that this routine neither loads nor imports the module; when the module hasn't already been loaded, what comes back is an empty module object. To actually import a module, reach for `PyImport_ImportModule()` or one of its relatives. Any package structures suggested by a dotted *name* go uncreated unless they already exist.

Added in version 3.13.

[Subject index](INDEX.md) · [Following source contract](pyimport-addmoduleobject-to-pyimport-getmoduledict.md)

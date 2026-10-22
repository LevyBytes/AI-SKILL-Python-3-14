# imports C API: Module registration, code execution and import metadata

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyImport_AddModuleObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *name)

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Behaves like `PyImport_AddModuleRef()`, but it yields a [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) and *name* is a Python [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object.

Added in version 3.3.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyImport_AddModule(const char *name)

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Behaves like `PyImport_AddModuleRef()`, but it yields a [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyImport_ExecCodeModule(const char *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *co)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Supply a module name (which may look like `package.module`) together with a code object — read from a Python bytecode file or produced by the built-in function [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) — and this loads the module. It returns a fresh reference to the module object, or `NULL` with an exception set should something go wrong. On any error, *name* gets pulled out of [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules), even when *name* was already present in `sys.modules` at the moment `PyImport_ExecCodeModule()` was entered. Allowing half-initialized modules to linger in `sys.modules` is risky, because anything importing those modules has no means of detecting that the module object sits in an unknown (and likely broken, relative to what the module author intended) condition.

The module's [`__spec__`](https://docs.python.org/3.14/reference/datamodel.html#module.__spec__) and [`__loader__`](https://docs.python.org/3.14/reference/datamodel.html#module.__loader__) get populated with suitable values whenever they aren't already set. The spec's loader is assigned the module's `__loader__` when that exists, and otherwise an instance of [`SourceFileLoader`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.SourceFileLoader).

The module's [`__file__`](https://docs.python.org/3.14/reference/datamodel.html#module.__file__) attribute takes the code object's [`co_filename`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_filename). Where it applies, [`__cached__`](https://docs.python.org/3.14/reference/datamodel.html#module.__cached__) gets set as well.

Should the module already be imported, this function reloads it. Consult `PyImport_ReloadModule()` for the way reloading a module is meant to be done.

Whenever *name* refers to a dotted name shaped like `package.module`, any package structures that haven't yet been created remain uncreated.

See also `PyImport_ExecCodeModuleEx()` and `PyImport_ExecCodeModuleWithPathnames()`.

Changed in version 3.12: assigning [`__cached__`](https://docs.python.org/3.14/reference/datamodel.html#module.__cached__) plus [`__loader__`](https://docs.python.org/3.14/reference/datamodel.html#module.__loader__) is now deprecated; consult [`ModuleSpec`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec) for replacements.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyImport_ExecCodeModuleEx(const char *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *co, const char *pathname)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Resembles `PyImport_ExecCodeModule()`, except the module object's [`__file__`](https://docs.python.org/3.14/reference/datamodel.html#module.__file__) attribute is assigned *pathname* whenever that argument is non-`NULL`.

See also `PyImport_ExecCodeModuleWithPathnames()`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyImport_ExecCodeModuleObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *co, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *pathname, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *cpathname)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Resembles `PyImport_ExecCodeModuleEx()`, except the module object's [`__cached__`](https://docs.python.org/3.14/reference/datamodel.html#module.__cached__) attribute is assigned *cpathname* whenever that argument is non-`NULL`. Among the three functions, this one is the recommended choice.

Added in version 3.3.

Changed in version 3.12: assigning [`__cached__`](https://docs.python.org/3.14/reference/datamodel.html#module.__cached__) is now deprecated; consult [`ModuleSpec`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec) for replacements.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyImport_ExecCodeModuleWithPathnames(const char *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *co, const char *pathname, const char *cpathname)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Resembles `PyImport_ExecCodeModuleObject()`, except *name*, *pathname* and *cpathname* arrive as UTF-8 encoded strings. The function additionally tries to derive an appropriate value for *pathname* from *cpathname* whenever the former comes in as `NULL`.

Added in version 3.2.

Changed in version 3.3: when nothing but the bytecode path is supplied, `imp.source_from_cache()` now serves to work out the source path.

Changed in version 3.12: No longer uses the removed `imp` module.

 long PyImport_GetMagicNumber()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yield the magic number used for Python bytecode files (otherwise known as `.pyc` file). That magic number occupies the first four bytes of the bytecode file, laid out in little-endian byte order. Returns `-1` on error.

Changed in version 3.3: Return value of `-1` upon failure.

 const char *PyImport_GetMagicTag()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yield the magic tag string used for [**PEP 3147**](https://peps.python.org/pep-3147/) format Python bytecode file names. Remember that the authoritative value lives at `sys.implementation.cache_tag` and ought to be consulted in place of this function.

Added in version 3.2.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyImport_GetModuleDict()

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yield the dictionary that handles the module administration (otherwise known as `sys.modules`). Bear in mind that this is a per-interpreter variable.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyimport-importmodule-to-pyimport-addmoduleref.md) · [Following source contract](pyimport-getmodule-to-pyimport-importfrozenmodule.md)

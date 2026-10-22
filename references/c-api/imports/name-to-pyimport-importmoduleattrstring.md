# imports C API: Builtin-module initialization table and attribute imports

struct _inittab

A structure that describes one entry within the list of built-in modules. Programs embedding Python may pair an array of these structures with `PyImport_ExtendInittab()` to contribute extra built-in modules. Two members make up the structure:

 const char *name

The module name, as an ASCII encoded string.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *(*initfunc)(void)

Initialization function for a module built into the interpreter.

 int PyImport_ExtendInittab(struct _inittab *newtab)

Append a group of modules to the table of built-in modules. The *newtab* array has to finish with a sentinel entry whose `name` field holds `NULL`; omitting that sentinel may trigger a memory fault. Returns `0` on success or `-1` when there wasn't enough memory to grow the internal table. Should it fail, none of the modules end up added to the internal table. Make this call before [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize).

Whenever Python gets initialized more than once, `PyImport_AppendInittab()` or `PyImport_ExtendInittab()` has to run ahead of each Python initialization.

 struct _inittab *PyImport_Inittab

The built-in module table that Python initialization relies on. Rather than touching it directly, work through `PyImport_AppendInittab()` and `PyImport_ExtendInittab()`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyImport_ImportModuleAttr([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *mod_name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *attr_name)

*Return value: New reference.*

Import the module *mod_name* and get its attribute *attr_name*.

Names must be Python [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) objects.

A helper that pairs `PyImport_Import()` with [`PyObject_GetAttr()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetAttr). For instance, it may raise [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) when the module can't be found, and [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) when the attribute is absent.

Added in version 3.14.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyImport_ImportModuleAttrString(const char *mod_name, const char *attr_name)

*Return value: New reference.*

Behaves like `PyImport_ImportModuleAttr()`, but the names arrive as UTF-8 encoded strings in place of Python [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) objects.

Added in version 3.14.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyimport-importmodule-to-pyimport-addmoduleref.md) · [Previous source contract](pyimport-frozenmodules-to-pyimport-appendinittab.md)

# int PyInitConfig_AddModule(PyInitConfig *config, const char *name, PyObject *(*initfunc)(void))

### Module

 int PyInitConfig_AddModule(PyInitConfig *config, const char *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *(*initfunc)(void))

Register a built-in extension module within the table of built-in modules.

That fresh module becomes importable under the name *name*, and *initfunc* serves as its initialization routine, invoked the first time an import is attempted.

- On success, hand back `0`.

- On error, record an error within *config* and hand back `-1`.

Whenever Python gets initialized more than once, `PyInitConfig_AddModule()` has to run at every Python initialization.

This parallels the [`PyImport_AppendInittab()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_AppendInittab) function.

[Subject index](INDEX.md) · [Previous source contract](pyinitconfig-setint-to-pyinitconfig-setstrlist.md) · [Following source contract](py-initializefrominitconfig.md)

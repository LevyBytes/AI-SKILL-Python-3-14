# Python 3.13.0 beta 1 / core and builtins / modules

[gh-116322](https://github.com/python/cpython/issues/116322): Extension modules can now tell the runtime that they are able to run GIL-free. Multi-phase init modules signal this by supplying `Py_MOD_GIL_NOT_USED` for the `Py_mod_gil` slot, whereas single-phase init modules invoke `PyUnstable_Module_SetGIL(mod, Py_MOD_GIL_NOT_USED)` within their init function.

[gh-117953](https://github.com/python/cpython/issues/117953): The very first time a builtin or extension module gets imported while a subinterpreter is running, the main interpreter now executes that module's init function before the import proceeds in the subinterpreter. As a result, single-phase init modules now fail within an isolated subinterpreter without ever running their init function under that interpreter; previously the init would run beneath the subinterpreter *before* failing, which risked leaving global state and callbacks behind and otherwise placing the module into an inconsistent state.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# The Module’s Method Table and Initialization Function - PyStatus, PyConfig, PyConfig_InitPythonConfig, Py_Initialize, PyImport_AppendInittab, PyInit_spam, PyConfig_SetBytesString, PyStatus_Exception, Py_InitializeFromConfig, PyConfig_Clear, PyObject, PyImport_ImportModule, PyErr_Print, Py_ExitStatusException, Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED

The complete program is in the [upstream source](https://docs.python.org/3.14/extending/extending.html#the-module-s-method-table-and-initialization-function).

Note

Declaring a global variable, or a local static one, can expose the module to unwanted side-effects upon re-initialisation — for example when entries get pulled from `sys.modules`, or when compiled modules are imported into several interpreters inside one process (or after a `fork()` with no `exec()` in between). When the module state has not yet been fully [isolated](https://docs.python.org/3.14/howto/isolating-extensions.html#isolating-extensions-howto), authors should think about flagging the module as offering no subinterpreter support (through [`Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED`](https://docs.python.org/3.14/c-api/module.html#c.Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED)).

The Python source distribution ships a fuller example module at `Modules/xxlimited.c`. You can adopt that file as a template or just study it as an example.

[Subject index](INDEX.md) · [Previous source section](method-tables-and-initialization-registration.md) · [Next source section](compilation-and-linkage.md) · [Owning section and setup](method-tables-and-initialization-registration.md)

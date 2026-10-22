# The Module’s Method Table and Initialization Function — PyStatus, PyConfig, PyConfig_InitPythonConfig, Py_Initialize, PyImport_AppendInittab, PyInit_spam, PyConfig_SetBytesString, PyStatus_Exception, Py_InitializeFromConfig, PyConfig_Clear, PyObject, PyImport_ImportModule, PyErr_Print, Py_ExitStatusException, Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED

```c
#define PY_SSIZE_T_CLEAN
#include <Python.h>

int
main(int argc, char *argv[])
{
    PyStatus status;
    PyConfig config;
    PyConfig_InitPythonConfig(&config);

    /* Add a built-in module, before Py_Initialize */
    if (PyImport_AppendInittab("spam", PyInit_spam) == -1) {
        fprintf(stderr, "Error: could not extend in-built modules table\n");
        exit(1);
    }

    /* Pass argv[0] to the Python interpreter */
    status = PyConfig_SetBytesString(&config, &config.program_name, argv[0]);
    if (PyStatus_Exception(status)) {
        goto exception;
    }

    /* Initialize the Python interpreter.  Required.
       If this step fails, it will be a fatal error. */
    status = Py_InitializeFromConfig(&config);
    if (PyStatus_Exception(status)) {
        goto exception;
    }
    PyConfig_Clear(&config);

    /* Optionally import the module; alternatively,
       import can be deferred until the embedded script
       imports it. */
    PyObject *pmodule = PyImport_ImportModule("spam");
    if (!pmodule) {
        PyErr_Print();
        fprintf(stderr, "Error: could not import module 'spam'\n");
    }

    // ... use Python C API here ...

    return 0;

  exception:
     PyConfig_Clear(&config);
     Py_ExitStatusException(status);
}

```

Note

Declaring a global variable, or a local static one, can expose the module to unwanted side-effects upon re-initialisation — for example when entries get pulled from `sys.modules`, or when compiled modules are imported into several interpreters inside one process (or after a `fork()` with no `exec()` in between). When the module state has not yet been fully [isolated](https://docs.python.org/3.14/howto/isolating-extensions.html#isolating-extensions-howto), authors should think about flagging the module as offering no subinterpreter support (through [`Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED`](https://docs.python.org/3.14/c-api/module.html#c.Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED)).

The Python source distribution ships a fuller example module at `Modules/xxlimited.c`. You can adopt that file as a template or just study it as an example.

[Subject index](INDEX.md) · [Previous source section](method-tables-and-initialization-registration.md) · [Next source section](compilation-and-linkage.md) · [Owning section and setup](method-tables-and-initialization-registration.md)

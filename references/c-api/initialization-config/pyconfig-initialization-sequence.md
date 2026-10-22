# initialization config C API: Interpreter startup and PyStatus handling with PyConfig

### Initialization with PyConfig

Bringing the interpreter up from a filled-in configuration struct is done by calling [`Py_InitializeFromConfig()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig).

It falls to the caller to deal with exceptions (error or exit) by way of `PyStatus_Exception()` and `Py_ExitStatusException()`.

When [`PyImport_FrozenModules()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_FrozenModules), [`PyImport_AppendInittab()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_AppendInittab), or [`PyImport_ExtendInittab()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ExtendInittab) come into play, they have to be assigned or invoked once Python preinitialization is finished but before Python initialization. Where Python gets initialized more than once, `PyImport_AppendInittab()` or `PyImport_ExtendInittab()` has to run ahead of every Python initialization.

The configuration in force (of `PyConfig` type) lives in `PyInterpreterState.config`.

Example setting the program name:

```c
void init_python(void)
{
    PyStatus status;

    PyConfig config;
    PyConfig_InitPythonConfig(&config);

    /* Set the program name. Implicitly preinitialize Python. */
    status = PyConfig_SetString(&config, &config.program_name,
                                L"/path/to/my_program");
    if (PyStatus_Exception(status)) {
        goto exception;
    }

    status = Py_InitializeFromConfig(&config);
    if (PyStatus_Exception(status)) {
        goto exception;
    }
    PyConfig_Clear(&config);
    return;

exception:
    PyConfig_Clear(&config);
    Py_ExitStatusException(status);
}

```

A fuller example that adjusts the default configuration, reads the configuration, and afterward overrides a few parameters. Bear in mind that as of 3.11 many parameters stay uncomputed until initialization, so their values cannot be read back out of the configuration structure. Whatever values you assign before initialize runs are carried through initialization untouched:

[Subject index](INDEX.md) · [Previous source contract](warnoptions-to-pystats.md) · [Following source contract](pyconfig-initialization.md)

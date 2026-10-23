# Very High Level Embedding - PyStatus, PyConfig, PyConfig_InitPythonConfig, PyConfig_SetBytesString, PyStatus_Exception, Py_InitializeFromConfig, PyConfig_Clear, PyRun_SimpleString, Py_FinalizeEx, Py_ExitStatusException, Py_ssize_t, Py_Initialize, PyRun_SimpleFile

### 1.1. Very High Level Embedding

Embedding Python at its most basic means reaching for the very high level interface. That interface aims to run a Python script with no need to deal with the application directly. As an illustration, you could put it to work performing some operation on a file.

```c
#define PY_SSIZE_T_CLEAN
#include <Python.h>

int
main(int argc, char *argv[])
{
    PyStatus status;
    PyConfig config;
    PyConfig_InitPythonConfig(&config);

    /* optional but recommended */
    status = PyConfig_SetBytesString(&config, &config.program_name, argv[0]);
    if (PyStatus_Exception(status)) {
        goto exception;
    }

    status = Py_InitializeFromConfig(&config);
    if (PyStatus_Exception(status)) {
        goto exception;
    }
    PyConfig_Clear(&config);

    PyRun_SimpleString("from time import time,ctime\n"
                       "print('Today is', ctime(time()))\n");
    if (Py_FinalizeEx() < 0) {
        exit(120);
    }
    return 0;

  exception:
     PyConfig_Clear(&config);
     Py_ExitStatusException(status);
}

```

Note

The line `#define PY_SSIZE_T_CLEAN` served to signal that certain APIs should take `Py_ssize_t` rather than `int`. From Python 3.13 onward it is no longer required, yet it stays here for the sake of backward compatibility. Turn to [Strings and buffers](https://docs.python.org/3.14/c-api/arg.html#arg-parsing-string-and-buffers) for an account of this macro.

You ought to set [`PyConfig.program_name`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.program_name) prior to [`Py_InitializeFromConfig()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig) so the interpreter learns where the Python run-time libraries reside. After that, [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize) starts up the Python interpreter, which then runs a hard-coded Python script that prints out the date and time. The [`Py_FinalizeEx()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_FinalizeEx) call subsequently brings the interpreter down, and the program ends. Within an actual program you would likely fetch the Python script from somewhere else — a text-editor routine, a file, or a database, perhaps. Pulling the Python code out of a file is better accomplished with the [`PyRun_SimpleFile()`](https://docs.python.org/3.14/c-api/veryhigh.html#c.PyRun_SimpleFile) function, sparing you the chore of allocating memory and reading in the file's contents.

[Subject index](INDEX.md) · [Previous source section](interpreter-initialization-and-script-execution.md) · [Next source section](beyond-very-high-level-embedding-an-overview.md)

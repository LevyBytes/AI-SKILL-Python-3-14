# Useful macros

### Useful macros

The Python header files declare a number of handy macros. A lot of them sit nearer to wherever they come in handy (consider [`Py_RETURN_NONE`](https://docs.python.org/3.14/c-api/none.html#c.Py_RETURN_NONE), [`PyMODINIT_FUNC`](https://docs.python.org/3.14/c-api/extension-modules.html#c.PyMODINIT_FUNC)). The more broadly useful ones appear here. What follows isn't guaranteed to be exhaustive.

 Py_CAN_START_THREADS

When this macro has been defined, it signals that the present system can spin up threads.

At the moment, every platform CPython supports (according to [**PEP 11**](https://peps.python.org/pep-0011/)) can spin up threads, save for a handful of WebAssembly platforms.

Added in version 3.13.

 Py_GETENV(s)

Behaves like `getenv(*s*)`, except it yields `NULL` whenever [`-E`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-E) appeared on the command line (consult [`PyConfig.use_environment`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.use_environment)).

[Subject index](INDEX.md) · [Previous source contract](include-files.md) · [Following source contract](pydoc-strvar-to-pydoc-var.md)

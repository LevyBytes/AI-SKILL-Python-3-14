# PyInitConfig C API

### Python Initialization Configuration

### PyInitConfig C API

Added in version 3.14.

To bring up Python, call `Py_InitializeFromInitConfig()`.

A bespoke Python program can be authored around the [`Py_RunMain()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_RunMain) function.

Consult also [Initialization, Finalization, and Threads](https://docs.python.org/3.14/c-api/interp-lifecycle.html#initialization).

See also

[**PEP 741**](https://peps.python.org/pep-0741/) "Python Configuration C API".

[Subject index](INDEX.md) · [Following source contract](example.md)

# PyConfig C API

### PyConfig C API

Added in version 3.8.

To bring up Python, use [`Py_InitializeFromConfig()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig) together with the `PyConfig` structure. Preinitialization is done with `Py_PreInitialize()` and the `PyPreConfig` structure.

Configuration comes in two flavors:

- The Python Configuration serves to assemble a tailored Python that acts just like the standard Python. Environment variables and command-line arguments, for example, feed into how Python is set up.

- The Isolated Configuration serves to embed Python within an application. It walls Python off from the surrounding system. As examples, environment variables get ignored, the LC_CTYPE locale stays untouched, and no signal handler is installed.

A bespoke Python program can be authored around the [`Py_RunMain()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_RunMain) function.

Consult also [Initialization, Finalization, and Threads](https://docs.python.org/3.14/c-api/interp-lifecycle.html#initialization).

See also

[**PEP 587**](https://peps.python.org/pep-0587/) "Python Initialization Configuration".

[Subject index](INDEX.md) · [Previous source contract](pyconfig-set.md) · [Following source contract](example.md)

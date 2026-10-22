# PY_BUILTIN_MODULE_CFLAGS

PY_BUILTIN_MODULE_CFLAGS

The compiler flags for compiling a standard library extension module as a built-in module, as is done with the [`posix`](https://docs.python.org/3.14/library/posix.html#module-posix) module.

Default: `$(PY_STDMODULE_CFLAGS) -DPy_BUILD_CORE_BUILTIN`.

Added in version 3.8.

[Subject index](INDEX.md) · [Previous source section](py-core-cflags.md) · [Following source section](purify.md)

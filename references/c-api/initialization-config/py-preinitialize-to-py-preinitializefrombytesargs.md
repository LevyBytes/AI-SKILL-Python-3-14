# Preinitialize Python with PyPreConfig

### Preinitialize Python with PyPreConfig

Preinitializing Python does the following:

- Establishes the Python memory allocators (`PyPreConfig.allocator`)

- Sets up the LC_CTYPE locale ([locale encoding](https://docs.python.org/3.14/glossary.html#term-locale-encoding))

- Establishes the [Python UTF-8 Mode](https://docs.python.org/3.14/library/os.html#utf8-mode) (`PyPreConfig.utf8_mode`)

The active preconfiguration (the `PyPreConfig` type) lives in `_PyRuntime.preconfig`.

Functions to preinitialize Python:

 PyStatus Py_PreInitialize(const PyPreConfig *preconfig)

Preinitialize Python using the *preconfig* preconfiguration.

A non-`NULL` value is required for *preconfig*.

 PyStatus Py_PreInitializeFromBytesArgs(const PyPreConfig *preconfig, int argc, char *const *argv)

Preinitialize Python using the *preconfig* preconfiguration.

Interpret the *argv* command-line arguments (bytes strings) whenever `parse_argv` of *preconfig* is non-zero.

A non-`NULL` value is required for *preconfig*.

[Subject index](INDEX.md) · [Previous source contract](coerce-c-locale-to-utf8-mode.md)

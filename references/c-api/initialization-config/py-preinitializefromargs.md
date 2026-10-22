# PyStatus Py_PreInitializeFromArgs(const PyPreConfig *preconfig, int argc, wchar_t *const *argv)

PyStatus Py_PreInitializeFromArgs(const PyPreConfig *preconfig, int argc, wchar_t *const *argv)

Run Python's preinitialization step driven by the *preconfig* preconfiguration.

When `parse_argv` of *preconfig* holds a non-zero value, the *argv* command line arguments (supplied as wide strings) are parsed.

A `NULL` value for *preconfig* is not permitted.

It falls to the caller to deal with exceptions (whether an error or an exit) via `PyStatus_Exception()` and `Py_ExitStatusException()`.

Under Python Configuration (`PyPreConfig_InitPythonConfig()`), whenever Python starts up with command line arguments, those same arguments need to reach the preinitialization step too, because they influence the pre-configuration such as encodings. As one illustration, the [`-X utf8`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command line option turns on the [Python UTF-8 Mode](https://docs.python.org/3.14/library/os.html#utf8-mode).

You may invoke `PyMem_SetAllocator()` once `Py_PreInitialize()` has run and prior to [`Py_InitializeFromConfig()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig) so as to plug in a custom memory allocator. Invoking it ahead of `Py_PreInitialize()` is also possible provided `PyPreConfig.allocator` carries the value `PYMEM_ALLOCATOR_NOT_SET`.

Routines for Python memory allocation, for instance [`PyMem_RawMalloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_RawMalloc), are off-limits ahead of the Python preinitialization, though a direct call to `malloc()` and `free()` remains safe at any point. Likewise, [`Py_DecodeLocale()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_DecodeLocale) is not to be called before Python preinitialization.

An example that relies on the preinitialization to switch on the [Python UTF-8 Mode](https://docs.python.org/3.14/library/os.html#utf8-mode):

```c
PyStatus status;
PyPreConfig preconfig;
PyPreConfig_InitPythonConfig(&preconfig);

preconfig.utf8_mode = 1;

status = Py_PreInitialize(&preconfig);
if (PyStatus_Exception(status)) {
    Py_ExitStatusException(status);
}

/* at this point, Python speaks UTF-8 */

Py_Initialize();
/* ... use Python API here ... */
Py_Finalize();

```

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-preinitialize-to-py-preinitializefrombytesargs.md) · [Following source contract](pyconfig-to-pyconfig-parse-argv.md)

# int Py_Main(int argc, wchar_t **argv)

int Py_Main(int argc, wchar_t **argv)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The principal program for the standard interpreter, wrapping an entire initialization/finalization cycle plus extra behaviour to read configuration settings from the environment and command line and then run `__main__` according to [Command line](https://docs.python.org/3.14/using/cmdline.html#using-on-cmdline).

It is supplied for programs that want to back the complete CPython command line interface, rather than merely embedding a Python runtime inside a bigger application.

The *argc* and *argv* parameters mirror those handed to a C program's `main()` function, save that the *argv* entries are first converted to `wchar_t` via [`Py_DecodeLocale()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_DecodeLocale). Note too that entries in the argument list may be altered to reference strings other than those originally passed in (though the contents of the strings the argument list points to stay unchanged).

The return value is `2` when the argument list is not a valid Python command line, and otherwise matches that of `Py_RunMain()`.
Expressed using the CPython runtime configuration APIs covered in the [runtime configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config) section (and setting error handling aside), `Py_Main` behaves roughly like the following:

```c
PyConfig config;
PyConfig_InitPythonConfig(&config);
PyConfig_SetArgv(&config, argc, argv);
Py_InitializeFromConfig(&config);
PyConfig_Clear(&config);

Py_RunMain();

```

Typically, embedding code invokes this function *rather than* reaching for `Py_Initialize()`, `Py_InitializeEx()` or `Py_InitializeFromConfig()` on its own, and every setting takes effect just as the rest of this documentation describes. Should you instead call it *after* an earlier runtime initialization API call has run, then which environment and command line configuration settings end up refreshed varies by version (since that hinges on which settings actually permit being changed once they were already assigned during the runtime's first initialization).

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-initialize-to-py-bytesmain.md) · [Previous source contract](py-runmain.md)

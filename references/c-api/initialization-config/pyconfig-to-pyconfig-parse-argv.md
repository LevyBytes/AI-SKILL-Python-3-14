# initialization config C API: PyConfig construction, setters, reading and cleanup

### PyConfig

 type PyConfig

A structure that holds the bulk of the parameters used to configure Python.

Once finished, free the configuration memory by invoking the `PyConfig_Clear()` function.

Structure methods:

 void PyConfig_InitPythonConfig(PyConfig *config)

Set up the configuration using the Python Configuration.

 void PyConfig_InitIsolatedConfig(PyConfig *config)

Set up the configuration using the Isolated Configuration.

 PyStatus PyConfig_SetString(PyConfig *config, wchar_t *const *config_str, const wchar_t *str)

Duplicate the wide character string *str* into `*config_str`.

Preinitialize Python if needed.

 PyStatus PyConfig_SetBytesString(PyConfig *config, wchar_t *const *config_str, const char *str)

Decode *str* via [`Py_DecodeLocale()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_DecodeLocale) and store the outcome in `*config_str`.

Preinitialize Python if needed.

 PyStatus PyConfig_SetArgv(PyConfig *config, int argc, wchar_t *const *argv)

Populate the command line arguments (the `argv` member of *config*) from the *argv* list, which holds wide character strings.

Preinitialize Python if needed.

 PyStatus PyConfig_SetBytesArgv(PyConfig *config, int argc, char *const *argv)

Populate the command line arguments (the `argv` member of *config*) from the *argv* list, which holds bytes strings. The bytes are decoded through [`Py_DecodeLocale()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_DecodeLocale).

Preinitialize Python if needed.

 PyStatus PyConfig_SetWideStringList(PyConfig *config, PyWideStringList *list, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) length, wchar_t **items)

Assign *length* and *items* to the wide string list *list*.

Preinitialize Python if needed.

 PyStatus PyConfig_Read(PyConfig *config)

Load the entire Python configuration.

Any fields that have already been initialized stay as they are.

Beginning with Python 3.11, this function neither computes nor alters the fields used for path configuration.

The `PyConfig_Read()` function processes the `PyConfig.argv` arguments a single time only: after the arguments have been parsed, `PyConfig.parse_argv` becomes `2`. Because the Python arguments get removed from `PyConfig.argv`, a second parse would treat the application's own options as if they were Python options.

Preinitialize Python if needed.

Changed in version 3.10: Parsing of the `PyConfig.argv` arguments now happens only one time, `PyConfig.parse_argv` is assigned `2` once the arguments have been parsed, and parsing occurs only where `PyConfig.parse_argv` is `1`.

Changed in version 3.11: `PyConfig_Read()` stops computing every path, with the result that the fields grouped under Python Path Configuration might not be refreshed until [`Py_InitializeFromConfig()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig) runs.

 void PyConfig_Clear(PyConfig *config)

Free the configuration memory.

The majority of `PyConfig` methods will preinitialize Python where required. Should that happen, the Python preinitialization configuration (`PyPreConfig`) draws from the `PyConfig`. Where configuration fields that overlap with `PyPreConfig` get adjusted, you have to assign them prior to invoking any `PyConfig` method:

- `PyConfig.dev_mode`

- `PyConfig.isolated`

- `PyConfig.parse_argv`

-

[Subject index](INDEX.md) · [Previous source contract](py-preinitializefromargs.md) · [Following source contract](pyconfig-use-environment-to-base-prefix.md)

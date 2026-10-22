# Set Options

### Set Options

The configuration option *name* argument has to be a non-NULL, null-terminated string encoded in UTF-8. Refer to Configuration Options.

A handful of configuration options influence other options. That behavior kicks in only during `Py_InitializeFromInitConfig()`, never through the "Set" functions shown here. As an example, assigning `1` to `dev_mode` will not turn `faulthandler` into `1`.

 int PyInitConfig_SetInt(PyInitConfig *config, const char *name, int64_t value)

Assign an integer-valued configuration option.

- On success, hand back `0`.

- On error, record an error within *config* and hand back `-1`.

 int PyInitConfig_SetStr(PyInitConfig *config, const char *name, const char *value)

Assign a string-valued configuration option from a null-terminated UTF-8 string. A copy of the string is taken.

- On success, hand back `0`.

- On error, record an error within *config* and hand back `-1`.

 int PyInitConfig_SetStrList(PyInitConfig *config, const char *name, size_t length, char *const *items)

Assign a string-list configuration option whose values arrive as an array of UTF-8 strings, each null-terminated. A copy of the string list is taken.

- On success, hand back `0`.

- On error, record an error within *config* and hand back `-1`.

[Subject index](INDEX.md) · [Previous source contract](pyinitconfig-hasoption-to-pyinitconfig-freestrlist.md) · [Following source contract](pyinitconfig-addmodule.md)

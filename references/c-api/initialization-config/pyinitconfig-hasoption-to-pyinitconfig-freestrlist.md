# Get Options

### Get Options

The configuration option *name* argument has to be a non-NULL, null-terminated string encoded in UTF-8. Refer to Configuration Options.

 int PyInitConfig_HasOption(PyInitConfig *config, const char *name)

Check whether the configuration carries an option named *name*.

When the option is present, hand back `1`; if not, hand back `0`.

 int PyInitConfig_GetInt(PyInitConfig *config, const char *name, int64_t *value)

Retrieve an integer-valued configuration option.

- On success, write **value* and hand back `0`.

- On error, record an error within *config* and hand back `-1`.

 int PyInitConfig_GetStr(PyInitConfig *config, const char *name, char **value)

Retrieve a string-valued configuration option as a null-terminated string encoded in UTF-8.

- On success, write **value* and hand back `0`.

- On error, record an error within *config* and hand back `-1`.

When the option is an optional string that has not been set, **value* may end up being `NULL`.

If it isn't `NULL`, the returned string has to be freed via `free(value)` once you're done.

 int PyInitConfig_GetStrList(PyInitConfig *config, const char *name, size_t *length, char ***items)

Retrieve a string-list configuration option in the form of an array of null-terminated UTF-8 strings.

- On success, write **length* and **value* and hand back `0`.

- On error, record an error within *config* and hand back `-1`.

After success, release the string list through `PyInitConfig_FreeStrList(length, items)`.

 void PyInitConfig_FreeStrList(size_t length, char **items)

Release the memory of a string list produced by `PyInitConfig_GetStrList()`.

[Subject index](INDEX.md) · [Previous source contract](pyinitconfig-geterror-to-pyinitconfig-getexitcode.md) · [Following source contract](pyinitconfig-setint-to-pyinitconfig-setstrlist.md)

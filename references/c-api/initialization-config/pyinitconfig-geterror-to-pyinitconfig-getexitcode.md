# Error Handling

### Error Handling

 int PyInitConfig_GetError(PyInitConfig *config, const char **err_msg)

Retrieve the error text associated with *config*.

- When an error is present, point **err_msg* at it and hand back `1`.

- Otherwise, point **err_msg* at `NULL` and hand back `0`.

Error text comes as a string encoded in UTF-8.

Should *config* carry an exit code, render that exit code into an error message.

That error text stays usable up until the next `PyInitConfig` call made with *config*. Freeing the error message is not the caller's responsibility.

 int PyInitConfig_GetExitCode(PyInitConfig *config, int *exitcode)

Retrieve the exit code carried by *config*.

- When *config* holds an exit code, write it to **exitcode* and hand back `1`.

- When *config* lacks an exit code, hand back `0`.

An exit code may be assigned solely by `Py_InitializeFromInitConfig()`, and only when the `parse_argv` option is non-zero.

Setting an exit code happens when command-line parsing fails (exit code `2`) or when a command-line flag requests that the command-line help be shown (exit code `0`).

[Subject index](INDEX.md) · [Previous source contract](pyinitconfig-to-pyinitconfig-free.md) · [Following source contract](pyinitconfig-hasoption-to-pyinitconfig-freestrlist.md)

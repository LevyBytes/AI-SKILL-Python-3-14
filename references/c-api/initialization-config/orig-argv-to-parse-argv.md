# initialization config C API: Original command-line arguments and parsing

PyWideStringList orig_argv

The roster of the original command line arguments handed to the Python executable: [`sys.orig_argv`](https://docs.python.org/3.14/library/sys.html#sys.orig_argv).

Where the `orig_argv` list is empty and `argv` is not a list holding only one empty string, `PyConfig_Read()` duplicates `argv` into `orig_argv` ahead of altering `argv` (when `parse_argv` is non-zero).

See also the `argv` member together with the `Py_GetArgcArgv()` function.

Default: empty list.

Added in version 3.10.

 int parse_argv

Parse command line arguments?

When this is `1`, `argv` is parsed just as ordinary Python parses [command line arguments](https://docs.python.org/3.14/using/cmdline.html#using-on-cmdline), and the Python arguments are stripped out of `argv`.

The `PyConfig_Read()` function processes the `PyConfig.argv` arguments a single time only: after the arguments have been parsed, `PyConfig.parse_argv` becomes `2`. Because the Python arguments get removed from `PyConfig.argv`, a second parse would treat the application's own options as if they were Python options.

Default: `1` in Python mode, `0` in isolated mode.

Changed in version 3.10: The `PyConfig.argv` arguments are now parsed only where `PyConfig.parse_argv` equals `1`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyconfig-to-pyconfig-parse-argv.md) · [Previous source contract](legacy-windows-stdio-to-optimization-level.md) · [Following source contract](parser-debug.md)

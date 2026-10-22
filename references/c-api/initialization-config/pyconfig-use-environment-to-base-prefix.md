# initialization config C API: Argument parsing, safe paths and base installation configuration

`PyConfig.use_environment`

On top of that, when `PyConfig_SetArgv()` or `PyConfig_SetBytesArgv()` comes into play, that method has to run ahead of the others, because the preinitialization configuration hinges on the command line arguments (when `parse_argv` is non-zero).

Whoever calls these methods bears responsibility for dealing with exceptions (an error or an exit) via `PyStatus_Exception()` and `Py_ExitStatusException()`.

Structure fields:

 PyWideStringList argv

Populate the [`sys.argv`](https://docs.python.org/3.14/library/sys.html#sys.argv) command line arguments out of `argv`. Such parameters resemble the ones handed to the program's `main()` function, except that the opening entry ought to name the script file slated to run rather than the executable that hosts the Python interpreter. When no script is going to run, the opening entry of `argv` may be left as an empty string.

Assign `1` to `parse_argv` so that `argv` is parsed in the same fashion as ordinary Python parses Python command line arguments, after which the Python arguments are stripped out of `argv`.

When `argv` is empty, an empty string gets appended so that [`sys.argv`](https://docs.python.org/3.14/library/sys.html#sys.argv) is guaranteed to exist and never end up empty.

Default: `NULL`.

See also the `orig_argv` member.

 int safe_path

When this is zero, `Py_RunMain()` puts a possibly unsafe path at the front of [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) during startup:

- When `argv[0]` matches `L"-m"` (`python -m module`), the current working directory is prepended.

- When a script is being run (`python script.py`), the script's directory is prepended. Should it be a symbolic link, symbolic links are resolved.

- In every other case (`python -c code` and `python`), an empty string is prepended, signifying the current working directory.

Assigned `1` by the [`-P`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-P) command line option together with the [`PYTHONSAFEPATH`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONSAFEPATH) environment variable.

Default: `0` in Python config, `1` in isolated config.

Added in version 3.11.

 wchar_t *base_exec_prefix

[`sys.base_exec_prefix`](https://docs.python.org/3.14/library/sys.html#sys.base_exec_prefix).

Default: `NULL`.

Part of the Python Path Configuration output.

See also `PyConfig.exec_prefix`.

 wchar_t *base_executable

Python base executable: `sys._base_executable`.

Assigned by the `__PYVENV_LAUNCHER__` environment variable.

Derived from `PyConfig.executable` when `NULL`.

Default: `NULL`.

Part of the Python Path Configuration output.

See also `PyConfig.executable`.

 wchar_t *base_prefix

[`sys.base_prefix`](https://docs.python.org/3.14/library/sys.html#sys.base_prefix).

Default: `NULL`.

Part of the Python Path Configuration output.

See also `PyConfig.prefix`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyconfig-to-pyconfig-parse-argv.md) · [Following source contract](buffered-stdio-to-configure-c-stdio.md)

# initialization config C API: Installation prefixes and execution target configuration

wchar_t *prefix

The site-specific directory prefix under which the platform-independent Python files end up installed: [`sys.prefix`](https://docs.python.org/3.14/library/sys.html#sys.prefix).

Default: `NULL`.

Belongs to the Python Path Configuration output.

Consult also `PyConfig.base_prefix`.

 wchar_t *program_name

The program name that seeds `executable` and shows up in the earliest error messages emitted while Python is starting up.

- Under macOS, fall back to the [`PYTHONEXECUTABLE`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONEXECUTABLE) environment variable when it is set.

- Where the `WITH_NEXT_FRAMEWORK` macro is defined, fall back to the `__PYVENV_LAUNCHER__` environment variable when it is set.

- Take `argv[0]` from `argv` whenever it is present and not empty.

- Failing that, use `L"python"` on Windows and `L"python3"` everywhere else.

Default: `NULL`.

Belongs to the Python Path Configuration input.

 wchar_t *pycache_prefix

The directory into which cached `.pyc` files get written: [`sys.pycache_prefix`](https://docs.python.org/3.14/library/sys.html#sys.pycache_prefix).

Established through the [`-X pycache_prefix=PATH`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command line option as well as the [`PYTHONPYCACHEPREFIX`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPYCACHEPREFIX) environment variable, with the command-line option winning out.

Should this be `NULL`, [`sys.pycache_prefix`](https://docs.python.org/3.14/library/sys.html#sys.pycache_prefix) ends up as `None`.

Default: `NULL`.

 int quiet

Quiet mode. Any value above `0` suppresses the copyright and version banner shown when Python launches in interactive mode.

Bumped up by the [`-q`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-q) command line option.

Default: `0`.

 wchar_t *run_command

The value carried by the [`-c`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-c) command line option.

Consumed by [`Py_RunMain()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_RunMain).

Default: `NULL`.

 wchar_t *run_filename

The filename handed over on the command line: the final command line argument that is neither [`-c`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-c) nor [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m). The [`Py_RunMain()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_RunMain) function relies on it.

To illustrate, the `python3 script.py arg` command line leaves it holding `script.py`.

Consult also the `PyConfig.skip_source_first_line` option.

Default: `NULL`.

 wchar_t *run_module

The value carried by the [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) command line option.

Consumed by [`Py_RunMain()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_RunMain).

Default: `NULL`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyconfig-to-pyconfig-parse-argv.md) · [Previous source contract](pathconfig-warnings.md) · [Following source contract](run-presite-to-stdio-errors.md)

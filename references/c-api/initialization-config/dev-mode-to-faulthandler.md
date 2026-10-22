# initialization config C API: Development mode and fault handling configuration

int dev_mode

When non-zero, the [Python Development Mode](https://docs.python.org/3.14/library/devmode.html#devmode) is switched on.

Assigned `1` by the [`-X dev`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) option together with the [`PYTHONDEVMODE`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONDEVMODE) environment variable.

Default: `-1` in Python mode, `0` in isolated mode.

 int dump_refs

Dump Python references?

When non-zero, every object still living at exit is dumped.

Assigned `1` by the [`PYTHONDUMPREFS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONDUMPREFS) environment variable.

Calls for a special build of Python that defines the `Py_TRACE_REFS` macro: refer to the [`configure --with-trace-refs option`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-trace-refs).

Default: `0`.

 wchar_t *dump_refs_file

The filename in which Python references are dumped.

Assigned by the [`PYTHONDUMPREFSFILE`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONDUMPREFSFILE) environment variable.

Default: `NULL`.

Added in version 3.11.

 wchar_t *exec_prefix

The site-specific directory prefix housing the platform-dependent Python files: [`sys.exec_prefix`](https://docs.python.org/3.14/library/sys.html#sys.exec_prefix).

Default: `NULL`.

Part of the Python Path Configuration output.

See also `PyConfig.base_exec_prefix`.

 wchar_t *executable

The absolute path to the executable binary belonging to the Python interpreter: [`sys.executable`](https://docs.python.org/3.14/library/sys.html#sys.executable).

Default: `NULL`.

Part of the Python Path Configuration output.

See also `PyConfig.base_executable`.

 int faulthandler

Enable faulthandler?

When non-zero, [`faulthandler.enable()`](https://docs.python.org/3.14/library/faulthandler.html#faulthandler.enable) is invoked during startup.

Assigned `1` by [`-X faulthandler`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) together with the [`PYTHONFAULTHANDLER`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONFAULTHANDLER) environment variable.

Default: `-1` in Python mode, `0` in isolated mode.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyconfig-to-pyconfig-parse-argv.md) · [Previous source contract](buffered-stdio-to-configure-c-stdio.md) · [Following source contract](filesystem-encoding-to-home.md)

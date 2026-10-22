# initialization config C API: Windows stdio, search paths and optimization configuration

int legacy_windows_stdio

When non-zero, [`io.FileIO`](https://docs.python.org/3.14/library/io.html#io.FileIO) is used rather than `io._WindowsConsoleIO` for [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin), [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout) and [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr).

Assigned `1` whenever the [`PYTHONLEGACYWINDOWSSTDIO`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSSTDIO) environment variable holds a non-empty string.

Offered on Windows only. The `#ifdef MS_WINDOWS` macro serves for Windows specific code.

Default: `0`.

See also the [**PEP 528**](https://peps.python.org/pep-0528/) (Change Windows console encoding to UTF-8).

 int malloc_stats

When non-zero, statistics for the [Python pymalloc memory allocator](https://docs.python.org/3.14/c-api/memory.html#pymalloc) are dumped at exit.

Assigned `1` by the [`PYTHONMALLOCSTATS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONMALLOCSTATS) environment variable.

This option carries no effect should Python be [`configured using the --without-pymalloc option`](https://docs.python.org/3.14/using/configure.html#cmdoption-without-pymalloc).

Default: `0`.

 wchar_t *platlibdir

The platform library directory name: [`sys.platlibdir`](https://docs.python.org/3.14/library/sys.html#sys.platlibdir).

Assigned by the [`PYTHONPLATLIBDIR`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPLATLIBDIR) environment variable.

Default: the value of the `PLATLIBDIR` macro, itself set by the [`configure --with-platlibdir option`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-platlibdir) (default: `"lib"`, or `"DLLs"` on Windows).

Part of the Python Path Configuration input.

Added in version 3.9.

Changed in version 3.11: This macro now serves on Windows to find the standard library extension modules, generally beneath `DLLs`. For compatibility, though, be aware that this value is disregarded for any non-standard layouts, in-tree builds and virtual environments included.

 wchar_t *pythonpath_env

The module search paths ([`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path)) expressed as one string delimited by `DELIM` ([`os.pathsep`](https://docs.python.org/3.14/library/os.html#os.pathsep)).

Assigned by the [`PYTHONPATH`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPATH) environment variable.

Default: `NULL`.

Part of the Python Path Configuration input.

 PyWideStringList module_search_paths

 int module_search_paths_set

The module search paths: [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path).

When `module_search_paths_set` equals `0`, [`Py_InitializeFromConfig()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig) overwrites `module_search_paths` and assigns `module_search_paths_set` the value `1`.

Default: an empty list (`module_search_paths`) and `0` (`module_search_paths_set`).

Part of the Python Path Configuration output.

 int optimization_level

The compilation optimization level:

- `0`: Peephole optimizer, set `__debug__` to `True`.

- `1`: Level 0, remove assertions, set `__debug__` to `False`.

- `2`: Level 1, strip docstrings.

Incremented by the [`-O`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-O) command line option. Assigned the value of the [`PYTHONOPTIMIZE`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONOPTIMIZE) environment variable.

Default: `0`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyconfig-to-pyconfig-parse-argv.md) · [Previous source contract](import-time-to-isolated.md) · [Following source contract](orig-argv-to-parse-argv.md)

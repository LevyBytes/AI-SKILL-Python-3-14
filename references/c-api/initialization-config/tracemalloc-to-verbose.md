# initialization config C API: Allocation tracing, environment use and verbose imports

int tracemalloc

Enable tracemalloc?

When non-zero, invoke [`tracemalloc.start()`](https://docs.python.org/3.14/library/tracemalloc.html#tracemalloc.start) during startup.

Established through the [`-X tracemalloc=N`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command line option together with the [`PYTHONTRACEMALLOC`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONTRACEMALLOC) environment variable.

Default: `-1` in Python mode, `0` in isolated mode.

 int perf_profiling

Turn on Linux `perf` profiler support?

A value of `1` switches on support for the Linux `perf` profiler.

A value of `2` switches on support for the Linux `perf` profiler together with DWARF JIT support.

Turned to `1` by the [`-X perf`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command-line option and the [`PYTHONPERFSUPPORT`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPERFSUPPORT) environment variable.

Turned to `2` by the [`-X perf_jit`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command-line option and the [`PYTHON_PERF_JIT_SUPPORT`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_PERF_JIT_SUPPORT) environment variable.

Default: `-1`.

See also

Refer to [Python support for the Linux perf profiler](https://docs.python.org/3.14/howto/perf_profiling.html#perf-profiling) for further details.

Added in version 3.12.

 wchar_t *stdlib_dir

The directory holding the Python standard library.

Default: `NULL`.

Added in version 3.11.

 int use_environment

Honor [environment variables](https://docs.python.org/3.14/using/cmdline.html#using-on-envvars)?

A value of zero leaves the [environment variables](https://docs.python.org/3.14/using/cmdline.html#using-on-envvars) ignored.

Turned to `0` by the [`-E`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-E) environment variable.

Default: `1` in Python config and `0` in isolated config.

 int use_system_logger

When non-zero, both `stdout` and `stderr` get rerouted to the system log.

Offered solely on macOS 10.12 or newer and on iOS.

Default: `0` (skip the system log) on macOS; `1` on iOS (route to the system log).

Added in version 3.14.

 int user_site_directory

When non-zero, append the user site directory onto [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path).

Turned to `0` by the [`-s`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-s) and [`-I`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-I) command line options.

Turned to `0` by the [`PYTHONNOUSERSITE`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONNOUSERSITE) environment variable.

Default: `1` in Python mode, `0` in isolated mode.

 int verbose

Verbose mode. With a value above `0`, emit a line whenever a module is imported, naming where (a filename or a built-in module) it was loaded from.

At a value of `2` or more, emit a line for every file probed while hunting for a module, and additionally report on module cleanup during exit.

Bumped up by the [`-v`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-v) command line option.

Driven by the value of the [`PYTHONVERBOSE`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONVERBOSE) environment variable.

Default: `0`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyconfig-to-pyconfig-parse-argv.md) · [Previous source contract](run-presite-to-stdio-errors.md) · [Following source contract](warnoptions-to-pystats.md)

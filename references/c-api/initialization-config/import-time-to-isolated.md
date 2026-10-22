# initialization config C API: Import profiling and interpreter isolation

int import_time

>

When `1`, import time is profiled. When `2`, extra output is added that flags when an imported module has already been loaded.

Assigned by the [`-X importtime`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) option together with the [`PYTHONPROFILEIMPORTTIME`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPROFILEIMPORTTIME) environment variable.

Default: `0`.

Changed in version 3.14: Added support for `import_time = 2`

 int inspect

Drop into interactive mode once a script or a command finishes running.

When above `0`, inspect is switched on: where a script arrives as the first argument or the -c option is supplied, interactive mode is entered after the script or command has run, even if [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin) does not look like a terminal.

Incremented by the [`-i`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-i) command line option. Assigned `1` when the [`PYTHONINSPECT`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONINSPECT) environment variable is non-empty.

Default: `0`.

 int install_signal_handlers

Install Python signal handlers?

Default: `1` in Python mode, `0` in isolated mode.

 int interactive

When above `0`, the interactive mode (REPL) is switched on.

Incremented by the [`-i`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-i) command line option.

Default: `0`.

 int int_max_str_digits

Sets the [integer string conversion length limitation](https://docs.python.org/3.14/library/stdtypes.html#int-max-str-digits). An opening value of `-1` signals that the value is drawn from the command line or environment, or else falls back to 4300 ([`sys.int_info.default_max_str_digits`](https://docs.python.org/3.14/library/sys.html#sys.int_info.default_max_str_digits)). A value of `0` switches off the limitation. Anything above zero yet under 640 ([`sys.int_info.str_digits_check_threshold`](https://docs.python.org/3.14/library/sys.html#sys.int_info.str_digits_check_threshold)) is unsupported and raises an error.

Set through the [`-X int_max_str_digits`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command line flag or the [`PYTHONINTMAXSTRDIGITS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONINTMAXSTRDIGITS) environment variable.

Default: `-1` in Python mode. 4300 ([`sys.int_info.default_max_str_digits`](https://docs.python.org/3.14/library/sys.html#sys.int_info.default_max_str_digits)) in isolated mode.

Added in version 3.12.

 int cpu_count

Where the value of `cpu_count` differs from `-1`, it supersedes whatever [`os.cpu_count()`](https://docs.python.org/3.14/library/os.html#os.cpu_count), [`os.process_cpu_count()`](https://docs.python.org/3.14/library/os.html#os.process_cpu_count), and [`multiprocessing.cpu_count()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.cpu_count) would otherwise return.

Set through the `-X cpu_count=*n|default*` command line flag or the [`PYTHON_CPU_COUNT`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_CPU_COUNT) environment variable.

Default: `-1`.

Added in version 3.13.

 int isolated

When above `0`, isolated mode is switched on:

- Assign `1` to `safe_path`: refrain from prepending a possibly unsafe path to [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) during Python startup, for instance the current directory, the script's directory or an empty string.

- Assign `0` to `use_environment`: pay no attention to `PYTHON` environment variables.

- Assign `0` to `user_site_directory`: leave the user site directory out of [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path).

- The Python REPL neither imports [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline) nor activates default readline configuration on interactive prompts.

Assigned `1` by the [`-I`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-I) command line option.

Default: `0` in Python mode, `1` in isolated mode.

See also the Isolated Configuration and `PyPreConfig.isolated`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyconfig-to-pyconfig-parse-argv.md) · [Previous source contract](filesystem-encoding-to-home.md) · [Following source contract](legacy-windows-stdio-to-optimization-level.md)

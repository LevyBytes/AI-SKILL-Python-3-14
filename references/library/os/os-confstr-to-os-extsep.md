# os: `os.confstr()`, `os.confstr_names`, `os.cpu_count()`, `os.getloadavg()`, `os.process_cpu_count()`, `os.sysconf()`, `os.sysconf_names`, `os.curdir`, `os.pardir`, `os.sep`, `os.altsep`, `os.extsep`

### Miscellaneous System Information

 os.confstr(*name*, */*)

Return string-valued system configuration values. *name* names the configuration value to fetch; it may be a string giving the name of a defined system value; such names appear across a number of standards (POSIX, Unix 95, Unix 98, and others). Certain platforms define extra names too. The names the host operating system recognizes show up as the keys of the `confstr_names` dictionary. For configuration variables left out of that mapping, supplying an integer for *name* is accepted as well.

When the configuration value that *name* specifies is not defined, `None` comes back.

When *name* is a string and is not recognized, [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised. When a particular *name* value is unsupported by the host system, even where it appears in `confstr_names`, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised carrying [`errno.EINVAL`](https://docs.python.org/3.14/library/errno.html#errno.EINVAL) for the error number.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

 os.confstr_names

Dictionary that maps names `confstr()` accepts to the integer values the host operating system defines for those names. You can use this to learn the set of names the system recognizes.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

 os.cpu_count()

Return the count of logical CPUs in the **system**. Returns `None` when undetermined.

The `process_cpu_count()` function can be used to obtain the count of logical CPUs that the calling thread of the **current process** may use.

Added in version 3.4.

Changed in version 3.13: Where [`-X cpu_count`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) is supplied or [`PYTHON_CPU_COUNT`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_CPU_COUNT) is set, `cpu_count()` returns the override value *n*.

 os.getloadavg()

Return the count of processes in the system run queue averaged over the past 1, 5, and 15 minutes, or raise [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) when the load average could not be obtained.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

 os.process_cpu_count()

Obtain the count of logical CPUs that the calling thread of the **current process** may use. Returns `None` when undetermined. It may fall below `cpu_count()` depending on the CPU affinity.

The `cpu_count()` function can be used to obtain the count of logical CPUs in the **system**.

Where [`-X cpu_count`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) is supplied or [`PYTHON_CPU_COUNT`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_CPU_COUNT) is set, `process_cpu_count()` returns the override value *n*.

See also the `sched_getaffinity()` function.

Added in version 3.13.

 os.sysconf(*name*, */*)

Return integer-valued system configuration values. When the configuration value that *name* specifies is not defined, `-1` comes back. The remarks about the *name* parameter for `confstr()` hold here too; the dictionary supplying information on the recognized names is `sysconf_names`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

 os.sysconf_names

Dictionary that maps names `sysconf()` accepts to the integer values the host operating system defines for those names. You can use this to learn the set of names the system recognizes.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Changed in version 3.11: Add `'SC_MINSIGSTKSZ'` name.

The data values below back path manipulation operations. They are defined across all platforms.

Higher-level operations on pathnames live in the [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path) module.

 os.curdir

The constant string the operating system uses to denote the current directory. This is `'.'` for Windows and POSIX. Also available via [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path).

 os.pardir

The constant string the operating system uses to denote the parent directory. This is `'..'` for Windows and POSIX. Also available via [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path).

 os.sep

The character the operating system uses to part pathname components. This is `'/'` for POSIX and `'\\'` for Windows. Be aware that knowing this alone is not enough to parse or concatenate pathnames — use [`os.path.split()`](https://docs.python.org/3.14/library/os.path.html#os.path.split) and [`os.path.join()`](https://docs.python.org/3.14/library/os.path.html#os.path.join) — yet it does come in handy now and then. Also available via [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path).

 os.altsep

An alternative character the operating system uses to part pathname components, or `None` where just one separator character exists. This is set to `'/'` on Windows systems whose `sep` is a backslash. Also available via [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path).

 os.extsep

The character that parts the base filename from the extension; take, for instance, the `'.'` in `os.py`. Also available via [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path).

[Subject index](INDEX.md) · [Previous](os-sched-get-priority-min-to-os-sched-getaffinity.md) · [Continue](os-pathsep-to-os-rtld-deepbind.md) · [Owning module, declaration or section: os](os-error-to-os-name.md)

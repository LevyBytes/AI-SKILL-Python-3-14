# sysconfig - Other functions

### Other functions

 sysconfig.get_python_version()

Yields the `MAJOR.MINOR` Python version number as a string. Comparable to `'%d.%d' % sys.version_info[:2]`.

 sysconfig.get_platform()

Yields a string that pins down the platform you are on.

Its main job is to tell platform-specific build directories and platform-specific built distributions apart. As a rule it folds in the OS name and version plus the architecture (as furnished by [`os.uname()`](https://docs.python.org/3.14/library/os.html#os.uname)), though precisely what it carries hinges on the OS; on Linux, for instance, the kernel version matters little.

Sample return values:

Windows:

- win-amd64 (64-bit Windows running on AMD64, also called x86_64, Intel64, and EM64T)

- win-arm64 (64-bit Windows running on ARM64, also called AArch64)

- win32 (everything else: here, sys.platform is what comes back)

POSIX based OS:

- linux-x86_64

- macosx-15.5-arm64

- macosx-26.0-universal2 (macOS running on Apple Silicon or Intel)

- android-24-arm64_v8a

On the remaining non-POSIX platforms it presently hands back nothing more than [`sys.platform`](https://docs.python.org/3.14/library/sys.html#sys.platform).

 sysconfig.is_python_build()

Yields `True` when the Python interpreter in use was compiled from source and is executing from the place it was built, rather than from somewhere produced by, say, `make install` or a binary installer.

 sysconfig.parse_config_h(*fp*[, *vars*])

Reads a file in the `config.h` style.

*fp* is a file-like object aimed at the `config.h`-style file.

What comes back is a dictionary of name/value pairs. Pass an optional dictionary as the second argument and it is used in place of a fresh one, updated with whatever values the file yields.

 sysconfig.get_config_h_filename()

Yields the path to `pyconfig.h`.

 sysconfig.get_makefile_filename()

Yields the path to `Makefile`.

[Subject index](INDEX.md) · [Previous](sysconfig-get-scheme-names-to-sysconfig-get-paths.md) · [Continue](command-line-usage.md) · [Owning module, declaration or section: sysconfig](python-configuration-access-overview.md)

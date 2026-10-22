# Python 3.14.0 alpha 4 / core and builtins / sys

[gh-127970](https://github.com/python/cpython/issues/127970): To compute [`sys.base_prefix`](https://docs.python.org/3.14/library/sys.html#sys.base_prefix), the interpreter now reads the path of the `libpython` runtime library currently loaded into the process. This applies to every platform that ships the [dladdr](https://pubs.opengroup.org/onlinepubs/9799919799/functions/dladdr.html) routine from the UNIX standard — covering Linux, Android, macOS, iOS, FreeBSD, and so on. Windows together with macOS Framework builds already behaved this way.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.12.0 alpha 1 / library / syslog

[gh-98178](https://github.com/python/cpython/issues/98178): Corrects a macOS crash in [`syslog.syslog()`](https://docs.python.org/3.14/library/syslog.html#syslog.syslog) for multi-threaded applications. Because the macOS libc `syslog()` function isn't thread-safe, `syslog.syslog()` stops releasing the GIL around that call. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

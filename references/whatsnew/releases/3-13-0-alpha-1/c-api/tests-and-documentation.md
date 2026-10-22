# Python 3.13.0 alpha 1 / c api / tests and documentation

[gh-108765](https://github.com/python/cpython/issues/108765): The `<unistd.h>` standard header is no longer pulled in by `Python.h`. Include it directly when you need it. As an example, it supplies the functions: `close()`, `getpagesize()`, `getpid()` and `sysconf()`. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

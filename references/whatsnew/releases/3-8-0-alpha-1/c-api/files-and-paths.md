# Python 3.8.0 alpha 1 / c api / files and paths

[bpo-35296](https://bugs.python.org/issue?@action=redirect&bpo=35296): Now `make install` also lays down the internal API: the `Include/internal/*.h` header files.

[bpo-35081](https://bugs.python.org/issue?@action=redirect&bpo=35081): Internal APIs wrapped by `#ifdef Py_BUILD_CORE` moved out of the `Include/*.h` headers into fresh header files `Include/internal/pycore_*.h`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

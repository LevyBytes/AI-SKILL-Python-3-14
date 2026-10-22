# Python 3.14.0 alpha 4 / build / build and platforms

[gh-115765](https://github.com/python/cpython/issues/115765): Generating `configure` now demands GNU Autoconf 2.72. Erlend Aasland authored the patch.

[gh-100384](https://github.com/python/cpython/issues/100384): Treat `unguarded-availability` as an error on macOS builds, which blocks improper references to symbols missing from older releases of the OS.

[gh-128104](https://github.com/python/cpython/issues/128104): Drop the `Py_STRFTIME_C99_SUPPORT` conditionals and instead insist on C99 *[strftime(3)](https://manpages.debian.org/strftime(3))* specifier support when building. Cross-compiles skip the build-time check and simply presume the support exists.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

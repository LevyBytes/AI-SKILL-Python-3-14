# Python 3.12.0 alpha 1 / core and builtins / build and platforms

[gh-84694](https://github.com/python/cpython/issues/84694): Both the `--experimental-isolated-subinterpreters` configure option and the `EXPERIMENTAL_ISOLATED_SUBINTERPRETERS` macro are gone.

[gh-93143](https://github.com/python/cpython/issues/93143): Skips `NULL` checks on uninitialized local variables by working out at compile time which variables are guaranteed to be initialized.

[gh-93841](https://github.com/python/cpython/issues/93841): With a `-enable-pystats` build, the `sys._stats_on()`, `sys._stats_off()`, `sys._stats_clear()` and `sys._stats_dump()` functions are now present so stats can be collected for portions of programs.

[gh-92658](https://github.com/python/cpython/issues/92658): Introduces support for connecting to and binding Hyper-V sockets on Windows Hyper-V hosts as well as guests.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

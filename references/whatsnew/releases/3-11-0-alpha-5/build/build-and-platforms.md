# Python 3.11.0 alpha 5 / build / build and platforms

[bpo-46602](https://bugs.python.org/issue?@action=redirect&bpo=46602): Cleaned up configure.ac so that conftest.c gets truncated instead of appended. That helps in the scenario where the ?rm? of conftest.c does not occur between tests. Knock-on problems like a clobbered SOABI can otherwise follow.

[bpo-46513](https://bugs.python.org/issue?@action=redirect&bpo=46513): **configure** has stopped using the `AC_C_CHAR_UNSIGNED` macro, and `pyconfig.h` no longer defines the reserved symbol `__CHAR_UNSIGNED__`.

[bpo-45925](https://bugs.python.org/issue?@action=redirect&bpo=45925): Move the Windows installer onto SQLite 3.37.2.

[bpo-43112](https://bugs.python.org/issue?@action=redirect&bpo=43112): Recognize musl libc as its own SOABI (tagged as `linux-musl`).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.11.0 alpha 6 / core and builtins / long

[bpo-30496](https://bugs.python.org/issue?@action=redirect&bpo=30496): Repaired a small portability wrinkle in how [`PyLong_FromLong()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromLong) is implemented, plus a fast path for single-digit integers within [`PyLong_FromLongLong()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromLongLong).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

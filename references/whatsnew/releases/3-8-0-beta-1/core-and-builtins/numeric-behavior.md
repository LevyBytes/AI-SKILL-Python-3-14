# Python 3.8.0 beta 1 / core and builtins / numeric behavior

[bpo-26423](https://bugs.python.org/issue?@action=redirect&bpo=26423): Guards against a possible overflow within `wrap_lenfunc()` once `sizeof(long) < sizeof(Py_ssize_t)` (such as 64-bit Windows).

[bpo-36946](https://bugs.python.org/issue?@action=redirect&bpo=36946): Heads off a possible signed integer overflow during slice handling.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

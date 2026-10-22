# Python 3.14.0 alpha 2 / core and builtins / sys

[gh-126018](https://github.com/python/cpython/issues/126018): A crash in [`sys.audit()`](https://docs.python.org/3.14/library/sys.html#sys.audit) that arose when its first argument was not a string and Python had been built in debug mode is now fixed.

[gh-125942](https://github.com/python/cpython/issues/125942): Under Android, the `errors` mode for [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout) switched away from `surrogateescape` over to `backslashreplace`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

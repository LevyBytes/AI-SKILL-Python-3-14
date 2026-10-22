# Python 3.13.0 alpha 1 / core and builtins / sys monitoring

[gh-106897](https://github.com/python/cpython/issues/106897): Introduce a `RERAISE` event into `sys.monitoring`; it fires whenever an exception gets reraised, whether by an explicit bare `raise` statement, or implicitly through an `except` or `finally` block.

[gh-107724](https://github.com/python/cpython/issues/107724): In the pre-release versions of 3.12, up through rc1, the sys.monitoring callback for the `PY_THROW` event lacked the third, exception argument. That omission is now corrected.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

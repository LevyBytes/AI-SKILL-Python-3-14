# Python 3.9.0 alpha 5 / core and builtins / exceptions

[bpo-39871](https://bugs.python.org/issue?@action=redirect&bpo=39871): Fix a potential [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) within `math.{atan2,copysign,remainder}()` whenever the first argument can't be coerced to a [`float`](https://docs.python.org/3.14/library/functions.html#float). Zackery Spytz wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

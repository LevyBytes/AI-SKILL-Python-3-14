# Python 3.14.3 final / core and builtins / io

[gh-142737](https://github.com/python/cpython/issues/142737): Even where [`io.open()`](https://docs.python.org/3.14/library/io.html#io.open) has been lost, tracebacks now show up via fallback mode. The interpreter previously crashed under those conditions. Bartosz Sławecki authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

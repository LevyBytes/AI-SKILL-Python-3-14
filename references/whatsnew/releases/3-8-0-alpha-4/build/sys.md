# Python 3.8.0 alpha 4 / build / sys

[bpo-36465](https://bugs.python.org/issue?@action=redirect&bpo=36465): Debug and release builds are once again ABI compatible: setting the `Py_DEBUG` macro no longer pulls in the `Py_TRACE_REFS` macro, the lone source of ABI incompatibility. You can still turn on `Py_TRACE_REFS` — which supplies the [`sys.getobjects()`](https://docs.python.org/3.14/library/sys.html#sys.getobjects) function plus the [`PYTHONDUMPREFS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONDUMPREFS) environment variable — through the freshly added `./configure --with-trace-refs` build option.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

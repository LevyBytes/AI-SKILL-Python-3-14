# Python 3.8.0 alpha 4 / library / io

[bpo-18748](https://bugs.python.org/issue?@action=redirect&bpo=18748): Within development mode ([`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) `dev`) and in a debug build, the [`io.IOBase`](https://docs.python.org/3.14/library/io.html#io.IOBase) destructor will now record any `close()` exceptions. Such exceptions stay quiet by default in release mode.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

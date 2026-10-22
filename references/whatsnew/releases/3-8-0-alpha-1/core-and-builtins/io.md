# Python 3.8.0 alpha 1 / core and builtins / io

[bpo-34068](https://bugs.python.org/issue?@action=redirect&bpo=34068): Within [`io.IOBase.close()`](https://docs.python.org/3.14/library/io.html#io.IOBase.close), make sure the [`closed`](https://docs.python.org/3.14/library/io.html#io.IOBase.closed) attribute is not assigned while a live exception is present. Patch by Zackery Spytz and Serhiy Storchaka.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

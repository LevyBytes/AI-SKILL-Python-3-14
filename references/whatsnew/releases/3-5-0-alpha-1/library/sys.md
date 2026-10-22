# Python 3.5.0 alpha 1 / library / sys

[bpo-22696](https://bugs.python.org/issue?@action=redirect&bpo=22696): The function [`sys.is_finalizing()`](https://docs.python.org/3.14/library/sys.html#sys.is_finalizing) was added to report whether the interpreter is shutting down.

[bpo-19977](https://bugs.python.org/issue?@action=redirect&bpo=19977): Where the `LC_TYPE` locale equals the POSIX locale (`C` locale), [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin) together with [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout) now apply the `surrogateescape` error handler in place of the `strict` error handler.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

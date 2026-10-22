# Python 3.11.0 alpha 2 / library / contextlib

[bpo-25625](https://bugs.python.org/issue?@action=redirect&bpo=25625): Added a non parallel-safe [`chdir()`](https://docs.python.org/3.14/library/contextlib.html#contextlib.chdir) context manager that switches the current working directory and then puts it back on exit. It is a thin wrapper over [`chdir()`](https://docs.python.org/3.14/library/os.html#os.chdir).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

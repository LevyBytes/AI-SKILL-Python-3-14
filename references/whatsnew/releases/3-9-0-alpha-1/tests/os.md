# Python 3.9.0 alpha 1 / tests / os

[bpo-38502](https://bugs.python.org/issue?@action=redirect&bpo=38502): When running multiprocessing mode (the -jN command line option), test.regrtest now relies on process groups provided they exist: that is, when the [`os.setsid()`](https://docs.python.org/3.14/library/os.html#os.setsid) and [`os.killpg()`](https://docs.python.org/3.14/library/os.html#os.killpg) functions are present.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

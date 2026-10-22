# Python 3.7.0 alpha 3 / c api / removed

[bpo-30697](https://bugs.python.org/issue?@action=redirect&bpo=30697): The `PyExc_RecursionErrorInst` singleton has been removed and `PyErr_NormalizeException()` no longer relies on it. Because that singleton was persistent and its members were never cleared, it could trigger a segfault while the interpreter was finalizing. Refer also to [bpo-22898](https://bugs.python.org/issue?@action=redirect&bpo=22898).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

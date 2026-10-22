# Python 3.6.4 release candidate 1 / c api / pyexc recursionerrorinst singleton dropped pyerr normalizeexception no longer references

[bpo-30697](https://bugs.python.org/issue?@action=redirect&bpo=30697): The `PyExc_RecursionErrorInst` singleton has been dropped and `PyErr_NormalizeException()` no longer references it. Being persistent, that singleton kept members that were never cleared, which could provoke a segfault while the interpreter finalizes. Refer additionally to [bpo-22898](https://bugs.python.org/issue?@action=redirect&bpo=22898).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.6.3 release candidate 1 / core and builtins / text and unicode

[bpo-31291](https://bugs.python.org/issue?@action=redirect&bpo=31291): Repair an assertion failure inside `zipimport.zipimporter.get_data` on Windows whenever the value returned by `pathname.replace('/','\\')` is not a string. Oren Milman wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

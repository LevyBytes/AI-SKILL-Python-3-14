# Python 3.10.0 alpha 2 / core and builtins / memory and lifetimes

[bpo-42143](https://bugs.python.org/issue?@action=redirect&bpo=42143): Corrected the handling of errors while a `PyFunctionObject` is being created, which had led to operations against uninitialized memory. Yonatan Goldschmidt supplied the patch.

[bpo-42150](https://bugs.python.org/issue?@action=redirect&bpo=42150): Closed a potential buffer overflow inside the new parser during its check for continuation lines. Pablo Galindo supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

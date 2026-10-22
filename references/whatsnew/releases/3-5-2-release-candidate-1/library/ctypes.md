# Python 3.5.2 release candidate 1 / library / ctypes

[bpo-24114](https://bugs.python.org/issue?@action=redirect&bpo=24114): An uninitialized variable in `ctypes.util` is fixed. The defect surfaces only on SunOS while the ctypes implementation looks for the `crle` program. Xiang Zhang wrote the patch, and Kees Bos tested it on SunOS.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

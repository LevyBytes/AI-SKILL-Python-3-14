# Python 3.6.0 alpha 1 / library / ctypes

[bpo-24114](https://bugs.python.org/issue?@action=redirect&bpo=24114): Repaired an uninitialized variable inside `ctypes.util`. This defect surfaces only under SunOS while the ctypes implementation hunts for the `crle` program. Xiang Zhang wrote the patch; Kees Bos verified it on SunOS.

[bpo-25498](https://bugs.python.org/issue?@action=redirect&bpo=25498): Repaired a crash arising while garbage-collecting ctypes objects produced by wrapping a memoryview. The defect was a regression dating to 3.5a1. Eryksun's patch served as the basis.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.5.1 release candidate 1 / library / ctypes

[bpo-25498](https://bugs.python.org/issue?@action=redirect&bpo=25498): Corrected a crash while garbage-collecting ctypes objects that were created by wrapping a memoryview. This had been a regression introduced in 3.5a1. The fix builds on a patch from Eryksun.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

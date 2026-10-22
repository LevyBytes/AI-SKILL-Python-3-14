# Python 3.10.0 alpha 2 / library / ctypes

[bpo-41976](https://bugs.python.org/issue?@action=redirect&bpo=41976): Squashed a defect that made [`ctypes.util.find_library()`](https://docs.python.org/3.14/library/ctypes.html#ctypes.util.find_library) hand back `None` when attempting to find a library in an environment where gcc>=9 exists yet `ldconfig` is absent. Pablo Galindo supplied the patch

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

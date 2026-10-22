# Python 3.7.0 alpha 1 / core and builtins / memory and lifetimes

[bpo-29949](https://bugs.python.org/issue?@action=redirect&bpo=29949): A memory usage regression affecting set and frozenset object was fixed.

[bpo-29849](https://bugs.python.org/issue?@action=redirect&bpo=29849): A memory leak triggered when an ImportError is raised mid from-import was fixed.

[bpo-28509](https://bugs.python.org/issue?@action=redirect&bpo=28509): dict.update() stopped allocating an unnecessarily large block of memory.

[bpo-23782](https://bugs.python.org/issue?@action=redirect&bpo=23782): Repaired a potential memory leak in _PyTraceback_Add() along with an exception loss in PyTraceBack_Here().

[bpo-29683](https://bugs.python.org/issue?@action=redirect&bpo=29683): Memory allocation within _PyCode_SetExtra was fixed. Brian Coleman provided the patch.

[bpo-29438](https://bugs.python.org/issue?@action=redirect&bpo=29438): A use-after-free issue in the key sharing dict was fixed.

[bpo-28147](https://bugs.python.org/issue?@action=redirect&bpo=28147): A memory leak in split-table dictionaries was fixed: setattr() must avoid turning a combined table into a split table. INADA Naoki wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

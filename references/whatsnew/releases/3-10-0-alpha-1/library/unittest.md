# Python 3.10.0 alpha 1 / library / unittest

[bpo-29620](https://bugs.python.org/issue?@action=redirect&bpo=29620): [`assertWarns()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertWarns) will no longer throw a `RuntimeException` if reading a module's `__warningregistry__` ends up importing a new module, or if some other thread imports a new module. Patch by Kernc.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

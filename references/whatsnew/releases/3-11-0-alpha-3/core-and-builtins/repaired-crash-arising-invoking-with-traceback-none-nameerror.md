# Python 3.11.0 alpha 3 / core and builtins / repaired crash arising invoking with traceback none nameerror

[bpo-45826](https://bugs.python.org/issue?@action=redirect&bpo=45826): Repaired a crash arising from invoking `.with_traceback(None)` on `NameError`. The situation comes up internally within `unittest.TestCase.assertRaises()`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

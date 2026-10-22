# Python 3.6.3 release candidate 1 / core and builtins / exceptions and tracebacks

[bpo-30597](https://bugs.python.org/issue?@action=redirect&bpo=30597): `print` now reports the expected input within its custom error message whenever it is used as a Python 2 statement. Sanyam Khurana wrote the patch.

[bpo-31418](https://bugs.python.org/issue?@action=redirect&bpo=31418): Repair an assertion failure inside `PyErr_WriteUnraisable()` for an exception whose `__module__` attribute is faulty. Oren Milman wrote the patch.

[bpo-30978](https://bugs.python.org/issue?@action=redirect&bpo=30978): str.format_map() now lets key lookup exceptions propagate. Formerly every exception got swapped for a KeyError exception.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

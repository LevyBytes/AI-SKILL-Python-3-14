# Python 3.7.0 alpha 1 / core and builtins / exceptions and tracebacks

[bpo-30978](https://bugs.python.org/issue?@action=redirect&bpo=30978): Key lookup exceptions are now propagated by str.format_map(). Formerly such an exception got swapped for a KeyError exception.

[bpo-30597](https://bugs.python.org/issue?@action=redirect&bpo=30597): When invoked as a Python 2 statement, `print` now reflects the expected input in its custom error message. Sanyam Khurana provided the patch.

[bpo-28214](https://bugs.python.org/issue?@action=redirect&bpo=28214): Made the exception reporting better for problematic __set_name__ attributes.

[bpo-21578](https://bugs.python.org/issue?@action=redirect&bpo=21578): Corrected the misleading error message produced whenever ImportError is called with invalid keyword args.

[bpo-28203](https://bugs.python.org/issue?@action=redirect&bpo=28203): Corrected the wrong type in the complex(1.0, {2:3}) error message. Soumya Sharma wrote the patch.

[bpo-29159](https://bugs.python.org/issue?@action=redirect&bpo=29159): A regression in bytes(x) when x.__index__() raises Exception was fixed.

[bpo-31418](https://bugs.python.org/issue?@action=redirect&bpo=31418): Within `PyErr_WriteUnraisable()`, an assertion failure was fixed for an exception carrying a faulty `__module__` attribute. Oren Milman provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

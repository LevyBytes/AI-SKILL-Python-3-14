# Python 3.11.0 alpha 1 / core and builtins / exceptions and tracebacks

[bpo-25782](https://bugs.python.org/issue?@action=redirect&bpo=25782): Resolved a bug in which `PyErr_SetObject` would hang if the active exception held a cycle within its context chain.

[bpo-40222](https://bugs.python.org/issue?@action=redirect&bpo=40222): "Zero cost" exception handling.

  - Relies on a lookup table to decide how exceptions get handled.

  - Drops the SETUP_FINALLY and POP_TOP block instructions, removing the runtime cost that try statements carried.

  - Shrinks the frame object by roughly 60%.

Mark Shannon wrote the patch

[bpo-39091](https://bugs.python.org/issue?@action=redirect&bpo=39091): Resolved a crash from passing a non-exception into a generator's `throw()` method. Noah Oxer wrote the patch.

[bpo-44305](https://bugs.python.org/issue?@action=redirect&bpo=44305): Better error message for `try` blocks that lack `except` or `finally` blocks. Pablo Galindo authored the patch.

[bpo-44110](https://bugs.python.org/issue?@action=redirect&bpo=44110): Better `str.__getitem__()` error message

[bpo-44472](https://bugs.python.org/issue?@action=redirect&bpo=44472): Corrected ltrace behaviour while exceptions are raised. Pablo Galindo wrote the patch.

[bpo-43950](https://bugs.python.org/issue?@action=redirect&bpo=43950): Where available, code objects can now expose column information for instructions. Traceback printing draws on this to highlight the expressions that caused errors.

As part of [**PEP 657**](https://peps.python.org/pep-0657/), Pablo Galindo, Batuhan Taskaya, and Ammar Askar contributed this.

[bpo-34013](https://bugs.python.org/issue?@action=redirect&bpo=34013): Broadened the invalid legacy statement custom error message (such as the one raised when "print" is used without parentheses) so it also covers more generic expressions. Pablo Galindo authored this change.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

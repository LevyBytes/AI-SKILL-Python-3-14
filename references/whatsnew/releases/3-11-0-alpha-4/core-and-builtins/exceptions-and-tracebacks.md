# Python 3.11.0 alpha 4 / core and builtins / exceptions and tracebacks

[bpo-46107](https://bugs.python.org/issue?@action=redirect&bpo=46107): Resolve a defect where `ExceptionGroup.split()` along with `ExceptionGroup.subgroup()` failed to carry the exception group’s `__note__` field over to the resulting parts.

[bpo-45711](https://bugs.python.org/issue?@action=redirect&bpo=45711): How the interpreter state stores handled exceptions (a.k.a exc_info, or _PyErr_StackItem) now keeps just the `exc_value` field; both `exc_type` and `exc_traceback` are gone, since each can be obtained from `exc_value`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

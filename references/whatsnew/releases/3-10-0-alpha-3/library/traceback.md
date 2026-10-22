# Python 3.10.0 alpha 3 / library / traceback

[bpo-26389](https://bugs.python.org/issue?@action=redirect&bpo=26389): The [`traceback.format_exception()`](https://docs.python.org/3.14/library/traceback.html#traceback.format_exception), [`traceback.format_exception_only()`](https://docs.python.org/3.14/library/traceback.html#traceback.format_exception_only), and [`traceback.print_exception()`](https://docs.python.org/3.14/library/traceback.html#traceback.print_exception) functions now accept an exception object passed as a positional-only argument.

[bpo-42482](https://bugs.python.org/issue?@action=redirect&bpo=42482): [`TracebackException`](https://docs.python.org/3.14/library/traceback.html#traceback.TracebackException) no longer keeps a reference to the exception's traceback object. As a result, TracebackException instances built from equivalent yet non-equal exceptions now compare equal.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

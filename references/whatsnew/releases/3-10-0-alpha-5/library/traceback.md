# Python 3.10.0 alpha 5 / library / traceback

[bpo-42877](https://bugs.python.org/issue?@action=redirect&bpo=42877): A `compact` parameter joined the constructor of [`traceback.TracebackException`](https://docs.python.org/3.14/library/traceback.html#traceback.TracebackException), cutting time and memory for callers who only ever invoke `TracebackException.format()` and `TracebackException.format_exception_only()`.

[bpo-42848](https://bugs.python.org/issue?@action=redirect&bpo=42848): Took recursion out of [`TracebackException`](https://docs.python.org/3.14/library/traceback.html#traceback.TracebackException) so that lengthy exception chains can be handled.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

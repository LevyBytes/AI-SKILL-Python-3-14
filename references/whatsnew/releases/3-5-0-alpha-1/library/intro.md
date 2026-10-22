# Python 3.5.0 alpha 1 / library / intro

[bpo-21932](https://bugs.python.org/issue?@action=redirect&bpo=21932): For the size argument, os.read() now relies on a [`Py_ssize_t()`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) type rather than int so it can read past 2 GB in one call. The size gets clamped to INT_MAX on Windows. Just like any os.read() invocation, the OS may return fewer bytes than were asked for.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

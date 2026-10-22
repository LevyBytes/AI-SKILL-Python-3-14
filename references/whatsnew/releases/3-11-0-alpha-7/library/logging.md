# Python 3.11.0 alpha 7 / library / logging

[bpo-45171](https://bugs.python.org/issue?@action=redirect&bpo=45171): Handling of the `stacklevel` argument passed to logging functions within the [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) module is fixed so that every logging function treats it the same way, matching, as documented, the `stacklevel` argument that [`warn()`](https://docs.python.org/3.14/library/warnings.html#warnings.warn) accepts.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

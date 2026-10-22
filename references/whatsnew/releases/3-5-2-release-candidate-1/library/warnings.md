# Python 3.5.2 release candidate 1 / library / warnings

[bpo-21925](https://bugs.python.org/issue?@action=redirect&bpo=21925): [`warnings.formatwarning()`](https://docs.python.org/3.14/library/warnings.html#warnings.formatwarning) now traps exceptions from `linecache.getline(...)` so that it can still log a [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning) raised late in the Python shutdown sequence.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.6.0 alpha 1 / library / exceptions

[bpo-21925](https://bugs.python.org/issue?@action=redirect&bpo=21925): So that a [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning) emitted late in the Python shutdown sequence can still be logged, [`warnings.formatwarning()`](https://docs.python.org/3.14/library/warnings.html#warnings.formatwarning) now traps exceptions raised by [`linecache.getline()`](https://docs.python.org/3.14/library/linecache.html#linecache.getline) and [`tracemalloc.get_object_traceback()`](https://docs.python.org/3.14/library/tracemalloc.html#tracemalloc.get_object_traceback).

[bpo-26567](https://bugs.python.org/issue?@action=redirect&bpo=26567): Introduced a new [`PyErr_ResourceWarning()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_ResourceWarning) function for passing along the destroyed object. A *source* attribute was added to `warnings.WarningMessage`, and warnings._showwarnmsg() was added, which leans on tracemalloc to obtain the traceback for where the source object was allocated.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

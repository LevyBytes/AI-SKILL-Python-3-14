# Python 3.13.0 alpha 1 / library / imports and modules

[gh-104780](https://github.com/python/cpython/issues/104780): Deleted the `2to3` program together with the `lib2to3` module, both deprecated in Python 3.11. Victor Stinner authored the change.

[gh-104399](https://github.com/python/cpython/issues/104399): Readied the `_tkinter` module for builds against Tcl 9.0 and an eventual libtommath by swapping out the deprecated `mp_to_unsigned_bin_n()` and `mp_unsigned_bin_size()` functions wherever required.

[gh-75552](https://github.com/python/cpython/issues/75552): Deleted the `tkinter.tix` module, which had been deprecated since Python 3.6.

[gh-106075](https://github.com/python/cpython/issues/106075): Folded `asyncio.taskgroups.__all__` into `asyncio.__all__` so it gets exported by star imports.

[gh-105375](https://github.com/python/cpython/issues/105375): Address bugs within `_datetime` where, on a module initialisation failure, exceptions could be overwritten.

[gh-90876](https://github.com/python/cpython/issues/90876): Stop `multiprocessing.spawn` from failing to *import* wherever `sys.executable` happens to be `None`. The regression landed in 3.11 alongside the new support for path-like objects within multiprocessing.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

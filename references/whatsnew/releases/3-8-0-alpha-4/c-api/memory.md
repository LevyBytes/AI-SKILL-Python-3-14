# Python 3.8.0 alpha 4 / c api / memory

[bpo-36389](https://bugs.python.org/issue?@action=redirect&bpo=36389): Adjust the values of the `CLEANBYTE`, `DEADDYTE` and `FORBIDDENBYTE` internal constants that the debug hooks on Python's memory allocators use (the [`PyMem_SetupDebugHooks()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_SetupDebugHooks) function). The byte patterns `0xCB`, `0xDB` and `0xFB` are swapped for `0xCD`, `0xDD` and `0xFD`, matching the values that Windows CRT's debug `malloc()` and `free()` use.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

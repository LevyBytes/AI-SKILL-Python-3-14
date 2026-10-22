# Python 3.14.4 final / windows / ctypes

[gh-145307](https://github.com/python/cpython/issues/145307): Loading of the `psapi.dll` module is now postponed until [`ctypes.util.dllist()`](https://docs.python.org/3.14/library/ctypes.html#ctypes.util.dllist) actually needs it.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

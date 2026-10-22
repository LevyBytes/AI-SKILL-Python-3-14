# Python next / library / exceptions

[gh-151126](https://github.com/python/cpython/issues/151126): Resolve a segfault on an unset [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) triggered by allocation failure within [`ctypes.get_errno()`](https://docs.python.org/3.14/library/ctypes.html#ctypes.get_errno).

[gh-151126](https://github.com/python/cpython/issues/151126): Repair a segfault occurring when a [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) inside `os._path_splitroot()` had not been configured correctly.

[gh-151126](https://github.com/python/cpython/issues/151126): Repair a segfault, arising once a device has run out of memory, occurring within the `_interpchannels` module.

Going forward it surfaces correct [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) errors.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

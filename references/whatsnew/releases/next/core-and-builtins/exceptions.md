# Python next / core and builtins / exceptions

[gh-151126](https://github.com/python/cpython/issues/151126): Repair a segfault, arising once a device has run out of memory, occurring within the `_interpchannels` module.

Going forward it surfaces correct [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) errors.

[gh-150988](https://github.com/python/cpython/issues/150988): Repair a reference leak within [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) when its attributes get assigned ahead of `super().__init__()`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

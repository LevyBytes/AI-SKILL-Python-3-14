# Python 3.14.6 final / core and builtins / exceptions

[gh-151126](https://github.com/python/cpython/issues/151126): Repair a segfault, arising once a device has run out of memory, occurring within:

  - code compilation - `_winapi.CreateProcess()`

Going forward these spots surface correct [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) errors.

[gh-150700](https://github.com/python/cpython/issues/150700): Repair a [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) thrown while compiling a class-scope comprehension whose `lambda` refers to `__class__`, `__classdict__`, or `__conditional_annotations__`. Bartosz Sławecki authored the change.

[gh-150207](https://github.com/python/cpython/issues/150207): Repair a segfault triggered when a memory allocation fails as the tokenizer initializes. A correct [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) now surfaces instead.

[gh-149805](https://github.com/python/cpython/issues/149805): Repair a [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) thrown while compiling a `__classdict__` class annotation. OSS-Fuzz surfaced this in [#512907042](https://issues.oss-fuzz.com/issues/512907042).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

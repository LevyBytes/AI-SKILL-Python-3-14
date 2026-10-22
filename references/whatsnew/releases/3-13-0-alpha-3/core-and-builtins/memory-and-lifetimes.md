# Python 3.13.0 alpha 3 / core and builtins / memory and lifetimes

[gh-112625](https://github.com/python/cpython/issues/112625): Resolves a defect where a bytearray object might be cleared mid-iteration over an argument inside the `bytearray.join()` method, which could lead to reading memory once it had been freed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

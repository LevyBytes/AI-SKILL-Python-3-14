# Python 3.13.0 alpha 6 / core and builtins / memory and lifetimes

[gh-115776](https://github.com/python/cpython/issues/115776): The values array, namely the `PyDictValues` struct, is now placed inside the object at allocation time. The common case runs faster as a result, and performance holds up better once the object's `__dict__` gets materialized.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

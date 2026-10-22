# Python 3.13.0 alpha 1 / core and builtins / removed

[gh-110309](https://github.com/python/cpython/issues/110309): Pointless empty constant nodes were removed from the ast of f-string specs.

[gh-108035](https://github.com/python/cpython/issues/108035): The `_PyCFrame` struct was removed, returning the pointer to the current interpreter frame back into the threadstate, just as it was for 3.10 and earlier. The `_PyCFrame` had served as a tracing performance optimization. Now that PEP 669 is implemented, that optimization is no longer relevant.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

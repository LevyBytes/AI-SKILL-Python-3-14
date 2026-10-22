# Python 3.14.0 alpha 1 / core and builtins / move python evaluation stack over internal stack references

[gh-117139](https://github.com/python/cpython/issues/117139): Move the Python evaluation stack over to internal stack references. The goal is enabling tagged pointers. Under [**PEP 703**](https://peps.python.org/pep-0703/), that opens the door to its style of deferred reference counting. Across both the default and free-threaded builds, this lays groundwork for future unboxed integers.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

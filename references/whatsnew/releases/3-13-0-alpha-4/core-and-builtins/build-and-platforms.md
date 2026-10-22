# Python 3.13.0 alpha 4 / core and builtins / build and platforms

[gh-112529](https://github.com/python/cpython/issues/112529): In the free-threaded build, objects that participate in cyclic garbage collection no longer reserve room for the `PyGC_Head` structure. Several other fields and structures stand in for it, among them `ob_gc_bits`, `ob_tid`, and mimalloc internal data structures.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

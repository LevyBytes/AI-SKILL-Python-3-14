# Python 3.13.0 alpha 1 / core and builtins / modules

[gh-106176](https://github.com/python/cpython/issues/106176): A `WeakValueDictionary` is now used to keep track of the lists holding the modules each thread is presently importing. That keeps a reference leak from arising by holding the list longer than required. Weakrefs are chosen because GC cannot break into the cleanup.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

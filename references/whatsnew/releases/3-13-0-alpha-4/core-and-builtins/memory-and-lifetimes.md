# Python 3.13.0 alpha 4 / core and builtins / memory and lifetimes

[gh-113055](https://github.com/python/cpython/issues/113055): Turn interp->obmalloc into a pointer. Interpreters that share state with the main interpreter point at the same static memory structure, whereas interpreters holding their own obmalloc state get it heap allocated. Also add free_obmalloc_arenas(), which releases the obmalloc arenas and radix tree structures for interpreters that own their obmalloc state.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

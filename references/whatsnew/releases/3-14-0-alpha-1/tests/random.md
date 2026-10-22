# Python 3.14.0 alpha 1 / tests / random

[gh-121084](https://github.com/python/cpython/issues/121084): Repair random leaks in test_typing. Empty the typing ABC caches during refleak runs (`-R` option): invoke `_abc_caches_clear()` on the typing abstract classes plus their subclasses. Patch by Victor Stinner.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

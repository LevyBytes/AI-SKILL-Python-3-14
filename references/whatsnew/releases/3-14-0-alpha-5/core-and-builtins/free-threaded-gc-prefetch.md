# Python 3.14.0 alpha 5 / core and builtins / free threaded cyclic garbage collector optionally issues cpu prefetch instructions

[gh-129201](https://github.com/python/cpython/issues/129201): The free-threaded cyclic garbage collector now optionally issues CPU prefetch instructions while collecting. Doing so can shorten collection times by raising the odds that data already sits in the CPU cache when it is required. Those prefetch instructions kick in once the count of long-lived objects (the objects that survive a full collection) passes a threshold.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.14.5 release candidate 1 / core and builtins / build and platforms

[gh-142516](https://github.com/python/cpython/issues/142516): Bring the generational cycle garbage collector forward into the default 3.14 build, swapping out the incremental collector while the free-threaded collector stays as it was.

[gh-148284](https://github.com/python/cpython/issues/148284): Curb the large stack usage seen in the CPython interpreter loop under Clang 22, achieved by capping the inlining function thresholds during a computed-gotos build.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

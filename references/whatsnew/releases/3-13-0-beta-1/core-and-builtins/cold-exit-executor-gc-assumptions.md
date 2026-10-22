# Python 3.13.0 beta 1 / core and builtins / ensure executor objects within cold exits array not presumed gc able

[gh-118074](https://github.com/python/cpython/issues/118074): Ensure the Executor objects within the COLD_EXITS array are not presumed GC-able, which would otherwise read bytes lying outside the object.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

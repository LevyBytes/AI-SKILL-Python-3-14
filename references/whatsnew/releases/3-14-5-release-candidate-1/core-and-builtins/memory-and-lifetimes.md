# Python 3.14.5 release candidate 1 / core and builtins / memory and lifetimes

[gh-147998](https://github.com/python/cpython/issues/147998): Sealed a memory leak in interpreter helper calls, so teardown runs even when an operation crosses interpreter boundaries. Maurycy Pawłowski-Wieroński wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

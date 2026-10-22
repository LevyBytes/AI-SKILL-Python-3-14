# Python 3.14.0 alpha 2 / library / collections and iteration

[gh-125789](https://github.com/python/cpython/issues/125789): Repair a potential crash arising from mutating the callbacks list handed back by `asyncio.Future._callbacks`. The C implementation `_asyncio` now hands back a fresh copy every time. Kumar Aditya supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

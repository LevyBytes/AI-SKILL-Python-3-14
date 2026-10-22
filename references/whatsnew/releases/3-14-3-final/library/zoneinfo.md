# Python 3.14.3 final / library / zoneinfo

[gh-143241](https://github.com/python/cpython/issues/143241): [`zoneinfo`](https://docs.python.org/3.14/library/zoneinfo.html#module-zoneinfo): an infinite loop in [`ZoneInfo.from_file`](https://docs.python.org/3.14/library/zoneinfo.html#zoneinfo.ZoneInfo.from_file) while parsing a malformed TZif file is now fixed. Fatih Celik supplied the patch.

[gh-142783](https://github.com/python/cpython/issues/142783): A zoneinfo use-after-free tied to the descriptor _weak_cache is now fixed. Using a descriptor as _weak_cache could provoke crashes during object creation. The fix guarantees correct reference counting for objects supplied by a descriptor.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

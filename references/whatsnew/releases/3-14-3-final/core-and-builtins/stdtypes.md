# Python 3.14.3 final / core and builtins / stdtypes

[gh-142560](https://github.com/python/cpython/issues/142560): Address use-after-free in the search-style [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) methods ([`find()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.find), [`count()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.count), [`index()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.index), [`rindex()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.rindex), and [`rfind()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.rfind)) by flagging the storage as exported, so any reallocation attempt raises [`BufferError`](https://docs.python.org/3.14/library/exceptions.html#BufferError). The same goal is met for [`contains()`](https://docs.python.org/3.14/library/operator.html#operator.contains), [`split()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.split), and [`rsplit()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.rsplit) through the [buffer protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects).

[gh-141805](https://github.com/python/cpython/issues/141805): Fix a [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) crash that could happen when objects sharing a hash are added concurrently to the set, right after an element with that hash was removed, while the set is still holding other elements carrying the same hash.

[gh-143189](https://github.com/python/cpython/issues/143189): Fix a crash that struck when a non-[`str`](https://docs.python.org/3.14/library/stdtypes.html#str) key was inserted into a split table dictionary and that key matched a key already present in the split table yet had no value associated with it in the dict.

[gh-142557](https://github.com/python/cpython/issues/142557): Address a use-after-free crash in [bytearray.__mod__](https://docs.python.org/3.14/library/stdtypes.html#bytes-formatting) that arose when the `bytearray` was changed during formatting of the `%`-style arguments. Bénédikt Tran authored the patch.

[gh-143195](https://github.com/python/cpython/issues/143195): Address use-after-free crashes in [`bytearray.hex()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.hex) and [`memoryview.hex()`](https://docs.python.org/3.14/library/stdtypes.html#memoryview.hex) that occurred when the separator's [`__len__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__len__) altered the original object. Bénédikt Tran authored the patch.

[gh-143003](https://github.com/python/cpython/issues/143003): Address an overflow of the shared empty buffer inside [`bytearray.extend()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.extend) that arose when `__length_hint__()` returned 0 for a non-empty iterator.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

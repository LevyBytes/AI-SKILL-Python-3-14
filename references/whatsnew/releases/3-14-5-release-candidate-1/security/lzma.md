# Python 3.14.5 release candidate 1 / security / lzma

[gh-148395](https://github.com/python/cpython/issues/148395): Resolve a dangling input pointer affecting [`lzma.LZMADecompressor`](https://docs.python.org/3.14/library/lzma.html#lzma.LZMADecompressor), [`bz2.BZ2Decompressor`](https://docs.python.org/3.14/library/bz2.html#bz2.BZ2Decompressor), plus the internal `zlib._ZlibDecompressor`, where a failed allocation raising [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) could leave a later `decompress()` invocation reading or writing through a stale pointer into the already-freed caller buffer.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

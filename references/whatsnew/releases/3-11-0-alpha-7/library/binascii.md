# Python 3.11.0 alpha 7 / library / binascii

[bpo-38256](https://bugs.python.org/issue?@action=redirect&bpo=38256): Repair [`binascii.crc32()`](https://docs.python.org/3.14/library/binascii.html#binascii.crc32), when it is built atop zlib’c crc32, so inputs of 4+GiB length yield the right answer rather than a wrong one. Before the fix, the workaround was either to feed the function chunks under 4GiB or to call the zlib module function directly.

On bigger inputs [`binascii.crc32()`](https://docs.python.org/3.14/library/binascii.html#binascii.crc32) now drops the GIL while it computes, much as [`zlib.crc32()`](https://docs.python.org/3.14/library/zlib.html#zlib.crc32) and [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) already do.

Windows gains here too, since [`binascii.crc32()`](https://docs.python.org/3.14/library/binascii.html#binascii.crc32) now leans on the zlib crc32 implementation for a 2-3x speedup.

Having a crc32 API spread across two stdlib modules is a long-known quirk. This step brings us nearer to one shared implementation behind them.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# lzma — `lzma` — Compression using the LZMA algorithm

# Lzma

### `lzma` — Compression using the LZMA algorithm

Added in version 3.3.

**Source code:** [Lib/lzma.py](https://github.com/python/cpython/tree/3.14/Lib/lzma.py)

---

Here you get classes plus handy helper functions for shrinking and restoring data through the LZMA compression algorithm. A file interface ships alongside them, covering the `.xz` plus legacy `.lzma` formats emitted by the **xz** utility, and raw compressed streams too.

The API surfaced here closely tracks what the [`bz2`](https://docs.python.org/3.14/library/bz2.html#module-bz2) module offers. Keep in mind that both `LZMAFile` and [`bz2.BZ2File`](https://docs.python.org/3.14/library/bz2.html#bz2.BZ2File) are *not* thread-safe; consequently, driving one shared `LZMAFile` object from several threads obliges you to guard it behind a lock.

This counts as an [optional module](https://docs.python.org/3.14/glossary.html#term-optional-module). Should your CPython build lack it, turn to whoever supplied Python to you for the relevant documentation. Anyone acting as that distributor should consult [Requirements for optional modules](https://docs.python.org/3.14/using/configure.html#optional-module-requirements).

 *exception *lzma.LZMAError

Any failure that surfaces mid-compression or mid-decompression — or as the compressor/decompressor state gets initialized — triggers this exception.

[Subject index](INDEX.md) · [Continue](lzma-open.md)

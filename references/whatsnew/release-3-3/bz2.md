# What's New In Python 3.3 / bz2 — bz2, io

### bz2

A complete from-the-ground-up rewrite was done on the [`bz2`](https://docs.python.org/3.14/library/bz2.html#module-bz2) module. Along the way, a number of capabilities were introduced:

- New [`bz2.open()`](https://docs.python.org/3.14/library/bz2.html#bz2.open) function: open a bzip2-compressed file in binary or text mode.

- Through its constructor’s *fileobj* argument, [`bz2.BZ2File`](https://docs.python.org/3.14/library/bz2.html#bz2.BZ2File) is now able to read from, and write to, any file-like object you choose.

(Contributed by Nadeem Vawda in [bpo-5863](https://bugs.python.org/issue?@action=redirect&bpo=5863).)

- Multi-stream inputs (the kind the **pbzip2** tool emits) can now be decompressed by [`bz2.BZ2File`](https://docs.python.org/3.14/library/bz2.html#bz2.BZ2File) and [`bz2.decompress()`](https://docs.python.org/3.14/library/bz2.html#bz2.decompress). Supplying the `'a'` (append) mode also lets `bz2.BZ2File` produce a file of that kind.

(This was contributed by Nir Aides under [bpo-1625](https://bugs.python.org/issue?@action=redirect&bpo=1625).)

- Every part of the [`io.BufferedIOBase`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase) API is now realized by [`bz2.BZ2File`](https://docs.python.org/3.14/library/bz2.html#bz2.BZ2File), save for its `detach()` and `truncate()` methods.

[Subject index](INDEX.md) · [Previous source section](binascii.md) · [Next source section](codecs.md) · [Release/subject declaration](summary-release-highlights.md)

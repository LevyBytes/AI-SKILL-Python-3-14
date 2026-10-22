# Python 3.13.0 alpha 2 / library / mmap

[gh-111835](https://github.com/python/cpython/issues/111835): A [`seekable()`](https://docs.python.org/3.14/library/mmap.html#mmap.mmap.seekable) method is now provided on the [`mmap.mmap`](https://docs.python.org/3.14/library/mmap.html#mmap.mmap) class, useful wherever a seekable file-like object is expected. Its [`seek()`](https://docs.python.org/3.14/library/mmap.html#mmap.mmap.seek) method has been updated to return the resulting absolute position. Donghee Na supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

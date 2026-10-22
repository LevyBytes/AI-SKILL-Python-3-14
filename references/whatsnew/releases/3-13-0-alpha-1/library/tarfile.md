# Python 3.13.0 alpha 1 / library / tarfile

[gh-107845](https://github.com/python/cpython/issues/107845): [`tarfile.data_filter()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.data_filter) now factors in where symlinks sit while working out their target, so it stops rejecting certain valid tarballs with `LinkOutsideDestinationError`.

[gh-102120](https://github.com/python/cpython/issues/102120): Gave `tarfile` a stream mode letting archives be read without caching details about the contained files.

[gh-107811](https://github.com/python/cpython/issues/107811): Within [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile): pulling out members whose UID or GID is excessively large (say, on an OS using a 32-bit `id_t`) now fails the very same way that failing to set the ID does.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

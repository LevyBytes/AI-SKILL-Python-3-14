# Python 3.14.0 alpha 4 / library / zipfile

[gh-127847](https://github.com/python/cpython/issues/127847): Corrected the position when seeks and reads are interleaved over uncompressed, unencrypted zip files that [`zipfile.ZipFile.open()`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipFile.open) hands back.

[gh-123424](https://github.com/python/cpython/issues/123424): Added [`zipfile.ZipInfo._for_archive()`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipInfo._for_archive), which sets default properties onto [`ZipInfo`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipInfo) objects. Bénédikt Tran and Jason R. Coombs wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

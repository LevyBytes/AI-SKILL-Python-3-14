# Python 3.14.0 alpha 5 / library / zipfile

[gh-91279](https://github.com/python/cpython/issues/91279): [`zipfile.ZipFile.writestr()`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipFile.writestr) now honours `SOURCE_DATE_EPOCH`, which distributions can configure centrally so that build tools read it and emit reproducible output.

[gh-128131](https://github.com/python/cpython/issues/128131): Provide full random-access support for uncompressed, unencrypted, read-only zip files obtained via [`ZipFile.open`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipFile.open).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# What's new in Python 3.14 / zipfile - zipfile

### zipfile

- Introduced [`ZipInfo._for_archive`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipInfo._for_archive), a method that works out sensible defaults for a [`ZipInfo`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipInfo) object such as the one consumed by [`ZipFile.writestr`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipFile.writestr). (Contributed by Bénédikt Tran in [gh-123424](https://github.com/python/cpython/issues/123424).)

- [`ZipFile.writestr()`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipFile.writestr) now honors the `SOURCE_DATE_EPOCH` environment variable so as to give reproducible builds better support. (Contributed by Jiahao Li in [gh-91279](https://github.com/python/cpython/issues/91279).)

[Subject index](INDEX.md) · [Previous source section](webbrowser.md) · [Next source section](optimizations.md) · [Release/subject declaration](summary-release-highlights.md)

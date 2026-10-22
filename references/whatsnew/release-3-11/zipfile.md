# What's New In Python 3.11 / zipfile — zipfile

### zipfile

- Support landed for declaring the member name encoding used when reading metadata out of a [`ZipFile`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipFile)'s directory plus file headers. (Contributed by Stephen J. Turnbull and Serhiy Storchaka in [bpo-28080](https://bugs.python.org/issue?@action=redirect&bpo=28080).)

- To make fresh directories within ZIP archives, [`ZipFile.mkdir()`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipFile.mkdir) was added. (Contributed by Sam Ezeh in [gh-49083](https://github.com/python/cpython/issues/49083).)

- [`stem`](https://docs.python.org/3.14/library/zipfile.html#zipfile.Path.stem), [`suffix`](https://docs.python.org/3.14/library/zipfile.html#zipfile.Path.suffix) and [`suffixes`](https://docs.python.org/3.14/library/zipfile.html#zipfile.Path.suffixes) were added onto [`zipfile.Path`](https://docs.python.org/3.14/library/zipfile.html#zipfile.Path). (Contributed by Miguel Brito in [gh-88261](https://github.com/python/cpython/issues/88261).)

[Subject index](INDEX.md) · [Previous source section](warnings.md) · [Next source section](optimizations.md) · [Release/subject declaration](summary-release-highlights.md)

# What's New In Python 3.6 / zipfile - zipfile

### zipfile

A fresh [`ZipInfo.from_file()`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipInfo.from_file) class method lets you build a [`ZipInfo`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipInfo) instance out of a filesystem file. A fresh [`ZipInfo.is_dir()`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipInfo.is_dir) method serves to test whether the `ZipInfo` instance stands for a directory. (Contributed by Thomas Kluyver in [bpo-26039](https://bugs.python.org/issue?@action=redirect&bpo=26039).)

The [`ZipFile.open()`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipFile.open) method now serves to write data into a ZIP file in addition to extracting data. (Contributed by Thomas Kluyver in [bpo-26039](https://bugs.python.org/issue?@action=redirect&bpo=26039).)

[Subject index](INDEX.md) · [Previous source section](xmlrpc-client.md) · [Next source section](zlib.md) · [Release/subject declaration](summary-release-highlights.md)

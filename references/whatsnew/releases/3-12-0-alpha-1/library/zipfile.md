# Python 3.12.0 alpha 1 / library / zipfile

[bpo-39064](https://bugs.python.org/issue?@action=redirect&bpo=39064): When a damaged zip archive whose central directory offset comes out negative is opened, [`zipfile.ZipFile`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipFile) now signals [`zipfile.BadZipFile`](https://docs.python.org/3.14/library/zipfile.html#zipfile.BadZipFile) rather than `ValueError`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

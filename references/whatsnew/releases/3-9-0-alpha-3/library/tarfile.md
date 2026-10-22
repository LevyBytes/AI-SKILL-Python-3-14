# Python 3.9.0 alpha 3 / library / tarfile

[bpo-39430](https://bugs.python.org/issue?@action=redirect&bpo=39430): A race condition affecting lazy imports inside [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) was fixed.

[bpo-29435](https://bugs.python.org/issue?@action=redirect&bpo=29435): [`tarfile.is_tarfile()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.is_tarfile) may now accept file objects and file-like objects, mirroring [`zipfile.is_zipfile()`](https://docs.python.org/3.14/library/zipfile.html#zipfile.is_zipfile). William Woodruff wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

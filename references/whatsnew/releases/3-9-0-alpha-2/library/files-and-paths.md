# Python 3.9.0 alpha 2 / library / files and paths

[bpo-38994](https://bugs.python.org/issue?@action=redirect&bpo=38994): Provide `__class_getitem__` on `os.PathLike`, `pathlib.Path`.

[bpo-37523](https://bugs.python.org/issue?@action=redirect&bpo=37523): Adjust `zipfile.ZipExtFile` so it raises `ValueError` on any attempt to reach the underlying file object once that object has been closed. The fresh behavior lines up with how the rest of Python treats access to closed files.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.9.0 alpha 5 / library / files and paths

[bpo-39674](https://bugs.python.org/issue?@action=redirect&bpo=39674): Roll back [bpo-37330](https://bugs.python.org/issue?@action=redirect&bpo=37330): open() no longer accept "U" in file mode. To smooth migration away from Python 2.7, open()'s "U" mode stays in Python 3.9, though Python 3.10 will drop it.

[bpo-39719](https://bugs.python.org/issue?@action=redirect&bpo=39719): Drop `tempfile.SpooledTemporaryFile.softspace()`, given that files in Python 3 no longer carry the `softspace` attribute. Shantanu supplied the patch.

[bpo-39667](https://bugs.python.org/issue?@action=redirect&bpo=39667): Boost the pathlib.Path compatibility of zipfile.Path and undo the performance regression observed in zipp 3.0.

[bpo-39916](https://bugs.python.org/issue?@action=redirect&bpo=39916): `Path.glob()` now leans on `os.scandir()` more dependably. A ResourceWarning is no longer raised on interruption.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

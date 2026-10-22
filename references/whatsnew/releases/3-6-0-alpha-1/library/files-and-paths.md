# Python 3.6.0 alpha 1 / library / files and paths

[bpo-25717](https://bugs.python.org/issue?@action=redirect&bpo=25717): Brought back the earlier behavior of tolerating most fstat() errors during file opening. That regression entered in 3.5a1 and had broken anonymous temporary files in certain special cases.

[bpo-25624](https://bugs.python.org/issue?@action=redirect&bpo=25624): For directory entries ZipFile now invariably emits a ZIP_STORED header. Dingyuan Wang contributed this patch.

[bpo-24657](https://bugs.python.org/issue?@action=redirect&bpo=24657): Stopped CGIRequestHandler from squashing slashes inside the query segment of the URL as though that segment were a path. Xiang Zhang submitted the patch.

[bpo-20589](https://bugs.python.org/issue?@action=redirect&bpo=20589): Calling Path.owner() and Path.group() under Windows now raises NotImplementedError in place of ImportError.

[bpo-26385](https://bugs.python.org/issue?@action=redirect&bpo=26385): When the internal open() call within NamedTemporaryFile() fails, the file is now deleted. Silent Ghost supplied the patch.

[bpo-26012](https://bugs.python.org/issue?@action=redirect&bpo=26012): For the `**` pattern in pathlib.Path.[r]glob(), symlinks are no longer traversed into.

[bpo-24120](https://bugs.python.org/issue?@action=redirect&bpo=24120): PermissionError is now ignored while walking a tree with pathlib.Path.[r]glob(). Ulrich Petri contributed the patch.

[bpo-25860](https://bugs.python.org/issue?@action=redirect&bpo=25860): When an error happens, os.fwalk() no longer skips the directories that remain. Samson Lee supplied the original patch.

[bpo-26807](https://bugs.python.org/issue?@action=redirect&bpo=26807): The "files" produced by mock_open will no longer raise when readline runs past the end of the file. Yolanda Robla supplied the patch.

[bpo-26039](https://bugs.python.org/issue?@action=redirect&bpo=26039): Besides pulling data out, zipfile.ZipFile.open() can now also write data into a ZIP file. Thomas Kluyver wrote the patch.

[bpo-25911](https://bugs.python.org/issue?@action=redirect&bpo=25911): Brought back support for bytes paths in os.walk() under Windows.

[bpo-23076](https://bugs.python.org/issue?@action=redirect&bpo=23076): Calling Path.glob() with an invalid pattern now raises a ValueError. Thomas Nyberg contributed the patch.

[bpo-16620](https://bugs.python.org/issue?@action=redirect&bpo=16620): Corrected an AttributeError within msilib.Directory.glob().

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

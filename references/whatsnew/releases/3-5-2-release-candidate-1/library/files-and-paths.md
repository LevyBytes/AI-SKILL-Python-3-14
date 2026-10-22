# Python 3.5.2 release candidate 1 / library / files and paths

[bpo-26807](https://bugs.python.org/issue?@action=redirect&bpo=26807): mock_open "files" no longer raise an error on readline once the end of file is reached. Yolanda Robla supplied the patch.

[bpo-26012](https://bugs.python.org/issue?@action=redirect&bpo=26012): Refrain from following symlinks for the `**` pattern in pathlib.Path.[r]glob().

[bpo-24120](https://bugs.python.org/issue?@action=redirect&bpo=24120): Disregard PermissionError while walking a tree through pathlib.Path.[r]glob(). Ulrich Petri contributed the patch.

[bpo-25860](https://bugs.python.org/issue?@action=redirect&bpo=25860): os.fwalk() no longer abandons the remaining directories once an error happens. Samson Lee supplied the original patch.

[bpo-25717](https://bugs.python.org/issue?@action=redirect&bpo=25717): Bring back the earlier behavior of tolerating most fstat() errors while opening files. This had regressed in 3.5a1 and had prevented anonymous temporary files from functioning in certain cases.

[bpo-25624](https://bugs.python.org/issue?@action=redirect&bpo=25624): For directory entries, ZipFile now consistently emits a ZIP_STORED header. Dingyuan Wang wrote the patch.

- Whenever the host has already been resolved, getaddrinfo is now skipped. A. Jesse Jiryu Davis contributed the patch.

[bpo-26385](https://bugs.python.org/issue?@action=redirect&bpo=26385): Delete the file whenever the internal open() call within NamedTemporaryFile() fails. Silent Ghost contributed the patch.

[bpo-25911](https://bugs.python.org/issue?@action=redirect&bpo=25911): Support for bytes paths in os.walk() on Windows has been restored.

[bpo-23076](https://bugs.python.org/issue?@action=redirect&bpo=23076): Path.glob() now raises a ValueError when invoked with an invalid pattern. Thomas Nyberg contributed the patch.

[bpo-16620](https://bugs.python.org/issue?@action=redirect&bpo=16620): An AttributeError inside msilib.Directory.glob() has been fixed.

[bpo-20589](https://bugs.python.org/issue?@action=redirect&bpo=20589): Calling Path.owner() and Path.group() on Windows now raises NotImplementedError rather than ImportError.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

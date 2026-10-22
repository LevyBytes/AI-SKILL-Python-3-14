# Python 3.8.0 alpha 3 / library / build and platforms

[bpo-36103](https://bugs.python.org/issue?@action=redirect&bpo=36103): On non-Windows platforms, the default buffer size that `shutil.copyfileobj()` employs moves from 16 KiB up to 64 KiB to cut down on system call overhead. Inada Naoki contributed this.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

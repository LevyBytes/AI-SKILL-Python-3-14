# Python 3.5.0 alpha 1 / library / io fileio readall no longer swallows i o errors

[bpo-21090](https://bugs.python.org/issue?@action=redirect&bpo=21090): io.FileIO.readall() no longer swallows I/O errors. Previously it would overlook I/O errors provided at least the first C read() call had succeeded.

[Subject index](INDEX.md) · [Release version, date and status](../../release-overview/overview.md)

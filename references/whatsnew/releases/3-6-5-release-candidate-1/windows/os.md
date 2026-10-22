# Python 3.6.5 release candidate 1 / windows / os

[bpo-29248](https://bugs.python.org/issue?@action=redirect&bpo=29248): Repaired [`os.readlink()`](https://docs.python.org/3.14/library/os.html#os.readlink) under Windows, where the `PrintNameOffset` field of the reparse data buffer had been wrongly read as a count of characters rather than bytes. Craig Holmquist and SSE4 supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

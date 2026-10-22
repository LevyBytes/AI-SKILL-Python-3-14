# Python 3.7.0 beta 2 / windows / os

[bpo-29248](https://bugs.python.org/issue?@action=redirect&bpo=29248): Correct [`os.readlink()`](https://docs.python.org/3.14/library/os.html#os.readlink) under Windows, where it had wrongly handled the `PrintNameOffset` field of the reparse data buffer as a count of characters rather than bytes. Patch by Craig Holmquist and SSE4.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

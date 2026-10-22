# Python 3.8.0 alpha 1 / windows / os

[bpo-29248](https://bugs.python.org/issue?@action=redirect&bpo=29248): Repair [`os.readlink()`](https://docs.python.org/3.14/library/os.html#os.readlink) under Windows, which had erroneously interpreted the `PrintNameOffset` field within the reparse data buffer as a count of characters rather than bytes. Patch contributed by Craig Holmquist and SSE4.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

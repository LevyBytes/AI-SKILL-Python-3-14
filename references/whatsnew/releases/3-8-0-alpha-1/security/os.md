# Python 3.8.0 alpha 1 / security / os

[bpo-33871](https://bugs.python.org/issue?@action=redirect&bpo=33871): Repaired the sending of a portion of the file within [`os.sendfile()`](https://docs.python.org/3.14/library/os.html#os.sendfile) on macOS. Supplying the *trailers* argument could result in more bytes being sent from the input file than were requested.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

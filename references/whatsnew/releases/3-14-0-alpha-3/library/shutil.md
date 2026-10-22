# Python 3.14.0 alpha 3 / library / shutil

[gh-127035](https://github.com/python/cpython/issues/127035): Repair [`shutil.which`](https://docs.python.org/3.14/library/shutil.html#shutil.which) under Windows. It now considers a direct match purely when the command finishes with a PATHEXT extension or when X_OK is absent from mode. Extensionless files are honoured if "." appears in PATHEXT, and PATHEXT extensions terminating in a dot are also handled.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

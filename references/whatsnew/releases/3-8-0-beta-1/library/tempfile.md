# Python 3.8.0 beta 1 / library / tempfile

[bpo-26660](https://bugs.python.org/issue?@action=redirect&bpo=26660): Cleared up permission errors during [`TemporaryDirectory`](https://docs.python.org/3.14/library/tempfile.html#tempfile.TemporaryDirectory) cleanup. Earlier, `TemporaryDirectory.cleanup()` broke whenever non-writeable or non-searchable files or directories had been placed inside a temporary directory.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

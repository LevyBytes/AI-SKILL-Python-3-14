# Python 3.5.0 alpha 1 / library / tempfile

[bpo-21058](https://bugs.python.org/issue?@action=redirect&bpo=21058): Corrected a file descriptor leak within [`tempfile.NamedTemporaryFile()`](https://docs.python.org/3.14/library/tempfile.html#tempfile.NamedTemporaryFile); the descriptor is closed should [`io.open()`](https://docs.python.org/3.14/library/io.html#io.open) fail

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

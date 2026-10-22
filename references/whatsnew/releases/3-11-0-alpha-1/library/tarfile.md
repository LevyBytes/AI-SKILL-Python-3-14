# Python 3.11.0 alpha 1 / library / tarfile

[bpo-32695](https://bugs.python.org/issue?@action=redirect&bpo=32695): Both the *compresslevel* and *preset* keyword arguments accepted by [`tarfile.open()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.open) now carry documentation and test coverage.

[bpo-39039](https://bugs.python.org/issue?@action=redirect&bpo=39039): tarfile.open now throws [`ReadError`](https://docs.python.org/3.14/library/tarfile.html#tarfile.ReadError) whenever a zlib failure crops up while a file is being extracted.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

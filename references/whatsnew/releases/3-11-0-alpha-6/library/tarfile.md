# Python 3.11.0 alpha 6 / library / tarfile

[bpo-45863](https://bugs.python.org/issue?@action=redirect&bpo=45863): Whenever the [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) module builds a pax format archive, it now records an integer form of timestamps in the ustar header (where it can) to help older unarchivers, on top of the full-precision timestamps already stored in the pax extended header.

[bpo-44289](https://bugs.python.org/issue?@action=redirect&bpo=44289): Settle a problem in the [`is_tarfile()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.is_tarfile) method whenever a *fileobj* argument was supplied: the position inside *fileobj* moved forward, leaving it unreadable through [`tarfile.TarFile.open()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.TarFile.open).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

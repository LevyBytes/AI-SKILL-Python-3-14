# Python 3.5.2 release candidate 1 / security / os

[bpo-26839](https://bugs.python.org/issue?@action=redirect&bpo=26839): On Linux, [`os.urandom()`](https://docs.python.org/3.14/library/os.html#os.urandom) now invokes `getrandom()` with `GRND_NONBLOCK` so it falls back to reading `/dev/urandom` whenever the urandom entropy pool has not yet been initialized. Colm Buckley wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

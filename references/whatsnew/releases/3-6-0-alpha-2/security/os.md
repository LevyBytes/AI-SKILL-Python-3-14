# Python 3.6.0 alpha 2 / security / os

[bpo-26839](https://bugs.python.org/issue?@action=redirect&bpo=26839): Under Linux, [`os.urandom()`](https://docs.python.org/3.14/library/os.html#os.urandom) now invokes `getrandom()` together with `GRND_NONBLOCK`, falling back to reading `/dev/urandom` whenever the urandom entropy pool has yet to be seeded. Colm Buckley authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

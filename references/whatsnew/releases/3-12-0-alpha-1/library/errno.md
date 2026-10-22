# Python 3.12.0 alpha 1 / library / errno

[gh-95231](https://github.com/python/cpython/issues/95231): Loading `crypt` methods now fails gracefully whenever [`EPERM`](https://docs.python.org/3.14/library/errno.html#errno.EPERM) or [`ENOSYS`](https://docs.python.org/3.14/library/errno.html#errno.ENOSYS) gets raised. Such a situation can arise while attempting to load `MD5` against a Linux kernel running with FIPS enabled.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

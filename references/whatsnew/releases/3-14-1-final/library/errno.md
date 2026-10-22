# Python 3.14.1 final / library / errno

[gh-137490](https://github.com/python/cpython/issues/137490): Treats [`ECANCELED`](https://docs.python.org/3.14/library/errno.html#errno.ECANCELED) the same as [`EINTR`](https://docs.python.org/3.14/library/errno.html#errno.EINTR) inside [`signal.sigwaitinfo()`](https://docs.python.org/3.14/library/signal.html#signal.sigwaitinfo) on NetBSD.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

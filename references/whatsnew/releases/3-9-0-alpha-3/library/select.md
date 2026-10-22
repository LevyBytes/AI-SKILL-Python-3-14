# Python 3.9.0 alpha 3 / library / select

[bpo-39239](https://bugs.python.org/issue?@action=redirect&bpo=39239): The [`select.epoll.unregister()`](https://docs.python.org/3.14/library/select.html#select.epoll.unregister) method stopped silently swallowing the [`EBADF`](https://docs.python.org/3.14/library/errno.html#errno.EBADF) error.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.14.0 alpha 5 / library / collections and iteration

[gh-128916](https://github.com/python/cpython/issues/128916): Skip trying to set `SO_REUSEPORT` on sockets whose address family is neither `AF_INET` nor `AF_INET6`, since the option is pointless for those families and the call would fail under Linux kernel 6.12.9 and later.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.14.0 alpha 7 / library / socket

[gh-132075](https://github.com/python/cpython/issues/132075): Closed off the possibility of using [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) address structures whose members were uninitialized. By default every structure member now starts out filled with zeroes.

[gh-131668](https://github.com/python/cpython/issues/131668): For [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket): repaired the code that parses AF_BLUETOOTH socket addresses.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

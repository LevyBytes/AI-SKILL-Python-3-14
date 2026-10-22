# Python 3.13.0 alpha 3 / library / multiprocessing

[gh-101225](https://github.com/python/cpython/issues/101225): Raise the backlog on [`multiprocessing.connection.Listener`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.connection.Listener) objects produced by `multiprocessing.manager` and `multiprocessing.resource_sharer`, sharply lowering the chance of a connection refused error while building a [`multiprocessing.connection.Connection`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.connection.Connection) to them.

[gh-113421](https://github.com/python/cpython/issues/113421): Resolved the multiprocessing logger for `%(filename)s`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

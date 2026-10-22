# Python 3.14.0 alpha 2 / library / ssl

[gh-126106](https://github.com/python/cpython/issues/126106): Corrects a potential `NULL` pointer dereference within [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl).

[gh-124984](https://github.com/python/cpython/issues/124984): Made [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) thread-safe under the free-threaded build. A per-object lock now guards OpenSSL operations.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

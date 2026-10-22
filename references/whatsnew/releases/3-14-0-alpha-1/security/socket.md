# Python 3.14.0 alpha 1 / security / socket

[gh-122133](https://github.com/python/cpython/issues/122133): On platforms lacking `AF_UNIX`, such as Windows, authenticate the socket connection used by the `socket.socketpair()` fallback.

Patch by Gregory P. Smith <[greg@krypto.org](mailto:greg%40krypto.org)> and Seth Larson <[seth@python.org](mailto:seth%40python.org)>. Reported by Ellie <[el@horse64.org](mailto:el%40horse64.org)>

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

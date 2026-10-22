# Python 3.13.0 alpha 1 / library / ssl

[gh-105293](https://github.com/python/cpython/issues/105293): Drop the `SSL_CTX_set_session_id_context` call while a client-side context is being built inside the [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) module.

[gh-109109](https://github.com/python/cpython/issues/109109): The raw TLS certificate chains from TLS connections are now obtainable through the [`ssl.SSLSocket.get_verified_chain()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket.get_verified_chain) and [`ssl.SSLSocket.get_unverified_chain()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket.get_unverified_chain) methods.

Mateusz Nowak contributed this.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

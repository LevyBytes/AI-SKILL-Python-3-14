# Python 3.14.0 alpha 1 / library / ssl

[gh-109109](https://github.com/python/cpython/issues/109109): Raw TLS certificate chains can now be pulled from TLS connections through the [`ssl.SSLSocket.get_verified_chain()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket.get_verified_chain) and [`ssl.SSLSocket.get_unverified_chain()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket.get_unverified_chain) methods.

Mateusz Nowak contributed this.

[gh-116810](https://github.com/python/cpython/issues/116810): Closes a leak of memory that arrived with CPython 3.10's [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) whenever code touched the [`ssl.SSLSocket.session`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket.session) property. Reading and writing that property is now quicker because session objects are no longer needlessly duplicated through serialization.

[gh-122334](https://github.com/python/cpython/issues/122334): Stop a crash that struck when [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) was imported following a restart of the main interpreter.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

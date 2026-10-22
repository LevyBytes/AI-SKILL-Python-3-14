# Python 3.11.0 beta 1 / library / socket

[gh-74166](https://github.com/python/cpython/issues/74166): Provide a way to surface every error from [`create_connection()`](https://docs.python.org/3.14/library/socket.html#socket.create_connection) inside an [`ExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#ExceptionGroup) whenever it cannot establish a connection. By default it still reports only the final failure encountered after several addresses were attempted.

[gh-91498](https://github.com/python/cpython/issues/91498): Introduce the `TCP_CONNECTION_INFO` option (offered on macOS) into [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket).

[bpo-46696](https://bugs.python.org/issue?@action=redirect&bpo=46696): Add the `SO_INCOMING_CPU` constant to [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

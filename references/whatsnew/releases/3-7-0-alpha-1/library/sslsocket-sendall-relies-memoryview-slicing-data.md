# Python 3.7.0 alpha 1 / library / sslsocket sendall relies memoryview slicing data

[bpo-27340](https://bugs.python.org/issue?@action=redirect&bpo=27340): SSLSocket.sendall() now relies on memoryview when slicing data. This brings support for every bytes-like object, runs more efficiently, and skips expensive copies.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

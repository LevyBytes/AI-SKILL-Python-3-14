# Python 3.14.0 alpha 2 / library / correct defect where sslprotocol connection lost failed fire after oserror raised

[gh-118950](https://github.com/python/cpython/issues/118950): Correct a defect where SSLProtocol.connection_lost failed to fire after an OSError was raised while writing to the socket.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

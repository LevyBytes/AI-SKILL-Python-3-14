# Python 3.5.2 release candidate 1 / library / http server

[bpo-26586](https://bugs.python.org/issue?@action=redirect&bpo=26586): Within http.server, reply with "413 Request header fields too large" when there are too many header fields to parse, instead of dropping the connection and raising an unhandled exception. Xiang Zhang contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

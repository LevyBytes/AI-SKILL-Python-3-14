# Python 3.6.0 alpha 1 / library / http server

[bpo-26586](https://bugs.python.org/issue?@action=redirect&bpo=26586): When http.server encounters too many header fields to parse, it now answers with "413 Request header fields too large" rather than dropping the connection and surfacing an unhandled exception. Xiang Zhang contributed the patch.

[bpo-24902](https://bugs.python.org/issue?@action=redirect&bpo=24902): When http.server starts, it now prints the server URL. Felix Kaiser provided the initial patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

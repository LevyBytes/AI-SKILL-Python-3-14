# Python 3.8.0 alpha 1 / library / http server

[bpo-31639](https://bugs.python.org/issue?@action=redirect&bpo=31639): http.server now publishes a ThreadingHTTPServer class and runs it whenever the module starts via `-m`, so it handles web browsers that pre-open sockets.

[bpo-34711](https://bugs.python.org/issue?@action=redirect&bpo=34711): http.server now reports HTTPStatus.NOT_FOUND whenever the local path ends with "/" yet is not a directory, even where the host OS (AIX, for example) would treat such a path as a valid file reference. Michael Felt wrote the patch.

[bpo-24209](https://bugs.python.org/issue?@action=redirect&bpo=24209): Provides IPv6 support when http.server is launched directly.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

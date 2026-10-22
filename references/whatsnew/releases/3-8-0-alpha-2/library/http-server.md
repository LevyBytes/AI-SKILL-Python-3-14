# Python 3.8.0 alpha 2 / library / http server

[bpo-24209](https://bugs.python.org/issue?@action=redirect&bpo=24209): Inside the http.server script, lean on getaddrinfo to bind to the preferred address according to the bind parameter. The default bind, or binding by a name, may now land on IPv6 or dual-stack, depending on the surrounding environment.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

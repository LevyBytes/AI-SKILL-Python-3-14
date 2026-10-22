# Python 3.9.0 alpha 3 / library / http server

[bpo-35292](https://bugs.python.org/issue?@action=redirect&bpo=35292): `SimpleHTTPRequestHandler.guess_type` now proxies through to `mimetypes.guess_type`, which defers the `mimetypes.init` call so that importing the [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server) module avoids needless overhead.

[bpo-38907](https://bugs.python.org/issue?@action=redirect&bpo=38907): The http.server script once again binds to IPv4 under Windows.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

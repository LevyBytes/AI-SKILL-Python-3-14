# Python 3.12.0 alpha 4 / library / http server

[gh-100474](https://github.com/python/cpython/issues/100474): Before attempting to serve an index page, [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server) now confirms it is genuinely a regular file. That sidesteps trouble caused by directories whose name is `index.html`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

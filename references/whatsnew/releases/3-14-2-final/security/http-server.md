# Python 3.14.2 final / security / http server

[gh-119452](https://github.com/python/cpython/issues/119452): Address a possible memory denial of service inside the [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server) module. With a malicious user connected to the CGI server on Windows, an arbitrary quantity of memory could end up allocated. Possible consequences ranged from a [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError), swapping, out of memory (OOM) killed processes or containers, through to outright system crashes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

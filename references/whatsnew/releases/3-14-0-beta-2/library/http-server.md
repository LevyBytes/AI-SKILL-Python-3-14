# Python 3.14.0 beta 2 / library / http server

[gh-134168](https://github.com/python/cpython/issues/134168): [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server): Correct IPv6 address binding together with [`--directory`](https://docs.python.org/3.14/library/http.server.html#cmdoption-http.server-d) handling whenever HTTPS is used.

[gh-133889](https://github.com/python/cpython/issues/133889): The directory listing page produced by [`http.server.SimpleHTTPRequestHandler`](https://docs.python.org/3.14/library/http.server.html#http.server.SimpleHTTPRequestHandler) now displays only the decoded path component of the requested URL, leaving out the query and fragment.

[gh-134098](https://github.com/python/cpython/issues/134098): Correct the handling of paths terminating in a percent-encoded slash (`%2f` or `%2F`) within [`http.server.SimpleHTTPRequestHandler`](https://docs.python.org/3.14/library/http.server.html#http.server.SimpleHTTPRequestHandler).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

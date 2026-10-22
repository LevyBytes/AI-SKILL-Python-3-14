# What's New In Python 3.7 / http.server — http.server, socketserver

### http.server

The HTTP `If-Modified-Since` header is now honored by [`SimpleHTTPRequestHandler`](https://docs.python.org/3.14/library/http.server.html#http.server.SimpleHTTPRequestHandler). Whenever the requested file went unmodified past the time named in that header, the server replies with the 304 status. (Contributed by Pierre Quentel in [bpo-29654](https://bugs.python.org/issue?@action=redirect&bpo=29654).)

Alongside the fresh `--directory` command line argument, [`SimpleHTTPRequestHandler`](https://docs.python.org/3.14/library/http.server.html#http.server.SimpleHTTPRequestHandler) takes a fresh *directory* argument. That parameter makes the server hand out the named directory; absent it, the current working directory is used. (Contributed by Stéphane Wirtel and Julien Palard in [bpo-28707](https://bugs.python.org/issue?@action=redirect&bpo=28707).)

A fresh [`ThreadingHTTPServer`](https://docs.python.org/3.14/library/http.server.html#http.server.ThreadingHTTPServer) class leans on threads to service requests by way of [`ThreadingMixIn`](https://docs.python.org/3.14/library/socketserver.html#socketserver.ThreadingMixIn). Running `http.server` with `-m` brings it into play. (Contributed by Julien Palard in [bpo-31639](https://bugs.python.org/issue?@action=redirect&bpo=31639).)

[Subject index](INDEX.md) · [Previous source section](http-client.md) · [Next source section](idlelib-and-idle.md) · [Release/subject declaration](summary-release-highlights.md)

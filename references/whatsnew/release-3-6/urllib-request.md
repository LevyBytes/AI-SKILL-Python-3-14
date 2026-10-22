# What's New In Python 3.6 / urllib.request — urllib.request

### urllib.request

Should an HTTP request carry a file or iterable body (something other than a bytes object) yet omit a `Content-Length` header, [`AbstractHTTPHandler`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.HTTPHandler) no longer raises an error and instead resorts to chunked transfer encoding. (Contributed by Demian Brecht and Rolf Krahl in [bpo-12319](https://bugs.python.org/issue?@action=redirect&bpo=12319).)

[Subject index](INDEX.md) · [Previous source section](unittest-mock.md) · [Next source section](urllib-robotparser.md) · [Release/subject declaration](summary-release-highlights.md)
